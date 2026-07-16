#!/usr/bin/env python3
"""
Host adapters: one project truth → host-specific cold-start surfaces.

Supported hosts: agents, claude, cursor, codex, grok, all
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

HOSTS = ("agents", "claude", "cursor", "codex", "grok")
CORE_DIR = Path(__file__).resolve().parent.parent / "core"
HOSTS_DIR = CORE_DIR / "hosts"
TEMPLATES_DIR = CORE_DIR / "templates"


def parse_hosts(spec: str | None) -> list[str]:
    """Parse --host value: comma-separated or 'all'."""
    if not spec or not spec.strip():
        return ["agents", "claude"]
    parts = [p.strip().lower() for p in spec.split(",") if p.strip()]
    if "all" in parts:
        return list(HOSTS)
    unknown = [p for p in parts if p not in HOSTS]
    if unknown:
        raise ValueError(
            f"Unknown host(s): {', '.join(unknown)}. "
            f"Choose from: {', '.join(HOSTS)}, all"
        )
    # preserve order, unique
    seen = set()
    out = []
    for p in parts:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def _render(template: str, ctx: dict) -> str:
    out = template
    for key, val in ctx.items():
        out = out.replace("{{" + key + "}}", str(val))
    return out


def _read_tmpl(name: str) -> str:
    path = HOSTS_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Missing host template: {path}")
    return path.read_text(encoding="utf-8")


def build_context(
    *,
    project_name: str,
    goal: str,
    archetype: str,
    tier: str,
    host: str,
) -> dict:
    return {
        "PROJECT_NAME": project_name or "project",
        "GOAL": (goal or "").strip().replace("\n", " ")[:500],
        "ARCHETYPE": archetype or "internal-tool",
        "TIER": tier or "T1",
        "HOST": host,
        "DATE": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "COLD_START_TITLE": {
            "agents": "AGENTS.md — Cold-Start Contract",
            "claude": "CLAUDE.md — Claude Code Cold-Start",
            "cursor": "AGENTS.md — Cold-Start Contract (Cursor)",
            "codex": "AGENTS.md — Cold-Start Contract (Codex)",
            "grok": "AGENTS.md — Cold-Start Contract (Grok Build)",
        }.get(host, "AGENTS.md — Cold-Start Contract"),
    }


def emit_host(output_dir: Path, host: str, ctx_base: dict) -> list[str]:
    """Write host-specific files. Returns list of relative paths written."""
    written: list[str] = []
    ctx = {**ctx_base, "HOST": host, "COLD_START_TITLE": build_context(
        project_name=ctx_base.get("PROJECT_NAME", "project"),
        goal=ctx_base.get("GOAL", ""),
        archetype=ctx_base.get("ARCHETYPE", "internal-tool"),
        tier=ctx_base.get("TIER", "T1"),
        host=host,
    )["COLD_START_TITLE"]}

    cold = _render(_read_tmpl("cold_start.md.tmpl"), ctx)

    if host in ("agents", "codex", "grok", "cursor"):
        path = output_dir / "AGENTS.md"
        # cursor also wants AGENTS.md; last writer wins if multiple — same content
        path.write_text(cold, encoding="utf-8")
        written.append("AGENTS.md")

    if host == "claude":
        (output_dir / "CLAUDE.md").write_text(cold, encoding="utf-8")
        written.append("CLAUDE.md")
        hook_dst = output_dir / ".claude" / "hooks" / "session-start.sh"
        hook_dst.parent.mkdir(parents=True, exist_ok=True)
        hook_src = HOSTS_DIR / "session-start.sh"
        hook_dst.write_text(hook_src.read_text(encoding="utf-8"), encoding="utf-8")
        hook_dst.chmod(0o755)
        written.append(".claude/hooks/session-start.sh")

    if host == "cursor":
        mdc = _render(_read_tmpl("cursor.adaptoid.mdc.tmpl"), ctx)
        mdc_path = output_dir / ".cursor" / "rules" / "adaptoid.mdc"
        mdc_path.parent.mkdir(parents=True, exist_ok=True)
        mdc_path.write_text(mdc, encoding="utf-8")
        written.append(".cursor/rules/adaptoid.mdc")

    return written


def emit_hosts(output_dir: Path, hosts: Iterable[str], ctx_base: dict) -> list[str]:
    """Emit all requested hosts. Always ensures AGENTS.md exists for Core."""
    all_written: list[str] = []
    hosts = list(hosts)
    if not hosts:
        hosts = ["agents", "claude"]

    # Prefer writing AGENTS.md once via agents if any agents-like host present
    for h in hosts:
        all_written.extend(emit_host(output_dir, h, ctx_base))

    # Guarantee AGENTS.md for cold-start even if only --host claude
    if "AGENTS.md" not in all_written and not (output_dir / "AGENTS.md").exists():
        all_written.extend(emit_host(output_dir, "agents", ctx_base))

    # de-dupe preserve order
    seen = set()
    unique = []
    for p in all_written:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique


def write_core_handoff_and_index(output_dir: Path, ctx: dict) -> list[str]:
    """Write Core HANDOFF.md and INDEX.md from templates."""
    written = []
    for name in ("HANDOFF.md", "INDEX.md"):
        src = TEMPLATES_DIR / name
        if not src.exists():
            continue
        text = _render(src.read_text(encoding="utf-8"), ctx)
        (output_dir / name).write_text(text, encoding="utf-8")
        written.append(name)
    return written
