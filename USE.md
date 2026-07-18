# How to use Adaptoid

## Two things only

| | What | Where |
|---|---|---|
| **Lite** | **ONE standalone markdown file** | **`ADAPTOID-LITE.md`** (repo root) |
| **Core** | **This whole folder** | the `Adaptoid-OS` repo |

Same Lite file also on your Desktop: `~/Desktop/ADAPTOID-LITE.md`  
(and `~/Desktop/OS_SETUP.md` — same content, old name)

---

## Lite (the single file)

**What I did:**  
Merged your Desktop `OS_SETUP.md` (v2.0: structure + failure modes + archetypes + adaptor)  
**with** Adaptoid SHIP SYSTEM + host playbook  
into **one final ultimate standalone file.**

**That file is:**

```
/Users/srujansai/Desktop/Adaptoid-OS/ADAPTOID-LITE.md
```

### How to use it
1. Open Grok Build (or Claude / Cursor)  
2. **Paste the whole `ADAPTOID-LITE.md`**  
3. Paste your project brief  
4. Say: **Use Adaptoid Lite Ultimate. Adapt the environment. Complete the project.**

---

## Core (the folder)

```bash
cd /Users/srujansai/Desktop/Adaptoid-OS
python3 adaptor/engine.py --brief "YOUR BRIEF" --output ../my-project --core-only --host all
```

Open `../my-project` and complete wave-1.

---

## Magic prompt

```
You are using Adaptoid.

MODE: Lite   (or Core)
FILE/FOLDER: <pasted ADAPTOID-LITE.md  OR  path to Adaptoid-OS / generated project>

BRIEF:
"""
...
"""

Adapt the environment for this brief. Intent-lock if needed.
Follow SHIP SYSTEM (SDLC + host tools). Complete wave-1 with evidence.
```
