# INDEX — Core progressive disclosure

> Load kernel always. Load the rest only when the trigger fires. Do not load the entire Pro kit.

## Always load (~2K tokens)

| File | Why |
|---|---|
| `kernel/PRINCIPLES.md` | 12 laws |
| `kernel/TWO-TIER.md` | Orchestrator vs workers |
| `kernel/ANTI-HALLUCINATION.md` | Evidence + state rules |
| `HANDOFF.md` | Current wave truth |
| `PROJECT-INTENT.md` | Done means + falsification |
| `adaptoid.config.yaml` | Project SSOT |

## Cold-start (host-specific)

| Host | File |
|---|---|
| Generic / Codex / Grok / OpenCode | `AGENTS.md` |
| Claude Code | `CLAUDE.md` |
| Cursor | `AGENTS.md` + `.cursor/rules/adaptoid.mdc` |

## Load on trigger

| Trigger | Path |
|---|---|
| Before claiming done | `orchestrator/scripts/preflight.sh` |
| Status claims in reports | `orchestrator/scripts/check_status_claims.sh` |
| New session feels lost | `orchestrator/scripts/check_handoff.sh` |
| Tool call policy | `policies/default.yaml` |
| Scope creep urge | PROJECT-INTENT Scope OUT |
| Full FM library / Pro protocols | parent Adaptoid-OS Pro kit |

## Core loop

```
orient (kernel + HANDOFF + intent)
  → plan wave
  → dispatch self-contained tasks
  → workers execute + report evidence
  → preflight
  → rewrite HANDOFF
  → next wave
```
