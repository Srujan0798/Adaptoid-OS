# Example: Core Finish Path (dogfood proof)

> **Product claim:** any model + any host + Adaptoid Core → project scaffold that agents can complete without the usual failure modes.

## Brief

```
48h hackathon: realtime collab whiteboard with presence cursors
```

## Commands (evidence)

```bash
# From Adaptoid-OS root
python3 adaptor/engine.py \
  --brief "48h hackathon: realtime collab whiteboard with presence cursors" \
  --output ./examples/core-finish/generated \
  --core-only \
  --host all \
  --skip-verify

python3 conductor/conductor.py init-wave \
  --project ./examples/core-finish/generated \
  --wave wave-1 -n 3

python3 conductor/conductor.py dispatch \
  --project ./examples/core-finish/generated \
  --wave wave-1 --mode stub

bash ./examples/core-finish/generated/orchestrator/scripts/preflight.sh \
  ./examples/core-finish/generated
```

## Expected surfaces

| File | Host |
|---|---|
| `AGENTS.md` | Codex / OpenCode / Grok / generic |
| `CLAUDE.md` | Claude Code |
| `.cursor/rules/adaptoid.mdc` | Cursor |
| `kernel/*` | always |
| `HANDOFF.md` | session continuity |
| `work/reports/wave-1/*.report.md` | evidence after dispatch |

## Before / after (harness)

| Without Core | With Core |
|---|---|
| Cold chat, no HANDOFF | `conductor wake` orients from files |
| "Done" with no evidence | Reports require evidence block |
| Host lock-in (CLAUDE.md only) | Same intent → many hosts |
| Scope freebies | PROJECT-INTENT IN/OUT box |

## Failure modes this path exercises

- FM-08 scope creep — INTENT OUT
- FM-09 false done — report evidence
- FM-13 parallel collision — `check-disjoint`
- FM-14 lost handoff — HANDOFF rewrite on dispatch

## Note

`generated/` is produced by the engine; re-run commands above to refresh. Do not hand-edit as source of truth — the engine is.
