# Pattern: Six Enforced Questions

## Context
Agents rush to implementation without clarifying intent, leading to FM-08 (scope creep) and FM-09 (false status).

## Pattern
Before any build phase, the orchestrator MUST answer six questions:

1. **What is the smallest thing that proves this works?**
2. **What are we explicitly NOT building?**
3. **What would falsify success?**
4. **Who will verify this is done?**
5. **What is the cost ceiling?**
6. **What is the rollback plan?**

## Recipe
Write answers into `PROJECT-INTENT.md` or `plan/EXECUTION.md`. No build starts until all six are answered.

## Anti-patterns
- "Let's just start coding and figure it out."
- Vague scope definitions like "make it better."
