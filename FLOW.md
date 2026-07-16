# Product flow — every live path is on this spine

> If a file is not listed here and not under `docs/historical/`, it is a bug.  
> **One flow.** No side timelines.

```
USE.md / START_HERE.md / LITE.md
    │
    ├── Lite: paste LITE.md + brief → agent adapts & completes
    │
    ▼ Core/Pro:
adaptor/engine.py --sdlc ──host──►  AGENTS.md / CLAUDE.md / Cursor rules
    │                          (core/hosts/*)
    ├── kernel/                always-load laws
    ├── core/                  kit + HOST-CAPABILITIES
    ├── templates/             project skeleton
    ├── archetypes/            brief → type
    ├── PROJECT-INTENT + HANDOFF + config
    ├── protocols/sdlc-loop.md + 4 security/verify protocols
    └── validators/  ──► preflight.sh
              │
              ▼
conductor/conductor.py  init-wave --sdlc → work/wave-1/tasks
              │
              ▼
     PLAN → DESIGN → BUILD → TEST → SHIP (preflight)
              │
              ▼
     rewrite HANDOFF → next wave
```

## Live inventory (product tree only)

### Entry
| Path | Role |
|---|---|
| `USE.md` | **how to hand Lite/Core/Pro + brief to a model** |
| `LITE.md` | paste-only Lite kit |
| `START_HERE.md` | short entry |
| `PRODUCT.md` | planned vs done |
| `FLOW.md` | this map |
| `INDEX.md` | progressive disclosure |
| `AGENTS.md` / `HANDOFF.md` | kit cold-start + state |
| `README.md` | GitHub front door |
| `VERSION` | semver |

### Runtime (executable)
| Path | Role |
|---|---|
| `adaptor/engine.py` | brief → project |
| `adaptor/host_emit.py` | host surfaces |
| `conductor/conductor.py` | SDLC tasks / dispatch / wake |
| `scripts/bootstrap.sh` | thin wrapper → engine |
| `scripts/ship_check.sh` | kit release gate |
| `scripts/healthcheck.sh` | health |
| `install.sh` | clone + dogfood |
| `Makefile` | make ship-check / test / … |

### Generated-project inputs
| Path | Role |
|---|---|
| `kernel/*` | laws |
| `core/*` | Core kit + host templates |
| `templates/*` | skeleton |
| `archetypes/*` | type detection |
| `failure-modes/*` | scar library |
| `schemas/ProjectIntent.schema.json` | intent schema |
| `tiers/TIERS.md` | T0–T4 |
| `protocols/sdlc-loop.md` | SDLC gates |
| `protocols/blast-radius.md` | safety |
| `protocols/verification.md` | verify layers |
| `protocols/oap-security.md` | tool policy |
| `protocols/route-sentinel.md` | DAG routes |
| `workflows/core/sdlc-agile.yaml` | stage machine |
| `reference/OS_SETUP_v1.3_full.md` | Lite paste path |
| `reference/ecosystem/SELECTION.md` | stack defaults |
| `config/claude-code/*` | kit maintainer Claude |

### Validators (preflight + kit)
All under `validators/` — only scripts wired by `preflight.sh`, `dogfood.sh`, or Core copy list.

### Quality / CI
| Path | Role |
|---|---|
| `tests/*` | host emit + conductor + dogfood |
| `benchmarks/*` | speed/correctness |
| `calibration/*` | harness calibration smoke |
| `.github/workflows/ci.yml` | CI |

### Meta (OSS)
LICENSE, SECURITY, CONTRIBUTING, CODE_OF_CONDUCT, CHANGELOG, ROADMAP, `.cursorrules`, issue templates

## Not live (archived on purpose)

Everything under `docs/historical/` — old launch kits, research dumps, super-adaptoid, claw_bridge, skills, extra protocols/validators, etc.

Restore only by copying out of attic when a real need appears.
