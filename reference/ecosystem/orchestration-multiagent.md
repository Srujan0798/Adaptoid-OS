# Ecosystem — Orchestration & Multi-Agent

> Pull when the work needs more than one agent coordinating. WARNING (Anthropic + Simon Willison): start with the simplest thing; add agents only when a single agent demonstrably fails. "11 agents" is usually hype.

## The 5 canonical patterns (Anthropic "Building Effective Agents")
1. **Prompt chaining** — linear steps, each on the prior output.
2. **Routing** — classify input, send to a specialist path.
3. **Parallelization** — independent subtasks at once (OS-Setup's default for wave tasks).
4. **Orchestrator-workers** — central planner delegates to workers (OS-Setup's CORE: Claude/Kimi → OpenCode).
5. **Evaluator-optimizer** — generator + independent reviewer loop (OS-Setup's `verifier` sub-agent).

## Frameworks / platforms
| Tool | Model | Pick when | Source |
|---|---|---|---|
| **Google ADK graph workflows** | ⚡ deterministic code + adaptive reasoning, sequential/loop/parallel templates, routing | enterprise multi-agent with structure | adk.dev ⚡ |
| **LangGraph** | stateful graph, durable | long-running coordinated agents | (corpus) |
| **OpenAI Agents SDK** | handoffs + guardrails | agent passes control to agent with safety | (corpus) |
| **Ruflo** | queen-led swarm, HNSW memory, 100+ agents, 32 plugins | heavy enterprise swarm (usually overkill) | github/ruvnet/ruflo (corpus) |
| **OpenHands** | scales to thousands of parallel agents | mass parallel engineering | (corpus) |
| **CrewAI / AutoGen** | role crews / conversational | quick multi-agent prototype | (corpus) |

## OS-Setup's stance
The dual-tier model IS orchestrator-workers (pattern #4) + parallelization (#3) + evaluator-optimizer (#5 via verifier). For 95% of projects that's enough — you do NOT need a swarm framework. Reach for ADK graph / LangGraph only when:
- the agent product itself must coordinate sub-agents at runtime (not just at dev time), OR
- you need durable, resumable, stateful multi-step flows in production.

## Coordination hygiene (the failures to avoid)
- **Disjoint work** — parallel agents on disjoint files (FM-13).
- **One brain** — a single orchestrator owns state; workers are stateless hands (kernel TWO-TIER).
- **Durable session** — coordinate through files (`work/`, `events.jsonl`), not through agents' memory.
- **Blast-radius gates** on any agent that can act externally (protocols/blast-radius.md).

`verified: 2026-05 (ADK ⚡; patterns + frameworks corpus)`
