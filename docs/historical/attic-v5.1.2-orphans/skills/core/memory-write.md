---
name: memory-write
version: "1.0.0"
description: Write verified facts, decisions, and lessons to memory bank
verification_gates: [schema]
cost_estimate_usd: 0.01
capabilities:
  tools: [Read, Write]
  files:
    - memory-bank/
---

# Skill: Memory Write

## Purpose
Persist knowledge so future sessions don't start cold.

## Trigger
After every checkpoint, merge, or lesson learned.

## Steps
1. Classify entry: fact, decision, lesson, session.
2. Write Markdown with YAML frontmatter (id, kind, created, ttl, sources).
3. Run `validators/memory_sync.sh --index` to update SQLite FTS.

## Output
New file in `memory-bank/`.
