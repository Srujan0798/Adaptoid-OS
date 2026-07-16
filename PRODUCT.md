# Adaptoid OS — Product (v5.1)

## One sentence

Portable **agent harness**: any coding host + any model → projects that finish.

## Direct use (only path that matters)

```bash
python3 adaptor/engine.py \
  --brief "YOUR real idea" \
  --output ../my-project \
  --core-only \
  --host all
```

Then open `../my-project` in Claude / Cursor / Codex / Grok and build.

See `START_HERE.md`.

## What shipped

| Surface | Path |
|---|---|
| Lite | `reference/OS_SETUP_v1.3_full.md` |
| Core | `core/` + engine `--core-only` |
| Pro | this full repository |
| Hosts | agents, claude, cursor, codex, grok |
| Conductor | `conductor/conductor.py` |
| Gate | `make ship-check` |

## Not this product

- Not a whiteboard or sample app  
- Not a chat UI  
- Not multi-channel Slack  
- Not enterprise packs until needed  
- Not research encyclopedias in the hot path (archived under `docs/historical/attic-v5.1-lean/`)

## Kit health

```bash
make ship-check
```
