# Start here — Adaptoid OS

**What this is:** harness so agents finish *your* project with a **correct SDLC loop**.  
**What this is not:** a second IDE, demo apps, or disconnected docs.

**Host** (Grok Build / Claude / Cursor / Codex) = tools.  
**Adaptoid** = intent + SDLC gates + multi-host rules + proof of done.

## 60-second path

```bash
python3 adaptor/engine.py \
  --brief "PASTE YOUR REAL PROJECT IDEA" \
  --output ../my-project \
  --core-only --host all

python3 conductor/conductor.py init-wave --project ../my-project --sdlc

# Open ../my-project in your host and work PLAN→DESIGN→BUILD→TEST→SHIP
bash ../my-project/orchestrator/scripts/preflight.sh ../my-project
```

## SDLC gates

| Stage | Evidence |
|---|---|
| Plan | `PROJECT-INTENT.md` success + falsification |
| Design | light design / task briefs |
| Build | code under `writes` only |
| Test | acceptance exit 0 in report |
| Ship | `preflight.sh` green |
| Maintain | `HANDOFF.md` rewritten |

## Map of this repo

**Every live file is on the spine:** [`FLOW.md`](FLOW.md)

Also: `PRODUCT.md` · `protocols/sdlc-loop.md` · `core/HOST-CAPABILITIES.md` · `make ship-check`

Archived (not required): `docs/historical/`
