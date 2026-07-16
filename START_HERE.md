# Start here — Adaptoid OS

## What you want (and what we built)

You give:

1. **A brief** — internship / job / hackathon / product / anything  
2. **A mode** — **Lite** (one md) · **Core** (engine) · **Pro** (full repo)  
3. A line to the model: **“Use this. Adapt the environment. Complete it.”**

The model:

- adapts the environment to that project  
- runs **SDLC** (plan → design → build → test → ship)  
- uses the **host** tools (Grok Build / Claude / Cursor / …)  
- finishes with **evidence**

Full recipes + magic prompt: **[`USE.md`](USE.md)**

---

## Three modes

### Lite — paste only
Hand them **`LITE.md`** + brief + magic prompt in `USE.md`.

### Core — recommended
```bash
python3 adaptor/engine.py \
  --brief "YOUR BRIEF" \
  --output ../my-project \
  --core-only --host all --sdlc
```
Open `../my-project` → say complete wave-1 with evidence.

### Pro — full kit
Same as Core **without** `--core-only` (more validators), from this repo clone.

---

## Map

| Doc | Why |
|---|---|
| `USE.md` | how to hand Lite/Core/Pro to a model |
| `LITE.md` | paste-only Lite kit |
| `FLOW.md` | every live file on the spine |
| `PRODUCT.md` | what’s complete / not |
| `protocols/sdlc-loop.md` | SDLC gates |

Archived only: `docs/historical/`

Kit health: `make ship-check`
