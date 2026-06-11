# FM-12 — Stale Derived Docs (README with old numbers)

**Symptom.** The README shows results from a run that's been superseded. A doc describes an architecture that changed three waves ago. The "current status" badge is months old.

**Real incident.** DRO-FairML README carried a results table from old wrong-param runs (`41/150 experiments`, specific win-rates) long after those runs were invalidated and replaced. It had to be manually purged. rfq2boq README linked a documentation table to deleted files.

**Root cause.** Derived content (results, status, file maps) was hand-written into docs, then the underlying reality changed, but the doc wasn't regenerated. Derived = should be generated, not authored.

**Blast.** Reviewer reads stale/wrong numbers → either misled or loses trust. Compounds FM-05 (inconsistency) and FM-03 (broken refs).

**Prevention rule.**
- Anything DERIVED is GENERATED, never hand-typed: results tables (from `results/metrics.json`), file maps (from the actual tree), status (from EXECUTION.md), API docs (from OpenAPI).
- README's results section `\input`s/embeds the generated artifact or is rebuilt by a script.
- "Status: as of <git-sha>" stamps so staleness is visible.

**Validator.** `validators/check_derived_docs.sh`:
- Re-generates derived sections to a temp file; diffs against committed; fails if they differ (someone hand-edited or forgot to regenerate).
- Checks README result numbers against `results/metrics.json` (overlaps FM-05).
- Checks any "file structure" block in docs against the real tree.

**Wire-in.** CI `docs_sync.yml`; `/ship` regenerates all derived docs before tagging.

**Fix when it fires.** Re-run the generator; never hand-patch the number.
