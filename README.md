<div align="center">

# Adaptoid OS v5.1
## Portable agent harness — SDLC gates + any host

[![Version](https://img.shields.io/badge/version-5.1.2-blue)](#)
[![CI](https://github.com/Srujan0798/Adaptoid-OS/actions/workflows/ci.yml/badge.svg)](https://github.com/Srujan0798/Adaptoid-OS/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-yellow)](#)

> **One spine.** Plan → build → test → ship. Host does tools. Adaptoid does mission rules + proof.

[Start](START_HERE.md) · [Flow](FLOW.md) · [Product](PRODUCT.md)

</div>

---

## The Problem

Agent projects fail from false “done”, lost handoff, scope creep, and no test gate — not from missing models.

---

## Quick Start

```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git && cd Adaptoid-OS

python3 adaptor/engine.py \
  --brief "YOUR real project idea" \
  --output ../my-project \
  --core-only --host all

python3 conductor/conductor.py init-wave --project ../my-project --sdlc
# Open ../my-project in Grok Build / Claude / Cursor / Codex
bash ../my-project/orchestrator/scripts/preflight.sh ../my-project
```

| Layer | Path |
|---|---|
| **Lite** | `reference/OS_SETUP_v1.3_full.md` |
| **Core** | command above |
| **Archived** | `docs/historical/` (not on hot path) |

Kit health: `make ship-check`

---

## Features

| Safety | Flow | Host |
|---|---|---|
| Failure modes + preflight | Agile SDLC tasks | Multi-host emit |
| Intent + falsification | Conductor `--sdlc` | Use plan mode / MCP / git on host |
| Blast-radius + OAP | HANDOFF rewrite | AGENTS.md / CLAUDE.md |

---

## Why Adaptoid OS Wins

| | Typical stack | Adaptoid |
|---|---|---|
| Process | Ad-hoc chat | **SDLC gates with evidence** |
| Hosts | One vendor file | **Claude + Cursor + Codex + Grok** |
| Done | Hope | **preflight + reports** |
| Tree | Doc sprawl | **Single spine (`FLOW.md`)** |

---

## Architecture

```
Host tools (plan, subagents, skills, MCP, terminal, git)
        ▲
        │ guided by
Adaptoid spine: intent → SDLC tasks → validators → HANDOFF
```

Every live file is listed in [`FLOW.md`](FLOW.md).

---

## Folder Map

```
START_HERE / FLOW / PRODUCT / AGENTS / HANDOFF
kernel/  core/  adaptor/  conductor/
protocols/   (sdlc + 4 safety/verify)
templates/ archetypes/ failure-modes/ validators/
reference/OS_SETUP…   workflows/core/sdlc-agile.yaml
tests/ benchmarks/ calibration/
docs/historical/   ← attic only
```

---

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md) — only changes that stay on `FLOW.md`.

## License

MIT — [LICENSE](LICENSE)

---

<div align="center">

**⭐ Star if it stops one false “done”.**

</div>
