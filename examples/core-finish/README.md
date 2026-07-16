# Example: Core usage (direct)

How to use Adaptoid **from this repo only** — no external demo apps.

## Command

```bash
# From Adaptoid-OS root — replace the brief with YOUR project
python3 adaptor/engine.py \
  --brief "YOUR project one-liner" \
  --output ../my-project \
  --core-only \
  --host all

python3 conductor/conductor.py init-wave --project ../my-project -n 3
bash ../my-project/orchestrator/scripts/preflight.sh ../my-project
```

## What you get (in `../my-project`)

| File | Purpose |
|---|---|
| `AGENTS.md` | Any host (Codex, OpenCode, Grok, …) |
| `CLAUDE.md` | Claude Code |
| `.cursor/rules/adaptoid.mdc` | Cursor |
| `kernel/` | Always-load laws |
| `HANDOFF.md` | Session continuity |
| `PROJECT-INTENT.md` | Done means + falsification |
| `orchestrator/scripts/preflight.sh` | Evidence gate |

## Next

Open `../my-project` in your coding agent and build **your** product there.  
Adaptoid only set the harness; it does not implement your app features.
