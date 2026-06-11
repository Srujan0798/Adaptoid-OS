# FM-16 — Wrong Route (Hallucinated DAG Transitions)

**Symptom.** Agent attempts to transition to a node that doesn't exist, loops back to itself, or skips required verification gates. Hallucinated tool calls, infinite loops, destructive actions executed because the route checker was bypassed.

**Root cause.** No static DAG_TRANSITIONS map. The agent "invents" transitions based on chat context rather than a pre-approved workflow graph.

**Blast.** Wrong outputs, skipped reviews, destructive actions, untraceable execution paths.

**Prevention rule.**
- Every project defines a static `DAG_TRANSITIONS` map in `adaptoid.config.yaml`.
- `Route Sentinel` validates every proposed transition before execution.
- Self-loops are blocked unless explicitly whitelisted.
- Retry exhaustion escalates to human, not to another guess.

**Validator.** `validators/route_sentinel.sh`:
- Checks `adaptoid.config.yaml` for valid `dag_transitions` block.
- Flags self-loops, unknown nodes, missing retry policies.

**Wire-in.** Every orchestrator transition calls Route Sentinel before dispatch.

**Fix when it fires.** Revert to last valid checkpoint, regenerate DAG from `adaptoid.config.yaml`, resume.
