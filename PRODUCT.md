# Adaptoid OS — Product status (v5.1.3)

## Promise

> Hand **brief + Lite/Core/Pro** to any coding model → it runs **Adaptoid SHIP SYSTEM**:  
> full **SDLC (plan→maintain)** **fused with** host toolkit (plan mode, subagents, skills, hooks, MCP, AGENTS.md, memory, search, multi-file edit, git, reasoning, web, terminal, CI, review, sandbox, background tasks) → **adapts environment and completes the project with evidence**.

## Planned vs done

| Plan | Status |
|---|---|
| Model is swappable; harness is the product | **Done** |
| **Lite** — single md, paste into any chat | **Done** → `LITE.md` (+ deep `reference/OS_SETUP_v1.3_full.md`) |
| **Core** — engine generates multi-host project + validators | **Done** → `engine --core-only --host all --sdlc` |
| **Pro** — full repo (FMs, all validators, archetypes) | **Done** → engine without `--core-only` |
| Multi-host: AGENTS / CLAUDE / Cursor / Codex / Grok | **Done** |
| SDLC (GFG 7 stages) fused into product | **Done** → `core/SHIP-SYSTEM.md` + 7 stage tasks |
| Host toolkit (Grok Build list) activated by stage | **Done** → SHIP-SYSTEM §A + cold-start + task host-tools |
| Lean tree; orphans archived | **Done** → `FLOW.md` + `docs/historical/` |
| One user entry: hand kit + brief + “complete it” | **Done** → `USE.md` |
| Ship gate | **Done** → `make ship-check` |

## What “complete” means for a *user project*

Not “Adaptoid docs finished” — **their** internship/hackathon/product:

1. Environment adapted (intent, AGENTS, HANDOFF, tasks)  
2. Wave-1+ implemented with acceptance evidence  
3. Preflight green (Core/Pro)  
4. HANDOFF ready for next session  

Adaptoid **does not** write their business app alone without a host agent working the tasks — it **orients and gates** that agent.

## How to run (copy)

```bash
# Core (default)
python3 adaptor/engine.py --brief "…" --output ../proj --core-only --host all --sdlc

# Pro
python3 adaptor/engine.py --brief "…" --output ../proj --host all --sdlc

# Lite: paste LITE.md into the agent + brief + USE.md magic prompt
```

## Recommendations (next, only if needed)

| Priority | Improvement | Why |
|---|---|---|
| P1 | Real user dogfood on *your* brief | Proves end-to-end, not kit self-test |
| P2 | Optional one-line `install` that prints USE.md | Onboarding |
| P3 | Keep Lite deep file or freeze it | `OS_SETUP_v1.3_full.md` is long; `LITE.md` is the daily path |
| Skip | Multi-channel, enterprise, more protocols | Off-promise |

## Kit health

```bash
make ship-check
```
