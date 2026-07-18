# Templates

> Sources the engine fills into a new project (archetype + tier). Never leave `{{placeholders}}` in generated files.

## Deep template bodies (Lite standalone)

Full filled examples for every major template live in the **Lite** file:

**[`../ADAPTOID-LITE.md`](../ADAPTOID-LITE.md)** — structure, FMs, archetypes, adaptor, invocation.

`reference/OS_SETUP_v1.3_full.md` is a **stub redirect** only — do not treat it as a template source.

## What gets generated where

| Project path | Notes |
|---|---|
| `AGENTS.md` / `CLAUDE.md` | Host cold-start from `core/hosts/*` |
| `SHIP-SYSTEM.md` | Copied from `core/SHIP-SYSTEM.md` |
| `HOST-OPERATING-PLAYBOOK.md` | Copied from `core/HOST-OPERATING-PLAYBOOK.md` |
| `HANDOFF.md` | Session continuity (FM-14) |
| `PROJECT-INTENT.md` | Goal, IN/OUT, tier |
| `work/*` | Wave tasks from conductor (`--sdlc` default) |
| `orchestrator/scripts/*` | Validators copied by engine |
| `plan/*` | Intent-lock + planning artifacts |

## Always copy validators

Engine copies `validators/*.sh` → project `orchestrator/scripts/`. Wire:

- pre-commit / CI: `preflight.sh`
- before claim-done: full preflight
- before dispatch: scope / disjoint checks when available

## Generation order

See root `FLOW.md` and `INDEX.md`.
