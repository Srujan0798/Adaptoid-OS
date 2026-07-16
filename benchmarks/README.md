# Benchmarks

Lightweight **speed + correctness** suite for Adaptoid Core (not model accuracy).

## Run

```bash
bash benchmarks/run_bench.sh
# or
make bench
```

Writes `benchmarks/last_results.json` on success.

## What it measures

| Metric | Meaning |
|---|---|
| `engine_core_all_hosts_s` | Time to generate Core project with `--host all` |
| `host_surfaces_ok` | AGENTS/CLAUDE/Cursor/kernel/preflight present |
| `preflight_ok` / `preflight_s` | Generated project preflight |
| `conductor_s` / `reports` | init-wave + stub dispatch + report count |
| `dogfood_ok` / `dogfood_s` | Kit self-validation |

## Targets (local laptop, guide rails)

| Metric | Healthy |
|---|---|
| engine core | &lt; 5s |
| preflight | pass |
| reports after stub dispatch | ≥ 3 |
| dogfood | pass |

Model quality / cost benchmarks are **out of band** — run those on your eval harness of choice and store under `calibration/`.
