# Evolution Engine Protocol

An optional, experimental protocol for improving an agent harness over time through trace capture, skill libraries, and reflective prompt evolution. The ideas here are derived from recent research (GEPA, Voyager-style skill libraries, Reflexion, TextGrad) and should be treated as advanced features, not core requirements.

**Status:** Experimental / optional.

---

## Overview

The evolution engine improves the harness by learning from execution traces rather than by fine-tuning model weights. It operates in three layers:

```
+----------------------------------------------------------+
| LAYER 3: META-OPTIMIZATION (GRAO)                        |
| Learns which optimization strategies work for which tasks|
+----------------------------------------------------------+
| LAYER 2: PROMPT EVOLUTION (GEPA + TextGrad)              |
| Reflects on failures and evolves prompts genetically     |
+----------------------------------------------------------+
| LAYER 1: EXECUTION LEARNING (Trace Intelligence)         |
| Captures and learns from every execution trace           |
+----------------------------------------------------------+
```

Each layer builds on the one below. A deployment can start with Layer 1 and add Layers 2 and 3 later.

---

## Layer 1: Trace Intelligence

**Purpose:** Capture and index every execution so that successes and failures become reusable signals.

**Trace schema (example):**

```python
class ExecutionTrace:
    trace_id: str               # UUID
    task_type: str              # Semantic category
    prompt_version: str         # Prompt lineage
    input_fingerprint: str      # Hash of anonymized input
    output: str                 # Generated output
    reasoning_chain: List[str]  # Step-by-step reasoning
    tool_calls: List[ToolCall]  # Tools invoked
    errors: List[ErrorLog]      # Exceptions or failures
    timing_ms: Dict[str, int]   # Per-phase latency
    success: bool               # Outcome
    confidence: float           # Self-assessed confidence
    verification: str           # Self-verification output
    user_feedback: Optional[str]
```

**What to do with traces:**

| Action | Description |
|---|---|
| Store | Index traces in a vector database for retrieval. |
| Mine patterns | Extract recurring success patterns and failure signatures. |
| Retrieve similar | Prepend relevant past reflections to similar tasks. |
| Elevate known issues | After N occurrences of the same failure, flag it for prompt repair. |

**Example:** If a web-search tool repeatedly returns stale results for a particular query shape, the pattern miner can surface this signature and trigger a workflow fix.

---

## Layer 2: Prompt Evolution (GEPA)

**Purpose:** Improve prompts over time by treating them as a population of variants and selecting the Pareto-optimal ones.

GEPA (Genetic-Pareto Prompt Evolution) uses reflection-guided mutation instead of random mutation. It reportedly improves over reinforcement-learning baselines in research settings, but results will vary by task.

### GEPA cycle

```
1. Initialize population from seed prompt
2. Select parent from Pareto front
3. Execute on minibatch and capture full traces
4. Reflect — diagnose failures in natural language
5. Mutate — generate child prompt guided by reflection
6. Evaluate child on full validation set
7. Accept if improved; update Pareto front
8. Repeat until convergence or budget exhausted
```

### Key parameters

| Parameter | Default | Range | Notes |
|---|---|---|---|
| `max_iterations` | 5–10 | 3–50 | Total mutation attempts. |
| `minibatch_size` | 4–8 | 2–16 | Examples used per reflection. |
| `patience` | 3–4 | 2–10 | Early stop after consecutive rejections. |
| `population_size` | 10–20 | 5–50 | Prompts maintained per generation. |
| `max_pareto_size` | 20 | 5–50 | Trim to control memory. |
| `reflection_lm` | GPT-4o | Any capable LLM | Model that diagnoses failures. |
| `mutation_lm` | GPT-4o | Any capable LLM | Model that generates child prompts. |

### Pareto selection

A prompt survives if it dominates at least one other prompt on at least one dimension (e.g., accuracy, cost, latency). This preserves diversity and reduces premature convergence.

### TextGrad complement

TextGrad performs instance-level optimization via textual gradients. While GEPA optimizes across many executions, TextGrad can correct a prompt within a single execution. The two can be combined:

- **TextGrad:** Immediate correction during a single task.
- **GEPA:** Long-term population-level improvement across tasks.

---

## Layer 3: Meta-Optimization (GRAO)

**Purpose:** Learn which optimization settings work best for different task profiles.

GRAO (Group Relative Agent Optimization) tracks historical optimization runs and adapts parameters such as mutation strategy, population size, and selection pressure based on what has worked in the past.

**Example adaptation:**

```python
class GRAO:
    def adapt_parameters(self, task_profile: TaskProfile) -> EvolutionConfig:
        similar_runs = self.find_similar_runs(task_profile, k=10)
        if len(similar_runs) < 3:
            return self.default_with_exploration(task_profile)
        best_params = self.analyze_what_worked(similar_runs)
        # 15% exploration
        if random.random() < 0.15:
            return self.perturb(best_params)
        return best_params
```

This layer is the most experimental. It requires substantial optimization history before it becomes useful.

---

## Skill Libraries (Voyager-Style)

**Purpose:** Store reusable capabilities as executable programs rather than as model weights.

A skill library helps avoid catastrophic forgetting and makes learned behavior inspectable. Each skill is a small, versioned artifact.

**Skill schema (example):**

```yaml
skill:
  name: summarize_web_page
  description: Fetch a URL and return a concise summary.
  embedding_description: "summarize web page url fetch content"
  code: |
    def run(url: str) -> str:
        html = fetch(url)
        text = extract_text(html)
        return llm_summarize(text)
  dependencies: [fetch, extract_text, llm_summarize]
  tests:
    - input: "https://example.com/article"
      asserts: ["len(output) < 500", "output contains 'summary'"]
```

**Skill lifecycle:**

1. **Propose:** The system proposes a new skill from repeated successful traces.
2. **Test:** The skill runs against a test suite in a sandbox.
3. **Review:** A human approves or rejects the skill.
4. **Register:** Approved skills are added to L4 procedural memory.
5. **Evolve:** Skills can be composed from simpler skills.

---

## Self-Modification Guardrails

Any system that can modify its own prompts, skills, or code needs strict guardrails. The following constraints are non-negotiable for evolved variants.

| Constraint | Requirement | Rationale |
|---|---|---|
| Test suite | 100% pass rate | Functional correctness must hold. |
| Size limits | Skills ≤ 15 KB, descriptions ≤ 500 chars | Prevents prompt bloat. |
| Semantic preservation | Cosine similarity ≥ 0.85 with original | Prevents drift to a different purpose. |
| Regression tests | All existing tasks must still pass | No improvement at the expense of prior capability. |
| Cost budget | Max $10 per optimization run | Controlled operational expenditure. |
| Human review | Required for score changes > 10 percentage points | Oversight for major capability shifts. |

### Additional safeguards

- **Sandboxed execution:** Test all evolved code in an isolated environment.
- **Rollback:** Maintain the previous prompt/skill version and revert automatically on regression.
- **Diversity enforcement:** Maintain multiple prompt variants to avoid monoculture failures.
- **Audit trail:** Log every proposed change, test result, and approval decision.

---

## Configuration Example

```yaml
evolution_engine:
  enabled: false  # Opt-in; default off

  layer1_trace_intelligence:
    trace_capture: true
    episodic_memory_capacity: 3
    skill_library_embedding_model: "text-embedding-3-large"
    pattern_miner_threshold: 3
    reflection_trigger: "on_failure"  # on_failure | always

  layer2_prompt_evolution:
    gepa:
      max_iterations: 8
      pareto_size: 4
      minibatch_size: 6
      patience: 3
      tie_breaker: "PREFER_ROOT"
      population_size: 15
      reflection_lm: "gpt-4o"
      mutation_lm: "gpt-4o"
      max_pareto_size: 20
    textgrad:
      backward_engine: "gpt-4o"
      optimization_steps: 3
      learning_rate: 0.3

  layer3_meta_optimization:
    grao:
      history_window: 50
      exploration_rate: 0.15
      adaptation_frequency: "per_run"
      similarity_threshold: 0.7

  safety:
    test_pass_rate_required: 1.0
    semantic_similarity_threshold: 0.85
    max_skill_size_kb: 15
    max_description_length: 500
    max_cost_per_run_usd: 10.0
    human_review_threshold_pp: 10.0
```

---

## Metrics

Track the following to decide whether the evolution engine is delivering value:

| Metric | Target | Notes |
|---|---|---|
| Improvement rate | +2% per optimization cycle | Delta in task success rate. |
| Prompt quality score | > 0.80 F1 | Weighted accuracy on held-out eval set. |
| Task completion rate | > 95% | Fraction completing without error. |
| Cost efficiency | <$5 per percentage point | Optimization cost per improvement. |
| Pareto coverage | > 10 distinct niches | Diversity of behaviors on the front. |
| Mutation acceptance rate | 20–40% | Accepted / total mutations. |
| Regression frequency | < 2% | Optimizations causing regressions. |
| Capability growth | +1 task type per week | New solvable categories. |

---

## Operational Notes

- **Start with Layer 1 only.** Trace capture and retrieval provide value with minimal risk.
- **Add GEPA only after you have a validated evaluation harness.** Without good evals, prompt evolution will game the wrong metric.
- **Keep humans in the loop for L4 changes.** Procedural memory affects behavior directly.
- **Treat reported research gains as ceilings, not guarantees.** Your task distribution and data quality will differ from the papers.
- **The evolution engine is optional.** A useful agent harness does not require self-improvement to operate.
