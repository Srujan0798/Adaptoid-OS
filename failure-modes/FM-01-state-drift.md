# FM-01 — State Drift (duplicate / contradictory state)

**Symptom.** A status file contains two rows for the same item that disagree; duplicate section headers; a "current state" that contradicts itself.

**Real incident.** ⚡LIVE in `swa-erp/plan/EXECUTION.md` at the time this folder was built:
- Line 32: `| 3 | Quotation / BOQ workflow | READY TO DISPATCH | 0/5 |`
- Line 33: `| 3 | Quotation/BOQ workflow | pending | — |`
- Two identical `## Changelog (waves shipped)` headers (lines 84 and 89).

**Root cause.** The agent **appended** new status instead of **replacing** the old. Across sessions, each update added a row rather than rewriting the table to current truth. The model then reads both and either contradicts itself or picks the stale one.

**Blast.** The orchestrator dispatches the wrong wave, re-does shipped work, or reports false progress to the user. Compounds every session.

**Prevention rule (kernel law 8).** Status files are REWRITTEN to current truth, never appended. Append-only is exclusively for `events.jsonl` and `attic/`. A status table has exactly one row per item.

**Validator.** `validators/validate_state.sh`:
- Parses every status table in `plan/EXECUTION.md`; fails if any item ID appears twice.
- Fails if any `##` header text appears more than once in the file.
- Fails if "Active wave" in EXECUTION.md ≠ "Active wave" in HANDOFF.md.

**Wire-in.**
- Pre-commit hook (blocks the commit).
- CI `docs_sync.yml`.
- Orchestrator review protocol: run before every `/merge` and `/ship`.

**Fix when it fires.** Open the file, delete the stale duplicate, keep ONE row reflecting current truth, re-run the validator.
