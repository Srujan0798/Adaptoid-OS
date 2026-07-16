# Adaptoid OS — Product Definition (v5.1)

## One sentence

A **portable agent harness** that adapts any coding host (Claude Code, Cursor, Codex, Grok, OpenCode, …) and any model so projects actually finish.

## What “100% product” means for v5.1

| Surface | Status | Proof |
|---|---|---|
| **Lite** — single paste file | Shipped | `reference/OS_SETUP_v1.3_full.md` |
| **Core** — min harness + hosts | Shipped | `core/` + `engine --core-only --host all` |
| **Pro** — full kit | Shipped | this repository |
| Host adapters | Shipped | agents / claude / cursor / codex / grok |
| Conductor runtime | Shipped | wake / init-wave / dispatch / handoff |
| Validators + dogfood | Shipped | `make ship-check` |
| Benchmarks | Shipped | `benchmarks/run_bench.sh` |
| Calibration (50) | Shipped | `calibration/cases.json` |
| CI | Shipped | `.github/workflows/ci.yml` |

## Not product (demand-gated — intentionally thin)

- Multi-channel Slack/Telegram gateway (`multi-channel/` stub only)
- Enterprise SOC2 packs
- Replacing LangGraph/CrewAI (bridges only)
- Model training

## Golden path (must always work)

```bash
python3 adaptor/engine.py --brief "…" --output ./proj --core-only --host all
python3 conductor/conductor.py init-wave --project ./proj -n 3
bash ./proj/orchestrator/scripts/preflight.sh ./proj
make ship-check   # on the kit itself
```

## Metaphor

| Layer | Role |
|---|---|
| Model | Weapon (swappable) |
| IDE / CLI / TUI | Field |
| MCP / skills / hooks | Loadout |
| **Adaptoid** | Harness that adapts the field to the mission |

## Version

See `VERSION` (semver of the kit). Kernel laws in `kernel/` change rarely; host adapters and engine evolve faster.
