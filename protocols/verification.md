# Protocol — Verification (Swiss Cheese)

> Load before claiming anything "done." No single layer catches everything; stack them. Per Anthropic Jan 2026.

## The stack (each catches what the prior misses)
| Layer | Catches | Runs |
|---|---|---|
| Type checks (mypy/tsc) | type/shape errors | pre-commit + CI |
| Lint (ruff/eslint) | style + obvious bugs | pre-commit + CI |
| Unit tests | logic in isolation | pre-commit + CI |
| Integration tests | module interaction | CI |
| Acceptance contracts | spec → reality | CI + /review |
| E2E (Playwright) | user-visible flows | CI nightly |
| Eval pass@k | capability present | CI for changed waves |
| Eval pass^k | capability not regressed | every commit |
| Perf budget | latency targets | pre-deploy |
| `verifier` sub-agent | independent code read | /review |
| **Human transcript read** | grader fairness, agent loopholes | weekly |
| Production monitoring | what all the above missed | live |
| OS-Setup validators | the 14 failure modes | preflight before merge/ship |

## Who runs what
- **Workers**: unit + integration locally before reporting.
- **Orchestrator**: re-runs acceptance + evals + validators; spawns verifier. (Never trusts worker claims — FM-09.)
- **CI**: everything, on every push.
- **Humans**: read transcripts/results; nothing is taken at face value until someone reads the details.

## The evidence rule (kernel law 5)
"Done" / "passes" / "works" must come with: the command run + its output, THIS session. A claim without evidence is a hypothesis, not a status.

## Before /ship
Run `validators/preflight.sh` — it runs all wired validators (state drift, refs, metrics, processes, publish gate, config, disjoint dispatch). Must be green. Then regenerate derived docs (FM-12) so README/report match reality.
