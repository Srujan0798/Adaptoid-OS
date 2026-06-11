# Hidden Gems Catalog

A reference list of 36 tools, libraries, and research patterns that are useful for building a framework-agnostic agent harness. The list favors function over popularity: small, focused projects are included when they solve a concrete problem more cleanly than the default choices. This is a living catalog, not a product endorsement.

---

## Memory & Knowledge

| # | Tool | URL | Scale | What it does | Integration idea |
|---|---|---|---|---|---|
| 1 | Cognee | <https://github.com/topoteretes/cognee> | ~500–1K stars | Ingests arbitrary data into a self-hosted knowledge graph for persistent agent memory. | Primary memory backbone; map `remember/recall/forget/improve` to the harness memory API. |
| 2 | Graphiti (Zep) | <https://github.com/getzep/graphiti> | ~1–3K stars | Real-time temporal knowledge graph with validity windows (`valid_from`, `valid_to`). | Temporal memory layer for tracking how facts change over time. |
| 3 | Auto-Dream / OpenClaw Dreaming | <https://github.com/LeoYeAI/openclaw-auto-dream> | ~100–300 stars | Background memory consolidation using sleep-cycle phases. | Run during idle periods to merge duplicates and remove contradictions. |
| 4 | SCM (Sleep-Consolidated Memory) | <https://arxiv.org/html/2604.20943v1> | Academic | Computational analogs of biological memory components: encoding, 4D importance tagging, working memory limits, NREM/REM consolidation, intentional forgetting. | Reference model for a tiered memory subsystem. |
| 5 | Mem0 | <https://github.com/mem0ai/mem0> | ~48K stars | Universal memory layer with vector store and optional knowledge graph. | Quick-start memory option; note that the graph layer may require a paid tier. |
| 6 | Zep (Temporal KG paper) | <https://arxiv.org/abs/2501.13956> | Academic | Temporally-aware knowledge graph with bi-temporal query capabilities. | Core reference for temporal memory architecture. |
| 7 | Claude AutoDream | Anthropic feature | N/A | Production sleep-cycle consolidation for large session volumes. | Reference implementation for scheduling background consolidation. |

## Orchestration & Agents

| # | Tool | URL | Scale | What it does | Integration idea |
|---|---|---|---|---|---|
| 8 | AgentScope | <https://github.com/modelscope/agentscope> | ~10.7K stars | Multi-agent framework from Alibaba with tool use, RL fine-tuning, real-time voice, MCP/A2A support, and visual debugging. | Reference architecture for multi-agent orchestration patterns. |
| 9 | Agently | <https://github.com/AgentEra/Agently> | ~500–800 stars | Event-driven GenAI framework with TriggerFlow and multi-model support. | Use TriggerFlow as a decision-pipeline primitive. |
| 10 | ChatDev / DevAll | <https://github.com/OpenBMB/ChatDev> | ~25K+ stars | Multi-agent software development with specialized roles (CEO, CTO, Programmer, Tester). | Role-based collaboration model for agent teams. |
| 11 | Marvin AI | <https://github.com/PrefectHQ/marvin> | ~5–8K stars | Pydantic-based agentic workflow framework with structured outputs. | Workflow orchestration with validated outputs. |
| 12 | Pydantic AI | <https://github.com/pydantic/pydantic-ai> | ~3–5K stars | Type-safe Python agent framework from the Pydantic team. | Structured output validation across agent operations. |
| 13 | smolagents | <https://github.com/huggingface/smolagents> | ~5–8K stars | Minimal Hugging Face agent framework emphasizing code over JSON for tool execution. | Lightweight agent execution for simple tasks. |

## Reasoning & Planning

| # | Tool | URL | Scale | What it does | Integration idea |
|---|---|---|---|---|---|
| 14 | LATS | <https://github.com/lapisrocks/LanguageAgentTreeSearch> | ~200–300 stars | Monte Carlo Tree Search over thought-action-observation trajectories. | Complex planning tasks that require exploring multiple solution paths. |
| 15 | ReVeal | <https://arxiv.org/html/2506.11442v1> | Academic | Multi-turn RL framework for code agents to generate-verify-refine with self-created test cases. | Self-improvement loop for code generation. |
| 16 | ReAct + Reflexion + LATS | Pattern | N/A | Progressive reasoning stack: reason-act, add reflection, add tree search. | Reasoning engine that selects depth based on task complexity. |
| 17 | Agentless | <https://dl.acm.org/doi/10.1145/3715754> | Academic | Three-phase autonomous coding approach with low per-task cost. | Reminder that simple pipelines can outperform complex agents for some tasks. |

## Tools & Infrastructure

| # | Tool | URL | Scale | What it does | Integration idea |
|---|---|---|---|---|---|
| 18 | LiteLLM | <https://github.com/BerriAI/litellm> | ~20K+ stars | Universal LLM API gateway with budget routing, fallback, and cost control. | Foundation model router: route simple tasks to cheap models, complex tasks to capable models. |
| 19 | Midscene.js | <https://github.com/web-infra-dev/midscene> | ~3–5K stars | Vision-driven browser automation via screenshots. | Web interaction without brittle CSS selectors. |
| 20 | TinyAgent | <https://github.com/SqueezeAILab/TinyAgent> | ~200–500 stars | 1.1B parameter models for local function calling. | Local tool-calling for privacy-sensitive or offline operations. |
| 21 | Aider | <https://github.com/Aider-AI/aider> | ~41.6K stars | Terminal AI pair programming with tree-sitter repo mapping and git integration. | Coding execution layer for autonomous codebase modification. |
| 22 | SGLang | <https://github.com/sgl-project/sglang> | ~10K+ stars | Efficient LLM execution with KV cache reuse. | Inference backend for agent reasoning loops. |
| 23 | Lucid Agents (Daydreams) | <https://github.com/daydreamsai/lucid-agents> | ~100–300 stars | Agents that can pay, sell, and participate in agent-to-agent commerce. | Wallet primitives for agent-to-agent payments. |
| 24 | llamafile | <https://github.com/Mozilla-Ocho/llamafile> | ~20K+ stars | Single-file, cross-platform LLM distribution by Mozilla. | Local inference fallback. |

## Code Intelligence

| # | Tool | URL | Scale | What it does | Integration idea |
|---|---|---|---|---|---|
| 25 | CodeRAG | <https://code-rag-bench.github.io/> | Academic | Code-specific retrieval using log-probability probing, multi-path retrieval, and LLM reranking. | Code retrieval for programming tasks. |
| 26 | CodexGraph | Part of ModelScope-Agent | N/A | Graph-based code understanding capturing structural relationships. | Deep code understanding for agent self-modification. |

## Evaluation & Benchmarks

| # | Tool | URL | Scale | What it does | Integration idea |
|---|---|---|---|---|---|
| 27 | Ragas | <https://github.com/explodinggradients/ragas> | ~5K stars | Research-backed evaluation for RAG and agent pipelines. | Continuous evaluation of memory retrieval quality. |
| 28 | DeepEval | <https://github.com/confident-ai/deepeval> | ~3–5K stars | Unit testing framework for LLM apps with 14+ metrics. | Automated regression testing for agent behavior. |
| 29 | MultiAgentBench | Academic | N/A | Benchmark measuring collaboration and competition in multi-agent systems. | Evaluation methodology for multi-agent coordination. |
| 30 | OSWorld / WebArena / Windows Agent Arena | Various | N/A | Real-world benchmarks for OS, web, and desktop agent tasks. | Capability evaluation on realistic environments. |

## Concepts & Patterns

| # | Pattern | Origin | What it does | Integration idea |
|---|---|---|---|---|
| 31 | Agent Sleep/Dream Cycles | Claude AutoDream, OpenClaw, SCM | Background consolidation, pruning, and refreshing of memory. | Core maintenance loop for long-running agents. |
| 32 | Agent Hormones (Curiosity, Pain, Boredom) | Curious3 system | Three drives that create intrinsic motivation and scheduling signals. | Heuristic for when to explore, focus, or innovate. |
| 33 | Agent-Native Development | Emerging pattern, 2025–2026 | Shift from "AI helps write code" to "agent config and tool definitions are core deliverables." | Design principle: the harness maintains its own configuration and skill library. |
| 34 | Execution Decomposition (ExeDec) | Code agent research | Decompose high-level goals into executable sub-programs at runtime with dynamic replanning. | Core execution strategy for goal decomposition. |
| 35 | Voyager-Style Skill Libraries | <https://voyager.minedojo.org> | Learned capabilities as executable, reusable, compositional programs. | Foundation for procedural memory / skill storage. |
| 36 | Agent Protocol Stack (MCP → A2A) | Anthropic / Google / IBM | Standardized protocols for model-to-tool and agent-to-agent interoperability. | Full protocol stack for ecosystem interoperability. |

---

## Integration Quality Gates

Before a gem enters the harness, it must pass the following gates:

| Gate | Threshold | Why it matters |
|---|---|---|
| Code quality | Static analysis score > 0.70 | Maintainable code that the team can debug. |
| Documentation | Completeness > 0.60 | Enough docs to integrate without reverse-engineering. |
| Test coverage | > 50% line coverage | Confidence that updates will not silently break. |
| Freshness | < 30 days since last commit | Active maintenance, or at least a responsive maintainer. |
| Security | 0 critical vulnerabilities | Safety for a component that may run with tool privileges. |
| License | OSI-approved (Apache/MIT/BSD) | Legal compliance for open-source distribution. |

## Discovery Pipeline

```
SCAN (GitHub, arXiv, Hacker News, regional ecosystems)
  → EVALUATE (quality gates above)
  → ADAPT (write adapter / plugin)
  → TEST (unit + integration + smoke tests)
  → ACTIVATE (plugin registry + rollback plan)
```

### Monitoring channels

| Channel | What to track | Frequency |
|---|---|---|
| GitHub | Agent-related topics, star velocity, issue resolution | Daily |
| arXiv | cs.AI / cs.SE papers with released code | Daily |
| Hacker News | "Show HN" posts and deep technical threads | Real-time during launches |
| Regional hubs | ModelScope, Zenn, Hugging Face | Weekly |

### Screening questions

For each candidate gem, answer:

1. **Capability gap** — Does it provide something the harness currently lacks?
2. **Quality delta** — Is it meaningfully better than the current tool for that job?
3. **Integration cost** — Can a first integration be done within two weeks?
4. **Maintenance burden** — Is it likely to be maintained for 12+ months?
5. **Ecosystem fit** — Does it align with the harness philosophy (open, modular, protocol-native)?

A gem scoring positively on 3+ of 5 criteria enters the integration pipeline.

---

## Version Management

| Update type | Action |
|---|---|
| Patch | Auto-accepted after CI passes. |
| Minor | Manual review + integration test. |
| Major | Full re-evaluation required. |
| Abandoned (> 90 days inactive) | Flag for replacement search. |

## How to Contribute a Gem

Submit suggestions via:

- CLI (if implemented): `adaptoid gem suggest <url> --category <cat> --reason "<why>"`
- GitHub issue with the `gem-suggestion` label
- Community discussion channel

Evaluation weights for submissions:

| Criterion | Weight |
|---|---|
| Novelty | 25% |
| Quality | 25% |
| Impact | 20% |
| Maintainability | 15% |
| Integration cost | 15% |
