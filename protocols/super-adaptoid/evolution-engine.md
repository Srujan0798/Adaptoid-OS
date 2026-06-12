# Evolution Engine Protocol

> Safe, bounded self-improvement of prompts, skills, validators, and workflows.

## Purpose

Make the harness self-improving by proposing, testing, and selectively adopting better artifacts — while preventing runaway mutation, hype, and unverified rollouts.

## Subsystems

### GEPA — Generate, Evaluate, Promote, Archive

1. **Generate** — produce ≤ `max_variants` candidate changes from a falsifiable hypothesis.
2. **Evaluate** — run the existing eval suite plus a new regression test for each variant.
3. **Promote** — adopt the winner in one workflow or archetype first (canary).
4. **Archive** — move rejected or superseded variants to `docs/historical/` or `attic/`, never delete.

### Hermes Loop — closed anomaly → fix cycle

1. **Observe** anomaly or performance regression from metrics, transcripts, or anomaly log.
2. **Hypothesize** a root cause and a falsifiable fix.
3. **Patch** a minimal, scoped candidate.
4. **Evaluate** against evals and at least one real task transcript.
5. **Ship** or **Archive**, then monitor.

## Cycle diagram

```text
        ┌─────────────┐
        │   Observe   │◄────── anomalies / metrics / transcripts
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │  Hypothesize│
        └──────┬──────┘
               ▼
   ┌─────────────────────────┐
   │   GEPA: Generate        │
   │         Evaluate        │
   │         Promote (canary)│
   │         Archive (reject)│
   └──────┬──────────────────┘
          ▼
   ┌─────────────┐
   │ Ship/Archive │
   └──────┬──────┘
          ▼
   ┌─────────────┐
   │   Monitor   │────────► back to Observe
   └─────────────┘
```

## GEPA rules

- Every variant has a falsifiable hypothesis and a rollback plan.
- Eval before merge; regressions are blockers.
- Canary rollout in one archetype or workflow before global promotion.
- Superseded variants are archived, never deleted.

## Hermes rules

- Every loop starts with an observed anomaly or metric, not a guess.
- Patches are minimal and scoped to the hypothesis.
- Evaluation includes at least one real task transcript.
- A loop that fails `escalation_after_failures` times escalates to human review.

## Required `PROJECT-INTENT.md` / `adaptoid.config.yaml` fields

```yaml
super_adaptoid:
  loaded:
    - evolution-engine
  evolution_engine:
    enabled: true
    gepa:
      max_variants: 3
      eval_threshold: 0.90
      canary_archetype: cli-tool
    hermes:
      max_cycles: 5
      escalation_after_failures: 3
      monitor_interval_hours: 168
    archive_dir: docs/historical/evolution/
```

## Failure modes addressed

- **FM-02 — Stale Process:** `check_processes.sh` prevents duplicate evolution runs.
- **FM-05 — Metric Inconsistency:** all eval results live in `results/metrics.json`; docs reference the canonical source.
- **FM-14 — Lost Handoff:** every evolution cycle updates `HANDOFF.md` and `events.jsonl`.
- **FM-16 — Wrong Route:** transitions to the `evolve` node are validated by `route_sentinel.sh`.

## Relationship to the Kernel

Extends `kernel/PRINCIPLES.md` (laws 2, 4, 12) and `kernel/ANTI-HALLUCINATION.md` (evidence-required).

## Validator

```bash
bash validators/check_processes.sh
[ -f results/metrics.json ] && bash validators/check_metrics.sh
[ -f HANDOFF.md ] && bash validators/check_handoff.sh
[ -f adaptoid.config.yaml ] && bash validators/route_sentinel.sh
bash validators/dogfood.sh
```
