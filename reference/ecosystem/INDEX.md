---
last-verified: 2026-06-11
confidence: corpus
---

# Ecosystem Library — Card Catalog

> The agentic-AI ecosystem, curated from trending repos (last 6 months) + leading practitioners. Read this first; pull the specific catalog file you need. See `../HOW-TO-PULL.md`.
>
> Legend: ⚡ = freshly verified from live source · (corpus) = from this project's accumulated May-2026 research.

## Catalog files
| File | Covers | Pull when |
|---|---|---|
| `coding-agents.md` | Claude Code, Cursor, Codex, Cline, Aider, Goose, Amp, OpenHands, Continue, oh-my-pi, Kiro, Factory | building software |
| `sdks-adks.md` | Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangGraph, DSPy, Pydantic AI, CrewAI, AutoGen | building an agent product/runtime |
| `protocols-standards.md` | MCP, A2A, agentskills.io, AGENTS.md/CLAUDE.md | always (universal) |
| `skills-catalog.md` | the 1000+ skill taxonomy + sources (mattpocock, Skills/, knowledge-work-plugins) | wiring skills |
| `memory-context.md` | Letta, Mem0, Graphiti, agentmemory, headroom, codegraph, compaction | memory/long-context matters |
| `optimizations.md` | token compression, caching, indexing, progressive disclosure, the latest perf wins | every project (cost/speed) |
| `knowledge-systems.md` | Obsidian, NotebookLM, RAG, second-brain, markitdown | knowledge/RAG/docs-heavy |
| `orchestration-multiagent.md` | orchestrator-workers, Ruflo, swarms, ADK graph workflows, parallelization | multi-agent / complex |
| `personal-agents.md` | OpenClaw, Hermes, nanobot, multi-channel companions | personal/multi-channel product |
| `people.md` | Karpathy, Boris Cherny, Simon Willison, Garry Tan/YC, mattpocock, ruvnet | learning the discipline |
| `SELECTION.md` | archetype → recommended stack | every setup (the decision engine) |
| `compatibility-adapters.md` | LangGraph, CrewAI, AutoGen, MetaGPT, LlamaIndex, ADK, DSPy | bridging to external frameworks |
| `hidden-gems.md` | 36 under-hyped tools/patterns with scoring rubric | evaluating lesser-known tools |
| `ecosystem-analysis.md` | 50+ project competitive landscape + positioning | positioning vs the broader ecosystem |
| `tools-compendium.md` | broad tool catalog by category | choosing your tool stack |
| `skills-registry.md` | skill sources and authoring guidance | selecting or authoring skills |
| `../workflows/fable-5-index.md` | 10 Fable 5 workflow patterns → OS-Setup assets | choosing a long-horizon workflow |

## The shape of the 2026 ecosystem (one-screen mental model)
```
              ┌─────────────────────────────────────────────┐
 STANDARDS    │  MCP (agent↔tools) · A2A (agent↔agent) ·     │  universal, pick-anything
              │  agentskills.io SKILL.md · AGENTS.md/CLAUDE  │
              └─────────────────────────────────────────────┘
 SURFACES     Claude Code · Cursor · Codex · Cline · Aider · Goose · Amp · OpenHands
              (where you actually work; all speak MCP + Skills)
 RUNTIMES     Claude Agent SDK · OpenAI Agents SDK · Google ADK · LangGraph · DSPy · Pydantic AI
              (when you BUILD an agent product, not just code in one)
 MEMORY       Letta · Mem0 · Graphiti · agentmemory  |  CONTEXT: headroom · codegraph · compaction
 KNOWLEDGE    Obsidian+SmartConnections · NotebookLM · RAG · markitdown
 ORCHESTRATION orchestrator-workers (default) · ADK graph · Ruflo swarm · parallel worktrees
 PERSONAL     OpenClaw · Hermes · nanobot (multi-channel companions)
```

## The 5 forces shaping 2026 (what every entry reflects)
1. **Skills > prompts.** Portable `SKILL.md` folders, progressive disclosure, 40+ compatible tools.
2. **Context is the bottleneck.** Compression (headroom), indexing (codegraph), memory (Letta) are now first-class.
3. **One config, many surfaces.** CLAUDE.md = AGENTS.md = .cursor/rules; write once, run in every IDE.
4. **Eval-driven.** pass@k / pass^k; tests-as-contract; transcript review.
5. **Brain/Hands/Session split.** Stateless brain, disposable hands, durable session log.

## How OS-Setup uses this
At setup, after archetype+tier: read `SELECTION.md`, pull the 2–4 matching files, choose tools, write an ADR, wire them in. Then close the books (don't keep them in context). See `../HOW-TO-PULL.md`.

## Freshness
Run `bash STALE_CHECK.sh [max_days]` to flag entries older than your threshold. Re-verify stale entries before relying on them (FM-12 applied to the library itself).
