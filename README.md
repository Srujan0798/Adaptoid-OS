<div align="center">

# Adaptoid OS
## Agent harness — Lite (standalone md) · Core (this folder)

[![Version](https://img.shields.io/badge/version-5.1.5-blue)](#)
[![CI](https://github.com/Srujan0798/Adaptoid-OS/actions/workflows/ci.yml/badge.svg)](https://github.com/Srujan0798/Adaptoid-OS/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-yellow)](#)

> Hand a **project brief** + **Lite file** or **this Core folder** → model adapts the environment and ships with evidence.

[Use it](USE.md) · [Lite file](reference/OS_SETUP_v1.3_full.md) · [SHIP SYSTEM](core/SHIP-SYSTEM.md) · [Flow](FLOW.md)

</div>

---

## The Problem

Agent projects fail from false “done”, lost handoff, and no test/ship gate — not from missing models.

---

## Quick Start

**Two products only:**

| | What | Where |
|---|---|---|
| **Lite** | **Standalone markdown** (original OS-Setup) | [`reference/OS_SETUP_v1.3_full.md`](reference/OS_SETUP_v1.3_full.md) |
| **Core** | **This entire repository** | engine, SHIP-SYSTEM, validators, archetypes, … |

**Lite:** paste `reference/OS_SETUP_v1.3_full.md` + brief → “Use Adaptoid. Complete it.”  

**Core:**
```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git && cd Adaptoid-OS

python3 adaptor/engine.py \
  --brief "YOUR real project idea" \
  --output ../my-project \
  --core-only --host all
# --sdlc is default (7 GFG stages). --no-sdlc to skip.
```

Open `../my-project` in Grok Build / Claude / Cursor.  
Full recipes: **[`USE.md`](USE.md)** · Kit health: `make ship-check`

---

## Features

| Safety | Ship OS | Host |
|---|---|---|
| Failure modes + preflight | GFG SDLC 7 stages | Multi-host AGENTS/CLAUDE/Cursor |
| Intent + falsification | Required host tools per stage | Plan mode, subagents, MCP, git, … |
| Blast-radius + OAP | `SHIP-SYSTEM.md` | Evidence before “done” |

---

## Why Adaptoid OS Wins

| | Typical | Adaptoid |
|---|---|---|
| Surfaces | Confused packs | **Lite file** or **Core folder** |
| Process | Ad-hoc chat | **SDLC × host toolkit** |
| Done | Hope | **preflight + reports** |

---

## Architecture

```
Lite:  OS_SETUP_v1.3_full.md  →  paste → adapt → complete
Core:  this folder → engine --sdlc → project → SHIP-SYSTEM → complete
```

Every live file: [`FLOW.md`](FLOW.md). Archived only: `docs/historical/`.

---

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md) — stay on FLOW.md.

## License

MIT — [LICENSE](LICENSE)

---

<div align="center">

**⭐ Star this repo if it saves you from one agentic failure.**

</div>
