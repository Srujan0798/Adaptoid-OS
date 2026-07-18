# Adaptoid Core

The **portable harness** that turns any coding agent into a project-finishing system.

Models are weapons. IDEs/CLIs/TUIs are the field. **Core is the loadout** that adapts the field to the project.

## Product surfaces

| Surface | What | When |
|---|---|---|
| **Lite** | Repo root **`ADAPTOID-LITE.md`** only | Paste into one chat; no clone |
| **Core** | **This whole repository** + `engine --core-only` | Every real multi-file project |

`reference/OS_SETUP_v1.3_*` is a **legacy stub** — not a product.

## What Core includes

1. **Kernel** (~2K tokens) — 12 laws, two-tier, anti-hallucination  
2. **Ship OS** — `SHIP-SYSTEM.md` + `HOST-OPERATING-PLAYBOOK.md`  
3. **Contracts** — `AGENTS.md`, `HANDOFF.md`, `PROJECT-INTENT.md`, `adaptoid.config.yaml`  
4. **Must-run validators** — handoff, status claims, silent failures, intent, preflight, …  
5. **Host adapters** — same source of truth → Claude / Cursor / Codex / Grok / AGENTS.md  

What Core **excludes**: anything under `docs/historical/` (attic only).

## Generate a Core project

```bash
python3 adaptor/engine.py \
  --brief "YOUR BRIEF" \
  --output ./my-project \
  --core-only \
  --host all
# --sdlc is default → 00-intent-lock … 07-maintain
```

Open `./my-project` → follow `SHIP-SYSTEM.md` + `HOST-OPERATING-PLAYBOOK.md` → finish with evidence.

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
  → SHIP-SYSTEM.md + HOST-OPERATING-PLAYBOOK.md
  → kernel/
  → HANDOFF.md
  → PROJECT-INTENT.md
  → adaptoid.config.yaml
  → work
  → bash orchestrator/scripts/preflight.sh before claiming done
```

## After generate

```bash
python3 conductor/conductor.py wake --project ./my-project
bash ./my-project/orchestrator/scripts/preflight.sh ./my-project
```

- Process: `protocols/sdlc-loop.md`
- Host tools: `HOST-CAPABILITIES.md` (in generated project) / this folder’s playbook
- Kit release gate: `make ship-check`

## Design rule

Before adding anything to Core, ask:

1. Does it help an agent finish a project on a host we don't control?  
2. Does it prevent a known failure mode with an executable check?  
3. Can a stranger use it in under 10 minutes?

If no → archive under `docs/historical/`, do not bloat the live tree.
