# PRODUCT — closed for use (v5.3.0)

## What this is

**Adaptoid OS** = harness so AI coding agents finish real projects — and **adapts** as the agentic era evolves.

| Surface | What | How |
|---|---|---|
| **Lite** | One file: **`ADAPTOID-LITE.md`** | Paste + brief → complete |
| **Core** | **This whole folder** | `adaptor/engine.py` → generated project → complete |

## Status: READY TO USE (+ era adapt)

| Item | Status |
|---|---|
| Lite hybrid standalone | Done |
| Core engine + multi-host + SDLC | Done |
| SHIP-SYSTEM + playbook + host matrix | Done |
| Agent Skills emit (`.agents/skills`) | Done |
| agent-product archetype · FM-19/20 | Done |
| Lean live tree + attic | Done |
| Dogfood / ship-check | Must pass before release |

Era notes: **`ADAPTATION.md`**

## How to start today

**Lite**
1. Open `ADAPTOID-LITE.md` (or `~/Desktop/ADAPTOID-LITE.md`)
2. Paste into Grok/Claude + your brief  
3. Say: *Use Adaptoid Lite. Adapt the environment. Complete the project.*

**Core**
```bash
cd /path/to/Adaptoid-OS
python3 adaptor/engine.py --brief "YOUR BRIEF" --output ../my-project --core-only --host all
# open ../my-project and complete wave-1
```

## Not product

- `OS_SETUP_v1.3` name (legacy stub only)
- Anything under `docs/historical/`

## Kit check

```bash
make ship-check
```
