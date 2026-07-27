#!/usr/bin/env python3
"""
OS-Setup Adaptor Engine — The Adaptoid.
Feed it (this DevKit + a project brief) and it analyzes the target,
pulls exactly the relevant components, and emits an executable, tailored setup.

Usage:
    python3 adaptor/engine.py --brief "Convert RFQ PDFs to structured BOQ" \\
        --output ./my-project --host claude,agents --core-only

The engine is sovereign: needs no network, no daemon, no git.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from host_emit import (
    HOSTS,
    build_context,
    emit_hosts,
    parse_hosts,
    write_core_handoff_and_index,
)

# ─── paths relative to this file ───
ENGINE_DIR = Path(__file__).parent.resolve()
OS_SETUP_ROOT = ENGINE_DIR.parent
CORE_DIR = OS_SETUP_ROOT / "core"

# Must-run validators (Core). Mirrors core/MANIFEST.yaml validators list.
CORE_VALIDATORS = [
    "preflight.sh",
    "validate_state.sh",
    "check_handoff.sh",
    "check_status_claims.sh",
    "check_silent_failures.sh",
    "check_references.sh",
    "check_intent.sh",
    "check_scope.sh",
    "publish_gate.sh",
    "route_sentinel.sh",
    "oap_security.sh",
    "context_budget.sh",
    "check_config.sh",
    "check_tests.sh",
    "check_metrics.sh",
    "check_processes.sh",
    "audit_chain.sh",
    "vault_mmu.sh",
    "wake.sh",
    "emit_event.sh",
]


def log(msg: str):
    print(f"[adaptoid] {msg}", file=sys.stderr)


def yaml_escape(s: str) -> str:
    """Escape a string for double-quoted YAML."""
    return (
        s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", " ")
        .replace("\r", "")
    )


def slugify(brief: str) -> str:
    words = re.findall(r"[a-zA-Z0-9]+", brief.lower())
    return "-".join(words[:4]) if words else "project"


# ═══════════════════════════════════════════════════════════════════════════════
# 1. INGEST
# ═══════════════════════════════════════════════════════════════════════════════
def kit_version() -> str:
    """Read kit VERSION file (authoritative)."""
    p = OS_SETUP_ROOT / "VERSION"
    if p.exists():
        return p.read_text(encoding="utf-8").strip() or "5.3.0"
    return "5.3.0"


def utc_now() -> str:
    """RFC3339 UTC without double timezone suffix."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ingest(brief: str, context: dict) -> dict:
    """Read the brief + any existing code/config."""
    log("INGEST: reading brief + context")
    return {
        "brief": brief,
        "context": context,
        "timestamp": utc_now(),
    }


# ═══════════════════════════════════════════════════════════════════════════════
# 2. ANALYZE
# ═══════════════════════════════════════════════════════════════════════════════
ARCHETYPE_SIGNALS = {
    "hackathon": ["hackathon", "48 hours", "demo day", "48h", "weekend", "competition"],
    "internship": ["internship", "report", "presentation", "mentor", "professor", "academic"],
    "job-take-home": ["take-home", "assessment", "interview", "evaluate my code", "coding test"],
    "research-ml": ["paper", "experiments", "ablations", "baselines", "metrics", "f1", "accuracy"],
    "nlp-pipeline": ["ner", "ocr", "extraction", "pipeline", "documents", "pdf", "text"],
    "internal-tool": ["internal tool", "erp", "admin", "for our team", "dashboard", "workflow"],
    "saas-product": ["customers", "multi-tenant", "billing", "saas", "subscription"],
    "startup-mvp": ["mvp", "pmf", "launch", "customers", "pitch", "investor"],
    "cli-tool": ["cli", "library", "package", "npm", "pip", "command-line"],
    "data-pipeline": ["etl", "warehouse", "analytics", "dashboard", "data pipeline"],
    # Mid-2026: product IS the agent / tool-using system
    "agent-product": [
        "agent", "multi-agent", "tool use", "tool-use", "mcp server", "mcp tool",
        "coding agent", "agentic", "function calling", "subagent", "autonomous agent",
    ],
}

TIER_SIGNALS = {
    "T0": ["throwaway", "spike", "script", "weekend", "48h"],
    "T1": ["internal tool", "mvp", "small team"],
    "T2": ["production", "customers", "on-call", "observability"],
    "T3": ["compliance", "gdpr", "hipaa", "soc2", "audit"],
    "T4": ["startup", "pmf", "investor", "funding"],
}


def detect_archetype(brief: str) -> tuple:
    """Score brief against archetype signals. Returns (archetype, confidence, ask)."""
    text = brief.lower()
    scores = {}
    for archetype, signals in ARCHETYPE_SIGNALS.items():
        scores[archetype] = sum(1 for s in signals if s in text)
    best = max(scores, key=scores.get)
    confidence = scores[best]
    if confidence == 0:
        return None, 0, "Ambiguous — need one multiple-choice question"
    return best, confidence, None


def detect_tier(brief: str, archetype: str) -> str:
    """Pick smallest tier that fits."""
    text = brief.lower()
    for tier in ["T4", "T3", "T2", "T1", "T0"]:
        signals = TIER_SIGNALS.get(tier, [])
        if any(s in text for s in signals):
            return tier
    defaults = {
        "hackathon": "T0",
        "internship": "T1",
        "job-take-home": "T1",
        "research-ml": "T1",
        "nlp-pipeline": "T1",
        "internal-tool": "T1",
        "saas-product": "T2",
        "startup-mvp": "T2",
        "cli-tool": "T0",
        "data-pipeline": "T1",
        "agent-product": "T2",
    }
    return defaults.get(archetype, "T1")


def analyze(brief: str, context: dict) -> dict:
    """Detect archetype, tier, domain, risk profile."""
    log("ANALYZE: detecting archetype + tier")
    archetype, confidence, ask = detect_archetype(brief)
    tier = detect_tier(brief, archetype or "internal-tool")

    domain_map = {
        "research-ml": "ML", "nlp-pipeline": "NLP", "saas-product": "web",
        "internal-tool": "web", "cli-tool": "systems", "data-pipeline": "data",
        "hackathon": "varies", "startup-mvp": "web", "agent-product": "agents",
        "internship": "general", "job-take-home": "general",
    }
    domain = domain_map.get(archetype, "general")

    text = brief.lower()
    stack = []
    if "python" in text or "fastapi" in text or "django" in text:
        stack.append("python")
    if "react" in text or "next" in text:
        stack.append("react")
    if "postgres" in text or "postgresql" in text:
        stack.append("postgres")
    if "node" in text or "express" in text or "typescript" in text:
        stack.append("node")
    if "mcp" in text:
        stack.append("mcp")

    risk_fms = {
        "hackathon": ["FM-08", "FM-09"],
        "research-ml": ["FM-05", "FM-06", "FM-10"],
        "nlp-pipeline": ["FM-03", "FM-05", "FM-11"],
        "internal-tool": ["FM-01", "FM-02", "FM-08"],
        "saas-product": ["FM-01", "FM-02", "FM-07", "FM-09"],
        "startup-mvp": ["FM-08", "FM-09"],
        "cli-tool": ["FM-07", "FM-11"],
        "data-pipeline": ["FM-05", "FM-11"],
        "internship": ["FM-01", "FM-09"],
        "job-take-home": ["FM-01", "FM-09"],
        "agent-product": ["FM-09", "FM-13", "FM-18", "FM-19", "FM-20"],
    }

    return {
        "archetype": archetype,
        "tier": tier,
        "domain": domain,
        "stack_hints": stack,
        "risk_fms": risk_fms.get(archetype, ["FM-01", "FM-09"]),
        "ask": ask,
        "confidence": confidence,
    }


# ═══════════════════════════════════════════════════════════════════════════════
# 3. PULL — consult ecosystem library
# ═══════════════════════════════════════════════════════════════════════════════
def pull_ecosystem(analysis: dict) -> dict:
    """Return recommended stack for archetype.

    Note: uses built-in tables (fast, offline). reference/ecosystem/SELECTION.md
    is human documentation, not parsed at runtime. Keep smallest stack.
    """
    log("PULL: consulting built-in archetype defaults")
    archetype = analysis["archetype"]
    stacks = {
        "hackathon": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd-lite", "verify-before-done"],
            "skip": ["sdk", "memory", "multi-agent"],
            "language": "python",
            "backend": "",
            "frontend": "",
        },
        "internship": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd", "verify-before-done"],
            "skip": ["sdk"],
            "language": "python",
            "backend": "",
            "frontend": "",
        },
        "job-take-home": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd", "code-review", "verify-before-done"],
            "skip": ["sdk", "memory"],
            "language": "python",
            "backend": "",
            "frontend": "",
        },
        "research-ml": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd", "diagnose", "verify-before-done"],
            "skip": ["ui"],
            "language": "python",
            "backend": "",
            "frontend": "",
        },
        "nlp-pipeline": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd", "verify-before-done"],
            "skip": ["ui"],
            "language": "python",
            "backend": "",
            "frontend": "",
        },
        "internal-tool": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd", "code-review", "verify-before-done"],
            "skip": ["sdk"],
            "language": "python",
            "backend": "fastapi",
            "frontend": "",
        },
        "saas-product": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd", "code-review", "verify-before-done"],
            "skip": [],
            "language": "typescript",
            "backend": "node",
            "frontend": "react",
        },
        "startup-mvp": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd-lite", "verify-before-done"],
            "skip": ["multi-agent"],
            "language": "typescript",
            "backend": "node",
            "frontend": "react",
        },
        "cli-tool": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd", "verify-before-done"],
            "skip": ["ui", "sdk"],
            "language": "python",
            "backend": "",
            "frontend": "",
        },
        "data-pipeline": {
            "mcp": ["filesystem", "git"],
            "skills": ["tdd", "verify-before-done"],
            "skip": ["ui"],
            "language": "python",
            "backend": "",
            "frontend": "",
        },
        "agent-product": {
            "mcp": ["filesystem", "git"],
            "skills": [
                "intent-lock",
                "verify-before-done",
                "blast-radius-check",
                "handoff-rewrite",
            ],
            "skip": ["crew-framework-default"],
            "language": "python",
            "backend": "",
            "frontend": "",
        },
    }
    base = {
        "mcp": ["filesystem", "git"],
        "skills": ["tdd", "verify-before-done"],
        "skip": [],
        "language": "",
        "backend": "",
        "frontend": "",
    }
    out = {**base, **stacks.get(archetype or "", {})}
    # Prefer brief stack_hints when present
    hints = analysis.get("stack_hints") or []
    if "python" in hints and not out.get("language"):
        out["language"] = "python"
    if "node" in hints:
        out["language"] = out.get("language") or "typescript"
        out["backend"] = out.get("backend") or "node"
    if "react" in hints:
        out["frontend"] = "react"
    if "postgres" in hints:
        out["database"] = "postgres"
    else:
        out.setdefault("database", "")
    return out


# ═══════════════════════════════════════════════════════════════════════════════
# 4. COMPOSE — generate project structure
# ═══════════════════════════════════════════════════════════════════════════════
def copy_templates(tier: str, output_dir: Path, core_only: bool):
    """Copy template skeleton. Product path is Core only (lean kit)."""
    templates = OS_SETUP_ROOT / "templates"
    # Pro multi-dir scaffold archived — always Core root templates
    if not core_only:
        log("  note: non-core-only requested but Pro templates archived → using Core")
    dirs_to_copy = ["root"]

    for d in dirs_to_copy:
        src = templates / d
        if not src.exists():
            continue
        if d == "root":
            # root templates go at project root
            for item in src.iterdir():
                dst = output_dir / item.name
                if item.is_dir():
                    if dst.exists():
                        shutil.rmtree(dst)
                    shutil.copytree(item, dst)
                else:
                    shutil.copy2(item, dst)
            log("  copied template: root → project root")
        else:
            dst = output_dir / d
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            log(f"  copied template: {d}")

    # Core always needs work/ for two-tier dispatch
    (output_dir / "work").mkdir(parents=True, exist_ok=True)
    (output_dir / "work" / "reports").mkdir(parents=True, exist_ok=True)
    (output_dir / "plan").mkdir(parents=True, exist_ok=True)
    (output_dir / "attic").mkdir(parents=True, exist_ok=True)


def copy_kernel(output_dir: Path):
    """Copy always-load kernel into the project."""
    src = OS_SETUP_ROOT / "kernel"
    dst = output_dir / "kernel"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    log("  copied kernel/")


# Portable Agent Skills (agentskills.io) — progressive disclosure procedures
ADAPTOID_SKILLS = {
    "intent-lock": {
        "description": (
            "Use when the brief is ambiguous or multi-path. "
            "Offer ≤4 A/B/C options, write decisions into PROJECT-INTENT and plan/intent-lock.md."
        ),
        "body": """# Intent lock

1. If industry, stack, offline, or success criteria are open → **stop coding**.
2. Ask ≤4 options (A/B/C/D); mark one recommended.
3. Write answers into `PROJECT-INTENT.md` + `plan/intent-lock.md` with **Status: Locked**.
4. Only then enter plan mode for stages 1–3.

Do not scaffold a full stack while decisions are open.
""",
    },
    "verify-before-done": {
        "description": (
            "Use before claiming done, ship, or PR. "
            "Run acceptance commands and preflight; paste exit codes."
        ),
        "body": """# Verify before done

1. Run the task `acceptance` command(s); require exit 0.
2. Run `bash orchestrator/scripts/preflight.sh .`
3. Paste command + output in the report. No green claim without evidence.
4. If background tasks were started, wait for exit codes first.

Status without evidence = false (FM-09).
""",
    },
    "blast-radius-check": {
        "description": (
            "Use before destructive, production, money, network-write, or MCP write actions. "
            "Classify r0–r5 and pause for human if high."
        ),
        "body": """# Blast radius check

| Tier | Examples | Action |
|---|---|---|
| r0–r1 | read files, local edit | free |
| r2 | git commit local | free after tests |
| r3 | push, PR, network write | confirm |
| r4–r5 | prod deploy, secrets, money, `rm -rf` | **stop — human** |

MCP write/network is often **unsandboxed** (esp. Codex) → treat as ≥ r3.
See `protocols/blast-radius.md` + `policies/default.yaml`.
""",
    },
    "handoff-rewrite": {
        "description": (
            "Use at end of session or wave. Rewrite HANDOFF.md (never append). "
            "Cold session must resume from HANDOFF alone."
        ),
        "body": """# Handoff rewrite

Replace entire `HANDOFF.md` with current truth:

- Active wave / task
- Done (with evidence pointers)
- Next 1–3 steps
- Do NOT list (pitfalls)

Never append. Stale HANDOFF = FM-14.
""",
    },
    "worktree-parallel": {
        "description": (
            "Use when ≥2 agents might edit overlapping paths. "
            "One task → one git worktree → disjoint writes → merge after tests."
        ),
        "body": """# Worktree parallel (FM-13)

1. Parallel BUILD only if `writes` sets are disjoint **or** each agent has its own worktree.
2. Prefer host worktree isolation (Claude `--worktree`, Grok/Codex worktrees).
3. Merge only after TEST evidence on each branch/worktree.
4. Single writer for `HANDOFF.md` on the primary tree.
""",
    },
}


def emit_adaptoid_skills(output_dir: Path) -> list[str]:
    """Emit agentskills-compliant skills under .agents/skills/ (+ Claude mirror)."""
    written: list[str] = []
    root = output_dir / ".agents" / "skills"
    root.mkdir(parents=True, exist_ok=True)
    for name, meta in ADAPTOID_SKILLS.items():
        skill_dir = root / name
        skill_dir.mkdir(parents=True, exist_ok=True)
        body = (
            f"---\n"
            f"name: {name}\n"
            f"description: >\n"
            f"  {meta['description']}\n"
            f"---\n\n"
            f"{meta['body'].strip()}\n"
        )
        path = skill_dir / "SKILL.md"
        path.write_text(body, encoding="utf-8")
        written.append(f".agents/skills/{name}/SKILL.md")

    # Claude Code common path (mirror) — progressive disclosure same content
    claude_skills = output_dir / ".claude" / "skills"
    for name in ADAPTOID_SKILLS:
        src = root / name / "SKILL.md"
        dst_dir = claude_skills / name
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / "SKILL.md"
        dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        written.append(f".claude/skills/{name}/SKILL.md")

    index = root / "README.md"
    index.write_text(
        """# Adaptoid Agent Skills

Portable procedures ([agentskills.io](https://agentskills.io) format).

| Skill | When |
|---|---|
| `intent-lock` | Ambiguous brief / multi-path |
| `verify-before-done` | Before ship / done claims |
| `blast-radius-check` | Prod, secrets, money, MCP write |
| `handoff-rewrite` | End of wave / session |
| `worktree-parallel` | Parallel agents risk collisions |

Always-on law stays in `AGENTS.md` / `SHIP-SYSTEM.md`. Load skills on demand.
""",
        encoding="utf-8",
    )
    written.append(".agents/skills/README.md")
    return written


def write_config(analysis: dict, brief: str, output_dir: Path, hosts: list, core_only: bool):
    """Write adaptoid.config.yaml."""
    cfg_path = output_dir / "adaptoid.config.yaml"
    eco = pull_ecosystem(analysis)
    goal = yaml_escape(brief[:120])
    now = utc_now()
    lang = yaml_escape(str(eco.get("language") or ""))
    backend = yaml_escape(str(eco.get("backend") or ""))
    frontend = yaml_escape(str(eco.get("frontend") or ""))
    database = yaml_escape(str(eco.get("database") or ""))
    content = f"""---
project:
  name: "{slugify(brief)}"
  goal: "{goal}"
  domain: "{analysis['domain']}"

archetype: "{analysis['archetype']}"
tier: "{analysis['tier']}"
kit: "core"
hosts: {json.dumps(hosts)}

stack:
  language: "{lang}"
  backend: "{backend}"
  frontend: "{frontend}"
  database: "{database}"
  extras: {json.dumps(eco.get("skills") or [])}

compliance: []
mcp_servers: {json.dumps(eco['mcp'])}

orchestrator:
  model: "claude-or-kimi"
  auto_mode: false

workers:
  tool: "opencode-cli"
  max_parallel: 5

cost:
  max_usd_per_wave: 10
  on_ceiling: "pause-and-ask"

dag_transitions:
  plan:
    allowed_next: [dispatch, review]
    max_retries: 3
  dispatch:
    allowed_next: [review, merge]
    max_retries: 2
  review:
    allowed_next: [merge, dispatch]
    max_retries: 3
  merge:
    allowed_next: [ship]
    max_retries: 1

policies:
  active_pack: "default.yaml"
  auto_load: true

vault:
  enabled: true
  hash_algorithm: "sha256"

event_sourcing:
  enabled: true
  hash_chain: true

waves:
  active: "wave-1"
  total_planned: 0
  shipped: 0

adapted_at: "{now}"
last_verified: "{now}"
version: "{kit_version()}"
"""
    cfg_path.write_text(content, encoding="utf-8")
    log(f"  wrote {cfg_path.name}")


def project_type_for(analysis: dict) -> str:
    """Map domain/archetype → ProjectIntent.schema.json project_type enum."""
    allowed = {
        "web_app",
        "data_analysis",
        "api_design",
        "ml_pipeline",
        "infrastructure",
        "research",
        "content_creation",
    }
    domain = (analysis.get("domain") or "").lower()
    arch = (analysis.get("archetype") or "").lower()
    mapping = {
        "ml": "ml_pipeline",
        "nlp": "ml_pipeline",
        "web": "web_app",
        "systems": "infrastructure",
        "data": "data_analysis",
        "general": "web_app",
        "varies": "web_app",
    }
    arch_map = {
        "research-ml": "research",
        "cli-tool": "infrastructure",
        "data-pipeline": "data_analysis",
        "nlp-pipeline": "ml_pipeline",
        "saas-product": "web_app",
        "startup-mvp": "web_app",
        "internal-tool": "web_app",
        "hackathon": "web_app",
        "job-take-home": "api_design",
        "internship": "research",
    }
    pt = arch_map.get(arch) or mapping.get(domain) or "web_app"
    return pt if pt in allowed else "web_app"


def write_intent(analysis: dict, brief: str, output_dir: Path):
    """Write PROJECT-INTENT.md filled from brief."""
    risk = ", ".join(analysis["risk_fms"])
    project_type = project_type_for(analysis)
    content = f"""---
schema_version: "1.0"
project_type: "{project_type}"
archetype: "{analysis['archetype']}"
tier: "{analysis['tier']}"
stakeholders:
  - role: "user"
    needs: "complete the project with evidence-backed done"
success_criteria:
  - "preflight passes"
  - "HANDOFF.md reflects current wave"
  - "scope stays inside IN box"
failure_modes:
  - "hallucination"
  - "wrong_route"
  - "false_done"
non_negotiables:
  - "evidence or it did not happen"
  - "replace never append state"
preferences:
  tech_stack: "{', '.join(analysis.get('stack_hints') or []) or 'unspecified'}"
  worker_tool: "host-native agent"
verification_level: "standard"
---

# Project Intent

## Problem Statement
{brief.strip()}

## Scope
### IN
- Deliver the capability described in the problem statement
- Keep harness contracts (kernel, HANDOFF, preflight) healthy

### OUT
- Speculative features not in the brief
- Rewriting the harness itself unless required

### LATER
- Stretch polish after success criteria pass

## Falsification
- Preflight fails and is ignored
- "Done" claimed without command evidence
- Scope expands into OUT without a new intent revision

## Highest-risk failure modes
{risk}

## Intent lock (resolve before BUILD if open)
If any of these are unclear, ask the user A/B/C options (one recommended) and record answers here — do not full-build until locked:
- Target user / industry / domain specifics
- Must-have constraints (offline, language, Excel-only, deadline)
- Success metric for v0.1 (what demo proves)

## Operating law
Follow `HOST-OPERATING-PLAYBOOK.md`: plan→approve→implement for big work; one outcome per turn; verify before done.
"""
    path = output_dir / "PROJECT-INTENT.md"
    path.write_text(content, encoding="utf-8")
    log("  wrote PROJECT-INTENT.md")

    # Intent-lock stub for ambiguous briefs (engine confidence low or generic domain)
    lock = output_dir / "plan" / "intent-lock.md"
    lock.parent.mkdir(parents=True, exist_ok=True)
    lock.write_text(
        f"""# Intent lock — resolve before BUILD

> Grok-style: lock intent before code. Fill after user answers A/B/C.

## Brief (raw)
{brief.strip()[:2000]}

## Detected
- Archetype: `{analysis.get('archetype')}`
- Tier: `{analysis.get('tier')}`
- Stack hints: `{', '.join(analysis.get('stack_hints') or []) or 'none'}`

## Open questions (agent: ask ≤4, one recommended)
1. Primary user / industry for v0.1?
   - A) …
   - B) …
   - C) …
2. Hard constraints (offline, languages, formats)?
3. What single demo proves success?
4. Must-not-do?

## Decisions (record here)
- …

## Status
- [ ] Locked — then continue SDLC stage 3 design / stage 4 build
""",
        encoding="utf-8",
    )
    log("  wrote plan/intent-lock.md")


def copy_validators(output_dir: Path, core_only: bool):
    """Copy validators into orchestrator/scripts/."""
    src = OS_SETUP_ROOT / "validators"
    dst = output_dir / "orchestrator" / "scripts"
    dst.mkdir(parents=True, exist_ok=True)
    if core_only:
        names = CORE_VALIDATORS
        count = 0
        for name in names:
            f = src / name
            if f.exists():
                shutil.copy2(f, dst / name)
                count += 1
        log(f"  copied {count} Core validators → orchestrator/scripts/")
    else:
        files = list(src.glob("*.sh"))
        for f in files:
            shutil.copy2(f, dst / f.name)
        log(f"  copied {len(files)} validators → orchestrator/scripts/")


def copy_core_marker(output_dir: Path, core_only: bool):
    """Record which kit was installed."""
    marker = output_dir / ".adaptoid-kit"
    marker.write_text(
        "core\n" if core_only else "pro\n",
        encoding="utf-8",
    )


def copy_intent_schema(output_dir: Path):
    """Copy PROJECT-INTENT JSON schema when present in the kit."""
    src = OS_SETUP_ROOT / "schemas" / "ProjectIntent.schema.json"
    if not src.exists():
        return
    dst_dir = output_dir / "schemas"
    dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst_dir / src.name)
    log("  copied schemas/ProjectIntent.schema.json")


def write_project_readme(
    analysis: dict,
    brief: str,
    output_dir: Path,
    hosts: list,
    core_only: bool,
):
    """Minimal README so generated projects are navigable without the kit docs."""
    name = slugify(brief)
    content = f"""# {name}

Generated by **Adaptoid OS** (`{'core' if core_only else 'pro'}` kit).

## Brief
{brief.strip()}

## Meta
| | |
|---|---|
| Archetype | `{analysis['archetype']}` |
| Tier | `{analysis['tier']}` |
| Hosts | {', '.join(f'`{h}`' for h in hosts)} |
| Risk FMs | {', '.join(analysis['risk_fms'])} |

## Start here (SHIP SYSTEM)
1. Read `AGENTS.md` / `CLAUDE.md` then **`SHIP-SYSTEM.md`** (SDLC × full host toolkit)
2. Read `HANDOFF.md` + `PROJECT-INTENT.md` + `kernel/`
3. Tasks: already created if engine used `--sdlc`, else  
   `python3 <adaptoid>/conductor/conductor.py init-wave --project . --sdlc`
4. Execute stages 1→7 with **required host tools** listed on each task
5. Before complete: `bash orchestrator/scripts/preflight.sh .`

## Layout
```
SHIP-SYSTEM.md          ← product OS: SDLC + Grok/Claude toolkit
AGENTS.md / CLAUDE.md   cold-start
kernel/ HANDOFF.md PROJECT-INTENT.md
protocols/              sdlc + safety
orchestrator/scripts/   preflight
work/wave-*/tasks/      01-plan … 07-maintain
```
"""
    (output_dir / "README.md").write_text(content, encoding="utf-8")
    log("  wrote README.md")


def copy_sdlc_docs(output_dir: Path):
    """Copy SHIP SYSTEM (SDLC × host toolkit) into the project."""
    proto_dst = output_dir / "protocols"
    proto_dst.mkdir(parents=True, exist_ok=True)
    pairs = [
        ("core/SHIP-SYSTEM.md", output_dir / "SHIP-SYSTEM.md"),
        ("core/HOST-OPERATING-PLAYBOOK.md", output_dir / "HOST-OPERATING-PLAYBOOK.md"),
        ("core/HOST-CAPABILITIES.md", output_dir / "HOST-CAPABILITIES.md"),
        ("protocols/sdlc-loop.md", proto_dst / "sdlc-loop.md"),
        ("protocols/blast-radius.md", proto_dst / "blast-radius.md"),
        ("protocols/verification.md", proto_dst / "verification.md"),
        ("protocols/oap-security.md", proto_dst / "oap-security.md"),
        ("protocols/route-sentinel.md", proto_dst / "route-sentinel.md"),
    ]
    for rel, dst in pairs:
        src = OS_SETUP_ROOT / rel
        if not src.exists():
            continue
        shutil.copy2(src, dst)
        log(f"  copied {dst.relative_to(output_dir)}")


def compose(
    analysis: dict,
    brief: str,
    output_dir: Path,
    hosts: list,
    core_only: bool,
):
    """Generate the full project structure + host surfaces."""
    log("COMPOSE: generating project structure")
    output_dir.mkdir(parents=True, exist_ok=True)

    copy_templates(analysis["tier"], output_dir, core_only)
    copy_kernel(output_dir)
    write_config(analysis, brief, output_dir, hosts, core_only)
    write_intent(analysis, brief, output_dir)
    copy_validators(output_dir, core_only)
    copy_core_marker(output_dir, core_only)
    copy_intent_schema(output_dir)
    write_project_readme(analysis, brief, output_dir, hosts, core_only)
    copy_sdlc_docs(output_dir)

    host_label = ",".join(hosts)
    ctx = build_context(
        project_name=slugify(brief),
        goal=brief,
        archetype=analysis["archetype"] or "internal-tool",
        tier=analysis["tier"],
        host=host_label,
    )
    written_state = write_core_handoff_and_index(output_dir, ctx)
    for w in written_state:
        log(f"  wrote {w}")

    host_files = emit_hosts(output_dir, hosts, ctx)
    for hf in host_files:
        log(f"  host emit: {hf}")

    skill_files = emit_adaptoid_skills(output_dir)
    for sf in skill_files:
        log(f"  skill emit: {sf}")

    # ADR stub in plan/
    adr_dir = output_dir / "plan"
    adr_dir.mkdir(parents=True, exist_ok=True)
    adr = adr_dir / "0002-stack-selection.md"
    eco = pull_ecosystem(analysis)
    adr.write_text(
        f"""# ADR 0002 — Stack Selection

| Decision | Why | Rejected |
|---|---|---|
| Archetype: {analysis['archetype']} | Detected from brief signals | — |
| Tier: {analysis['tier']} | Smallest that fits | — |
| Kit: core | Product path (Pro scaffold archived) | hollow pro |
| Hosts: {', '.join(hosts)} | --host flag | — |
| Language: {eco.get('language') or '—'} | Built-in + brief hints | — |
| MCP: {', '.join(eco['mcp'])} | Smallest stack | marketplace free-for-all |
| Skills: {', '.join(eco.get('skills') or [])} | agentskills paths | always-on mega-prompt |

Highest-risk failure modes: {', '.join(analysis['risk_fms'])}
""",
        encoding="utf-8",
    )
    log(f"  wrote {adr.relative_to(output_dir)}")


# ═══════════════════════════════════════════════════════════════════════════════
# 6. VERIFY — run preflight
# ═══════════════════════════════════════════════════════════════════════════════
def verify(output_dir: Path) -> bool:
    """Run preflight.sh. Must pass."""
    log("VERIFY: running preflight.sh")
    preflight = output_dir / "orchestrator" / "scripts" / "preflight.sh"
    if not preflight.exists():
        log("  preflight.sh not found — skipping")
        return True
    rc = os.system(f"cd '{output_dir}' && bash '{preflight}' '{output_dir}'")
    return rc == 0


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════
def main():
    parser = argparse.ArgumentParser(
        description="Adaptoid OS Adaptor Engine — adapt harness to project + host",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
hosts: {', '.join(HOSTS)}, all
examples:
  python3 adaptor/engine.py --brief "cli log parser" --output ./p --host all --core-only --sdlc
  python3 adaptor/engine.py --brief "internship API" --output ./p --core-only --host all --sdlc
""",
    )
    parser.add_argument("--brief", required=True, help="Project brief (one line or paragraph)")
    parser.add_argument("--output", required=True, help="Output directory for generated project")
    parser.add_argument("--deadline", default="", help="Deadline context")
    parser.add_argument("--audience", default="", help="Who will see it")
    parser.add_argument("--tech", default="", help="Tech preference")
    parser.add_argument(
        "--host",
        default="agents,claude",
        help="Host adapters to emit (comma-separated or 'all'). Default: agents,claude",
    )
    parser.add_argument(
        "--core-only",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Emit Core kit (default: on). Pro multi-dir scaffold is archived; --no-core-only still emits Core.",
    )
    parser.add_argument("--skip-verify", action="store_true", help="Skip preflight verification")
    parser.add_argument(
        "--archetype",
        default="",
        help="Force archetype (skip detection). Example: hackathon",
    )
    parser.add_argument(
        "--tier",
        default="",
        help="Force tier T0-T4 (skip detection)",
    )
    parser.add_argument(
        "--sdlc",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="After generate, run conductor init-wave --sdlc (default: on). Use --no-sdlc to skip.",
    )
    args = parser.parse_args()

    try:
        hosts = parse_hosts(args.host)
    except ValueError as e:
        log(str(e))
        sys.exit(2)

    context = {
        "deadline": args.deadline,
        "audience": args.audience,
        "tech": args.tech,
        "hosts": hosts,
        "core_only": args.core_only,
    }

    # 1. INGEST
    data = ingest(args.brief, context)

    # 2. ANALYZE
    analysis = analyze(args.brief, context)
    if args.archetype:
        analysis["archetype"] = args.archetype
        analysis["ask"] = None
    if args.tier:
        analysis["tier"] = args.tier
    # Product honesty: always Core (Pro templates not on live tree)
    args.core_only = True
    log(
        f"  archetype={analysis['archetype']}  tier={analysis['tier']}  "
        f"domain={analysis['domain']}  kit=core  "
        f"hosts={hosts}"
    )
    if analysis["ask"] and not args.archetype:
        log(f"  NEEDS CLARIFICATION: {analysis['ask']}")
        log("  tip: re-run with --archetype <name> or a more specific brief")
        sys.exit(1)

    # 3. PULL
    stack = pull_ecosystem(analysis)
    log(f"  stack: MCP={stack['mcp']}  skills={stack['skills']}")

    # 4. COMPOSE
    out = Path(args.output).resolve()
    compose(analysis, args.brief, out, hosts, args.core_only)

    # 5. RECORD — ADR already written in compose

    # 5b. Optional SDLC task scaffold
    sdlc_ok = None
    if args.sdlc:
        log("SDLC: conductor init-wave --sdlc")
        cond = OS_SETUP_ROOT / "conductor" / "conductor.py"
        if cond.exists():
            # Keep conductor JSON off stdout so engine JSON stays parseable
            r = subprocess.run(
                [
                    sys.executable,
                    str(cond),
                    "init-wave",
                    "--project",
                    str(out),
                    "--wave",
                    "wave-1",
                    "--sdlc",
                ],
                capture_output=True,
                text=True,
            )
            if r.stderr:
                print(r.stderr, file=sys.stderr, end="")
            sdlc_ok = r.returncode == 0
            if not sdlc_ok:
                log("SDLC init-wave failed (non-fatal if you init later)")
                if r.stdout:
                    log(r.stdout.strip()[:500])
        else:
            log("conductor.py missing — skip --sdlc")
            sdlc_ok = False

    # 6. VERIFY
    if not args.skip_verify:
        if not verify(out):
            log("VERIFY FAILED — fix above before declaring ready")
            sys.exit(1)

    next_steps = [
        f"cd {out}",
        "Open in Grok Build / Claude / Cursor / Codex",
        'Say: "Read AGENTS.md + HANDOFF + INTENT. Complete wave-1 with evidence."',
        "bash orchestrator/scripts/preflight.sh .",
    ]
    if not args.sdlc:
        next_steps.insert(
            1,
            f"python3 {OS_SETUP_ROOT}/conductor/conductor.py init-wave --project {out} --sdlc",
        )

    print(
        json.dumps(
            {
                "status": "READY",
                "output_dir": str(out),
                "kit": "core",
                "version": kit_version(),
                "hosts": hosts,
                "sdlc_tasks": sdlc_ok,
                "host_files": {
                    "AGENTS.md": (out / "AGENTS.md").exists(),
                    "CLAUDE.md": (out / "CLAUDE.md").exists(),
                    "cursor_rules": (out / ".cursor" / "rules" / "adaptoid.mdc").exists(),
                    "agents_skills": (out / ".agents" / "skills").is_dir(),
                },
                "archetype": analysis["archetype"],
                "tier": analysis["tier"],
                "domain": analysis["domain"],
                "risk_fms": analysis["risk_fms"],
                "mcp_servers": stack["mcp"],
                "use": "See USE.md — hand brief + kit to the model and say complete it",
                "next": next_steps,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
