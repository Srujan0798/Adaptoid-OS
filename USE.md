# How to use Adaptoid — Lite · Core

## Two surfaces only

| Mode | What | File / folder |
|---|---|---|
| **Lite** | **Ultimate standalone single markdown** | `reference/OS_SETUP_v1.3_full.md` **or** `reference/ADAPTOID-LITE.md` (same content) |
| **Core** | **Entire Adaptoid-OS folder/repo** | this repository |

Desktop copies (synced):  
`~/Desktop/OS_SETUP.md` · `~/Desktop/ADAPTOID-LITE.md`

---

## Lite — paste only (ultimate standalone)

1. Open Grok Build / Claude / Cursor / Codex  
2. Paste **entire** Lite file (either name above)  
3. Paste your brief  
4. Say:

```
Use Adaptoid Lite Ultimate v3.0-standalone.
Intent-lock if needed. Run Adaptor Engine. Follow SHIP SYSTEM.
Adapt the environment and complete wave-1 with evidence.
```

---

## Core — entire this folder

```bash
cd /Users/srujansai/Desktop/Adaptoid-OS   # or your clone

python3 adaptor/engine.py \
  --brief "YOUR BRIEF" \
  --output ../my-project \
  --core-only --host all
# --sdlc default ON
```

Open `../my-project` → SHIP-SYSTEM + HOST-OPERATING-PLAYBOOK + tasks.

---

## Magic prompt (any mode)

```
You are the Orchestrator using Adaptoid.

MODE: <Lite | Core>
ADAPTOID: <pasted Lite file  OR  path to Adaptoid-OS / generated project>

MY BRIEF:
"""
<your brief>
"""

Do this:
1. Adapt environment to this brief (intent, AGENTS, HANDOFF, structure).
2. Intent lock if ambiguous (≤4 A/B/C) before BUILD.
3. Plan → approve → implement for big work; one outcome per turn.
4. SDLC: plan→requirements→design→build→test→deploy→maintain.
5. Use host toolkit (plan mode, terminal, git, …). Verify before done.
6. Rewrite HANDOFF. No invented scope.

Start now.
```

Full ship matrix: Core `core/SHIP-SYSTEM.md` · Lite embeds §0S in the single file.
