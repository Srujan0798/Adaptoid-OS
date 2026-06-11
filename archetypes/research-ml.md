# Archetype — Research / ML Experiments

**Signals.** "paper", "experiments", "ablations", "baselines", "seeds", "reproduce", "metrics", "theorem", "benchmark". (DRO-FairML type.)

**Default tier.** T2 (reproducibility is production-grade here even if there's no "prod").

## Emphasize
- **Reproducibility above all.** Fixed seeds, pinned deps, one command reruns everything, results deterministic. A reviewer must reproduce your table.
- **Single source of truth for results.** `results/metrics.json` generated from raw runs; tables/figures/report all derive from it. (FM-05 is the #1 killer here.)
- **Config as law.** Every hyperparameter in one config, asserted at runtime (FM-06 — the epochs 60→30 revert wasted an evening).
- **One run at a time, tracked.** Process registry; never two batches on the same output dir (FM-02 — the live 157-min wrong-param run).
- **Honest results.** Report what happened, including failures (e.g., the Adult collapse). Negative results documented = rigor.
- **Statistical correctness.** State the test (Wilcoxon vs mean), apply it consistently everywhere (FM-05).

## Skip
- UI (unless the contribution is a tool)
- Multi-tenancy, billing, marketing
- Web deployment

## Folders
- Include: `src/` (data, models, training, evaluation), `experiments/`, `configs/`, `data/{raw,processed,gold}`, `results/`, `figures/`, `tests/` (incl. theory-verification + golden), `deliverables/{paper,report,slides}`, `docs/decisions`.
- `evals/` becomes `experiments/` with the same discipline (tasks=experiments, graders=metrics, pass^k≈seed-stability).

## Highest-risk failure modes (wire these first)
- **FM-02 stale process** — `check_processes.sh` before EVERY run. This is the most expensive recurring failure in research.
- **FM-05 metric inconsistency** — `check_metrics.sh` blocking; all numbers from `results/metrics.json`.
- **FM-06 config revert** — runtime assertions on every critical hyperparameter.
- **FM-09 false status** — never claim a result you didn't compute this run.
- **FM-11 silent failures** — NO synthetic-data fallback masquerading as real data; fail loud if data missing.
- **FM-12 stale derived docs** — README/report results regenerated, never hand-typed.

## Definition of done
- `make reproduce` reruns all experiments deterministically to the same numbers
- Every number in report/slides/README traces to `results/metrics.json`
- Theory/acceptance checks pass; seeds fixed; deps pinned
- Limitations + negative results documented honestly

## Deliverables
- Reproducible code + pinned env
- `results/metrics.json` (canonical) + generated tables/figures
- `deliverables/report/` + `deliverables/slides/`
