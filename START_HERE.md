# Start here — Adaptoid OS

**What this is:** a harness so AI coding agents finish *your* project with a **correct SDLC loop**.  
**What this is not:** a second IDE, a whiteboard app, or empty process docs.

Your **host** (Grok Build, Claude Code, Cursor, Codex, …) already has plan mode, subagents, skills, hooks, MCP, git, terminal, review, CI/headless.  
**Adaptoid** adds: intent, handoff, multi-host rules, validators, and SDLC gates.

## 60-second path

```bash
# 1. From this repo — YOUR real idea
python3 adaptor/engine.py \
  --brief "PASTE YOUR REAL PROJECT IDEA" \
  --output ../my-project \
  --core-only \
  --host all

# 2. SDLC task gates (plan → design → build → test → ship)
python3 conductor/conductor.py init-wave --project ../my-project --sdlc

# 3. Open ../my-project in Grok Build / Claude / Cursor / Codex and work the loop

# 4. Before claiming done
bash ../my-project/orchestrator/scripts/preflight.sh ../my-project
```

## SDLC (efficient)

| Stage | Do | Evidence |
|---|---|---|
| Plan / requirements | Fill intent | success criteria + falsification |
| Design | Light blueprint | `plan/design.md` or task design |
| Build | Code in `writes` only | git diff |
| Test | acceptance commands | exit 0 in report |
| Deploy / ship | preflight green | `preflight.sh` |
| Maintain | next wave | HANDOFF rewritten |

Details: `protocols/sdlc-loop.md` · Host map: `core/HOST-CAPABILITIES.md`

## Product ladder

| | Use |
|---|---|
| **Lite** | `reference/OS_SETUP_v1.3_full.md` |
| **Core** | command above — default |
| **Pro** | full repo + optional attic material |

## Kit health

```bash
make ship-check
```
