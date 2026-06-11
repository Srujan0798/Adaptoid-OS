# 🧠 ADAPTOID-ENGINE.md

> *The brain of Adaptoid-OS. Defines the Project Intent schema, the Problem
> Adapter mechanism, the execution-plan emission rules, and the controller loop
> that ties it all together. Mandatory bootstrap reading.*

---

## 0. What this file is

`ADAPTOID-ENGINE.md` is the **single specification** for how an Adaptoid turns a
project description into a live execution environment. It is intentionally
**framework-agnostic**: the same engine is implementable in Python (the reference
runtime ships in `scripts/intent-parse.py`), but also in TypeScript, Rust, or
plain markdown discipline.

**If you read only one file in Adaptoid-OS, read this one.**

---

## 1. The Adaptoid loop (high-level)

```
        ┌───────────────────────┐
        │   ProjectIntent       │  ←  schema-typed, written by humans
        │   (input)             │     from PROJECT-INTENT.md
        └─────────┬─────────────┘
                  │
                  ▼
        ┌───────────────────────┐
        │   ProblemAdapter      │  ←  maps failure modes to controls
        │   (input)             │     from PROBLEM-ADAPTER input
        └─────────┬─────────────┘
                  │
                  ▼
        ┌───────────────────────┐
        │   ContextBinder       │  ←  pulls docs/code/memory into scope
        └─────────┬─────────────┘
                  │
                  ▼
        ┌───────────────────────┐
        │   PlanEmission        │  ←  emits typed ExecutionPlan (DAG)
        │   (typed DAG)         │     + CheckpointSpec + RollbackSpec
        └─────────┬─────────────┘
                  │
                  ▼
        ┌───────────────────────┐
        │   ExecutionController │  ←  runs nodes under verification
        │   (the loop)          │     feeds back into memory bank
        └─────────┬─────────────┘
                  │
                  ▼ (on success / partial / failure)
        ┌───────────────────────┐
        │   MemoryWriter        │  ←  writes decisions, facts, lessons
        └───────────────────────┘     back to MEMORY-INDEX
```

This loop is **deterministic up to LLM sampling temperature**. Same inputs
(within the freshness window) → same plan. Any deviation is a signal worth
investigating.

---

## 2. ProjectIntent — the typed intake schema

A `ProjectIntent` is a **structured object** that captures everything the Adaptoid
needs to emit a plan. It is deliberately minimal and deliberately **typed** — the
Adaptoid cannot act on prose alone.

### 2.1 Schema (canonical form, JSON-Schema-style)

```yaml
# PROJECT-INTENT.md  (the file humans edit; Adaptoid parses to ProjectIntent)

# 1. WHO is asking
stakeholders:
  - name: "string"
    role: "owner|reviewer|user|external"
    authority: "final|advisory|block"      # can they veto?

# 2. WHAT is the project
project:
  name: "string"
  one_liner: "<= 120 chars"
  domain: "code|research|data|ops|product|creative|hybrid"
  success_criteria:                        # measurable, falsifiable
    - id: "SC-1"
      statement: "string"
      metric: "string"
      threshold: "number|string"
      evidence: "how we will prove it"

# 3. CONSTRAINTS
constraints:
  time_box: "ISO-8601 duration"            # e.g. PT48H, P14D
  budget_usd: number|null
  compute: { gpu: bool, local_llm: bool, cloud: bool }
  data_sensitivity: "public|internal|confidential|regulated"
  compliance: ["GDPR","HIPAA","SOC2", ...]
  tech_stack_required: ["python>=3.11", "postgres", ...]
  tech_stack_forbidden: [...]

# 4. KNOWN FAILURE MODES  ←  feeds the ProblemAdapter
known_failure_modes:
  - id: "FM-hallucination"
    description: "Agent invents non-existent APIs"
    severity: "high|medium|low"
  - id: "FM-wrong-route"
    description: "..."
  - id: "FM-context-forgetting"
    description: "..."
  # …extend freely; see adapters/failure-mode-mapper.md

# 5. NON-NEGOTIABLES
non_negotiables:
  - "No production writes without human approval"
  - "All outputs type-checked"
  - ...

# 6. PREFERRED TOOLING
preferences:
  harness: "langgraph|openai_agents|claude_agent|letta|crewai|autogen|agno|smolagents|atomic_agents|other"
  llm: { primary: "...", fallback: "..." }
  memory: "letta|mem0|zep|graphiti|cognee|layered"
  durable_exec: "temporal|inngest|restate|dbos|none"
  observability: "langfuse|langsmith|logfire|phoenix|otel-only"
  local_runtime: "ollama|vllm|lm-studio|none"

# 7. DELIVERABLES
deliverables:
  - id: "D-1"
    type: "code|report|dashboard|service|doc|..."
    acceptance: "what 'done' means"

# 8. HANDOFFS
handoffs:
  - from: "agent-x"
    to: "agent-y"
    artifact: "..."
    gate: "..."

# 9. META
meta:
  freshness_window: "P7D"                  # how stale info can be
  risk_tolerance: "conservative|balanced|aggressive"
  iteration_style: "ship-fast|ship-correct|ship-once"
```

### 2.2 Parsing rules

`scripts/intent-parse.py` reads the file and:

1. Validates against the JSON Schema (`schemas/ProjectIntent.schema.json`).
2. Rejects intents with **untyped success criteria** ("looks good", "fast enough"
   are *not* acceptable — see §2.1 SC-1).
3. Auto-expands shorthand (`PT48H` → `2026-06-11T19:47:33Z + 48h`).
4. Cross-references `known_failure_modes` against
   `adapters/failure-mode-mapper.md` and produces an **augmented
   `EffectiveFailureModeList`** that includes both declared *and* inferred failure
   modes (e.g. "if `data_sensitivity: regulated` and no compliance tooling, infer
   FM-audit-trail-missing").
5. Emits an `EffectiveContext` bundle (prompt fragment + structured plan slots).

### 2.3 Worked example (intake for a 48h hackathon project)

```yaml
# PROJECT-INTENT.md  —  filled-in example

stakeholders:
  - { name: "Alex", role: owner, authority: final }
  - { name: "Jordan", role: reviewer, authority: advisory }

project:
  name: "PromptQA"
  one_liner: "Open-source eval harness for prompt regressions; ships a green/red dashboard"
  domain: code
  success_criteria:
    - id: SC-1
      statement: "Detects prompt regressions with >= 95% accuracy on a 50-case eval set"
      metric: "agreement-with-human-judge"
      threshold: 0.95
      evidence: "Eval report in reports/eval-v1.md"
    - id: SC-2
      statement: "Runs end-to-end on a fresh clone in < 5 minutes"
      metric: "time-to-first-green"
      threshold: "300s"
      evidence: "CI run on GitHub Actions"

constraints:
  time_box: PT48H
  budget_usd: 50
  compute: { gpu: false, local_llm: true, cloud: true }
  data_sensitivity: public
  compliance: []
  tech_stack_required: ["python>=3.11"]
  tech_stack_forbidden: ["closed-source-llm-only"]

known_failure_modes:
  - { id: FM-hallucination,   description: "LLM invents test cases", severity: high }
  - { id: FM-wrong-route,     description: "Eval labels confused with predictions", severity: high }
  - { id: FM-context-forget,  description: "Loses track of eval set version", severity: medium }

non_negotiables:
  - "Every test case has provenance (file + commit)"
  - "Eval is deterministic given a fixed seed"

preferences:
  harness: pydantic_ai
  llm: { primary: "ollama/llama3.1-8b-instruct", fallback: "openai/gpt-4o-mini" }
  memory: layered
  durable_exec: none
  observability: langfuse
  local_runtime: ollama

deliverables:
  - { id: D-1, type: code,    acceptance: "github.com/.../promptqa, green CI" }
  - { id: D-2, type: report,  acceptance: "reports/eval-v1.md exists" }

handoffs: []
meta:
  freshness_window: P7D
  risk_tolerance: balanced
  iteration_style: ship-fast
```

---

## 3. The Problem Adapter — the killer feature

The **Problem Adapter** is what makes Adaptoid *adaptive*. It maps a list of
known / inferred failure modes to **specific, enforceable controls** in the
generated ExecutionPlan.

### 3.1 The catalogue (excerpt — full list in `adapters/failure-mode-mapper.md`)

| Failure mode ID             | Description                                                  | Adaptoid control                                                                                  |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `FM-hallucination`          | LLM invents APIs, facts, citations                           | Require `evidence` field on every claim; route through `Verifier` node; ground in MCP-retrieved docs |
| `FM-wrong-route`            | Right tool, wrong problem / wrong file                       | Mandatory `RouteChecker` node before any side-effect; rollback spec on every non-read node        |
| `FM-context-forget`         | Agent loses setup, ignores `PROJECT-INTENT.md`               | Session-start hook re-loads `MEMORY-INDEX.md`; intent is bound to every plan, not just bootstrap  |
| `FM-orch-drift`             | Multi-agent crews desync                                     | State graph + explicit message contract; `STATE-MACHINE.md` generated per multi-agent workflow     |
| `FM-silent-ship`            | Outputs trusted without verification                         | Type-safe outputs (Pydantic AI / BAML) + evidence gate + cross-check                               |
| `FM-cost-blowup`            | Token / $ explosion                                          | Cost router: small model first, escalate on uncertainty; per-task budget guardrail                |
| `FM-skills-rot`             | Skills library goes stale                                    | Skills have `last_verified`; `verify-setup.sh` fails on stale skills                              |
| `FM-bad-eval`               | Wrong metric / wrong baseline                                | Required: holdout + human-graded subset + LLM-as-judge with calibration probe                      |
| `FM-data-leak`              | PII / secret leak across agents                              | Redaction layer in every node I/O; secret-scanner in CI                                            |
| `FM-undo-impossible`        | Long-running changes can't be rolled back                    | `RollbackSpec` required on every non-idempotent node; durable-execution step records pre-image    |
| `FM-context-bloat`          | Context window exhausted mid-task                            | Hierarchical summarization + skill pre-loading + scrollback window                                |
| `FM-wrong-model`            | Using a too-weak or too-expensive model for the task         | Cost-vs-quality matrix; per-node `model` field with downgrade path                                |
| `FM-vendor-lock`            | Hard-coupling to one provider                                | LiteLLM gateway; per-node `provider` indirection; failover in `profiles/`                          |
| `FM-bench-lying`            | Vendors / papers overstate benchmarks                        | Adaptoid requires reproducible eval runs in `reports/eval-*`; pinned seeds; pinned commit           |
| `FM-cold-start-blind`       | No context for what worked before                            | Memory Bank seeded from prior sessions; cold-start search always runs                              |

### 3.2 How the adapter emits controls

For each node in the emitted ExecutionPlan, the adapter tags it with:

```yaml
- id: "node-N"
  skill: "code.explore"           # from skills/
  inputs: [...]
  outputs: [...]
  model: { primary: "...", fallback: "..." }
  guards:
    required_evidence: true       # ←  FM-hallucination
    route_check: true             # ←  FM-wrong-route
    redaction: true               # ←  FM-data-leak
    cost_cap_usd: 0.05
    rollback:
      strategy: "git-revert"      # ←  FM-undo-impossible
      pre_image_required: true
  verification:
    - type: "type_check"          # Pydantic AI / BAML schema
    - type: "evidence_grounding"  # every claim has a source
    - type: "cross_check"         # independent second pass for high-stakes
```

The `intent-parse.py` tool emits the `EffectiveControlsBundle` directly; you
don't have to author this by hand.

### 3.3 Inferred failure modes (the smart part)

Beyond declared failure modes, the Adaptoid **infers** controls from the
ProjectIntent's other fields:

| ProjectIntent field              | Inferred failure modes                                     |
| -------------------------------- | ---------------------------------------------------------- |
| `data_sensitivity: regulated`   | `FM-audit-trail-missing`, `FM-data-leak`, `FM-undo-impossible` |
| `risk_tolerance: aggressive`     | `FM-silent-ship` (with weaker guard), `FM-cost-blowup`     |
| `iteration_style: ship-once`     | `FM-bad-eval`, `FM-context-forget` (upgraded severity)     |
| `harness: langgraph`            | `FM-graph-stale` (graph version drift)                     |
| `local_runtime: ollama`         | `FM-wrong-model` (small local model mismatch), `FM-cost-blowup` (reduced) |
| `time_box: < P7D`               | `FM-context-forget` (severity up), `FM-skills-rot` (severity up) |
| `deliverables[].type: code`      | `FM-bad-eval`, `FM-undo-impossible`                        |
| `deliverables[].type: report`    | `FM-citation-fabrication`                                   |

This inference table is open and editable; see
`adapters/failure-mode-mapper.md` for the canonical form.

---

## 4. Plan emission (the typed DAG)

The Adaptoid emits an **ExecutionPlan** as a typed DAG. Every node has:

- `id` — stable, unique
- `kind` — `task | check | gate | fanout | join | handoff | durable | human`
- `skill` — references a `skills/*/SKILL.md` (folder-based)
- `inputs` / `outputs` — typed (Pydantic / Zod / JSON Schema)
- `preconditions` — node IDs that must succeed first
- `guards` — see §3.2
- `verification` — see §3.2
- `cost_cap_usd` — hard ceiling
- `rollback` — see §3.2
- `checkpoint` — what gets persisted to memory-bank on success
- `timeout` / `retry_policy` / `on_failure`

Example (excerpt from a `examples/hackathon/PROJECT-INTENT.md`-driven plan):

```yaml
plan:
  id: "plan-promptqa-v1"
  nodes:
    - id: "n1.intent-bind"
      kind: task
      skill: "core.intent-bind"
      outputs: { type: "IntentContext" }
    - id: "n2.scaffold"
      kind: task
      skill: "code.scaffold"
      preconditions: ["n1.intent-bind"]
      rollback: { strategy: "rm-rf", pre_image_required: true }
    - id: "n3.eval-design"
      kind: task
      skill: "code.eval-design"
      preconditions: ["n2.scaffold"]
      guards: { required_evidence: true, route_check: true }
      verification: [{ type: type_check }, { type: evidence_grounding }]
    - id: "n4.route-check"
      kind: gate
      preconditions: ["n3.eval-design"]
      skill: "core.route-check"
      # if FAIL → rollback n2, n3
    - id: "n5.run-eval"
      kind: durable
      preconditions: ["n4.route-check"]
      skill: "code.run-eval"
      durable_exec: "inngest"
    - id: "n6.report"
      kind: task
      preconditions: ["n5.run-eval"]
      skill: "core.write-report"
      guards: { required_evidence: true }
  edges: [...]
  checkpoints:
    - after: "n3.eval-design"
      persist: ["intent", "eval-design", "decisions"]
    - after: "n5.run-eval"
      persist: ["metrics", "evidence"]
```

The Adaptoid runtime executes this DAG, persisting checkpoints, and emitting a
**plan trace** (OpenTelemetry-style spans) to the configured observability
backend.

---

## 5. ExecutionController — the runtime loop

The controller is intentionally tiny. Its job is to be **boring and auditable**:

```python
# pseudocode (real implementation in scripts/intent-parse.py + runtime)
while not plan.finished():
    node = plan.next_runnable()
    if node is None: break

    ctx = bind_context(node, intent, memory_bank)  # the "5 I" step 2: ingest
    out = run_skill(node.skill, ctx, node.model)   # step 3: instruct
    out = apply_guards(out, node.guards)           # step 4: inspect
    out = apply_verification(out, node.verification)
    if not out.verified:
        rollback(node, plan)
        continue
    persist_checkpoint(node, out, memory_bank)     # step 5: improve
    mark_done(node, out)
```

The point is: **the same loop runs whether the underlying skill is a 5-line
prompt, a 5-day multi-agent run, or a 5-week production deployment.** Only the
node definitions change.

---

## 6. Controller profiles (Adaptoid personality)

Different projects want different "personalities" for the controller. Profiles
are YAML in `profiles/`:

```yaml
# profiles/aggressive.yaml
risk_tolerance: aggressive
cost_ceiling_per_node_usd: 0.20
escalation_threshold: 0.55        # when to bounce to bigger model
verification:
  - type: type_check
human_in_loop: false
auto_rollback: true
```

```yaml
# profiles/conservative.yaml
risk_tolerance: conservative
cost_ceiling_per_node_usd: 0.05
escalation_threshold: 0.30
verification:
  - type: type_check
  - type: evidence_grounding
  - type: cross_check
human_in_loop: true
auto_rollback: true
```

`bootstrap.sh` defaults to `balanced`. Override with
`./scripts/bootstrap.sh --profile conservative`.

---

## 7. The Adaptoid contract (what an Adaptoid *never* does)

An Adaptoid is bound by these rules, encoded into every plan:

1. **Never act on prose alone.** Every input that influences a side-effect is
   typed.
2. **Never claim without evidence.** Every claim in an output has a source.
3. **Never write without rollback.** Every non-read side-effect has a rollback
   spec.
4. **Never trust a single verifier for high-stakes decisions.** High-stakes nodes
   get cross-check (second independent pass, or a different model family).
5. **Never silently forget.** Checkpoint before, not after, side-effects.
6. **Never escalate cost without reason.** Cost-cap-per-node is hard.
7. **Never assume yesterday's benchmarks are still true.** `last_verified` is
   enforced.
8. **Never let a vendor paper replace a local reproduction.** All benchmarks
   cited in plans are locally reproducible in `reports/`.
9. **Never skip the route-checker.** Every non-read node passes through one.
10. **Never stop asking "what would falsify this?"** Every plan has a
    `falsification` section in `PROJECT-INTENT.md`.

These are the Adaptoid's invariants. Anything that violates them is a bug, not a
feature.

---

## 8. The Engine in 200 lines (Python reference)

See `scripts/intent-parse.py` for the full reference implementation. The runtime
is intentionally small — **the value is in the schema, the controls, and the
contract, not the code**.

---

## 9. Versioning this file

`ADAPTOID-ENGINE.md` is versioned. Breaking changes (schema additions, new
required fields) bump the major version. The version is also pinned in
`docker-compose.yml` (env: `ADAPTOID_ENGINE_VERSION`) so a project can opt to
freeze.

Current: **Adaptoid-Engine v1.0** (mid-2026 state of the art).

---

## 10. TL;DR

> The Engine says: *give me a typed Intent, a typed list of failure modes, and a
> profile; I'll emit a typed DAG, with guards, verification, and rollback, that
> runs under a controller loop, with checkpoints, that an Adaptoid AI can pick
> up cold in any session and execute without forgetting, hallucinating, or
> taking wrong routes.*

🜂
