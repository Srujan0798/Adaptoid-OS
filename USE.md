# USE — start using Adaptoid

## Lite (one file)

**`ADAPTOID-LITE.md`** (also `~/Desktop/ADAPTOID-LITE.md`)

1. Paste whole file into Grok Build / Claude / Cursor  
2. Paste brief  
3. Say: **Use Adaptoid Lite. Adapt the environment. Complete the project.**

---

## Core (this folder)

```bash
cd /path/to/Adaptoid-OS
python3 adaptor/engine.py \
  --brief "YOUR BRIEF" \
  --output ../my-project \
  --core-only --host all
```

Open `../my-project` → follow `SHIP-SYSTEM.md` + `HOST-OPERATING-PLAYBOOK.md` → finish wave-1 with evidence.

---

## Magic prompt

```
MODE: Lite or Core
ADAPTOID: <pasted ADAPTOID-LITE.md | path to Adaptoid-OS | generated project>
BRIEF: """ ... """

Adapt environment. Intent-lock if needed.
SHIP SYSTEM: plan→requirements→design→build→test→deploy→maintain.
Use host tools. Evidence or it didn't happen. Rewrite HANDOFF.
```

**Ignore:** `OS_SETUP_v1.3` (old name / stub only).
