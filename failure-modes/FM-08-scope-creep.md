# FM-08 — Scope Creep / Over-Building

**Symptom.** Features nobody asked for. 8 prompt files when 3 would do. 10 planning docs that go stale. A worker "also added" something outside its brief. The build balloons and confuses.

**Real incident.** Across the OS-Setup iterations themselves: a 10-document strategic plan, an 8-prompt folder, 30 pre-built slash commands — the user repeatedly said "it's too confusing." In rfq2boq, prompt folders multiplied across waves until navigation needed its own INDEX.

**Root cause.** No explicit boundary between "in scope now" and "maybe later." Agents optimize for completeness, not for the smallest thing that ships. Workers treat "while I'm here" as license.

**Blast.** Wasted effort, maintenance burden, stale docs, user confusion, slower shipping, more surface for every other failure mode.

**Prevention rule.**
- `docs/SCOPE_GUARD.md` lists IN / OUT / LATER explicitly. Anything not IN requires updating that file first (with an ADR for big additions).
- Every worker brief lists files it may touch AND files it must NOT.
- Tier discipline: don't pull T3/T4 features into a T1 MVP.
- "Start simple, add structure only when the simple version fails" (Anthropic).

**Validator.** `validators/check_scope.sh`:
- Compares files changed in a worker's report against the brief's declared file list; flags additions outside it.
- Flags new top-level files/dirs not declared in HIERARCHY.md.

**Wire-in.** Review protocol (orchestrator rejects out-of-scope additions); pre-commit warns on undeclared top-level files.

**Fix when it fires.** Revert the unrequested addition, or file it as a new task in `BACKLOG.md` for a future wave. Never silently absorb it.
