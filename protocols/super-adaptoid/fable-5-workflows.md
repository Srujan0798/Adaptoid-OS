# Fable 5 Workflows Protocol

> The v5.0 workflow library for long-horizon, multi-agent, and self-improving tasks.

## Purpose

Provide a curated, composable set of workflows that encode best practices for the five recurring v5.0 story types: research, build, review, launch, and evolve. Each workflow is a narrative with explicit triggers, steps, artifacts, and success criteria.

## Workflows

| # | Workflow | Trigger | Pattern | Success criteria |
|---|---|---|---|---|
| 1 | **Research Synthesis** | Open-ended question with conflicting sources | Three-stage research → falsification → synthesis | Source-backed answer; contradictions flagged |
| 2 | **Code Generation with Tests** | Typed intent available | Planner → coder → reviewer; tests written first | All tests pass; acceptance criteria met |
| 3 | **Review & Refactor Loop** | Existing code or report needs quality pass | Multi-critic review → ranked refactor plan → patch | Metrics improved or unchanged; no regressions |
| 4 | **Bug Hunt & Patch** | Anomaly or failure report | Reproduce → isolate → minimal patch → regression test | Bug reproduced before fix; new test prevents recurrence |
| 5 | **Documentation Sprint** | Feature shipped or API changed | Audit → generate derived docs → human read | Docs match code; no broken references |
| 6 | **Migration Assistant** | Stack or dependency upgrade | Inventory → compatibility map → canary migration → full cutover | Rollback plan exists; no silent behavior changes |
| 7 | **Release Orchestrator** | Public or internal release | Checklist → version bump → publish gate → tag | Publish gate clean; tag matches CHANGELOG |
| 8 | **Dependency Auditor** | Scheduled or pre-release | Scan → risk scoring → license check → update plan | Known CVEs documented; approved upgrades applied |
| 9 | **On-call Responder** | Alert or incident signal | Triage → runbook → mitigation → post-mortem | Incident contained; lesson logged |
| 10 | **Learning Loop** | Post-ship anomaly or eval gap | Observe → hypothesize → GEPA variant → monitor | Adopted improvement has passing eval + transcript |

## Common rules

- Every workflow starts from a typed `PROJECT-INTENT.md`.
- Each step produces a verifiable artifact (file, test, log, ADR).
- Workers are dispatched with disjoint write sets (FM-13).
- No step claims "done" without an evidence block (FM-09).
- Regressions block promotion (FM-10).
- Silent failures are surfaced, not swallowed (FM-11).
- Long-running steps check for stale processes before launching (FM-02).

## Required `PROJECT-INTENT.md` / `adaptoid.config.yaml` fields

```yaml
super_adaptoid:
  loaded:
    - fable-5-workflows
  fable_5_workflows:
    enabled: true
    default_workflow: code-generation-with-tests
    registry: workflows/fable-5/
    require_evidence: true
    require_disjoint_writes: true
```

## Failure modes addressed

- **FM-02 — Stale Process:** long-running workflows call `check_processes.sh` before launching.
- **FM-09 — False Status:** every workflow step requires an evidence block before proceeding.
- **FM-10 — Flaky Tests:** regression tests must pass in random order before promotion.
- **FM-11 — Silent Failures:** workflow steps log every exception; bare `except: pass` is forbidden.

## Relationship to the Kernel

Implements `kernel/PRINCIPLES.md` (laws 4, 10, 12) and `kernel/TWO-TIER.md` (orchestrator dispatches workers).

## Validator

```bash
bash validators/check_processes.sh
bash validators/check_status_claims.sh
bash validators/check_tests.sh
bash validators/check_silent_failures.sh
bash validators/dogfood.sh
```
