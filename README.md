<div align="center">

# Adaptoid OS
## Lite = one file · Core = this folder

[![Version](https://img.shields.io/badge/version-5.3.0-blue)](#)
[![CI](https://github.com/Srujan0798/Adaptoid-OS/actions/workflows/ci.yml/badge.svg)](https://github.com/Srujan0798/Adaptoid-OS/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-yellow)](#)

> Paste **Lite** or run **Core** with your brief → agent adapts the environment and ships with evidence.

[**USE**](USE.md) · [**Lite file**](ADAPTOID-LITE.md) · [FLOW](FLOW.md) · [PRODUCT](PRODUCT.md)

</div>

---

## The Problem

Agent projects fail from false “done”, lost handoff, and no ship gate — not from weak models.

---

## Quick Start

| | What | How |
|---|---|---|
| **Lite** | [`ADAPTOID-LITE.md`](ADAPTOID-LITE.md) | Paste + brief → complete |
| **Core** | This whole repo | Command below |

```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git && cd Adaptoid-OS

python3 adaptor/engine.py \
  --brief "YOUR real project idea" \
  --output ../my-project \
  --core-only --host all
```

Open `../my-project` in Grok Build / Claude / Cursor.  
`make ship-check` verifies the kit.

---

## Features

| Safety | Ship | Host |
|---|---|---|
| Failure modes + preflight | SDLC + intent lock + skills | Multi-host AGENTS/CLAUDE/Cursor |
| Evidence required | HOST-OPERATING-PLAYBOOK | Plan, worktrees, terminal, git, … |

---

## Why Adaptoid OS Wins

| | Typical | Adaptoid |
|---|---|---|
| Surfaces | Messy packs | **Lite file** or **Core folder** |
| Process | Ad-hoc chat | **SHIP SYSTEM** |
| Done | Hope | **Commands + preflight** |

---

## Architecture

```
Lite:  ADAPTOID-LITE.md  →  paste  →  adapt  →  complete
Core:  this folder       →  engine →  project →  complete
```

Full map: [FLOW.md](FLOW.md). Attic only: `docs/historical/`.

---

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT — [LICENSE](LICENSE)

---

<div align="center">

**⭐ Star this repo if it saves you from one agentic failure.**

</div>
