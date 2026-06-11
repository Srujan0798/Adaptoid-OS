# Pattern: Obsidian Second Brain

## Context
Agent memory is opaque (vector stores, chat logs). Humans can't read or edit it.

## Pattern
Use Markdown files as the primary archival memory. Human-editable, machine-parseable, version-controllable.

## Recipe
1. Store facts in `memory-bank/facts/` with TTL.
2. Store decisions in `memory-bank/decisions/` as ADRs.
3. Store lessons in `memory-bank/lessons/` with wave attribution.
4. Sync with Obsidian vault for human browsing.

## Anti-patterns
- Memory only in vector DB (opaque, non-editable).
- No TTL discipline — memory grows forever.
