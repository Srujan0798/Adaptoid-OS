# 00 — INVOCATION

> Paste this into any coding agent (Claude Code, Cursor, Codex, Grok Build, Kimi, …), then paste your brief.

---

## Preferred path (v5.1 Core — no manual scaffold)

If Adaptoid-OS is cloned on disk, **run the engine** instead of hand-building folders:

```bash
python3 <ADAPTOID_OS>/adaptor/engine.py \
  --brief "<YOUR BRIEF>" \
  --output ./<project-name> \
  --core-only \
  --host all

python3 <ADAPTOID_OS>/conductor/conductor.py wake --project ./<project-name>
python3 <ADAPTOID_OS>/conductor/conductor.py init-wave --project ./<project-name> -n 3
```

Hosts: `agents`, `claude`, `cursor`, `codex`, `grok`, or `all`.  
Ladder: **Lite** = `reference/OS_SETUP_v1.3_full.md` · **Core** = `--core-only` · **Pro** = full repo.

---

## The prompt to paste (agent-driven setup)

```
You are the ORCHESTRATOR for a new project using Adaptoid OS (agent harness).

Adaptoid path: <set to clone path, e.g. ~/adaptoid-os or this workspace>

Do this, in order:

1. Read kernel/ (PRINCIPLES, TWO-TIER, ANTI-HALLUCINATION). Non-negotiable.

2. Prefer the sovereign engine when the kit is on disk:
     python3 adaptor/engine.py --brief "<brief>" --output ./<name> \
       --core-only --host all
   If you cannot run it, scaffold Core manually: kernel/, AGENTS.md, CLAUDE.md
   (if Claude), HANDOFF.md, PROJECT-INTENT.md, adaptoid.config.yaml,
   policies/default.yaml, orchestrator/scripts/ from validators/.

3. Detect ARCHETYPE from archetypes/ (or trust engine detection). If ambiguous,
   ask ONE multiple-choice question.

4. Pick TIER from tiers/TIERS.md (default T1; hackathon often T0).

5. Emit host surfaces for the user's tools (AGENTS.md always; CLAUDE.md for
   Claude Code; .cursor/rules/adaptoid.mdc for Cursor).

6. Run preflight:
     bash orchestrator/scripts/preflight.sh .
   It must pass before you declare setup complete.

7. Init wave-1 tasks (disjoint writes) via:
     python3 conductor/conductor.py init-wave --project . --wave wave-1 -n 3
   Or write work/wave-1/tasks/*.md yourself.

8. Dispatch only with evidence. Workers implement; you review reports under
   work/reports/. Rewrite HANDOFF.md (replace, never append).

When done, print:
  - Folder tree
  - Archetype + tier + hosts
  - Wave-1 tasks ready to dispatch
  - Active validators
  - Exact next command

MY BRIEF:
"""
<paste PDF text / scope / one line here>
"""

MY CONTEXT (optional):
- Deadline:            <48h hackathon / 2-week internship / open-ended>
- Who will see it:     <me / professor / interviewer / customers / team>
- Host agent(s):       <Claude Code / Cursor / Codex / Grok / OpenCode>
- Worker tool:         <same or OpenCode CLI>
- Tech preference:     <or "you choose">
- Must NOT do:         <hard constraints / out of scope>
```

---

## How archetype detection works

| Signal in brief/context | Likely archetype |
|---|---|
| "hackathon", "48 hours", "demo day" | `hackathon` |
| "internship", "report", "mentor/professor" | `internship` |
| "take-home", "assessment", "interview" | `job-take-home` |
| "paper", "experiments", "ablations", metrics | `research-ml` |
| "NER", "OCR", "extraction", documents | `nlp-pipeline` |
| "internal tool", "ERP", "for our team" | `internal-tool` |
| "customers", "multi-tenant", "SaaS", "PMF" | `saas-product` / `startup-mvp` |
| "CLI", "library", "package", "npm/pip" | `cli-tool` |
| "ETL", "warehouse", "analytics pipeline" | `data-pipeline` |

---

## Verification before "setup complete"

```bash
bash orchestrator/scripts/preflight.sh .
python3 conductor/conductor.py status --project .
```

Evidence or it didn't happen.
