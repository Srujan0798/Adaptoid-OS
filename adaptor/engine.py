#!/usr/bin/env python3
"""
OS-Setup Adaptor Engine — The Adaptoid.
Feed it (this DevKit + a project brief) and it analyzes the target,
pulls exactly the relevant components, and emits an executable, tailored setup.

Usage:
    python3 adaptor/engine.py --brief "Convert RFQ PDFs to structured BOQ" \
        --deadline "2 weeks" --audience "team" --output ./my-project

The engine is sovereign: needs no network, no daemon, no git.
"""
import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# ─── paths relative to this file ───
ENGINE_DIR = Path(__file__).parent.resolve()
OS_SETUP_ROOT = ENGINE_DIR.parent


def log(msg: str):
    print(f"[adaptoid] {msg}", file=sys.stderr)


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
    # Default per archetype
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

    # Infer domain from archetype
    domain_map = {
        "research-ml": "ML", "nlp-pipeline": "NLP", "saas-product": "web",
        "internal-tool": "web", "cli-tool": "systems", "data-pipeline": "data",
        "hackathon": "varies", "startup-mvp": "web",
    }
    domain = domain_map.get(archetype, "general")

    # Detect tech stack hints
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

    # Risk profile = failure modes most likely
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
    }


# ═══════════════════════════════════════════════════════════════════════════════
# 3. PULL — consult ecosystem library
# ═══════════════════════════════════════════════════════════════════════════════
def pull_ecosystem(analysis: dict) -> dict:
    """Read SELECTION.md, return recommended stack."""
    log("PULL: consulting ecosystem/SELECTION.md")
    selection_path = OS_SETUP_ROOT / "reference" / "ecosystem" / "SELECTION.md"
    # We don't parse markdown deeply; we return the archetype's known defaults
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
def copy_templates(tier: str, output_dir: Path):
    """Copy template skeleton based on tier."""
    templates = OS_SETUP_ROOT / "templates"
    dirs_to_copy = ["root", "work", "specify", "plan", "docs", "orchestrator"]
    if tier in ("T2", "T3", "T4"):
        dirs_to_copy += ["evals"]
    if tier in ("T3", "T4"):
        dirs_to_copy += ["ci"]

    for d in dirs_to_copy:
        src = templates / d
        if src.exists():
            dst = output_dir / d
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            log(f"  copied template: {d}")


def write_config(analysis: dict, brief: str, output_dir: Path):
    """Write adaptoid.config.yaml."""
    cfg_path = output_dir / "adaptoid.config.yaml"
    content = f"""---
project:
  name: "project"
  goal: "{brief[:120]}"
  domain: "{analysis['domain']}"

archetype: "{analysis['archetype']}"
tier: "{analysis['tier']}"

stack:
  language: ""
  backend: ""
  frontend: ""
  database: ""
  extras: []

compliance: []
mcp_servers: {json.dumps(pull_ecosystem(analysis)['mcp'])}

orchestrator:
  model: "claude-or-kimi"
  auto_mode: false

workers:
  tool: "opencode-cli"
  max_parallel: 5

waves:
  active: "wave-1"
  total_planned: 0
  shipped: 0

adapted_at: "{datetime.now(timezone.utc).isoformat()}Z"
last_verified: "{datetime.now(timezone.utc).isoformat()}Z"
version: "1.0"
"""
    cfg_path.write_text(content)
    log(f"  wrote {cfg_path.name}")


def copy_validators(output_dir: Path):
    """Copy validators into orchestrator/scripts/."""
    src = OS_SETUP_ROOT / "validators"
    dst = output_dir / "orchestrator" / "scripts"
    dst.mkdir(parents=True, exist_ok=True)
    for f in src.glob("*.sh"):
        shutil.copy2(f, dst / f.name)
    log(f"  copied {len(list(src.glob('*.sh')))} validators → orchestrator/scripts/")


def compose(analysis: dict, brief: str, output_dir: Path):
    """Generate the full project structure."""
    log("COMPOSE: generating project structure")
    output_dir.mkdir(parents=True, exist_ok=True)
    copy_templates(analysis["tier"], output_dir)
    write_config(analysis, brief, output_dir)
    copy_validators(output_dir)
    # Write ADR stub
    adr = output_dir / "docs" / "decisions" / "0002-stack-selection.md"
    adr.parent.mkdir(parents=True, exist_ok=True)
    adr.write_text(f"""# ADR 0002 — Stack Selection

| Decision | Why | Rejected |
|---|---|---|
| Archetype: {analysis['archetype']} | Detected from brief signals | — |
| Tier: {analysis['tier']} | Smallest that fits | — |
| MCP: {', '.join(pull_ecosystem(analysis)['mcp'])} | Minimal viable tools | Others from SELECTION.md |

Highest-risk failure modes for this archetype: {', '.join(analysis['risk_fms'])}
""")
    log(f"  wrote {adr}")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. RECORD — already done in COMPOSE (ADR written)
# ═══════════════════════════════════════════════════════════════════════════════


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
    parser = argparse.ArgumentParser(description="OS-Setup Adaptor Engine")
    parser.add_argument("--brief", required=True, help="Project brief (one line or paragraph)")
    parser.add_argument("--output", required=True, help="Output directory for generated project")
    parser.add_argument("--deadline", default="", help="Deadline context")
    parser.add_argument("--audience", default="", help="Who will see it")
    parser.add_argument("--tech", default="", help="Tech preference")
    parser.add_argument("--skip-verify", action="store_true", help="Skip preflight verification")
    args = parser.parse_args()

    context = {
        "deadline": args.deadline,
        "audience": args.audience,
        "tech": args.tech,
    }

    # 1. INGEST
    data = ingest(args.brief, context)

    # 2. ANALYZE
    analysis = analyze(args.brief, context)
    log(f"  archetype={analysis['archetype']}  tier={analysis['tier']}  domain={analysis['domain']}")
    if analysis["ask"]:
        log(f"  NEEDS CLARIFICATION: {analysis['ask']}")
        sys.exit(1)

    # 3. PULL
    stack = pull_ecosystem(analysis)
    log(f"  stack: MCP={stack['mcp']}  skills={stack['skills']}")

    # 4. COMPOSE
    out = Path(args.output).resolve()
    compose(analysis, args.brief, out)

    # 5. RECORD — ADR already written in compose

    # 6. VERIFY
    if not args.skip_verify:
        if not verify(out):
            log("VERIFY FAILED — fix above before declaring ready")
            sys.exit(1)

    # Done
    print(json.dumps({
        "status": "READY",
        "output_dir": str(out),
        "archetype": analysis["archetype"],
        "tier": analysis["tier"],
        "domain": analysis["domain"],
        "risk_fms": analysis["risk_fms"],
        "mcp_servers": stack["mcp"],
        "next": f"cd {out} && claude  # or kimi",
    }, indent=2))


if __name__ == "__main__":
    main()
