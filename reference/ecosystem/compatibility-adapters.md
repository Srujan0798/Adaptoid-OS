# Ecosystem — Compatibility Adapters (independent core + framework bridges)

> Architecture decision: OS-Setup's core is INDEPENDENT (kernel, two-tier, failure-modes, validators, adaptor). It is NOT locked inside any framework. But it provides ADAPTERS so you can import/export workflows, skills, and context to/from the major frameworks when that adds value. Best of both: ecosystem reach + sovereign core.

## Why hybrid (not pure-independent, not pure-compatible)
- **Pure independent** → cut off from the ecosystem's skills, examples, momentum.
- **Pure compatible** → live inside another system's limits; no moat.
- **Hybrid** → extract the highest-leverage patterns from each framework, make them first-class in the independent core, bridge bidirectionally where useful.

## Framework catalog (what to extract from each)
| Framework | Best-in-class at | Extract this pattern | Source |
|---|---|---|---|
| **LangGraph** | stateful graphs, durable/resumable, human-in-loop, checkpoints | the persistence + checkpoint graph model | langchain (corpus) |
| **CrewAI** | role-based crews, simple multi-agent | role specialization + crew composition | (corpus) |
| **AutoGen** | conversational multi-agent, group chat | debate/negotiation protocols | (corpus) |
| **MetaGPT** | role-society SOPs (PM/architect/eng) | encoded SOP per role → repeatable software org | (corpus, verify activity) |
| **LlamaIndex Workflows** | event-driven step workflows + RAG | event-step decomposition | (corpus, verify) |
| **OpenAI Agents SDK** | handoffs, guardrails, sessions, tracing | guardrail + handoff primitives | (corpus) |
| **Google ADK 2.0** | graph workflows, context-as-source-code, multi-lang | the context-discipline model | adk.dev ⚡ |
| **Semantic Kernel** | enterprise .NET/Py plugins, planners | plugin + planner abstraction | (corpus, verify) |
| **Agno** | fast lightweight agents | minimal-overhead agent loop | (reported; verify) |
| **OWL / CAMEL** | multi-agent collaboration on benchmarks (GAIA) | role-play collaboration that scores on benchmarks | (reported; verify) |
| **DeerFlow / MagiC** | DAG routing + cost ("k8s for agents") | DAG + routing + cost-control orchestration | (reported; verify) |
| **DSPy** | optimize-don't-prompt (signatures/modules/optimizers) | auto-tuned prompt programs | dspy.ai (corpus) |

> ⚠️ Honesty: items marked "(reported; verify)" are from community description, not freshly fetched this session. Before relying on one, the orchestrator re-fetches its repo/docs (the FM-12 discipline applied to the catalog).

## Adapter contract (how a bridge works)
An adapter is a thin translator, not a rewrite. For framework F, an adapter provides:
- **import:** F-workflow → OS-Setup `workflows/*.plan.yaml` (map F's nodes/edges/roles to waves/tasks/gates).
- **export:** OS-Setup plan → F-runnable (when you want to run on F's runtime, e.g., LangGraph for durable production graphs).
- **skill bridge:** F-tool/skill ↔ agentskills.io `SKILL.md` (so skills port).
- **memory bridge:** F-state ↔ the project's memory layer (events.jsonl / chosen memory tool).

## When to actually bridge (not always)
- Need **durable, resumable production graphs** → export to LangGraph; keep planning/review in the core.
- Need a **role-debate** for a hard decision → import an AutoGen/CrewAI debate as one wave's "explore" step.
- Need **benchmark-grade multi-agent collab** → wrap OWL/CAMEL as a specialized sub-agent.
- Otherwise → the independent core (orchestrator-workers + conductor) is enough; don't add a framework for its own sake (FM-08).

## The rule
The core never depends on a framework. Adapters are opt-in, at the edges. A project must run with zero external frameworks if the user wants sovereignty — and still be excellent.

`verified: 2026-05 (ADK ⚡; LangGraph/CrewAI/AutoGen/OpenAI-SDK/DSPy corpus; MetaGPT/LlamaIndex/SK/Agno/OWL/DeerFlow reported — verify before relying)`
