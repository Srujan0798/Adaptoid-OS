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
def ingest(brief: str, context: dict) -> dict:
    """Read the brief + any existing code/config."""
    log("INGEST: reading brief + context")
    return {
        "brief": brief,
        "context": context,
        "timestamp": datetime.now(timezone.utc).isoformat() + "Z",
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
        "hackathon": "varies", "startup-mvp": "web",
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
    if "node" in text or "express" in text:
        stack.append("node")

    risk_fms = {
        "hackathon": ["FM-08", "FM-09"],
        "research-ml": ["FM-05", "FM-06", "FM-10"],
        "nlp-pipeline": ["FM-03", "FM-05", "FM-11"],
        "internal-tool": ["FM-01", "FM-02", "FM-08"],
        "saas-product": ["FM-01", "FM-02", "FM-07", "FM-09"],
        "startup-mvp": ["FM-08", "FM-09"],
        "cli-tool": ["FM-07", "FM-11"],
        "data-pipeline": ["FM-05", "FM-11"],
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
    """Return recommended stack for archetype."""
    log("PULL: consulting ecosystem defaults")
    archetype = analysis["archetype"]
    stacks = {
        "hackathon": {"mcp": ["filesystem", "git"], "skills": ["tdd-lite"], "skip": ["sdk", "memory"]},
        "research-ml": {"mcp": ["filesystem", "git", "tavily"], "skills": ["tdd", "diagnose"], "skip": ["ui"]},
        "internal-tool": {"mcp": ["filesystem", "git", "serena"], "skills": ["tdd", "code-review"], "skip": ["sdk"]},
        "saas-product": {"mcp": ["filesystem", "git", "playwright"], "skills": ["tdd", "code-review", "observability"], "skip": []},
        "cli-tool": {"mcp": ["filesystem", "git"], "skills": ["tdd"], "skip": ["ui", "sdk"]},
    }
    return stacks.get(archetype, {"mcp": ["filesystem", "git"], "skills": ["tdd"], "skip": []})


# ═══════════════════════════════════════════════════════════════════════════════
# 4. COMPOSE — generate project structure
# ═══════════════════════════════════════════════════════════════════════════════
def copy_templates(tier: str, output_dir: Path, core_only: bool):
    """Copy template skeleton based on tier / core mode."""
    templates = OS_SETUP_ROOT / "templates"
    if core_only:
        dirs_to_copy = ["root"]
    else:
        dirs_to_copy = ["root", "work", "specify", "plan", "docs", "orchestrator"]
        if tier in ("T2", "T3", "T4"):
            dirs_to_copy += ["evals"]
        if tier in ("T3", "T4"):
            dirs_to_copy += ["ci"]

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


def write_config(analysis: dict, brief: str, output_dir: Path, hosts: list, core_only: bool):
    """Write adaptoid.config.yaml."""
    cfg_path = output_dir / "adaptoid.config.yaml"
    eco = pull_ecosystem(analysis)
    goal = yaml_escape(brief[:120])
    now = datetime.now(timezone.utc).isoformat()
    content = f"""---
project:
  name: "{slugify(brief)}"
  goal: "{goal}"
  domain: "{analysis['domain']}"

archetype: "{analysis['archetype']}"
tier: "{analysis['tier']}"
kit: "{'core' if core_only else 'pro'}"
hosts: {json.dumps(hosts)}

stack:
  language: ""
  backend: ""
  frontend: ""
  database: ""
  extras: []

compliance: []
mcp_servers: {json.dumps(eco['mcp'])}

orchestrator:
  model: "claude-or-kimi"
  auto_mode: false

workers:
  tool: "opencode-cli"
  max_parallel: 5

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

adapted_at: "{now}Z"
last_verified: "{now}Z"
version: "5.1"
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
"""
    path = output_dir / "PROJECT-INTENT.md"
    path.write_text(content, encoding="utf-8")
    log("  wrote PROJECT-INTENT.md")


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

## Start here
1. Read `AGENTS.md` (or `CLAUDE.md` / Cursor rules)
2. Read `HANDOFF.md` + `PROJECT-INTENT.md` + `kernel/`
3. Init tasks: `python3 <adaptoid>/conductor/conductor.py init-wave --project . -n 3`
4. Before claiming done: `bash orchestrator/scripts/preflight.sh .`

## Layout
```
AGENTS.md / CLAUDE.md   cold-start for your host
kernel/                 always-load laws
HANDOFF.md              current wave truth (replace, don't append)
PROJECT-INTENT.md       done means + falsification
orchestrator/scripts/   validators + preflight
work/                   task briefs + reports
```
"""
    (output_dir / "README.md").write_text(content, encoding="utf-8")
    log("  wrote README.md")


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

    # ADR stub (Pro docs or core plan/)
    adr_dir = output_dir / "docs" / "decisions"
    if not core_only:
        adr_dir.mkdir(parents=True, exist_ok=True)
    else:
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
| Kit: {'core' if core_only else 'pro'} | User/engine selection | — |
| Hosts: {', '.join(hosts)} | --host flag | — |
| MCP: {', '.join(eco['mcp'])} | Minimal viable tools | Others from SELECTION.md |

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
  python3 adaptor/engine.py --brief "cli log parser" --output ./p --host agents,claude
  python3 adaptor/engine.py --brief "48h hackathon app" --output ./h --core-only --host all
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
        action="store_true",
        help="Emit Adaptoid Core kit only (kernel + contracts + must-run validators)",
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
    log(
        f"  archetype={analysis['archetype']}  tier={analysis['tier']}  "
        f"domain={analysis['domain']}  kit={'core' if args.core_only else 'pro'}  "
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

    # 6. VERIFY
    if not args.skip_verify:
        if not verify(out):
            log("VERIFY FAILED — fix above before declaring ready")
            sys.exit(1)

    print(
        json.dumps(
            {
                "status": "READY",
                "output_dir": str(out),
                "kit": "core" if args.core_only else "pro",
                "hosts": hosts,
                "host_files": {
                    "AGENTS.md": (out / "AGENTS.md").exists(),
                    "CLAUDE.md": (out / "CLAUDE.md").exists(),
                    "cursor_rules": (out / ".cursor" / "rules" / "adaptoid.mdc").exists(),
                },
                "archetype": analysis["archetype"],
                "tier": analysis["tier"],
                "domain": analysis["domain"],
                "risk_fms": analysis["risk_fms"],
                "mcp_servers": stack["mcp"],
                "next": [
                    f"cd {out}",
                    "Fill PROJECT-INTENT.md success criteria if needed",
                    "Open your host (claude / cursor / codex / grok) in this directory",
                    "bash orchestrator/scripts/preflight.sh .",
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
