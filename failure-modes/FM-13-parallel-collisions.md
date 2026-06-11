# FM-13 — Parallel Collisions (two workers, one file)

**Symptom.** Two OpenCode workers running in parallel both edit the same file; one's changes clobber the other's; merge conflicts; a "done" task silently overwritten.

**Real incident.** Risk inherent to the dual-tier parallel model (multiple OpenCode windows). In rfq2boq/swa-erp waves, the discipline of disjoint file ownership per task was what kept parallel dispatch safe — when briefs overlapped, collisions loomed.

**Root cause.** Two task briefs in the same wave were not disjoint — they shared a file in their "create/modify" lists. Parallel workers have no awareness of each other.

**Blast.** Lost work, corrupted files, a merge that drops one worker's output, time wasted re-doing.

**Prevention rule.**
- Within a wave, task briefs must have DISJOINT write sets. The orchestrator checks this at dispatch time.
- Shared foundational files (models, schema, config) are owned by a single early task; later tasks depend on it, not edit it concurrently.
- If two tasks truly need the same file, they are SEQUENCED (dependency), not parallelized.
- Optional: each worker on its own `git worktree`/branch; orchestrator merges serially.

**Validator.** `validators/check_dispatch_disjoint.sh`:
- Parses all `work/wave-N/*.md` "Files to create/modify" sections.
- Fails if any file appears in two task briefs' write sets without an explicit dependency ordering.

**Wire-in.** `/dispatch` runs it before writing briefs; refuses to dispatch overlapping briefs.

**Fix when it fires.** Re-cut the briefs so write sets are disjoint, or add a dependency so they run in sequence.
