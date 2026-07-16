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

python3 conductor/conductor.py init-wave --project ../my-project --sdlc
```

Then open `../my-project` in **Grok Build / Claude / Cursor / Codex** and run the SDLC loop  
(plan → build → test → ship). Host tools do execution; Adaptoid enforces gates + evidence.

See `START_HERE.md` · `protocols/sdlc-loop.md` · `core/HOST-CAPABILITIES.md`.

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
