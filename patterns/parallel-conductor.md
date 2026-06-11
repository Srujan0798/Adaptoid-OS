# Pattern: Parallel Conductor

## Source
Garry Tan / gstack (2026).

## Context
Single-threaded orchestration is too slow for complex projects. Multi-agent chat devolves into chaos.

## Pattern
Fork 10–15 **isolated sprint workspaces**, each with a typed handoff. Orchestrator plans; conductors execute; rollup merges.

## Recipe
1. Define workspace boundaries (file ownership, scope).
2. Assign each workspace a self-contained brief.
3. Run workspaces in parallel with token budgets and termination caps.
4. Roll up results through a matched review gate.

## Anti-patterns
- Shared state between workspaces.
- No termination cap — runaway parallel cost.

## Headroom
Verified from gstack: 23 skills, conductor pattern reduces wall-clock time by 60–80%.
