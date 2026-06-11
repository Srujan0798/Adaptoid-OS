# The Adaptor Engine

> The mechanism that makes OS-Setup an *adaptoid*: feed it (this DevKit + a project brief) and it analyzes the target, pulls exactly the relevant components, and emits an executable, tailored setup + execution plan. Not a static template — a self-adapting transform.

## Design decisions (locked)
1. **Hybrid architecture.** The core (kernel laws, two-tier orchestration, failure-modes, validators, adaptor) is INDEPENDENT — not locked inside any framework. Compatibility ADAPTERS bridge to LangGraph/CrewAI/AutoGen/etc. when beneficial (see `reference/ecosystem/compatibility-adapters.md`). Best of both: ecosystem reach + sovereign core.
2. **Executable-first output.** The engine emits machine-consumable artifacts FIRST (YAML/JSON specs, configs, manifests), human guidance SECOND. Velocity needs actionable artifacts, not prose to re-interpret. (See `OUTPUT_SPEC.md`.)
3. **Runtime-context-checks are primary persistence.** The generated project validates/refreshes context before each major phase; git hooks/daemons are optional enhancers, never dependencies. (See `../protocols/runtime-context-check.md`.)

## The 6-step transform

```
INGEST    Read: this DevKit (kernel + INDEX) + the project brief + any existing code/config.
   ↓
ANALYZE   Detect: archetype (archetypes/), tier (tiers/), domain, constraints, success criteria,
          deadline, audience, risk profile. Identify the highest-risk failure modes.
   ↓
PULL      From reference/ecosystem/SELECTION.md → the smallest winning stack.
          From skills-catalog → the skills tasks will need.
          From workflows/ → the flow templates that fit.
          From failure-modes/ → the validators to wire in.
          (Pull only what matches; close the books — HOW-TO-PULL.md.)
   ↓
COMPOSE   Produce the executable artifacts (OUTPUT_SPEC.md):
          - project structure (archetype+tier adapted)
          - workflow specs (DAG/phases/gates/parallelism) as YAML
          - skill/tool manifest + mcp.json + routing
          - validator wiring (pre-commit + CI + review)
          - tailored CLAUDE.md/KIMI.md kernel + wave-1 task files
   ↓
RECORD    Write docs/decisions/0002-stack-selection.md (ADR): chosen stack + why + rejected.
   ↓
VERIFY    Run validators/preflight.sh. Must pass before declaring ready.
```

## Inputs the engine accepts
A brief in any form (PDF text / paragraph / one line) plus optional context:
`deadline · audience · orchestrator model · worker tool · tech preference · must-not-do · success criteria (e.g. "win hackathon" / "production deploy")`.
Missing context → the engine runs the `interviewer` protocol (≤4 multiple-choice questions), never guesses silently.

## Outputs the engine produces
1. **Tailored harness setup** — structure + configs + setup commands.
2. **Optimal skill/workflow composition** — which skills, which workflow templates, wired.
3. **Execution plan** — waves, parallelism strategy, checkpoints, verification gates, blast-radius gates.
4. **Generated configs/code** — mcp.json, CI, pre-commit, kernel, wave-1 briefs, workflow YAML.

## Why this beats a static setup
A static template gives every project the same thing. The Adaptor gives each project the *smallest stack that wins it*, pulled from the collective frontier, with the *specific* failure-validators its risk profile needs, and an *executable* plan — so the AI that runs it starts at the frontier instead of from zero. The adaptation IS the moat.

## The invariant
Whatever it adapts, it never violates the kernel (PRINCIPLES, TWO-TIER, ANTI-HALLUCINATION) and always wires the failure-mode validators. Adaptation changes the *what*, never the *discipline*.
