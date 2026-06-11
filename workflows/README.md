# Workflows — Parameterized Flow Library

> Reusable execution patterns the Adaptor composes into a project's `workflows/<project>.plan.yaml`. Each is a named, parameterized flow with phases, gates, parallelism, and self-heal rules. Pull the ones that fit the archetype.

## Catalog
| Flow | Use for | Parallel? | Gates |
|---|---|---|---|
| `planner-coder-reviewer.yaml` | default feature work | yes (coders) | eng-review + acceptance |
| `conductor-parallel.yaml` | high-velocity, 5+ slices | heavy (10–15 sessions) | matched review per slice |
| `long-horizon-checkpoint.yaml` | multi-day tasks | partial | checkpoint every phase + resumable |
| `graph-synthesis.yaml` | research / docs / codebase understanding | yes | grounding + citation |
| `multi-agent-debate.yaml` | hard decisions, ambiguous design | yes (debaters) | converge + human ratify |
| `self-healing-verify.yaml` | reliability-critical | — | acceptance + verifier + retry loop |
| `cost-aware-routing.yaml` | cost-sensitive / high-volume | yes | budget gate + model cascade |
| `hackathon-sprint.yaml` | 24–72h demo build | yes | demo-path gate only |
| `production-deploy.yaml` | shipping to prod | — | security + perf + canary |

## Common shape (every flow)
```yaml
name: <flow>
params: {wave, parallelism, budget, ...}
phases:
  - {id, role, inputs, outputs, acceptance, blast_radius}
gates: {pre_dispatch, pre_merge, pre_ship}
parallelism: <n or "none">
self_heal: {on_acceptance_fail, on_flaky, on_drift, on_context_full}
verification: [layers from protocols/verification.md]
```

## How the Adaptor uses these
At COMPOSE time, the engine picks 1–3 flows for the archetype and parameterizes them into the project plan. Example: `internal-tool` → `planner-coder-reviewer` per wave + `self-healing-verify`; `hackathon` → `hackathon-sprint`; `research-ml` → `graph-synthesis` (lit review) + `long-horizon-checkpoint` (experiments).

## Design rules
- Phases declare disjoint write sets (FM-13).
- Every phase has an executable acceptance + a blast-radius tag.
- Every flow has self-heal rules so the runner recovers without a human.
- Gates are mandatory; parallelism never bypasses review.
