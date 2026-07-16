# Ecosystem — Memory & Context (the 2026 bottleneck)

> Context is THE constraint. These tools make agents remember across sessions and fit more useful signal in the window. Pull when long-context, cross-session memory, or large codebases are involved.

## Persistent memory
| Tool | What | Pick when | Source |
|---|---|---|---|
| **Letta** (ex-MemGPT) | stateful agents, memory blocks, self-improve over time; agentskills-compatible | agent needs durable identity/memory across sessions | github.com/letta-ai/letta (corpus) |
| **agentmemory** | ⚡ persistent memory for coding agents, "#1 on real-world benchmarks" — trending this month | give a coding agent cross-session recall | github (agentmemory) ⚡ |
| **Mem0** | memory layer, fast retrieval | app-level user memory | (corpus) |
| **Graphiti** | temporal knowledge-graph memory | relationships + time matter | (corpus) |

## Context compression / efficiency
| Tool | What | Win | Source |
|---|---|---|---|
| **headroom** | ⚡ compresses tool outputs + RAG chunks BEFORE they hit the LLM | **60–95% token reduction** — trending this month | github (headroom) ⚡ |
| **codegraph** | ⚡ pre-indexed code knowledge graph for Claude Code/Codex/Gemini/Cursor | agent navigates big repos without reading everything | github (codegraph) ⚡ |
| **Understand-Anything** | ⚡ code → interactive knowledge graph (Claude/Cursor/Copilot/Gemini) | onboarding to unfamiliar codebases | github ⚡ |
| **markitdown** | ⚡ any file/doc → clean Markdown for LLMs | prep messy inputs cheaply | github/microsoft (markitdown) ⚡ |
| **caveman skill** | ~75% token cut on summaries/handoffs | compaction | mattpocock (corpus) |

## The principle
Don't feed the model more — feed it BETTER. Three moves, in order of leverage:
1. **Index, don't dump.** codegraph/Understand-Anything so the agent fetches the 5 relevant files, not 500.
2. **Compress what you must send.** headroom on tool outputs/RAG; caveman on summaries; markitdown on raw docs.
3. **Persist what matters.** Letta/agentmemory/Mem0 so cross-session knowledge lives on disk, not re-derived.

## How OS-Setup uses this
- Maps directly onto FM-04 (context bloat) prevention.
- For large-codebase projects: recommend `codegraph` in the project's mcp.json / tooling.
- For RAG/tool-heavy agents: recommend `headroom` to cut cost 60–95%.
- For cross-session products: recommend Letta or `agentmemory`.
- The OS-Setup's own `events.jsonl` + `HANDOFF.md` are the lightweight built-in version of persistence; these tools are the upgrade path when the project needs more.

`verified: 2026-05 (headroom, codegraph, agentmemory, Understand-Anything, markitdown ⚡ this burst; Letta/Mem0/Graphiti corpus)`
