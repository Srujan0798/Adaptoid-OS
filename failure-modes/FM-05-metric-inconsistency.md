# FM-05 — Metric Inconsistency (same fact, two values)

**Symptom.** The report says one number, the README says another, the slide says a third. A reviewer catches the contradiction and trust collapses.

**Real incident.** DRO-FairML: IF wins reported as both `7/9` (mean-based) and `5/9` (Wilcoxon) in different files; runtime as both `~54×` and `~37.5×`; Credit α=0.3 IF as both `-100%` and `-96%`. Each required a hunt-and-fix sweep across many files.

**Root cause.** The same metric was hand-copied into multiple documents. When the computation was corrected once, the copies weren't. No single source of truth for results.

**Blast.** In a graded/reviewed/customer context, one caught inconsistency makes every other number suspect. Hours lost reconciling.

**Prevention rule.** Metrics have exactly ONE source: a generated file (e.g., `results/metrics.json` or `results/summary.csv`) produced by a script from raw data. Every doc either `\input`s/imports it or is regenerated from it. Humans never hand-type a metric into prose.

**Validator.** `validators/check_metrics.sh`:
- Reads `results/metrics.json` as canonical.
- Greps docs for number patterns near metric keywords; flags any that don't match canonical (within tolerance).
- Fails CI if a doc states a metric absent from / different than canonical.

**Wire-in.** CI on every push; review protocol before `/ship`.

**Fix when it fires.** Delete the hand-typed number; reference the generated source; regenerate the doc.

**Design note.** Prefer generated tables (CSV → LaTeX/MD) over prose numbers everywhere. A number that can't drift is a number generated, not typed.
