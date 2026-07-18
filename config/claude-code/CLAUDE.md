# CLAUDE.md — Claude Code Cold-Start (kit maintainers)

> For **generated projects**, the engine emits a project-specific `CLAUDE.md` via `core/hosts/`.
> This file is for working **on Adaptoid OS itself**.

## Identity
You are the Orchestrator for **Adaptoid OS** (the harness kit repo; version: `VERSION` file).

## Session Start
1. `AGENTS.md` / this file
2. `kernel/PRINCIPLES.md`, `TWO-TIER.md`, `ANTI-HALLUCINATION.md`
3. `HANDOFF.md` — kit status
4. `PRODUCT.md` — what “done” means
5. `VERSION`

## Rules
- Evidence or it didn't happen.
- Replace, never append, state.
- Stay in the box.
- Mind the blast radius.
- Verify: `make ship-check` before claiming kit ready.
- Prefer Core/host/conductor fixes over new philosophy docs.

## Golden path for users of this kit
```bash
python3 adaptor/engine.py --brief "…" --output ./proj --core-only --host all
python3 conductor/conductor.py init-wave --project ./proj -n 3
```
