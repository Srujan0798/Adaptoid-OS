# Protocol — Dispatch (writing worker task briefs)

> Load when writing task files for OpenCode workers. The brief is the ONLY thing the worker sees. It has zero project memory.

## The 5 laws of a good brief
1. **Self-contained.** Everything needed is IN the file. No "see the spec", no "follow existing patterns" — inline the schema, the example, the exact command.
2. **Skills are theirs.** List skills the WORKER has (tdd, code-review, pdf-processing, agentskills.io ones) — NOT `orchestrator/skills/`. The worker can't see yours.
3. **Executable acceptance.** Not "make it work" — `pytest tests/x.py::test_y` exits 0. A runnable check, not prose.
4. **Explicit boundaries.** List files to CREATE/MODIFY and files to NOT TOUCH. Disjoint from sibling tasks in the wave (FM-13).
5. **Budgeted.** Time + token budget. If > ~2h or > ~50K context, split the task.

## Required sections (see templates/work/TASK_TEMPLATE.md)
- What to do (one paragraph)
- Files to create / modify
- Files you must NOT touch
- Skills to use (worker-side)
- The core problem, inline (schemas, examples, sample I/O)
- Edge cases
- Acceptance criteria (executable)
- How to deliver (write report to work/reports/...)
- Constraints (time, deps, budget)

## Before dispatching a wave
- Run `validators/check_dispatch_disjoint.sh` — no two briefs share a write target (FM-13).
- Confirm each brief's acceptance maps to a contract in `.specify/specs/wave-N/contracts/`.
- Log each dispatch to `events.jsonl`.

## Anti-patterns (these cause worker failure)
- "Look at how auth.py does it" → INLINE the pattern instead.
- "Run the tests" → name the exact command.
- "Don't break anything" → list the FORBIDDEN paths.
- Two tasks both modifying `models/__init__.py` in parallel → sequence them or give one task ownership.
- Referencing `orchestrator/skills/foo` → the worker has no access; name a worker skill.

## When a brief is ambiguous
Don't dispatch a guess. Run the `interviewer` protocol — ask the user one multiple-choice question — then write the brief.
