# Start here — Adaptoid OS

## Two surfaces (do not confuse)

| Name | What | Path |
|---|---|---|
| **Lite** | **Standalone one markdown file** (the original) | `reference/OS_SETUP_v1.3_full.md` |
| **Core** | **This entire folder / repo** | `Adaptoid-OS/` (engine, SHIP-SYSTEM, validators, …) |

There is **no** root `LITE.md`. Lite = the long standalone OS-Setup file only.

## How you use it

**Lite:** paste `reference/OS_SETUP_v1.3_full.md` + brief → “adapt & complete.”  

**Core:**
```bash
cd /path/to/Adaptoid-OS
python3 adaptor/engine.py \
  --brief "YOUR BRIEF" \
  --output ../my-project \
  --core-only --host all
```
(`--sdlc` default on.) Open `../my-project` → complete with SHIP-SYSTEM.

| File | Role |
|---|---|
| **`USE.md`** | recipes + magic prompt |
| **`core/SHIP-SYSTEM.md`** | SDLC × host toolkit |
| **`core/HOST-OPERATING-PLAYBOOK.md`** | Grok-style how to proceed |
| **`FLOW.md`** | live file spine |
