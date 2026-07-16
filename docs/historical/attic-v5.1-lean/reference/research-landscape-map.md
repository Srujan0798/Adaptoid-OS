# 🗺️ references/landscape-map.md

> *The full landscape map of the agentic AI ecosystem as of mid-2026, with
> extraction notes per item. The Adaptoid-OS DevKit is built on top of
> this map; every "best-of-breed" picked has been measured against the
> alternatives. This is the bibliography behind the choices.*

---

## 0. The frame

The agentic AI ecosystem in mid-2026 has ~9 distinct layers. Each layer has
2–10 notable projects. The Adaptoid picks the best-of-breed per layer and
makes the choices *swappable* via `profiles/` and `.env`. The map below
is the *evidence* for those picks.

| Layer                              | Best-of-breed (Adaptoid default) | Notable alternatives                          |
| ---------------------------------- | -------------------------------- | --------------------------------------------- |
| **LLM gateway / router**           | LiteLLM                          | OpenRouter, Portkey, custom                    |
| **Local LLM runtime**              | Ollama                           | vLLM, LM Studio, llama.cpp                     |
| **Cloud LLM**                      | OpenAI + Anthropic + Google      | Azure OpenAI, Bedrock, Vertex, Groq            |
| **Orchestration / harness**        | LangGraph                        | OpenAI Agents SDK, Claude Agent SDK, Letta     |
| **Structured outputs**             | Pydantic AI                      | BAML, Instructor, Outlines, Zod                |
| **Tool-use protocol**              | MCP (Linux Foundation Agentic AI Foundation) | Function calling (legacy)         |
| **Multi-agent protocol**           | A2A (Google)                     | Direct, in-process, ACP (IBM), AGNTCY (Cisco)  |
| **Skills standard**                | Agent Skills (open std, Dec 2025)| Custom prompts, function-calling definitions   |
| **Memory: working**                | In-context + state graph         | —                                              |
| **Memory: semantic (vector)**      | Qdrant                           | Weaviate, Pinecone, Milvus, Chroma, pgvector   |
| **Memory: episodic / graph**       | Letta (default) / Zep (Graphiti) | Mem0, Cognee, MemGPT, OpenMemory, Hindsight   |
| **Memory: bank**                   | Markdown + SQLite FTS            | Notion, Obsidian, custom                       |
| **Durable execution**              | Inngest (default)                | Temporal, Restate, DBOS                        |
| **Observability**                  | Langfuse                         | LangSmith, Logfire, Phoenix, Arize, Laminar    |
| **Eval**                           | Promptfoo + DeepEval             | Inspect (UK AISI), custom                      |
| **Self-improving**                 | DSPy                             | TextGrad, ADAS, GEPA, SPO, OPRO                |
| **Browser use**                    | Stagehand                        | Browser-Use, Anthropic Computer Use, Operator  |
| **Editor / harness**               | Claude Code                      | Cursor, Codex CLI, Aider, Goose, Amp           |
| **Terminal multiplexer**           | tmux                             | zellij, WezTerm, iTerm2                        |
| **Secret management**              | 1Password CLI / sops             | HashiCorp Vault, Doppler, age                  |

Each row is detailed below with extraction notes.

---

## 1. LLM gateway

### LiteLLM (default)
- **Repo:** github.com/BerriAI/litellm
- **Stars (mid-2026):** 28k+
- **Why picked:** The single best abstraction over OpenAI, Anthropic, Google,
  Bedrock, Vertex, Azure, Groq, Mistral, Cohere, DeepSeek, xAI, Ollama,
  vLLM, etc. Single `/chat/completions` and `/responses` endpoint. OTel
  instrumented. Streaming, function calling, structured outputs, vision,
  audio. Mature.
- **Strengths:** Universal model support. Drop-in OpenAI replacement. Cost
  tracking. Fallback chains.
- **Weaknesses:** Some advanced features lag vendor-specific SDKs. Config
  is YAML-heavy.
- **Adaptoid integration:** The default gateway. Every Adaptoid node talks
  to `http://litellm:4000/v1` regardless of provider.
- **Extraction notes:** Use `config.yaml` for model definitions, fallbacks,
  and per-route overrides. Enable OTel export. Set `LITELLM_MASTER_KEY`
  as the bearer.

### Alternatives considered
- **OpenRouter** — great for "any model" routing, but fewer enterprise
  features (no OTel, no per-team cost allocation).
- **Portkey** — strong observability, weaker gateway.
- **Custom gateway** — too much yak-shaving for the median builder.

---

## 2. Local LLM runtime

### Ollama (default)
- **Repo:** github.com/ollama/ollama
- **Stars:** 95k+
- **Why picked:** The simplest local LLM runtime. One binary, one
  `ollama pull`, one `ollama run`. Apple Silicon native (very fast on
  M-series). CUDA support. OpenAI-compatible API. Modelfile for
  customization. Active community.
- **Strengths:** Zero-config. Wide model library. Fast.
- **Weaknesses:** Less control over inference (vLLM has more knobs).
  Some models don't quantize well.
- **Adaptoid integration:** The default `local_runtime`. Auto-warm at
  bootstrap. `OLLAMA_PRIMARY` is the default; `OLLAMA_FALLBACK` is the
  downgrade.
- **Extraction notes:** Pre-warm the model with a 1-token completion at
  bootstrap. The first real call would otherwise pay a 30–60s cold-start
  tax.

### vLLM (alternative for high-throughput)
- **Repo:** github.com/vllm-project/vllm
- **Stars:** 30k+
- **Why picked:** When you need *throughput* (multiple concurrent users,
  batched generation, PagedAttention). Used by serving production
  workloads.
- **When to pick:** Production serving with high QPS.
- **Adaptoid integration:** Swap in via `local_runtime: vllm` in
  `PROJECT-INTENT.md`. The compose file ships a `vllm` service.

### LM Studio (alternative for dev)
- GUI-based, very easy. Less scriptable than Ollama.

---

## 3. Cloud LLM

### OpenAI
- **Models (mid-2026):** GPT-4o, GPT-4.1, o3, o4-mini, GPT-5 family (per latest
  release). Strongest general capability, best function-calling.
- **Adaptoid integration:** `OPENAI_API_KEY` routes through LiteLLM.

### Anthropic
- **Models:** Claude Opus 4, Sonnet 4, Haiku 4. Strongest on long-context,
  tool use, agentic tasks. The reference model for many agent benchmarks.
- **Adaptoid integration:** `ANTHROPIC_API_KEY` routes through LiteLLM.

### Google
- **Models:** Gemini 2.5 Pro, Flash, Flash-Lite. Strong multimodal. Best
  price/performance at scale.
- **Adaptoid integration:** `GOOGLE_API_KEY` routes through LiteLLM.

### Why all three?
- The Adaptoid's cost router escalates between providers, not just between
  sizes.
- Different model families for cross-check (verifier is a *different family*
  than the worker).
- Vendor-lock prevention.

---

## 4. Orchestration / harness

### LangGraph (default for the runtime)
- **Repo:** github.com/langchain-ai/langgraph
- **Stars:** 8k+ on the core repo (LangChain has 100k+)
- **Why picked:** The most production-grade state-graph orchestrator.
  Cycles, branches, human-in-the-loop, durable, observable, integrated
  with LangSmith.
- **Strengths:** Real production deployments (Klarna, Replit, etc.).
  State persistence via checkpoints. Subgraph composition. Send API for
  fan-out. Human-in-loop primitives.
- **Weaknesses:** Steep learning curve. The "graph" abstraction can be
  over-engineered for simple cases.
- **Adaptoid integration:** The Adaptoid Engine runtime (`config/controller`)
  is implemented as a LangGraph state graph. The cold-start contract is
  a node at index 0; the controller loop is the rest of the graph.

### OpenAI Agents SDK (alternative)
- **Why picked:** First-class OpenAI-native. Built-in tracing, handoffs,
  guardrails, MCP support. Great for OpenAI-only setups.
- **When to pick:** OpenAI-only stack, simple multi-agent.

### Claude Agent SDK (alternative, for Anthropic stacks)
- **Why picked:** First-class Claude-native. Skills, MCP, Computer Use,
  sub-agents. The reference for the Skills standard.
- **When to pick:** Anthropic-only stack, heavy Skills usage.

### Letta (alternative, memory-centric)
- **Why picked:** Memory is the primary abstraction. Stateful agents with
  long-term memory as a first-class concept. Open-source.
- **When to pick:** Memory is the bottleneck.

### CrewAI
- **Why picked:** Role-based "crews". High abstraction. Quick to start.
- **Weaknesses:** Less explicit control over state. Harder to debug.

### AutoGen (Microsoft)
- **Why picked:** Multi-agent conversation. Mature. Microsoft backing.
- **Weaknesses:** Conversation-centric, less graph-friendly than LangGraph.

### Smolagents (Hugging Face)
- **Why picked:** ~1000 lines of code. CodeAgent that *writes code* to
  route. Very transparent.
- **When to pick:** Teaching, small prototypes, code-execution agents.

### Pydantic AI
- **Why picked:** Type-safe agents. Pydantic-typed inputs/outputs. MCP
  support. The default for *structured outputs* in Adaptoid.

### Agno (formerly Phi-Data)
- **Why picked:** Great developer experience. Clean abstractions.

### Atomic Agents
- **Why picked:** Lego-style building blocks. Strong structure + control.
  Single-author focus.

### Mastra
- **Why picked:** JavaScript / TypeScript native. From the Gatsby team.

### Google Agent Development Kit (ADK)
- **Why picked:** First-party Google. Gemini-native. A2A support.

### Why Adaptoid doesn't pick one
The Adaptoid Engine is **harness-agnostic**. The `preferences.harness`
field in `PROJECT-INTENT.md` selects which one. The cold-start contract
and the verification regime are the same.

---

## 5. Structured outputs

### Pydantic AI (default)
- **Repo:** github.com/pydantic/pydantic-ai
- **Stars:** 8k+
- **Why picked:** Type-safe agents with Pydantic-typed inputs/outputs.
  MCP-friendly. The default in the Adaptoid reference runtime.
- **Strengths:** Type safety as a first-class concept. Streaming typed
  outputs. Validation errors become the diagnostic.

### BAML
- **Repo:** github.com/BoundaryML/baml
- **Why picked:** Multi-language. Schema-as-tests. Stronger for
  multi-language codebases (TS, Go, Rust + Python).

### Instructor
- **Why picked:** Drop-in structured outputs for any OpenAI-compatible
  API. Lightest.

### Outlines
- **Why picked:** Constrained generation (regex / JSON schema / CFG) for
  *guaranteed* format. Use when tool calls must be exact.

### Zod
- **Why picked:** TypeScript / Node side. Mirror the Python types, do
  not drift.

---

## 6. Tool-use protocol

### MCP — Model Context Protocol (default; canonical)
- **Origin:** Anthropic, Nov 2024. Donated to the Linux Foundation's
  **Agentic AI Foundation** in Sept 2025.
- **Spec:** 1.0 (Nov 2025). 17 SEPs in the 1.0 release.
- **Adoption:** OpenAI Agents SDK, Claude Agent SDK, Google ADK, Cursor,
  VS Code, Cline, Continue, Block (goose), and 1000s of MCP servers.
- **Why picked:** The de facto standard. JSON-RPC 2.0 over stdio / HTTP
  / SSE. Client / server. Resource, tool, prompt, sampling primitives.
- **Adaptoid integration:** The Adaptoid stack ships MCP servers for
  memory (`mcp-memory`), filesystem (`mcp-filesystem`), git (`mcp-git`),
  shell (`mcp-shell`), plus the user can add their own. The
  `core.evidence-collect` skill uses MCP calls as the *default evidence
  substrate* — the single biggest lever against "I made up an API"
  hallucinations.
- **Risk noted:** MCP has known attack vectors (Sept 2025 paper,
  arxiv:2506.02040). The Adaptoid stack sandboxes every MCP server.

### Function calling (legacy)
- OpenAI-style JSON tool definitions. Still supported, but MCP is the
  upgrade path.

---

## 7. Multi-agent protocol

### A2A — Agent2Agent (default; canonical)
- **Origin:** Google, April 9, 2025.
- **Spec:** v1.x.
- **Adoption:** 50+ partners (Atlassian, Salesforce, SAP, PayPal, …),
  Microsoft (May 2025), Linux Foundation, AGNTCY (Cisco).
- **Why picked:** The de facto standard for agent-to-agent
  communication. JSON over HTTP/SSE. Agent Cards (capability
  discovery), Tasks (state management), Parts (multi-modal).
- **Complementary to MCP:** A2A is horizontal (agent ↔ agent); MCP is
  vertical (agent ↔ tool).
- **Adaptoid integration:** Used when 2+ Adaptoids are in play (multi-agent
  workflows, A2A-compatible `adaptoid-memory-agent`).

### ACP — Agent Communication Protocol (IBM)
- Alternative. Less adopted.

### AGNTCY (Cisco)
- "Internet of Agents" initiative. Specs + reference impls.

### Why Adaptoid uses A2A
The cross-agent memory pattern (§6.1 in `MEMORY-INDEX.md`) maps cleanly
onto A2A. The `MemoryRef` field in messages is a typed pointer into the
shared memory bank.

---

## 8. Skills standard

### Agent Skills (Anthropic, open standard)
- **Origin:** Anthropic, Oct 16, 2025. Open standard at `agentskills.io`
  on Dec 18, 2025.
- **Format:** Folder with `SKILL.md` (YAML frontmatter + Markdown body).
  Progressive disclosure: L1 metadata, L2 instructions, L3+ resources.
- **Adoption:** Claude Code, Claude API, Claude.ai, Microsoft Azure AI
  Studio, GitHub Copilot Workspace, Cursor (first full AI IDE adopter),
  VS Code, Goose, Amp, 85k+ skills, 27+ platforms (Feb 2026).
- **Why picked:** The de facto open standard. Folder-based, versioned,
  testable, MCP-compatible.
- **Adaptoid integration:** Every Adaptoid skill is a folder with
  `SKILL.md`. Adaptoid *extends* the format with `last_verified`,
  `test/`, `model`, `evidence_requirements`, `route_constraints`.

### Custom prompts
- Legacy. The Adaptoid stack treats them as "skills" too, but with
  weaker guarantees.

---

## 9. Memory systems

This is the layer with the most active controversy in the ecosystem.
The Mem0 / Letta fight (Aug 2025) revealed that vendor benchmarks are
not always reproducible. The Adaptoid **reproduces locally** before
citing.

### Letta (default for episodic / graph)
- **Origin:** MemGPT, the Berkeley project, spun out as Letta in 2024.
- **Stars:** 22k+ (GitHub, mid-2026).
- **Why picked:** Hierarchical memory (core / archival / recall).
  Stateful agents. Open-source. Strong benchmarks on the **properly run**
  LOCOMO evaluation.
- **Adaptoid integration:** Default `preferences.memory: letta` or
  `layered` (where Letta is the episodic layer).

### Zep (Graphiti)
- **Stars:** 24.7k+
- **Why picked:** Temporal knowledge graph. Strong on enterprise use
  cases. Beats MemGPT on DMR benchmark.
- **When to pick:** Memory-heavy, time-aware use cases.

### Mem0
- **Stars:** 52.5k+ (most starred memory project; controversial)
- **Why picked:** Vector + optional graph. Most popular.
- **Controversy:** MemGPT / Letta team publicly called out Mem0 (Aug 13,
  2025) for "fabricated benchmark comparisons" against MemGPT in the
  LOCOMO evaluation. Mem0's SOTA claims on LOCOMO were challenged;
  Letta and Zep both re-ran the benchmark and beat Mem0 by ~10%.
- **Adaptoid integration:** Supported as an alternative. The DevKit
  warns users to *reproduce* the benchmark in `reports/eval-*` before
  citing.

### Cognee
- **Why picked:** Claims best-in-class results on the benchmark
  suite (Sep 2025 community benchmark).

### OpenMemory
- Mem0-compatible, open-source, no vendor lock.

### Hindsight, Memvid
- Emerging; niche.

### Qdrant (default for vector)
- **Stars:** 25k+
- **Why picked:** Rust-based, very fast, OpenAI-compatible API,
  hybrid search (vector + BM25), great UX.

---

## 10. Durable execution

### Inngest (default for event-driven)
- **Why picked:** Event-driven. Functions as code. Built-in
  retries, sleep, parallelism. Developer experience is excellent.
  Great fit for AI agents that pause on tool calls.
- **When to pick:** Event-driven workflows, serverless deployments.

### Temporal (alternative for transactional)
- **Why picked:** The most battle-tested durable execution engine.
  Used by Netflix, Uber, Snap, etc. Strong correctness guarantees.
  Code-as-workflow.
- **When to pick:** Long-horizon, transactional correctness, large
  scale.

### Restate (alternative for simpler durable needs)
- Lighter than Temporal. Frictionless.

### DBOS (alternative for SQL-native)
- Lightweight library on top of Postgres. Simple to add to existing
  apps.

### Why Adaptoid lets you pick
Different tasks want different engines. Inngest for event-driven.
Temporal for long-horizon. DBOS for SQL-native. The
`preferences.durable_exec` field selects.

---

## 11. Observability

### Langfuse (default)
- **Repo:** github.com/langfuse/langfuse
- **Stars:** 12k+
- **Why picked:** Open-source. OTel-native. Self-hostable. Great
  eval + prompt management. Strong community.

### Alternatives
- **LangSmith** — LangChain-native, paid, excellent.
- **Logfire** — Pydantic-native, paid tier, great for Python.
- **Phoenix (Arize)** — open-source, strong on evaluation.
- **Laminar** — emerging, dev-friendly.
- **Helicone** — proxy-style observability.
- **Datadog LLM Observability** — enterprise.

### The Adaptoid principle
OTel-native so any of them work. Adaptoid ships a *baseline trace
contract* (see `references/trace-contract.md`).

---

## 12. Eval

### Promptfoo
- **Why picked:** LLM-as-judge evals, easy YAML config, CI-friendly.

### DeepEval
- **Why picked:** Metric assertions, similar to Pytest. Strong
  on RAG / agent metrics.

### Inspect (UK AISI)
- **Why picked:** Government-backed eval framework. Strong on
  safety / alignment.

### Calibration set
- The Adaptoid ships a 50-case calibration set per domain. Used to
  calibrate the LLM-as-judge's confidence scale to historical
  agreement rate.

---

## 13. Self-improving loops

### DSPy (default)
- **Why picked:** Programmatic prompt optimization. Compiles a
  pipeline of typed modules. Optimizers: BootstrapFewShot,
  MIPRO, GEPA, etc.
- **Adaptoid integration:** Used for prompt tuning of skill templates
  based on eval results.

### TextGrad
- **Why picked:** Textual gradients. Backprop-style optimization of
  compound AI systems.

### ADAS (Automated Design of Agentic Systems)
- **Why picked:** Meta-search over agent designs.

### GEPA, SPO, OPRO
- **Why picked:** Newer, cheaper prompt optimization.

### The Adaptoid principle
Self-improving is **tiered**: cheap reflection (free) → DSPy / TextGrad
(expensive) → human-in-loop (only when it matters).

---

## 14. Browser use

### Stagehand
- **Why picked:** Strong, TypeScript-native, structured actions.

### Browser-Use
- **Why picked:** Python-native, LLM-driven, open-source.

### Anthropic Computer Use
- Native to Claude. Direct OS / browser control.

### OpenAI Operator
- Managed, browser-based.

### Adaptoid principle
Browser use is a *destructive* node by default (adaptoid sets
`route_constraints.destructive: true` and requires a pre-image).

---

## 15. Editor / harness

### Claude Code
- **Why picked:** Reference for the Agent Skills standard. Strong
  on long-horizon. Sub-agents, hooks, MCP-native.

### Cursor
- **Why picked:** Best-in-class AI IDE. First to fully adopt Skills.

### Codex CLI, Aider, Goose, Amp
- Each has its niche. Adaptoid's cold-start contract works with all.

---

## 16. Terminal multiplexer

### tmux (default)
- **Why picked:** Universal, stable, every SSH session has it.

### zellij
- Modern alternative. Better UX. Rust-based.

### WezTerm, iTerm2
- For macOS.

---

## 17. Secret management

### 1Password CLI (`op`)
- **Why picked:** Most teams already have it. Simple.

### sops + age
- **Why picked:** Git-native, encrypted YAML / JSON / ENV.

### HashiCorp Vault
- Enterprise.

### Doppler
- SaaS, developer-friendly.

### Adaptoid principle
Never commit secrets. Always pull at bootstrap. Never log values.

---

## 18. The head-to-head (and what Adaptoid wins)

Detailed in `references/headroom-analysis.md`. The summary:

| Axis              | Best alternative in the wild   | Adaptoid's edge                                                      |
| ----------------- | ------------------------------ | ------------------------------------------------------------------- |
| Setup time        | LangGraph + LangSmith + Letta (3 hours) | Adaptoid (90 seconds)                                       |
| Tooling coverage  | Anything solo                  | Everything, opinionated, swappable                                  |
| Anti-hallucination| Pydantic AI + Instructor (good)| All four verification layers, enforced, with falsification           |
| Anti-wrong-route  | Manual code review             | 12-point RouteCheck, WR-1..WR-12, enforced on every non-read        |
| Anti-forgetting   | Mem0 / Letta cloud             | Markdown + SQLite FTS + graph + ACL + cross-agent MCP                |
| Cold start        | Re-explain context             | 5-second contract, hooks, AGENTS.md as system prompt                 |
| Long-horizon      | Mem0 / Letta cloud             | Durable exec + memory + DAG + checkpoint ledger + falsification     |
| Self-improving    | DSPy / TextGrad                | Tiered: cheap → expensive → human, with provenance                  |
| Adaptoid behavior | None — you configure           | First-class: the Engine adapts to your project                      |
| Cost              | Whatever you set                | Cost router + per-node cap + per-plan budget + downgrades            |
| Local-first       | Ollama standalone               | LiteLLM-routed, OTel-instrumented, gateway-fronted                   |

---

## 19. TL;DR

> The agentic AI ecosystem in mid-2026 has ~9 distinct layers, each with
> 2–10 notable projects. The Adaptoid picks the best-of-breed per layer
> (LiteLLM, Ollama, LangGraph, Pydantic AI, MCP, A2A, Skills, Letta,
> Qdrant, Inngest, Langfuse, Promptfoo, DSPy), makes the choices
> swappable, and adds a verification regime + a Project Intent +
> Problem Adapter + a memory bank + a cold-start contract that the
> alternatives do not have.

🜂
