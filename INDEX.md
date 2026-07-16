# Adaptoid OS INDEX — Progressive disclosure

> Load the minimum. Open the rest only when the trigger fires.

**Start:** [`START_HERE.md`](START_HERE.md) · **Product:** [`PRODUCT.md`](PRODUCT.md)

## Always load (~2K tokens)

| File | Why |
|---|---|
| `AGENTS.md` | cold-start |
| `kernel/PRINCIPLES.md` | 12 laws |
| `kernel/TWO-TIER.md` | orchestrator vs workers |
| `kernel/ANTI-HALLUCINATION.md` | evidence + state rules |
| `HANDOFF.md` | current truth |

## Core product (default path)

| Path | Load when |
|---|---|
| `adaptor/engine.py` | create a project from a brief |
| `adaptor/host_emit.py` | host adapters (Claude/Cursor/Grok/…) |
| `core/` | Core kit definition |
| `core/HOST-CAPABILITIES.md` | map host features (plan mode, MCP, …) → harness |
| `conductor/conductor.py` | wake / init-wave `--sdlc` / dispatch |
| `protocols/sdlc-loop.md` | correct Agile SDLC gates (not theater) |
| `workflows/core/sdlc-agile.yaml` | machine-readable stage map |
| `templates/` | project skeleton |
| `archetypes/` | project type |
| `validators/` | preflight / ship-check |
| `failure-modes/` | when a symptom appears |
| `reference/OS_SETUP_v1.3_full.md` | Lite single-file path |
| `schemas/ProjectIntent.schema.json` | intent validation |

## Generate a project

```bash
python3 adaptor/engine.py --brief "YOUR IDEA" --output ../proj --core-only --host all
python3 conductor/conductor.py init-wave --project ../proj --sdlc
```

## Load on trigger only

| Trigger | Path |
|---|---|
| Kit health | `make ship-check` |
| Benchmarks | `benchmarks/` |
| Calibration | `calibration/` |
| Framework export | `claw_bridge/` |
| Core protocols | `protocols/*.md` (blast-radius, verification, …) |
| Archived bulk | `docs/historical/attic-v5.1-lean/` |

## Do not load by default

Everything under `docs/historical/attic-v5.1-lean/` — launch kits, research dumps, optional protocol theater, extra examples.
