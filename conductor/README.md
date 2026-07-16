# Conductor — thin Brain/Hands runtime

Coordinates wave tasks without replacing Claude Code / Cursor / Codex / Grok.

## Commands

```bash
python3 conductor/conductor.py status --project ./my-project
python3 conductor/conductor.py wake --project ./my-project
python3 conductor/conductor.py init-wave --project ./my-project --wave wave-1 -n 3
python3 conductor/conductor.py check-disjoint --project ./my-project --wave wave-1
python3 conductor/conductor.py dispatch --project ./my-project --wave wave-1 --mode stub
python3 conductor/conductor.py dispatch --project ./my-project --wave wave-1 --mode shell
python3 conductor/conductor.py rewrite-handoff --project ./my-project --wave wave-1
```

| Mode | Behavior |
|---|---|
| `stub` | Acknowledges tasks, writes reports with evidence placeholders (CI / dry-run) |
| `shell` | Runs each task's `acceptance:` command and records stdout/stderr |

## Flow

```
engine --core-only --host all
  → conductor init-wave
  → (humans/agents implement in host)
  → conductor dispatch --mode shell   # or workers write reports
  → preflight
  → rewrite HANDOFF
```

## Non-goals

- Not a multi-channel Slack bot
- Not a full LangGraph runtime
- Not a model provider
