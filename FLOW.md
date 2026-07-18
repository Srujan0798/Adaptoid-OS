# FLOW — final product map

**Two surfaces. One spine. Start using.**

```
START_HERE / USE
       │
       ├── LITE  →  paste ADAPTOID-LITE.md + brief → adapt & complete
       │
       └── CORE  →  this whole folder
                      │
                      ▼
                 adaptor/engine.py  (--sdlc default)
                      │
                      ├── kernel/  core/SHIP-SYSTEM  HOST-OPERATING-PLAYBOOK
                      ├── templates/ archetypes/ failure-modes/
                      ├── AGENTS/CLAUDE + HANDOFF + INTENT
                      └── validators → preflight
                      │
                      ▼
                 conductor tasks: intent-lock → plan → … → maintain
                      │
                      ▼
                 host agent (Grok/Claude/Cursor) ships with evidence
```

---

## Lite

| | |
|---|---|
| **File** | **`ADAPTOID-LITE.md`** (repo root only) |
| **Desktop** | `~/Desktop/ADAPTOID-LITE.md` |
| **Not Lite** | `reference/OS_SETUP_v1.3_*` (legacy stub only) |

## Core (this folder)

| Area | Paths |
|---|---|
| Entry | `USE.md` `START_HERE.md` `PRODUCT.md` `FLOW.md` `README.md` |
| Engine | `adaptor/engine.py` `adaptor/host_emit.py` |
| Conductor | `conductor/conductor.py` |
| Ship OS | `core/SHIP-SYSTEM.md` `core/HOST-OPERATING-PLAYBOOK.md` `core/HOST-CAPABILITIES.md` |
| Kernel | `kernel/*` (always copied into projects) |
| Protocols | 5 spine files → copied into projects |
| Skills emit | `.agents/skills/*` (agentskills.io) into projects |
| Kit library | `templates/` `archetypes/` `failure-modes/` (kit-side; not full-copied) |
| Check | `validators/` → project `orchestrator/scripts/` |
| CI | `tests/` `benchmarks/` `calibration/` `.github/` |

## Ignore

`docs/historical/` — attic only. Do not load for normal use.
