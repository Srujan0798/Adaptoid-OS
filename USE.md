# How to use Adaptoid — Lite · Core

**Your product has two surfaces only:**

| Mode | What it is | What you hand the model |
|---|---|---|
| **Lite** | **Standalone one file** | `reference/OS_SETUP_v1.3_full.md` |
| **Core** | **This entire Adaptoid-OS folder/repo** | clone/path to Adaptoid-OS |

There is **no** separate short `LITE.md`. That was a mistake. **Lite = the original long standalone OS-Setup file.**

---

## Promise

1. Your **brief** (internship / job / hackathon / product / anything)  
2. **Lite file** *or* **Core folder**  
3. Say: **“Use Adaptoid. Adapt the environment. Complete the project.”**  
4. Model adapts setup + runs SHIP SYSTEM (SDLC × host tools) + finishes with evidence  

---

## Lite — standalone md only

**File:** `reference/OS_SETUP_v1.3_full.md`  
**Path on your machine:**  
`/Users/srujansai/Desktop/Adaptoid-OS/reference/OS_SETUP_v1.3_full.md`  
**GitHub:**  
https://github.com/Srujan0798/Adaptoid-OS/blob/main/reference/OS_SETUP_v1.3_full.md  

### Steps
1. Open Grok Build / Claude / Cursor / Codex  
2. Paste **entire** `OS_SETUP_v1.3_full.md`  
3. Paste brief  
4. Paste magic prompt below (`MODE: Lite`)

---

## Core — entire this folder

**Folder:** the whole Adaptoid-OS repo (everything on `FLOW.md` spine).

```bash
cd /Users/srujansai/Desktop/Adaptoid-OS   # or your clone

python3 adaptor/engine.py \
  --brief "YOUR BRIEF" \
  --output ../my-project \
  --core-only --host all
# --sdlc is ON by default (7 stage tasks). Use --no-sdlc to skip.
```

Open `../my-project` and say complete wave-1 (reads `SHIP-SYSTEM.md` + AGENTS.md).

For **full validators** (still Core folder):

```bash
python3 adaptor/engine.py --brief "…" --output ../my-project --host all
# omit --core-only
```

---

## Magic prompt

```
You are the Orchestrator using Adaptoid.

MODE: <Lite | Core>
ADAPTOID: <pasted OS_SETUP_v1.3_full.md  OR  path to Adaptoid-OS folder / generated project>

MY BRIEF:
"""
<internship / job / hackathon / product brief>
"""

Do this:
1. Adapt the environment (intent, AGENTS, HANDOFF, tasks, policies) to THIS brief.
2. Follow HOST-OPERATING-PLAYBOOK + SHIP-SYSTEM (Core projects have both):
   - Intent lock if ambiguous (≤4 A/B/C, record answers) before BUILD
   - Plan → approve → implement for big work; skip plan for tiny fixes
   - One clear outcome per turn
   - SDLC: plan→requirements→design→build→test→deploy→maintain
   - Host tools by stage; subagents only for large explore/tests
   - Verify before done (tests/preflight + exit code); rewrite HANDOFF
3. Do not invent scope outside the brief.
4. Evidence or it didn’t happen.

Start: orient on SHIP-SYSTEM + HOST-OPERATING-PLAYBOOK + INTENT, then intent-lock or stage 1.
```

---

## Done means

| | Evidence |
|---|---|
| Environment adapted | intent + AGENTS/structure present |
| Built | code in writes |
| Tested | acceptance exit 0 |
| Ship gate | preflight green (Core) or Lite checklist |
| Continuity | HANDOFF rewritten |
