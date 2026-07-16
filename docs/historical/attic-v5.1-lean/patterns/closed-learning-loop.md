# Pattern: Closed Learning Loop

## Source
Hermes Agent / Nous Research (2026).

## Context
Agent prompts and skills are static. They don't improve from experience.

## Pattern
After every task, a meta-agent analyzes traces and auto-generates/refines skills.

## Recipe
1. Capture trajectory (input, output, verification results, failures).
2. Analyze: what worked, what failed, what pattern emerged?
3. Crystallize: write/update `SKILL.md` entries.
4. Write lesson: append to `memory-bank/lessons/`.
5. Propose validator: if a new failure mode was observed, propose FM + validator.

## Anti-patterns
- Manual prompt tuning only.
- Ignoring failures rather than crystallizing them.
