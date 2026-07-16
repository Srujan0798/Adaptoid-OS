# Adaptoid OS — Product (v5.1.2)

## One sentence

Portable **agent harness**: any host + any model → **SDLC gates** → projects that finish with evidence.

## Direct path

```bash
python3 adaptor/engine.py --brief "YOUR idea" --output ../proj --core-only --host all
python3 conductor/conductor.py init-wave --project ../proj --sdlc
```

Spine of every live file: [`FLOW.md`](FLOW.md).

## Shipped surfaces

| Surface | Path |
|---|---|
| Entry | `START_HERE.md` |
| Engine + hosts | `adaptor/` |
| Core kit | `core/` |
| Conductor SDLC | `conductor/` |
| Gates | `protocols/sdlc-loop.md` + preflight validators |
| Lite | `reference/OS_SETUP_v1.3_full.md` |

## Explicitly not live

Anything under `docs/historical/` (launch kits, research dumps, claw_bridge, skills, extra protocols, super-adaptoid validators).

## Kit health

```bash
make ship-check
```
