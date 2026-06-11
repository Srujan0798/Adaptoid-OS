# Pattern: Three-Layer Planning Review

## Context
Plans are often written once and never revisited. Drift between plan and execution is invisible until it's catastrophic.

## Pattern
Every plan passes through three layers of review before execution:

1. **Layer 1 — Schema check** — Does the plan match the archetype template? (automated)
2. **Layer 2 — Sanity check** — Does the plan fit the tier and timebox? (orchestrator self-review)
3. **Layer 3 — Independent review** — Does a second agent (or human) agree the plan is sound?

## Recipe
- Layer 1: `validators/check_intent.sh` + archetype validator
- Layer 2: Orchestrator asks itself: "Would I ship this plan as-is?"
- Layer 3: Dispatch a reviewer sub-agent or ask the user

## Anti-patterns
- Single-author plans with no review.
- Plans that grow without updating EXECUTION.md.
