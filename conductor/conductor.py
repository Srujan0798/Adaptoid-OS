#!/usr/bin/env python3
"""
Adaptoid Conductor — thin Brain/Hands runtime reference.

Does not replace Claude Code / Cursor / Codex. It:
  - lists and dispatches wave task briefs under work/
  - enforces disjoint write sets (FM-13)
  - writes standardized reports
  - emits session events (hash-chained via validators/emit_event.sh when present)
  - rewrites HANDOFF.md (replace, never append)
  - wakes a cold session from durable files

Usage:
  python3 conductor/conductor.py status --project .
  python3 conductor/conductor.py wake --project .
  python3 conductor/conductor.py dispatch --project . --wave wave-1 [--mode stub|shell]
  python3 conductor/conductor.py check-disjoint --project . --wave wave-1
  python3 conductor/conductor.py rewrite-handoff --project . --wave wave-1
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def log(msg: str) -> None:
    print(f"[conductor] {msg}", file=sys.stderr)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ─── task parsing ─────────────────────────────────────────────────────────────

@dataclass
class Task:
    path: Path
    wave: str
    task_id: str
    title: str = ""
    writes: list[str] = field(default_factory=list)
    forbid: list[str] = field(default_factory=list)
    acceptance: str = ""
    body: str = ""


def _parse_list_field(text: str, key: str) -> list[str]:
    """Parse writes: [a, b] or writes: a, b from task markdown."""
    m = re.search(rf"(?im)^{re.escape(key)}\s*:\s*(.+)$", text)
    if not m:
        return []
    raw = m.group(1).strip()
    if raw.startswith("["):
        try:
            val = ast.literal_eval(raw)
            if isinstance(val, list):
                return [str(x).strip() for x in val]
        except (SyntaxError, ValueError):
            pass
    return [p.strip().strip("`'\"") for p in re.split(r"[, ]+", raw) if p.strip()]


def _parse_table_field(text: str, key: str) -> str:
    """Parse markdown table row: | key | value |"""
    m = re.search(
        rf"(?im)^\|\s*{re.escape(key)}\s*\|\s*(.+?)\s*\|?\s*$",
        text,
    )
    if not m:
        return ""
    return m.group(1).strip().strip("`").strip()


def parse_task(path: Path, wave: str) -> Task:
    text = path.read_text(encoding="utf-8")
    title = ""
    for line in text.splitlines():
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            break
    acc = ""
    m = re.search(r"(?im)^acceptance\s*:\s*(.+)$", text)
    if m:
        acc = m.group(1).strip().strip("`")
    if not acc:
        acc = _parse_table_field(text, "acceptance")
    # also accept ## Acceptance section with a command line
    if not acc:
        m2 = re.search(r"(?is)##\s*Acceptance\s*\n+`([^`]+)`", text)
        if m2:
            acc = m2.group(1).strip()
        else:
            m3 = re.search(r"(?is)##\s*Acceptance\s*\n+(\S.+)", text)
            if m3:
                acc = m3.group(1).strip()
    writes = _parse_list_field(text, "writes")
    if not writes:
        w = _parse_table_field(text, "writes")
        if w:
            # e.g. [`src/module_1/`] or src/module_1/
            writes = [
                p.strip().strip("`'\"[]")
                for p in re.split(r"[, ]+", w)
                if p.strip().strip("`'\"[]")
            ]
    forbid = _parse_list_field(text, "forbid")
    if not forbid:
        f = _parse_table_field(text, "forbid")
        if f:
            forbid = [f]
    return Task(
        path=path,
        wave=wave,
        task_id=path.stem,
        title=title or path.stem,
        writes=writes,
        forbid=forbid,
        acceptance=acc,
        body=text,
    )


def discover_tasks(project: Path, wave: str) -> list[Task]:
    """Find task briefs: work/<wave>/*.md or work/<wave>/tasks/*.md (not reports)."""
    roots = [
        project / "work" / wave / "tasks",
        project / "work" / wave,
    ]
    found: list[Path] = []
    for root in roots:
        if not root.is_dir():
            continue
        for p in sorted(root.glob("*.md")):
            if "report" in p.name.lower():
                continue
            found.append(p)
        if found:
            break
    return [parse_task(p, wave) for p in found]


# ─── FM-13 disjoint ───────────────────────────────────────────────────────────

def check_disjoint(tasks: list[Task]) -> list[str]:
    """Return list of collision messages (empty = ok)."""
    errors: list[str] = []
    owner: dict[str, str] = {}
    for t in tasks:
        for w in t.writes:
            key = w.strip()
            if not key:
                continue
            if key in owner and owner[key] != t.task_id:
                errors.append(
                    f"FM-13 collision: '{key}' written by both {owner[key]} and {t.task_id}"
                )
            else:
                owner[key] = t.task_id
        for f in t.forbid:
            # informational only here
            pass
    return errors


# ─── reports & events ─────────────────────────────────────────────────────────

def report_path(project: Path, wave: str, task_id: str) -> Path:
    d = project / "work" / "reports" / wave
    d.mkdir(parents=True, exist_ok=True)
    # also support work/<wave>/reports/
    alt = project / "work" / wave / "reports"
    alt.mkdir(parents=True, exist_ok=True)
    return d / f"{task_id}.report.md"


def write_report(
    project: Path,
    task: Task,
    *,
    status: str,
    evidence: str,
    mode: str,
    duration_s: float,
) -> Path:
    path = report_path(project, task.wave, task.task_id)
    content = f"""# Report: {task.task_id}

| Field | Value |
|---|---|
| Wave | {task.wave} |
| Task | {task.task_id} |
| Title | {task.title} |
| Status | **{status}** |
| Mode | {mode} |
| Duration | {duration_s:.2f}s |
| Written | {utc_now()} |

## Evidence
```
{evidence.strip() or "(none)"}
```

## Writes claimed
{chr(10).join(f"- `{w}`" for w in task.writes) or "- (none declared)"}

## Acceptance
`{task.acceptance or "n/a"}`

## Notes
Generated by Adaptoid conductor. Orchestrator must review before merge.
"""
    path.write_text(content, encoding="utf-8")
    # mirror under work/<wave>/reports for older layouts
    mirror = project / "work" / task.wave / "reports" / f"{task.task_id}.report.md"
    mirror.parent.mkdir(parents=True, exist_ok=True)
    mirror.write_text(content, encoding="utf-8")
    return path


def emit_event(project: Path, wave: str, task_id: str, etype: str, **kv: str) -> None:
    script = project / "orchestrator" / "scripts" / "emit_event.sh"
    if not script.exists():
        script = project / "validators" / "emit_event.sh"
    if not script.exists():
        # kit root
        kit = Path(__file__).resolve().parent.parent / "validators" / "emit_event.sh"
        script = kit if kit.exists() else None
    if not script or not script.exists():
        log(f"emit_event skipped (no emit_event.sh) {etype}")
        return
    args = [str(script), wave, task_id, etype]
    for k, v in kv.items():
        args.append(f"{k}={v}")
    try:
        subprocess.run(args, cwd=str(project), check=False, capture_output=True, text=True)
    except OSError as e:
        log(f"emit_event failed: {e}")


# ─── HANDOFF rewrite ──────────────────────────────────────────────────────────

def read_active_wave(project: Path) -> str:
    hand = project / "HANDOFF.md"
    if hand.exists():
        m = re.search(r"(?i)active wave[:\s*]*wave-?(\d+)", hand.read_text(encoding="utf-8"))
        if m:
            return f"wave-{m.group(1)}"
    cfg = project / "adaptoid.config.yaml"
    if cfg.exists():
        m = re.search(r'active:\s*"?(wave-\d+)"?', cfg.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return "wave-1"


def rewrite_handoff(
    project: Path,
    *,
    wave: str,
    active_task: str,
    done: list[str],
    next_items: list[str],
    goal: str = "",
) -> Path:
    path = project / "HANDOFF.md"
    archetype = "unknown"
    tier = "T1"
    host = "agents"
    cfg = project / "adaptoid.config.yaml"
    if cfg.exists():
        text = cfg.read_text(encoding="utf-8")
        m = re.search(r'archetype:\s*"?([^\n"]+)"?', text)
        if m:
            archetype = m.group(1).strip()
        m = re.search(r'tier:\s*"?([^\n"]+)"?', text)
        if m:
            tier = m.group(1).strip()
        m = re.search(r'hosts:\s*(\[[^\]]+\])', text)
        if m:
            host = m.group(1)
        m = re.search(r'goal:\s*"([^"]*)"', text)
        if m and not goal:
            goal = m.group(1)

    done_block = "\n".join(f"- {d}" for d in done) or "- (none yet)"
    next_block = "\n".join(f"{i+1}. {n}" for i, n in enumerate(next_items)) or "1. Plan next task"
    content = f"""# HANDOFF — Current Truth

> **Replace this file; never append.** Rewritten by conductor at {utc_now()}.

## Status
- **Active wave:** {wave}
- **Active task:** {active_task or "(none)"}
- **Last updated:** {today()}
- **Orchestrator host:** {host}
- **Archetype:** {archetype}
- **Tier:** {tier}

## Goal (one line)
{goal or "(see PROJECT-INTENT.md)"}

## Done so far
{done_block}

## Next (ordered)
{next_block}

## Pending decisions
- (none)

## Blockers
- (none)

## Evidence links
- Reports: `work/reports/{wave}/`
- Config: `adaptoid.config.yaml`
- Intent: `PROJECT-INTENT.md`
- Preflight: `bash orchestrator/scripts/preflight.sh .`

## Do NOT
- Claim "done" without command output
- Expand scope outside PROJECT-INTENT IN box
- Touch remote/money/humans without confirmation
"""
    path.write_text(content, encoding="utf-8")
    return path


# ─── commands ─────────────────────────────────────────────────────────────────

def cmd_status(project: Path) -> int:
    wave = read_active_wave(project)
    tasks = discover_tasks(project, wave)
    print(f"project: {project}")
    print(f"active_wave: {wave}")
    print(f"tasks_found: {len(tasks)}")
    for t in tasks:
        rp = report_path(project, wave, t.task_id)
        st = "HAS_REPORT" if rp.exists() else "PENDING"
        print(f"  - {t.task_id}: {st}  writes={t.writes or '[]'}")
    hand = project / "HANDOFF.md"
    print(f"handoff: {'present' if hand.exists() else 'MISSING'}")
    intent = project / "PROJECT-INTENT.md"
    print(f"intent: {'present' if intent.exists() else 'MISSING'}")
    kernel = project / "kernel" / "PRINCIPLES.md"
    print(f"kernel: {'present' if kernel.exists() else 'MISSING'}")
    return 0


def cmd_wake(project: Path) -> int:
    print("=== WAKE — cold session orientation ===")
    for rel in [
        "kernel/PRINCIPLES.md",
        "kernel/TWO-TIER.md",
        "kernel/ANTI-HALLUCINATION.md",
        "HANDOFF.md",
        "PROJECT-INTENT.md",
        "adaptoid.config.yaml",
        "AGENTS.md",
        "CLAUDE.md",
        "INDEX.md",
    ]:
        p = project / rel
        print(f"{'✓' if p.exists() else '✗'} {rel}")
    wave = read_active_wave(project)
    print(f"\nactive_wave: {wave}")
    if (project / "HANDOFF.md").exists():
        print("\n--- HANDOFF (first 40 lines) ---")
        lines = (project / "HANDOFF.md").read_text(encoding="utf-8").splitlines()
        print("\n".join(lines[:40]))
    wake_sh = project / "orchestrator" / "scripts" / "wake.sh"
    if wake_sh.exists():
        subprocess.run(["bash", str(wake_sh), str(project)], check=False)
    print("\n=== WAKE complete — orient, then act ===")
    return 0


def cmd_check_disjoint(project: Path, wave: str) -> int:
    tasks = discover_tasks(project, wave)
    if not tasks:
        print(f"OK disjoint: no tasks under work/{wave}/")
        return 0
    errs = check_disjoint(tasks)
    if errs:
        for e in errs:
            print(f"FAIL {e}")
        return 1
    print(f"OK FM-13: {len(tasks)} tasks have disjoint writes")
    return 0


def run_task_stub(task: Task) -> tuple[str, str]:
    evidence = (
        f"stub mode: task '{task.task_id}' acknowledged\n"
        f"title: {task.title}\n"
        f"writes: {task.writes}\n"
        f"acceptance: {task.acceptance or 'n/a'}\n"
        "Real workers (Claude/Cursor/Codex/OpenCode) should implement; "
        "conductor only coordinates."
    )
    return "STUB_COMPLETE", evidence


NOOP_ACCEPTANCE = re.compile(r"^\s*(true|:|exit\s+0)\s*$|^\s*echo\b[^|&;]*$")


def run_task_shell(project: Path, task: Task) -> tuple[str, str]:
    if not task.acceptance:
        return "FAIL", (
            f"no acceptance command on task '{task.task_id}' — shell mode requires one. "
            "Add `acceptance: <command>` to the task brief, or dispatch with --mode stub "
            "for coordination-only runs."
        )
    if NOOP_ACCEPTANCE.match(task.acceptance):
        return "FAIL", (
            f"acceptance is a no-op (`{task.acceptance}`) — auto-pass theater. "
            "Use a command that can actually fail (test runner, validator, curl check)."
        )
    try:
        proc = subprocess.run(
            task.acceptance,
            shell=True,
            cwd=str(project),
            capture_output=True,
            text=True,
            timeout=300,
        )
        evidence = (
            f"$ {task.acceptance}\n"
            f"exit={proc.returncode}\n"
            f"stdout:\n{proc.stdout[-4000:]}\n"
            f"stderr:\n{proc.stderr[-2000:]}"
        )
        status = "PASS" if proc.returncode == 0 else "FAIL"
        return status, evidence
    except subprocess.TimeoutExpired:
        return "FAIL", f"acceptance timed out: {task.acceptance}"
    except OSError as e:
        return "FAIL", f"acceptance error: {e}"


def cmd_dispatch(project: Path, wave: str, mode: str, tasks_filter: list[str]) -> int:
    tasks = discover_tasks(project, wave)
    if tasks_filter:
        tasks = [t for t in tasks if t.task_id in tasks_filter]
    if not tasks:
        log(f"no tasks found under work/{wave}/ — create *.md briefs first")
        return 1

    errs = check_disjoint(tasks)
    if errs:
        for e in errs:
            log(e)
        return 1

    done: list[str] = []
    failed: list[str] = []
    for t in tasks:
        log(f"dispatch {t.task_id} mode={mode}")
        emit_event(project, wave, t.task_id, "task.dispatched", mode=mode, file=str(t.path))
        t0 = time.time()
        if mode == "shell":
            status, evidence = run_task_shell(project, t)
        else:
            status, evidence = run_task_stub(t)
        dur = time.time() - t0
        rp = write_report(project, t, status=status, evidence=evidence, mode=mode, duration_s=dur)
        try:
            rel_report = str(rp.relative_to(project))
        except ValueError:
            rel_report = str(rp)
        emit_event(
            project,
            wave,
            t.task_id,
            "task.reported",
            status=status,
            report=rel_report,
        )
        log(f"  {status} → {rp}")
        if status in ("PASS", "STUB_COMPLETE"):
            done.append(f"{t.task_id}: {status}")
        else:
            failed.append(t.task_id)

    pending = [t.task_id for t in discover_tasks(project, wave) if t.task_id not in [d.split(":")[0] for d in done]]
    rewrite_handoff(
        project,
        wave=wave,
        active_task=failed[0] if failed else (pending[0] if pending else "(wave idle)"),
        done=done,
        next_items=[
            "Review reports under work/reports/",
            "Run bash orchestrator/scripts/preflight.sh .",
            "Merge only tasks with evidence",
        ]
        + ([f"Re-run failed: {', '.join(failed)}"] if failed else []),
    )
    print(
        json.dumps(
            {
                "wave": wave,
                "mode": mode,
                "dispatched": len(tasks),
                "done": done,
                "failed": failed,
            },
            indent=2,
        )
    )
    return 1 if failed else 0


def cmd_rewrite_handoff(project: Path, wave: str) -> int:
    tasks = discover_tasks(project, wave)
    done = []
    next_items = []
    for t in tasks:
        rp = report_path(project, wave, t.task_id)
        if rp.exists():
            done.append(f"{t.task_id}: report present")
        else:
            next_items.append(f"Dispatch {t.task_id}")
    if not next_items:
        next_items = ["Run preflight", "Plan next wave"]
    path = rewrite_handoff(
        project,
        wave=wave,
        active_task=next_items[0] if next_items else "(none)",
        done=done or ["Scaffold present"],
        next_items=next_items,
    )
    print(f"rewrote {path}")
    return 0


# Full GFG-aligned SDLC × host toolkit (see core/SHIP-SYSTEM.md + HOST-OPERATING-PLAYBOOK.md)
SDLC_TASKS = [
    (
        "00-intent-lock",
        "0-LOCK",
        "plan/intent-lock.md",
        "test -f plan/intent-lock.md",
        "INTENT LOCK (Grok-style): If brief is ambiguous, ask ≤4 A/B/C options, record in intent-lock + PROJECT-INTENT. No BUILD until locked. Tiny clear tasks may mark N/A.",
        "Plan mode, ask-user options, deep reasoning — NO feature code yet",
    ),
    (
        "01-plan",
        "1-PLAN",
        "plan/feasibility.md",
        "test -f PROJECT-INTENT.md",
        "Planning & feasibility: refine goal, IN/OUT, tier, viability. Touch plan/feasibility.md notes. No feature code.",
        "Plan mode, deep reasoning, web search (stack viability)",
    ),
    (
        "02-requirements",
        "2-REQ",
        "plan/requirements.md",
        "grep -q success_criteria PROJECT-INTENT.md",
        "Requirements: testable success criteria + NFRs + falsification. Capture in plan/requirements.md.",
        "Plan mode, subagents (research), web search, MCP tickets if configured",
    ),
    (
        "03-design",
        "3-DESIGN",
        "plan/design.md",
        "test -f plan/design.md",
        "Design (HLD/LLD-light): modules, APIs, data for THIS wave only. Write plan/design.md.",
        "Plan mode, code search, multi-file read",
    ),
    (
        "04-build",
        "4-BUILD",
        "src/",
        "test -d src",
        "Development: implement vertical slice under src/. Stay in writes. No OUT freebies.",
        "Terminal, multi-file edits, code search, git, skills, sandbox if untrusted",
    ),
    (
        "05-test",
        "5-TEST",
        "tests/",
        "test -d tests || test -f plan/design.md",
        "Testing: unit/integration as needed. Run acceptance. Paste exit codes in report.",
        "Terminal, subagents (parallel tests), background tasks (wait for exit)",
    ),
    (
        "06-deploy",
        "6-DEPLOY",
        "orchestrator/scripts/",
        "bash orchestrator/scripts/preflight.sh .",
        "Deployment gate: preflight PASS. Prod needs blast-radius confirm. Optional CI headless.",
        "Terminal, headless/CI, git PR, hooks, MCP observability if configured",
    ),
    (
        "07-maintain",
        "7-MAINT",
        "HANDOFF.md",
        "test -f HANDOFF.md",
        "Maintenance: rewrite HANDOFF with next wave. No silent scope. Bugs = new tasks.",
        "Memory=HANDOFF, plan mode for next slice, code search",
    ),
]


def cmd_init_wave(project: Path, wave: str, n: int, sdlc: bool = False) -> int:
    """Create task briefs for a wave (generic n modules, or SDLC stage gates)."""
    task_dir = project / "work" / wave / "tasks"
    task_dir.mkdir(parents=True, exist_ok=True)
    (project / "work" / "reports" / wave).mkdir(parents=True, exist_ok=True)

    if sdlc:
        specs = SDLC_TASKS
    else:
        specs = [
            (
                f"{i:02d}-task",
                "4-BUILD",
                f"src/module_{i}/",
                f"test -d src/module_{i} || mkdir -p src/module_{i}",
                f"Implement module {i} for this wave. Stay inside writes list.",
                "Terminal, multi-file edits, code search, git",
            )
            for i in range(1, n + 1)
        ]

    for tid, stage, writes, acceptance, goal, host_tools in specs:
        path = task_dir / f"{tid}.md"
        if path.exists():
            continue
        path.write_text(
            f"""# {tid} — SDLC {stage}

| Field | Value |
|---|---|
| Wave | {wave} |
| Stage | {stage} |
| writes | [`{writes}`] |
| forbid | [paths owned by other tasks] |
| acceptance | `{acceptance}` |
| blast_radius | r0 |

writes: [{writes}]
acceptance: {acceptance}

## Goal
{goal}

## Host tools REQUIRED this stage (Adaptoid SHIP SYSTEM)
{host_tools}

See `SHIP-SYSTEM.md` for full SDLC×toolkit matrix. Do not skip tools or evidence.

## Context
PROJECT-INTENT.md · HANDOFF.md · SHIP-SYSTEM.md · protocols/sdlc-loop.md

## Done means
- Stage goal met with artifacts
- Host tools above actually used where applicable
- acceptance exits 0 (paste output in report)
- No scope outside PROJECT-INTENT IN box
""",
            encoding="utf-8",
        )
        log(f"created {path}")

    first = specs[0][0]
    rewrite_handoff(
        project,
        wave=wave,
        active_task=first,
        done=[f"Initialized {wave} with {'SDLC' if sdlc else n} task stubs"],
        next_items=[
            f"Edit briefs under work/{wave}/tasks/",
            "Follow PLAN→BUILD→TEST→SHIP; never skip gates",
            f"conductor dispatch --wave {wave}",
        ],
    )
    print(
        json.dumps(
            {
                "wave": wave,
                "mode": "sdlc" if sdlc else "modules",
                "tasks": len(specs),
                "dir": str(task_dir),
            },
            indent=2,
        )
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Adaptoid Conductor — thin runtime")
    # Shared --project via parent so both work:
    #   conductor.py --project ./p status
    #   conductor.py status --project ./p
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument(
        "--project",
        type=Path,
        default=Path("."),
        help="Project root (default: .)",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", parents=[parent], help="Show wave/task/handoff status")
    sub.add_parser("wake", parents=[parent], help="Cold-start orientation from durable files")

    p_disp = sub.add_parser("dispatch", parents=[parent], help="Dispatch wave tasks")
    p_disp.add_argument("--wave", default="")
    p_disp.add_argument("--mode", choices=("stub", "shell"), default="stub")
    p_disp.add_argument("--only", nargs="*", default=[], help="Only these task ids")

    p_dj = sub.add_parser("check-disjoint", parents=[parent], help="FM-13 write-set check")
    p_dj.add_argument("--wave", default="")

    p_rh = sub.add_parser("rewrite-handoff", parents=[parent], help="Rewrite HANDOFF.md from reports")
    p_rh.add_argument("--wave", default="")

    p_init = sub.add_parser("init-wave", parents=[parent], help="Create task briefs (modules or SDLC)")
    p_init.add_argument("--wave", default="wave-1")
    p_init.add_argument("-n", type=int, default=3, help="Module tasks when not --sdlc")
    p_init.add_argument(
        "--sdlc",
        action="store_true",
        help="Create PLAN/DESIGN/BUILD/TEST/SHIP gate tasks (Agile SDLC)",
    )

    args = parser.parse_args(argv)
    project = args.project.resolve()
    if not project.is_dir():
        log(f"not a directory: {project}")
        return 2

    if args.cmd == "status":
        return cmd_status(project)
    if args.cmd == "wake":
        return cmd_wake(project)
    wave = getattr(args, "wave", "") or read_active_wave(project)
    if args.cmd == "dispatch":
        return cmd_dispatch(project, wave, args.mode, args.only)
    if args.cmd == "check-disjoint":
        return cmd_check_disjoint(project, wave)
    if args.cmd == "rewrite-handoff":
        return cmd_rewrite_handoff(project, wave)
    if args.cmd == "init-wave":
        return cmd_init_wave(
            project,
            args.wave or "wave-1",
            args.n,
            sdlc=bool(getattr(args, "sdlc", False)),
        )
    return 2


if __name__ == "__main__":
    sys.exit(main())
