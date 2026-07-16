# Protocol — Review (judging a worker report)

> Load when a worker report arrives. The cardinal rule: NEVER trust the worker's "done" claim. Verify yourself (FM-09).

## Steps
1. **Read the report** (`work/reports/wave-N/0X-*.report.md`). Note: Result, acceptance checks, decisions, blockers.
2. **Re-run every acceptance command yourself** via Bash. Paste the output. The worker saying "passes" is not evidence — your run is.
3. **Spawn the `verifier` sub-agent** for non-trivial tasks: independent read of the code with no bias toward what was just written.
4. **Cross-check against the spec** (`.specify/specs/wave-N/spec.md` + contracts). Did it hit every requirement? Only the happy path, or edge cases too?
5. **Check the boundaries.** Did the worker touch only its declared files? Anything in the NOT-TOUCH list? Anything added outside the brief (FM-08)?
6. **Check against the kernel + constitution.** No silent fallbacks (FM-11), no hardcoded config (FM-06), soft-delete not hard-delete, etc.
7. **Run the relevant validators** (`validate_state`, `check_references`, `check_metrics`, `publish_gate` as applicable).

## Decision
- **APPROVE** → `/merge`.
- **REVISE** → the brief was unclear or the work fell short. Rewrite the brief with specifics, redispatch. (Don't argue with the worker; fix the brief.)
- **REJECT** → fundamentally wrong. Move output to `attic/rejected-...`, re-plan the task.

## Red flags that force REVISE/REJECT
- Acceptance "passed" but no output pasted, or your re-run fails.
- Files created outside the declared set.
- A `try/except: pass` or silent fallback introduced.
- A metric stated that isn't from the canonical source.
- Tests that only pass in isolation (run them in the suite — FM-10).
- A config value hardcoded instead of read from config.

## After approve
- `/merge` runs post-merge-format, wave tests, updates EXECUTION.md (replace row), CHANGELOG, HANDOFF, events.jsonl.
- If anything fails post-merge, REVERT and downgrade to REVISE — never leave a half-merged broken state.
