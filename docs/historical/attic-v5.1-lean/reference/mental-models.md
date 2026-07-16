# Mental Models — the frames that make the rest make sense

> Two evergreen frames from the field's clearest thinkers. Load when you want the WHY behind the architecture.

## 1. LLM-as-OS (Karpathy)
Treat the LLM agent like an operating system. Maps every agent concern to an OS concept:

| OS concept | Agent equivalent | OS-Setup implementation |
|---|---|---|
| **Kernel** | LLM inference loop | the orchestrator (Claude/Kimi) |
| **RAM** | context window | what's loaded now — kept small via progressive disclosure (FM-04) |
| **Disk / filesystem** | RAG + vector + graph + files | `work/`, `docs/`, memory tools, codegraph, Obsidian |
| **Syscalls** | tools | MCP servers (`mcp.json`) |
| **Processes** | sub-agents / workers | OpenCode windows, sub-agents (REGISTRY) |
| **Process mgmt / scheduler** | multi-agent orchestration | the conductor (orchestrator-workers + parallelism) |
| **Permissions / rings** | blast-radius tiers | r0–r5 (blast-radius.md) |
| **Swap / paging** | context compaction | handoff + caveman + headroom (FM-04) |
| **Logs** | durable session | `events.jsonl` (FM-14) |

**Why it matters:** every hard agent problem becomes a known OS problem with a known answer. Context too big? That's memory management — page to disk (compress/index/persist). Agents colliding? That's concurrency — disjoint resources + locks (FM-13). Unsafe action? That's permissions — ring-gate it (blast-radius). OS-Setup is literally an agent OS built on this frame.

## 2. Freedom + Responsibility, guardrailed (Netflix culture, applied to agents)
The high-performance culture: **high talent density · minimal process · strong guardrails · learn from failure · observability**. Translated to agentic systems:

| Netflix principle | Agentic translation | OS-Setup implementation |
|---|---|---|
| Freedom + responsibility | autonomous agents, but accountable | auto mode for r0/r1; humans gate r3+ (blast-radius) |
| Minimal process | don't drown agents in ceremony | tier-down rule; CLAUDE.md short; start simple |
| Strong guardrails | bounded autonomy | validators, acceptance gates, failure-mode wiring |
| Learn from failure | every incident teaches | HALL_OF_SHAME + failure→prevention loop → new FM + test |
| Chaos / resilience eng | expect non-determinism, test for it | flaky-test discipline (FM-10), pass^k, self-heal rules |
| Observability | see what agents do | `events.jsonl`, audit log, metrics (T2 operational docs) |
| High talent density | use the best components | the DevKit library auto-pulls the frontier |

**Why it matters:** the tension in agentic systems is autonomy vs reliability. Netflix's answer — maximize autonomy, but wrap it in guardrails + eval loops + observability so the rare failure is caught and learned from — is exactly the right posture for non-deterministic agents. Freedom for speed; guardrails for trust.

## The synthesis (how the two frames combine)
- LLM-as-OS tells you **what the pieces are** (kernel, memory, syscalls, processes, permissions).
- Freedom+Responsibility tells you **how to run them** (autonomy inside guardrails, learn from failure, observe everything).

Together: an agent OS that is fast because it's autonomous and trustworthy because it's guardrailed and observable — which is the whole point of OS-Setup.

`verified: 2026-05 (Karpathy LLM-as-OS + Netflix culture, both well-documented; corpus)`
