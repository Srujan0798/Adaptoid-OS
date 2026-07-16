# Example: Data Pipeline

## Brief
Build an ETL pipeline that ingests e-commerce transactions, cleans them, and loads to a data warehouse.

## Archetype
`data-pipeline`

## Tier
T2

## Waves
1. **Ingest** — API connectors, schema validation, error handling
2. **Transform** — deduplication, enrichment, aggregation
3. **Load** — warehouse schema, incremental loads, partitioning
4. **Monitor** — data quality checks, alerting, lineage

## Outcome
- 1M+ records/day throughput
- Data quality score > 99%
- Full lineage tracked in `memory-bank/decisions/`
