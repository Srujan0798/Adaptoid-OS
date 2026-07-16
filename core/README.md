# Adaptoid Core

The **minimum portable harness** that turns any coding agent into a project-finishing system.

Models are weapons. IDEs/CLIs/TUIs are the field. **Core is the loadout** that adapts the field to the project.

## Product ladder

| Layer | What | When to use |
|---|---|---|
| **Lite** | `reference/OS_SETUP_v1.3_full.md` | Paste into one chat; no clone |
| **Core** | This directory + engine `--core-only` | Every real project (default) |
| **Pro** | Full Adaptoid-OS repo | Teams, long waves, full FM library, v5 protocols |

## What Core includes

1. **Kernel** (~2K tokens) — 12 laws, two-tier, anti-hallucination  
2. **Contracts** — `AGENTS.md`, `HANDOFF.md`, `PROJECT-INTENT.md`, `adaptoid.config.yaml`  
3. **Must-run validators** — handoff, status claims, silent failures, intent, preflight, …  
4. **Host adapters** — same source of truth → Claude Code / Cursor / Codex / Grok / AGENTS.md  

What Core **excludes** (Pro only): super-adaptoid consciousness/evolution protocols, full research encyclopedias, multi-channel gateways, enterprise packs.

## Generate a Core project

```bash
# Core kit + all host surfaces
python3 adaptor/engine.py \
  --brief "48h hackathon: realtime collab whiteboard" \
  --output ./my-hackathon \
  --core-only \
  --host all

# Claude Code only
python3 adaptor/engine.py \
  --brief "Internship: NLP invoice extractor" \
  --output ./invoice-intern \
  --core-only \
  --host claude

# Cursor + generic agents
python3 adaptor/engine.py \
  --brief "CLI tool for log parsing" \
  --output ./logparse \
  --core-only \
  --host cursor,agents
```

## Host matrix

| Host flag | Emits |
|---|---|
| `agents` | `AGENTS.md` |
| `claude` | `CLAUDE.md`, `.claude/hooks/session-start.sh` |
| `cursor` | `AGENTS.md`, `.cursor/rules/adaptoid.mdc` |
| `codex` | `AGENTS.md` |
| `grok` | `AGENTS.md` |
| `all` | every host above |

See `MANIFEST.yaml` for the authoritative file list.

## Session loop (any host)

```
read AGENTS.md / CLAUDE.md
  → kernel/
  → HANDOFF.md
  → PROJECT-INTENT.md
  → adaptoid.config.yaml
  → work
  → bash orchestrator/scripts/preflight.sh before claiming done
```

## After generate — conductor

```bash
python3 conductor/conductor.py wake --project ./my-hackathon
python3 conductor/conductor.py init-wave --project ./my-hackathon -n 3
python3 conductor/conductor.py dispatch --project ./my-hackathon --mode stub
bash ./my-hackathon/orchestrator/scripts/preflight.sh ./my-hackathon
```

Release gate on the kit itself: `make ship-check`.

## Design rule

Before adding anything to Core, ask:

1. Does it help an agent finish a project on a host we don't control?  
2. Does it prevent a known failure mode with an executable check?  
3. Can a stranger use it in under 10 minutes?

If no to all three → put it in Pro, not Core.
