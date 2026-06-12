# Consciousness Core Protocol

> Self-monitoring, runtime introspection, and honest status reporting for the Super-Adaptoid layer.

## Purpose

Give the agent a lightweight, always-on (when loaded) capability to observe its own state, attach confidence to every deliverable, detect drift/cost/latency anomalies, and report status honestly rather than confabulating confidence. This protocol extends `kernel/ANTI-HALLUCINATION.md` by making self-correction an explicit, reviewable step.

## Mechanisms

1. **Confidence checkpoints** — every deliverable gets a confidence score (`certain` / `likely` / `uncertain` / `blocked`) and a one-line uncertainty statement.
2. **Hard thresholds** — stop and escalate when confidence drops below `confidence_threshold` or when a destructive/remote action would occur below `irreversible_threshold`.
3. **Cost/latency guards** — track per-action and cumulative spend; abort or checkpoint if `cost_usd_limit` or `latency_ms_limit` is breached.
4. **State drift detection** — compare current claims against `HANDOFF.md`, `plan/EXECUTION.md`, and the vault hash chain; surface contradictions before they compound.
5. **Anomaly log** — append every detected anomaly to a durable log with severity, evidence, and resolution status.

## Required `PROJECT-INTENT.md` / `adaptoid.config.yaml` fields

```yaml
super_adaptoid:
  loaded:
    - consciousness-core
  consciousness_core:
    enabled: true
    confidence_threshold: 0.85          # below → escalate before claiming done
    irreversible_threshold: 0.95        # required for destructive / remote / human-facing actions
    cost_usd_limit: 10.0
    latency_ms_limit: 30000
    anomaly_log: orchestrator/memory/anomalies.jsonl
    checkpoint_file: orchestrator/memory/CHECKPOINT.md
```

## Checkpoints

Run at the following moments and answer the checkpoint question out loud:

| # | Checkpoint | Question to answer |
|---|---|---|
| 1 | Session start | What is the active wave/task? What do I assume? What evidence could invalidate this? |
| 2 | Before every tool call | Does this action match the brief? What is the blast radius? Am I above the irreversible threshold? |
| 3 | Before every "done" claim | What evidence do I have? Is confidence ≥ threshold? Are there unchecked acceptance items? |
| 4 | At every phase boundary | Does current state match `HANDOFF.md` / `EXECUTION.md`? Any contradictions or drift? |
| 5 | Session end or compaction | What was verified this session? What anomalies remain open? Is `HANDOFF.md` rewritten (not appended)? |

## Failure modes addressed

- **FM-01 — State Drift:** checkpoints compare state files; status files are replaced, never appended.
- **FM-09 — False Status:** every claim requires an evidence block; "uncertain" and "blocked" are valid statuses.
- **FM-10 — Flaky Tests:** confidence checkpoints require test evidence and forbid "re-run until green."
- **FM-17 — Tampered State:** drift detection recomputes vault hashes on load and on every major write.

## Relationship to the Kernel

Depends on `kernel/PRINCIPLES.md` (laws 5, 7, 8), `kernel/TWO-TIER.md` (orchestrator owns state), and `kernel/ANTI-HALLUCINATION.md`.

## Validator

```bash
# Validate Consciousness Core wiring and run the relevant FM validators
[ -f PROJECT-INTENT.md ] && grep -q "consciousness_core:" PROJECT-INTENT.md || echo "Note: consciousness_core not configured in PROJECT-INTENT.md"
[ -f plan/EXECUTION.md ] && bash validators/validate_state.sh
bash validators/check_status_claims.sh
bash validators/check_tests.sh
[ -d orchestrator/memory ] && bash validators/vault_mmu.sh
bash validators/dogfood.sh
```
