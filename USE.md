# How to use Adaptoid

## Only two things

| | What | Where |
|---|---|---|
| **Lite** | **One standalone file** | **`ADAPTOID-LITE.md`** (repo root) |
| **Core** | **Whole folder** | this `Adaptoid-OS` repo |

**`OS_SETUP_v1.3` is dead.** Old name. Do not use it. It only points here now.

Desktop Lite: `~/Desktop/ADAPTOID-LITE.md`

---

## Lite

1. Open **`ADAPTOID-LITE.md`**
2. Paste all of it into Grok/Claude
3. Paste your brief
4. Say: *Use Adaptoid Lite. Adapt the environment. Complete the project.*

---

## Core

```bash
cd /Users/srujansai/Desktop/Adaptoid-OS
python3 adaptor/engine.py --brief "YOUR BRIEF" --output ../my-project --core-only --host all
```

Open `../my-project` and complete.
