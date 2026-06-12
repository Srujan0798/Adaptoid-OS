# Proactive Assistant Protocol

> Proactive assistant mode: anticipate, surface, escalate, never act unilaterally.

## Purpose

Give Adaptoid OS a proactive-but-restrained assistant mode that surfaces the right information at the right time, asks permission before acting, and escalates when confidence is low. Proactive Assistant is not autonomous execution.

## Behaviors

1. **Intention prediction** — infer the next likely task from `HANDOFF.md`, recent events, and current context; state the inference as a question, not a command.
2. **Pre-fetch** — load relevant memory, protocols, or failure-mode warnings before they are explicitly requested, but only if within context budget.
3. **Background sentry** — watch for stale processes, config drift, or silent failures at `sentry_interval_s`; log findings, do not auto-fix.
4. **Polite interruption** — when a high-confidence risk is detected (e.g., duplicate process, out-of-scope action), interrupt with evidence and a recommended next step.

## Safety rules

- **Ask, don't act.** Proactive Assistant never executes tools without explicit approval (blast-radius rule applies).
- **Log everything.** Every proactive suggestion is appended to `events.jsonl`.
- **Disable switch.** Set `enabled: false` in config to turn off all proactive behaviors.
- **No remote/money/human actions** without human approval.
- **Disjoint from workers.** A proactive suggestion does not create a worker task unless the orchestrator explicitly dispatches one (FM-13).

## Required `PROJECT-INTENT.md` / `adaptoid.config.yaml` fields

```yaml
super_adaptoid:
  loaded:
    - proactive-assistant
  proactive_assistant:
    enabled: false
    prefetch_protocols:
      - memory-identity
      - consciousness-core
    sentry_interval_s: 300
    log: orchestrator/memory/proactive-events.jsonl
    approval_required_for:
      - Bash
      - Write
      - Edit
```

## Failure modes addressed

- **FM-02 — Stale Process:** sentry runs `check_processes.sh` and warns before duplicate runs start.
- **FM-08 — Scope Creep:** proactive suggestions are bounded by the current brief; no "while I'm here" actions.
- **FM-09 — False Status:** every surfaced claim includes an evidence block.
- **FM-13 — Parallel Collisions:** proactive hints do not spawn parallel workers on the same file.

## Relationship to the Kernel

Depends on `kernel/PRINCIPLES.md` (law 11 — blast radius), `kernel/TWO-TIER.md` (orchestrator owns dispatch), and `kernel/ANTI-HALLUCINATION.md`.

## Validator

```bash
bash validators/check_processes.sh
bash validators/check_scope.sh
bash validators/check_status_claims.sh
for wave in work/wave-*; do
  [ -d "$wave" ] && bash validators/check_dispatch_disjoint.sh "$wave"
done
bash validators/dogfood.sh
```
