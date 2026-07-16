# ADAPT Execution Loop Protocol

A workflow pattern for handling requests in an agentic harness. The loop consists of five phases: **Analyze**, **Discover**, **Adapt**, **Perform**, and **Transform**. It can be implemented as a state machine, a graph, or a set of explicit functions. This document describes the pattern without Marvel or superhero references.

---

## The Five Phases

```
+-----------+     +-----------+     +-----------+     +-----------+     +-----------+
|  ANALYZE  | --> | DISCOVER  | --> |   ADAPT   | --> |  PERFORM  | --> | TRANSFORM |
+-----------+     +-----------+     +-----------+     +-----------+     +-----------+
     ^                                                                      |
     |                                                                      |
     +--------------------- Feedback loop ----------------------------------+
```

| Phase | Purpose | Typical outputs |
|---|---|---|
| **A — Analyze** | Understand the problem, context, user intent, and constraints. | Intent classification, confidence estimate, risk flag, required inputs. |
| **D — Discover** | Research solutions and identify available capabilities, tools, and data. | Capability shortlist, relevant memories, applicable skills, model/tool candidates. |
| **A — Adapt** | Select and configure the best approach, assemble the agent/tool plan, and prepare prompts. | Execution plan, selected model(s), tool call sequence, prompt variants. |
| **P — Perform** | Execute the plan, synthesize outputs, and deliver results. | Tool results, generated artifacts, response, execution trace. |
| **T — Transform** | Learn from the encounter, update memory, and improve future runs. | Memory writes, prompt/skill updates, metrics, feedback signals. |

The last phase feeds back into future **Analyze** and **Adapt** steps.

---

## Phase Details

### 1. Analyze

**Goal:** Form a clear, validated understanding of what the user wants.

**Activities:**

- Parse the request and extract explicit goals.
- Load relevant user context from L1 working memory.
- Detect ambiguity, missing information, or safety concerns.
- Estimate confidence and flag high-stakes or irreversible actions.

**Decision gates:**

| Gate | Action |
|---|---|
| Request is ambiguous | Ask clarifying questions. |
| Request exceeds policy | Reject or escalate to human review. |
| High-stakes / irreversible | Require human approval before proceeding. |
| Confidence below threshold | Degrade gracefully or escalate. |

---

### 2. Discover

**Goal:** Find the capabilities and information needed to fulfill the request.

**Activities:**

- Query episodic memory for similar past tasks.
- Query semantic memory for relevant facts and entities.
- Load applicable skills from procedural memory.
- Discover tools via MCP / A2A registries or local tool catalogs.
- Identify candidate models via the model router.

**Outputs:**

- Shortlist of candidate tools, agents, and models
- Retrieved context and memories
- Estimated cost/latency for each candidate

---

### 3. Adapt

**Goal:** Assemble a concrete execution plan tailored to the request.

**Activities:**

- Select the model(s), tool(s), and agent configuration.
- Construct or evolve the prompt.
- Define the execution graph (sequential, parallel, deliberative, etc.).
- Apply cost and latency budgets.
- Set checkpoints for human-in-the-loop if needed.

**Plan schema (example):**

```yaml
plan:
  task_id: task_001
  intent: research_and_summarize
  budget:
    max_tokens: 10000
    max_cost_usd: 2.00
    max_latency_ms: 30000
  steps:
    - step: 1
      agent: researcher
      tool: web_search
      output: raw_results
    - step: 2
      agent: writer
      depends_on: [1]
      tool: summarize
      output: draft
    - step: 3
      agent: editor
      depends_on: [2]
      tool: proofread
      output: final
  approval_points: []
```

---

### 4. Perform

**Goal:** Execute the plan and produce a result.

**Activities:**

- Run the execution graph.
- Capture tool outputs and intermediate states.
- Handle failures with fallback or retry logic.
- Synthesize outputs into a coherent response.

**Outputs:**

- Final response or artifact
- Execution trace
- Cost and latency metrics
- Success / failure status

---

### 5. Transform

**Goal:** Convert the execution into durable improvement.

**Activities:**

- Store the episode in L2 memory.
- Extract facts for L3 semantic memory if thresholds are met.
- Propose skill updates for L4 procedural memory.
- Feed execution traces into the evolution engine for prompt optimization.
- Update user profile and relationship metadata.

**Outputs:**

- Memory writes
- Skill proposals
- Updated metrics
- Feedback signals for ranking and routing

---

## Feedback Loop

The ADAPT loop is not a one-way pipeline. Each execution generates traces that improve subsequent loops:

```
PERFORM --> capture trace
   ^                |
   |                v
ANALYZE <-- TRANSFORM (update memory & prompts)
   ^
   |
DISCOVER --> ADAPT --> PERFORM
```

At each iteration:

- Trace intelligence records what worked and what failed.
- Reflection diagnoses failures and proposes targeted fixes.
- Memory consolidation promotes significant learnings from episodic to semantic memory.
- Prompt evolution incorporates lessons into future instructions.

---

## Design Principles

| Principle | Rationale |
|---|---|
| **Orchestrate, do not overwhelm** | Avoid invoking every available tool at once. Select the minimal useful set. |
| **Create, do not just copy** | Use discovery to inform synthesis rather than replaying past solutions verbatim. |
| **Serve the user** | Keep human oversight for high-stakes, irreversible, or ambiguous actions. |
| **Avoid circular dependencies** | Structure agent/tool communication as a DAG, not a loop without exit. |
| **Filter, do not blindly replicate** | Vet discovered capabilities and external tools before use. |
| **Capability ≠ effectiveness** | A powerful tool is only useful if it fits the task; prefer confidence and cost-aware selection. |

---

## Implementation Notes

- The loop can be implemented in code, as a LangGraph-style state machine, or as a set of async jobs.
- Each phase should emit structured events for observability.
- Confidence estimates should be calibrated and logged.
- The loop should degrade gracefully: if discovery fails, fall back to a simpler plan rather than stopping.
- Cost and latency budgets should be enforced at the **Adapt** phase and monitored during **Perform**.

---

## Example Pseudocode

```python
class ADAPTLoop:
    def run(self, request: Request) -> Response:
        # ANALYZE
        analysis = self.analyze(request)
        if analysis.confidence < self.thresholds.min_confidence:
            return self.ask_clarification(analysis)

        # DISCOVER
        capabilities = self.discover(analysis)

        # ADAPT
        plan = self.adapt(analysis, capabilities)
        if plan.requires_approval:
            return self.request_approval(plan)

        # PERFORM
        result = self.perform(plan)

        # TRANSFORM
        self.transform(request, plan, result)

        return result
```

---

## Relation to Other Protocols

- **Memory tiers protocol:** Provides the L1–L4 stores that the Discover and Transform phases use.
- **Consolidation-cycle protocol:** Runs asynchronously to promote Transform outputs into durable memory.
- **Evolution-engine protocol:** Uses traces from Perform/Transform to evolve prompts and skills.
