# How to use Adaptoid — Lite · Core · Pro

**Your expectation (correct):**

1. You have a **project** (internship / job take-home / hackathon / product / anything).  
2. You give the model **the brief** + **one of: Lite file | Core setup | Pro repo**.  
3. You say: **“Use this. Adapt the environment. Complete the project.”**  
4. The model **sets up the harness**, then **plans → builds → tests → ships** with evidence.

That is the whole product.

---

## Pick a mode

| Mode | You hand them | When |
|---|---|---|
| **Lite** | `LITE.md` (this repo) **or** `reference/OS_SETUP_v1.3_full.md` | Fastest — paste into any chat, no clone |
| **Core** | This repo + run engine **or** a generated project folder | Default — multi-host files + validators |
| **Pro** | Full Adaptoid-OS clone (this repo) | Full failure-mode library + all validators + attic if needed |

---

## Magic prompt (say this every time)

Copy-paste to Claude / Grok Build / Cursor / Codex / Kimi:

```
You are the Orchestrator using Adaptoid.

MODE: <Lite | Core | Pro>
ADAPTOID: <path to LITE.md, or path to Adaptoid-OS repo, or already-generated project>

MY BRIEF:
"""
<paste internship / job / hackathon / product brief here>
"""

Do this:
1. Adapt the environment (intent, AGENTS/host files, SDLC tasks, policies).
2. Follow Adaptoid SHIP SYSTEM: full SDLC (plan→requirements→design→build→test→deploy→maintain)
   fused with this host’s full toolkit:
   Plan mode, Subagents, Skills, Hooks, MCP, AGENTS.md, Memory/HANDOFF, Code search,
   Multi-file edits, Git, Deep reasoning, Web search, Terminal, Headless/CI, Code review,
   Sandbox, Background tasks. (See SHIP-SYSTEM.md or LITE.md embedded rules.)
3. Do NOT invent scope outside the brief. Do NOT skip stages or tools when the stage requires them.
4. Evidence or it didn’t happen — paste command + exit code for every “done”.
5. Before claiming complete: preflight (Core/Pro) or Lite ship checklist.

Start now. Orient on SHIP-SYSTEM / AGENTS / HANDOFF / INTENT, then execute wave-1.
```

---

## Lite (paste only)

1. Open any agent.  
2. Paste entire contents of **`LITE.md`**.  
3. Paste the magic prompt with `MODE: Lite`.  
4. Paste the brief.  
5. Let it create the project folder and complete wave-1+.

Optional deep Lite: `reference/OS_SETUP_v1.3_full.md` (long form).

---

## Core (recommended)

```bash
# From Adaptoid-OS clone
python3 adaptor/engine.py \
  --brief "YOUR BRIEF HERE" \
  --output ../my-project \
  --core-only --host all --sdlc

# Open ../my-project in Grok / Claude / Cursor and say:
# "Read AGENTS.md + HANDOFF.md + PROJECT-INTENT.md. Complete wave-1. Evidence required."
```

`--sdlc` creates PLAN/DESIGN/BUILD/TEST/SHIP tasks automatically.

Or hand them the **generated folder** `../my-project` + magic prompt with `MODE: Core`.

---

## Pro (full kit)

```bash
git clone https://github.com/Srujan0798/Adaptoid-OS.git
cd Adaptoid-OS
python3 adaptor/engine.py \
  --brief "YOUR BRIEF HERE" \
  --output ../my-project \
  --host all --sdlc
# omit --core-only → more validators copied from full kit
```

Same magic prompt with `MODE: Pro` and path to this repo if the agent should consult failure-modes / archetypes itself.

---

## Done means (all modes)

| Gate | Evidence |
|---|---|
| Intent clear | `PROJECT-INTENT.md` success + falsification |
| Environment adapted | AGENTS + SHIP-SYSTEM (or LITE rules) + HANDOFF |
| SDLC stages run | plan→…→maintain with host tools used |
| Built | code under task `writes` |
| Tested | acceptance / tests exit 0 |
| Deploy gate | `preflight.sh` green (Core/Pro) |
| Continuity | `HANDOFF.md` rewritten |

**Adaptoid itself is the ship system** (SDLC × host toolkit), not a folder of optional tips.

---

## Not required

- Whiteboard demos  
- Reading `docs/historical/`  
- Rebuilding Grok/Claude features (plan mode, MCP, git) — **use the host**
