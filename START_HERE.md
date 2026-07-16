# Start here — Adaptoid OS

**What this is:** a harness so AI coding agents finish *your* project.  
**What this is not:** a whiteboard app, a chat product, or a model.

## 60-second path

```bash
# 1. From this repo
python3 adaptor/engine.py \
  --brief "PASTE YOUR REAL PROJECT IDEA" \
  --output ../my-project \
  --core-only \
  --host all

# 2. Open that folder in Claude Code / Cursor / Codex / Grok

# 3. Before claiming done
bash ../my-project/orchestrator/scripts/preflight.sh ../my-project
```

## Product ladder

| | Use |
|---|---|
| **Lite** | Paste `reference/OS_SETUP_v1.3_full.md` into any chat |
| **Core** | Command above (`--core-only`) — default |
| **Pro** | This full repo (validators library, workflows, protocols) |

## Read next (only if needed)

1. `PRODUCT.md` — what shipped  
2. `core/README.md` — Core kit  
3. `AGENTS.md` — rules for agents working in this repo  
4. `make ship-check` — prove the kit itself is healthy  

No external demo folders. Everything lives in this repository.
