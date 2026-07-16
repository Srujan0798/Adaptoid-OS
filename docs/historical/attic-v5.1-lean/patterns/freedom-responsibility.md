# Pattern: Freedom & Responsibility

## Source
Netflix Culture Memo (2009), adapted for agentic AI (2026).

## Context
Agents need autonomy to be useful, but autonomy without guardrails causes disasters.

## Pattern
High autonomy + strong guardrails + deep observability + resilient recovery.

## Recipe
1. Grant agents broad authority to read, plan, and execute within their scope.
2. Enforce runtime validation before any state persists.
3. Log every decision to an immutable audit trail with cost attribution.
4. On failure, automatically rollback and escalate after retry exhaustion.

## Anti-patterns
- Micromanaging agents (low autonomy).
- "Trust but don't verify" (no guardrails).
