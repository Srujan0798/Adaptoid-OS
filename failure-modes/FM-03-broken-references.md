# FM-03 — Broken References (links to deleted/nonexistent files)

**Symptom.** A doc, README, Makefile, or script references a file that doesn't exist. A command fails with "no such file." A markdown link 404s.

**Real incident.** In DRO-FairML, after cleanup, `generate_all_deliverables.py` still called `professor_review_simulator.py` (deleted), and README still linked `AGENTS.md` / `docs/DEFENSE_GUIDE.md` (deleted/renamed). In rfq2boq, the README "Documentation" table linked `agents/FINAL_AGENT_BRIEFING.md` after the `agents/` dir was removed.

**Root cause.** Files were deleted/renamed/moved but the references to them weren't updated. The agent that deleted didn't grep for inbound references first.

**Blast.** Broken builds, broken docs, the reviewer/professor clicks a dead link, the orchestrator tries to run a missing script and improvises (hallucinates) a replacement.

**Prevention rule.** Before deleting or renaming any file, grep the repo for inbound references and fix them in the same change. Every committed reference must resolve.

**Validator.** `validators/check_references.sh`:
- Extracts markdown links `[...](path)` from all `*.md`; fails on any local path that doesn't exist.
- Greps Makefile / scripts / CI for referenced file paths; fails on missing.
- Greps Python/TS imports of local modules; fails on unresolved local import.

**Wire-in.**
- Pre-commit hook.
- CI.
- Part of `validators/preflight.sh`.

**Fix when it fires.** Either restore the file (from `attic/`/git) or update the reference. Never leave a dangling pointer.
