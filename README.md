<div align="center">

# Adaptoid OS v5.1
## Portable agent harness — finish projects with any model + any host

[![Version](https://img.shields.io/badge/version-5.1.0-blue)](#)
[![CI](https://github.com/Srujan0798/Adaptoid-OS/actions/workflows/ci.yml/badge.svg)](https://github.com/Srujan0798/Adaptoid-OS/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-yellow)](#)

> **Adapt. Validate at runtime. Verify relentlessly. Compound carefully.**

**Model = weapon. IDE/CLI = field. Adaptoid = harness that adapts the field so the work finishes.**

[Start here](START_HERE.md) · [Product](PRODUCT.md) · [Index](INDEX.md)

</div>

---

## The Problem

Agentic projects fail the same ways: no handoff, false “done”, scope creep, wrong tools, silent errors, cold sessions with zero state.

Frameworks give primitives. **Adaptoid gives the control stack** — intent, handoff, validators, host files — so agents stay honest.

---

## Quick Start

```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git
cd Adaptoid-OS

python3 adaptor/engine.py \
  --brief "YOUR real project idea" \
  --output ../my-project \
  --core-only \
  --host all

# Open ../my-project in Claude / Cursor / Codex / Grok
bash ../my-project/orchestrator/scripts/preflight.sh ../my-project
```

| Layer | What |
|---|---|
| **Lite** | `reference/OS_SETUP_v1.3_full.md` — paste into any chat |
| **Core** | `--core-only` — default for real work |
| **Pro** | this repo + archived extras under `docs/historical/` |

Kit health: `make ship-check`

---

## Features

| Safety | Speed | Clarity |
|---|---|---|
| 18 failure modes + validators | Engine offline, no network | Typed `PROJECT-INTENT.md` |
| Preflight before “done” | Host emit in one flag | Progressive disclosure |
| Route / policy checks | Conductor wake/dispatch | Lean tree (bulk archived) |

---

## Why Adaptoid OS Wins

| Dimension | Typical frameworks | **Adaptoid OS** |
|---|---|---|
| Focus | Graphs / crews | **Harness / control stack** |
| Host lock-in | One vendor | **Claude + Cursor + Codex + Grok** |
| Done claims | Hope | **Evidence + preflight** |
| Cold start | Chat history | **HANDOFF.md files** |

---

## Architecture

```
Layer 2  Core product     engine · hosts · conductor · validators
Layer 1  Kernel           principles · two-tier · anti-hallucination
```

Optional archived material: `docs/historical/attic-v5.1-lean/`

---

## Folder Map (lean)

```
Adaptoid-OS/
├── START_HERE.md PRODUCT.md AGENTS.md HANDOFF.md
├── kernel/                 always-load laws
├── core/                   Core kit + host templates
├── adaptor/                engine + host_emit
├── conductor/              wake / dispatch / handoff
├── validators/             preflight + ship-check
├── templates/ archetypes/ failure-modes/
├── protocols/              core protocols only
├── reference/OS_SETUP…     Lite file
├── docs/historical/        attic (launch, research, extras)
└── tests/ benchmarks/ calibration/
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Filter: helps finish a project? prevents a failure mode? usable in 10 minutes?

---

## License

MIT — [LICENSE](LICENSE)

---

<div align="center">

**⭐ Star this repo if it saves you from one agentic failure.**

</div>
