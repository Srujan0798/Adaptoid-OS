# Example: Emergency Bug Fix

## Brief
Production API returning 500s under load. Root cause unknown.

## Archetype
`internal-tool`

## Tier
T1 (emergency)

## Process
1. **Diagnose** — logs, metrics, reproduction script
2. **Fix** — minimal patch, no refactoring
3. **Verify** — load test, regression test
4. **Document** — post-mortem in memory-bank/lessons/

## Outcome
- Root cause identified in 2 hours (connection pool exhaustion)
- Fix deployed in 4 hours
- Lesson crystallized: `memory-bank/lessons/LESSON-001.md`
