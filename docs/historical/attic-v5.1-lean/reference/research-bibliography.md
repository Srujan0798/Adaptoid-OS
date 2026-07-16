# 📚 references/bibliography.md

> *Primary sources for the Adaptoid-OS synthesis. Every claim about a
> project, a benchmark, a release, or a standard has a source here.
> Section 5+ are the high-signal pieces worth reading in full.*

---

## 1. Open standards

| Project / Spec       | Source                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------- |
| MCP 1.0 spec         | modelcontextprotocol.io — 17 SEPs, released Nov 2025 (1-year anniversary)                  |
| MCP donation         | anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation — Sept 2025 |
| A2A spec             | github.com/a2aproject/A2A — Google, April 9, 2025                                          |
| A2A + Microsoft      | microsoft.com/en-us/microsoft-cloud/blog/2025/05/07/empowering-multi-agent-apps-with-the-open-agent2agent-a2a-protocol/ — May 2025 |
| Agent Skills open std| agentskills.io — Anthropic et al., Dec 18, 2025                                            |
| Skills engineering   | anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills — Oct 2025 |
| OTel                 | opentelemetry.io                                                                        |

---

## 2. Frameworks and harnesses

| Project               | Source                                                                            |
| --------------------- | --------------------------------------------------------------------------------- |
| LangGraph             | github.com/langchain-ai/langgraph — 0.3+ series                                  |
| OpenAI Agents SDK     | github.com/openai/openai-agents-python                                            |
| Claude Agent SDK      | docs.anthropic.com / claude-code                                                  |
| Letta (ex-MemGPT)     | github.com/letta-ai/letta                                                         |
| CrewAI                | github.com/crewAIInc/crewAI                                                       |
| AutoGen (Microsoft)   | github.com/microsoft/autogen                                                       |
| Pydantic AI           | github.com/pydantic/pydantic-ai — 1.0+                                            |
| Smolagents (HF)       | github.com/huggingface/smolagents                                                 |
| Agno (Phi-Data)       | github.com/agno-agi/agno                                                          |
| Atomic Agents         | github.com/BrainBlend-AI/atomic-agents                                            |
| Mastra                | github.com/mastra-ai/mastra — JS / TS                                             |
| Google ADK            | github.com/google/adk-python                                                      |
| Semantic Kernel       | github.com/microsoft/semantic-kernel                                              |

Comparative analyses:
- Langfuse 2025 comparison: langfuse.com/blog/2025-03-19-ai-agent-comparison
- arxiv 2508.10146 — Hana Derouiche et al., "Agentic AI Frameworks: Architectures, Protocols, and Design Challenges" — Aug 13, 2025

---

## 3. Memory systems

| Project        | Source                                                                              |
| -------------- | ----------------------------------------------------------------------------------- |
| Letta          | github.com/letta-ai/letta, 22k+ stars                                                |
| Mem0           | github.com/mem0ai/mem0 — 52.5k+ stars, $24M funding (Oct 2025)                       |
| Zep (Graphiti) | github.com/getzep/zep — 24.7k+ stars, arxiv:2501.13956                               |
| Cognee         | github.com/topoteretes/cognee — Sep 2025 community benchmark                        |
| MemGPT (orig)  | arxiv:2310.08560 — Packer et al., UC Berkeley                                       |

Controversy:
- InfoQ, Aug 13, 2025: "MemGPT作者开撕Mem0" — Letta CTO Sarah Wooders public
  accusation that Mem0's April 2025 LOCOMO paper (arxiv:2504.19413) used a
  broken MemGPT baseline; Letta + Zep re-ran and beat Mem0 by ~10%.
- Zep blog: blog.getzep.com/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/

---

## 4. Verification, observability, eval

| Project     | Source                                                                          |
| ----------- | ------------------------------------------------------------------------------- |
| Pydantic AI | github.com/pydantic/pydantic-ai                                                  |
| BAML        | github.com/BoundaryML/baml                                                      |
| Instructor  | github.com/jxnl/instructor                                                       |
| Outlines    | github.com/outlines-dev/outlines                                                 |
| Langfuse    | github.com/langfuse/langfuse — 12k+ stars                                        |
| LangSmith   | smith.langchain.com                                                              |
| Logfire     | pydantic.dev/logfire                                                             |
| Phoenix     | github.com/Arize-ai/phoenix                                                      |
| Laminar     | laminar.sh — 2026 emerging                                                       |
| Helicone    | github.com/Helicone/helicone                                                     |
| Promptfoo   | github.com/promptfoo/promptfoo                                                   |
| DeepEval    | github.com/confident-ai/deepeval                                                 |
| Inspect     | github.com/UKGovernmentBEIS/inspect — UK AI Safety Institute                     |

eBPF for agent observability:
- arxiv:2508.02736 — Zheng et al., "AgentSight: System-Level Observability for
  AI Agents Using eBPF" — Aug 2025

---

## 5. Durable execution

| Project   | Source                                                                                |
| --------- | ------------------------------------------------------------------------------------- |
| Temporal  | github.com/temporalio/temporal — used by Snap, Netflix, Uber                          |
| Inngest   | github.com/inngest/inngest — event-driven, dev-mode and serverless                      |
| Restate   | github.com/restatedev/restate                                                        |
| DBOS      | github.com/dbos-inc/dbos-transact — Postgres-backed library                            |

Long-running agents:
- Anthropic, "Effective harnesses for long-running agents" — Nov 26, 2025
- Inngest, "Durable Execution: The Key to Harnessing AI Agents in Production" — 2025

---

## 6. Self-improving loops

| Project  | Source                                                                                |
| -------- | ------------------------------------------------------------------------------------- |
| DSPy     | dspy.ai, github.com/stanfordnlp/dspy — Stanford NLP                                    |
| TextGrad | arxiv:2406.07496 — Yuksekgonul et al., Stanford                                        |
| ADAS     | arxiv:2308.08442 — Hu et al., "Automated Design of Agentic Systems"                    |
| GEPA     | (referenced in DSPy ecosystem)                                                        |
| SPO      | EMNLP 2025 — Self-Supervised Prompt Optimization                                       |
| OPRO     | arxiv:2309.03409 — Yang et al., Google DeepMind                                        |
| Voyager  | arxiv:2305.16291 — Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models" — skill library growth |

---

## 7. MCP and A2A in depth

| Topic                            | Source                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| MCP attack vectors               | arxiv:2506.02040 — Song et al., "Beyond the Protocol: Unveiling Attack Vectors in the Model Context Protocol (MCP) Ecosystem" — May 2025 |
| MCP context-aware servers        | arxiv:2601.11595 — Jayanti & Han, "Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration" — Jan 2026 |
| Code execution with MCP          | anthropic.com/engineering/code-execution-with-mcp                                     |
| A2A vs MCP                       | koyeb.com/blog/a2a-and-mcp-start-of-the-ai-agent-protocol-wars                         |
| A2A + Microsoft                  | microsoft.com/en-us/microsoft-cloud/blog/2025/05/07/...                                |
| A2A spec details                 | developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability                  |
| MCP donated to Linux Foundation  | anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation |

---

## 8. Browser use and Computer Use

| Project             | Source                                                                          |
| ------------------- | ------------------------------------------------------------------------------- |
| Anthropic Computer Use | anthropic.com/news/3-5-models-and-computer-use — Oct 2024                    |
| OpenAI Operator     | openai.com/index/introducing-operator — Jan 2025                                |
| Browser-Use         | github.com/browser-use/browser-use                                              |
| Stagehand           | github.com/browserbasehq/stagehand                                              |
| Manus               | manus.im (early 2025 launch)                                                    |

---

## 9. LLM gateway and local LLM

| Project | Source                                                                  |
| ------- | ----------------------------------------------------------------------- |
| LiteLLM | github.com/BerriAI/litellm — 28k+ stars                                 |
| Ollama  | github.com/ollama/ollama — 95k+ stars                                   |
| vLLM    | github.com/vllm-project/vllm — 30k+ stars                               |
| LM Studio | lmstudio.ai                                                            |
| OpenRouter | openrouter.ai                                                        |
| Portkey | github.com/Portkey-AI/portkey                                            |

---

## 10. The skill standard and ecosystem

| Topic                            | Source                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| Agent Skills launch              | anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills — Oct 16, 2025 |
| Open standard release            | agentskills.io — Dec 18, 2025                                                          |
| Anthropic Skills GitHub          | github.com/anthropics/skills — 16+ reference skills                                    |
| Adoption                         | 85k+ public skills, 27+ platforms (Feb 2026)                                           |
| "AI's Dockerfile" framing        | TechCrunch, late 2025                                                                  |
| DeepLearning.AI course           | deeplearning.ai/courses/agent-skills-with-anthropic                                    |
| Skills economy / market          | 华福证券, "AI Agent的C端新标杆, Claude Skills" — Jan 2026                               |

---

## 11. Key papers (extraction notes)

### 11.1 "Building effective agents" (Anthropic, Dec 20, 2024)
- **Source:** anthropic.com/research/building-effective-agents
- **Core thesis:** Workflows vs agents. The "agent" label is overused.
  Workflows (chained LLM calls with explicit control flow) are often
  the right call before "full" agents. Workflows are *not* a
  step-down from agents — they are *deliberate* choices.
- **Extraction:** Adaptoid ships both. The Adaptoid Engine emits
  *workflows* (typed DAGs) by default; the *conductor* pattern (§3.3
  in `workflows/README.md`) is the path to "true" agents. The choice
  is per-project, not per-framework.

### 11.2 "Agentic AI Frameworks: Architectures, Protocols, and Design Challenges" (Aug 13, 2025)
- **Source:** arxiv:2508.10146 — Hana Derouiche, Zaki Brahmi, Haithem Mazeni
- **Core:** Systematic review of CrewAI, LangGraph, AutoGen, Semantic Kernel,
  Agno, Google ADK, MetaGPT. Architectural principles, communication
  mechanisms, memory management, safety guardrails, service-orientation.
- **Extraction:** Confirms the Adaptoid's choice of multi-harness support
  over single-framework lock-in. Validates the "swappable harness"
  pattern.

### 11.3 "AgentSight: System-Level Observability for AI Agents Using eBPF" (Aug 2025)
- **Source:** arxiv:2508.02736
- **Core:** Observability for non-deterministic agents. eBPF to bridge
  the "semantic gap" between LLM-level intent and OS-level actions.
- **Extraction:** The Adaptoid's OTel-first observability + trace
  contract is the right call. eBPF-level observability is a future
  extension for security-sensitive deployments.

### 11.4 "Effective harnesses for long-running agents" (Anthropic, Nov 26, 2025)
- **Source:** anthropic.com engineering blog
- **Core:** Patterns for agents that span days/weeks. Memory, durable
  execution, context compaction, resumability.
- **Extraction:** The Adaptoid's `long-horizon/multi-session.yaml`
  workflow implements these patterns. The memory bank + durable
  execution + DAG + falsification is the Adaptoid's answer to the
  long-horizon problem.

### 11.5 "Zep: A Temporal Knowledge Graph Architecture for Agent Memory" (Jan 2025)
- **Source:** arxiv:2501.13956 — Rasmussen et al., Zep AI
- **Core:** Temporal knowledge graph. Outperforms MemGPT on DMR. Better
  on enterprise use cases than DMR alone.
- **Extraction:** Validates the Adaptoid's choice of *layered* memory
  (semantic + episodic) over single-system memory.

### 11.6 "Beyond the Protocol: Unveiling Attack Vectors in the Model Context Protocol (MCP) Ecosystem" (May 2025)
- **Source:** arxiv:2506.02040 — Song et al.
- **Core:** MCP has a rapidly expanding attack surface. Client-server
  architecture introduces vulnerabilities (tool poisoning, prompt
  injection, etc.).
- **Extraction:** The Adaptoid's `mcp-shell`, `mcp-git`, `mcp-filesystem`,
  `mcp-memory` are all sandboxed. RouteCheck refuses to run an MCP
  call that doesn't match the intent. Redaction layer is on by
  default. Skill provenance is required.

### 11.7 "Reflection-Enhanced Meta-Optimization Integrating TextGrad-style Prompt Optimization with Memory-Driven Self-Evolution" (Aug 2025)
- **Source:** arxiv:2508.18749 — Wu & Qu
- **Core:** Stateful, memory-driven prompt optimization. Extends
  TextGrad with a memory of past optimization runs.
- **Extraction:** The Adaptoid's tiered self-improving (cheap → expensive
  → human) is the right shape. Memory-driven optimization is the
  natural next step for the Adaptoid's skill-tuning pipeline.

### 11.8 "Voyager: An Open-Ended Embodied Agent with Large Language Models" (Wang et al., 2023)
- **Source:** arxiv:2305.16291
- **Core:** Skill library growth. The agent adds new skills over time
  based on experience.
- **Extraction:** The Adaptoid's skills library *grows* through
  `core.memory-write` + the `lessons/` writer. The Voyager pattern
  is the long-term vision for the Adaptoid's skill registry.

### 11.9 "ADAS: Automated Design of Agentic Systems" (Hu et al., 2023)
- **Source:** arxiv:2308.08442
- **Core:** Meta-search over agent designs. The agent invents new agent
  designs, evaluates them, and keeps the best.
- **Extraction:** The Adaptoid's self-improving tier includes ADAS-style
  meta-search as the *expensive* option, behind cheap reflection and
  behind DSPy/TextGrad.

### 11.10 "Self-Supervised Prompt Optimization" (SPO, EMNLP 2025)
- **Source:** EMNLP 2025
- **Core:** Self-supervised prompt optimization that achieves TextGrad-
  level performance at 1.1%–5.6% of the cost.
- **Extraction:** The Adaptoid's tiered ladder is the right call —
  SPO is the "cheap but not free" rung.

---

## 12. Industry reports and surveys (high-signal)

- LangChain "AI Agents in Production" survey — langchain.com
- Langbase "State of AI Agents 2024" — langbase.com
- ACE Camp, "李飞飞携手五大机构综述AI agent" — Dec 2024
- 华福证券 "AI Agent的C端新标杆, Claude Skills" — Jan 2026
- 莫尔索 "MCP 发布一周年回顾" — InfoQ, Nov 2025

---

## 13. People to follow (cultural map)

- **Harrison Chase** (LangChain / LangGraph) — langchain.com
- **Andrew Ng** (DeepLearning.AI) — deeplearning.ai
- **Lilian Weng** (formerly OpenAI, "Agent" canonical post) — lilianweng.github.io
- **Simon Willison** (independent, agentic systems thinker) — simonwillison.net
- **Anthropic engineering** — anthropic.com/engineering
- **Yoav Goldberg** (NLP / agent critique) — yobibyte.github.io
- **Letta team** (MemGPT originators) — letta.com/blog
- **Zep team** (temporal graph memory) — getzep.com/blog
- **The MAVRK / Latent Space / Cognitive Revolution podcasts** (weekly agentic news)

---

## 14. The "what's coming next" radar

- **MCP 2.x** — additional SEPs in flight (governance, auth, transport)
- **A2A v2** — better state management, more parts
- **Agent Skills 2.0** — more cross-platform adoption expected by Q4 2026
- **Self-improving** — DSPy 3.x, TextGrad 2.x, more meta-search
- **Memory** — consolidation around graph + vector + procedural; vendors
  trying to standardize benchmarks (after the Mem0/Letta fight)
- **Browser use** — Operator-style managed offerings + open-source
  alternatives converging
- **DURABLE EXECUTION + AGENTS** — Temporal + Inngest + DBOS becoming
  standard for any non-trivial agent (predicted: default in 2027)
- **VERIFICATION + STANDARDS** — first "agent benchmark" standards bodies
  forming; expect a "reproducible eval" badge in 2026–2027

---

## 15. TL;DR

> The Adaptoid-OS DevKit is grounded in ~50+ primary sources. Open
> standards (MCP, A2A, Skills, OTel), best-of-breed open-source (LangGraph,
> Pydantic AI, Letta, Qdrant, LiteLLM, Ollama, Temporal / Inngest, Langfuse,
> DSPy / TextGrad), and the most cited recent papers (arXiv 2508.10146,
> 2506.02040, 2601.11595, 2501.13956, 2406.07496, 2308.08442, 2508.18749).
> The map in `landscape-map.md` and the headroom in
> `headroom-analysis.md` are the synthesis of this bibliography.

🜂
