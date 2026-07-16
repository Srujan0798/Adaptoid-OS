# Adaptoid OS INDEX

> Progressive disclosure. Start at [`START_HERE.md`](START_HERE.md). Full spine: [`FLOW.md`](FLOW.md).

## Always load

| File | Why |
|---|---|
| `AGENTS.md` | cold-start |
| `kernel/PRINCIPLES.md` | 12 laws |
| `kernel/TWO-TIER.md` | orchestrator vs workers |
| `kernel/ANTI-HALLUCINATION.md` | evidence rules |
| `HANDOFF.md` | current truth |

## Product spine (in order)

| Step | Path |
|---|---|
| 0 | `START_HERE.md` · `PRODUCT.md` · `FLOW.md` |
| 1 | `adaptor/engine.py` + `adaptor/host_emit.py` |
| 2 | `core/` (hosts, templates, HOST-CAPABILITIES) |
| 3 | `conductor/conductor.py` (`init-wave --sdlc`) |
| 4 | `protocols/sdlc-loop.md` |
| 5 | `validators/preflight.sh` |
| 6 | `workflows/core/sdlc-agile.yaml` |

## Support (on trigger)

| Path | When |
|---|---|
| `archetypes/` | engine detects project type |
| `failure-modes/` | a failure symptom appears |
| `templates/` | engine copies skeleton |
| `tiers/TIERS.md` | size the project |
| `schemas/` | intent validation |
| `protocols/blast-radius.md` | remote/money/humans |
| `protocols/verification.md` | how to verify |
| `protocols/oap-security.md` | tool policy |
| `protocols/route-sentinel.md` | DAG transitions |
| `reference/OS_SETUP_v1.3_full.md` | Lite paste path |
| `make ship-check` | kit health |

## Generate

```bash
python3 adaptor/engine.py --brief "YOUR IDEA" --output ../proj --core-only --host all
python3 conductor/conductor.py init-wave --project ../proj --sdlc
bash ../proj/orchestrator/scripts/preflight.sh ../proj
```

## Archived (not in flow)

`docs/historical/` — do not load unless restoring deliberately.
