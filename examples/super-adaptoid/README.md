# Example: Super-Adaptoid Personal Research Assistant

## Brief
Stand up a long-running research+build assistant for a solo developer that survives sessions, reports honestly, and improves itself weekly — the full v5.0 protocol layer in action on a deliberately small project.

## Archetype
`internal-tool`

## Tier
T2

## What this example demonstrates

| Layer | Protocol | What it does here |
|---|---|---|
| Self-monitoring | `protocols/super-adaptoid/consciousness-core.md` | Every deliverable carries confidence + evidence; <0.85 → escalate, not guess |
| Durable memory | `protocols/super-adaptoid/memory-identity.md` | Identity card + 4-tier memory; HANDOFF.md rewritten each session |
| Self-improvement | `protocols/super-adaptoid/evolution-engine.md` | Weekly Hermes loop; GEPA variants canaried before adoption |
| Workflows | `protocols/super-adaptoid/fable-5-workflows.md` | Research Synthesis default; Learning Loop weekly |
| Proactive mode | `protocols/super-adaptoid/proactive-assistant.md` | **Deliberately disabled** until two clean waves — trust is earned |

See `PROJECT-INTENT.md` in this directory for the complete typed intent with the `super_adaptoid:` configuration block.

## Wave plan

1. **Foundation** — memory-bank init (identity card, facts, lessons), HANDOFF + events.jsonl wired, consciousness checkpoints active
2. **Research loop** — Research Synthesis workflow on the first real question; every claim source-backed
3. **Learning loop** — first Hermes cycle: review anomaly log, propose one improvement, eval, adopt or archive
4. **Trust gate** — if waves 1–3 ran with zero FM-08/FM-09 hits, enable `proactive_assistant` (still ask-don't-act)

## A session in this project looks like

```
session start
  └─ wake.sh                      # rebuild state from kernel + HANDOFF + events
  └─ consciousness checkpoint 1   # state the active wave, assumptions, invalidators
work
  └─ each deliverable             # confidence tag + evidence block
  └─ emit_event.sh                # hash-chained event per major action
  └─ anomaly? → anomalies.jsonl   # logged, severity-tagged, never silently fixed
session end
  └─ rewrite HANDOFF.md           # replace, never append (FM-01)
  └─ consciousness checkpoint 5   # what was verified; what's still open
  └─ audit_chain.sh               # event log integrity before walking away
```

## Validate this example

```bash
bash validators/check_intent.sh examples/super-adaptoid       # typed intent parses
bash validators/check_consciousness.sh                        # protocol invariants
bash validators/check_memory_identity.sh
bash validators/check_evolution.sh
bash validators/dogfood.sh                                    # whole-kit integrity
```

## Expected outcome

- Session N+1 starts with full context from durable files alone — no re-explaining
- Honest status by construction: claims without evidence don't survive checkpoint 3
- One adopted-or-archived improvement per week, each with a passing eval
- Falsification criteria in PROJECT-INTENT.md make "it's working" a testable claim, not a feeling
