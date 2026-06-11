# Archetype — Data Pipeline / Analytics

**Signals.** "ETL", "ELT", "data warehouse", "pipeline", "Airflow/dbt", "analytics", "dashboard", "ingest → transform → load", scheduled jobs.

**Default tier.** T2 (data correctness is production-grade).

## Emphasize
- **Idempotency.** Re-running a job produces the same result; no double-counting. Partition + upsert, not blind append.
- **Data contracts + validation.** Schema checks at every boundary; reject/quarantine bad rows loudly (FM-11), never silently drop.
- **Lineage.** Know what feeds what; a change upstream's blast radius is traceable.
- **Reproducible runs.** Same input window → same output. Backfills are deterministic.
- **One source of truth for metrics.** Dashboard numbers come from defined, tested transformations, not ad-hoc SQL (FM-05).
- **Freshness + volume checks.** Alert when a source is stale or row counts swing.

## Skip
- UI beyond the dashboard
- Multi-tenancy (unless multi-customer data)
- Auth/RBAC beyond warehouse roles

## Folders
- `src/{ingest,transform,load,quality}`, `pipelines/` (DAG defs), `tests/{unit,data_quality}`, `sql/` or `models/` (dbt), `configs/`, `docs/{lineage,schema,runbook}`.
- `data/` with raw/staged/marts conventions.

## Highest-risk failure modes
- **FM-11 silent failures** — a dropped/null-coalesced row corrupts a metric invisibly. Quarantine + alert, never silent.
- **FM-02 stale process** — overlapping pipeline runs double-count. One run per window; lock.
- **FM-05 metric inconsistency** — dashboard vs report vs ad-hoc query disagree. One transformation layer is canonical.
- **FM-06 config revert** — date windows / source configs asserted.
- **FM-10 flaky** — data-quality tests must be deterministic against fixtures.

## Definition of done
- Pipeline runs idempotently end-to-end on a sample window
- Data-quality checks pass; bad data quarantined + alerted
- Dashboard metrics trace to tested transformations
- Backfill reproduces historical output

## Deliverables
- The pipeline (DAGs/dbt project)
- Data-quality suite
- Lineage + schema docs
- Dashboard
