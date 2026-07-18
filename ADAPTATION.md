# ADAPTATION — how Adaptoid stays Adaptoid (v5.3.0)

> Multi-agent corner audit + live agentic-era research (2026-07-18).  
> **Adopt what compounds. Refuse framework theater.**

## Product (unchanged)

| Surface | Path |
|---|---|
| **Lite** | `ADAPTOID-LITE.md` |
| **Core** | this folder + `adaptor/engine.py` |

## What mid-2026 changed (industry)

1. **`AGENTS.md`** is the open project-law standard (AAIF / Linux Foundation; 60k+ repos).
2. **Agent Skills** (`SKILL.md` @ agentskills.io) = portable progressive procedures across Claude/Cursor/Codex/Grok/Gemini.
3. **MCP** is universal; security still host-dependent (**Codex: shell sandboxed, MCP often not**).
4. **Hooks + worktrees** are the hard parallel/enforcement layer (Claude/Grok/Codex), not more multi-agent frameworks.
5. Winners: **one strong agent + sparse subagents + evidence gates** — not CrewAI-as-OS.

## What we adapted into Core

| Adoption | Where |
|---|---|
| Skills emit (agentskills paths) | engine → `.agents/skills/*` + `.claude/skills/*` |
| Worktrees + soft/hard enforcement | `SHIP-SYSTEM` rows 19–22, playbook §3b, `HOST-CAPABILITIES` |
| Host matrix (not flat list only) | `core/HOST-CAPABILITIES.md` |
| `agent-product` archetype | `archetypes/agent-product.md` + engine signals |
| FM-19 cost runaway · FM-20 MCP trust | `failure-modes/` |
| Host-neutral TWO-TIER | `kernel/TWO-TIER.md` |
| Engine honesty (always Core) | `adaptor/engine.py` defaults + no hollow pro |
| Wake paths for generated layout | `validators/wake.sh` |
| Stack fill from archetype tables | `adaptoid.config.yaml` language/backend |

## What we refuse (bloat)

- Becoming LangGraph/CrewAI/AutoGen
- A2A multi-agent OS as Core
- Fat always-on per-host megaprompts
- Skills marketplace / protocol zoo on hot path
- Restoring attic “consciousness / super-prompt” packs

## Corner audit leftovers (next demand-gated)

| Item | Priority |
|---|---|
| Harden SDLC shell acceptances (no auto-pass theater) | P1 |
| `sha256sum` → portable hash on macOS emit_event/vault | P1 |
| Optional `--host gemini` + GEMINI.md | P2 |
| PreToolUse hook templates beyond SessionStart | P1 |
| Conductor optional worktree create flag | P2 |

## How to keep adapting

```
New agentic idea
  → FM + optional validator (executable)
  → short protocol or SHIP-SYSTEM row
  → archetype/engine signal if project-shape
  → skill SKILL.md if procedure
  → kernel PRINCIPLES only if universal + tiny
Never: dump attic wholesale onto hot path
```

Proof gate: `make ship-check`
