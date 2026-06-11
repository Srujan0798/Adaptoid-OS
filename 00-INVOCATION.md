# 00 — INVOCATION

> Paste this whole file into Claude Code or Kimi, then paste your brief. The agent does the rest.

---

## The prompt to paste

```
You are the ORCHESTRATOR for a new project. You will set it up using the OS-Setup
operating system located at ~/Desktop/OS-Setup/ (or the path I give you).

Do this, in order:

1. Read OS-Setup/kernel/ (all 3 files). These are your non-negotiable laws.

2. Read my brief (below). Detect the ARCHETYPE by matching against
   OS-Setup/archetypes/. If ambiguous, ask me ONE multiple-choice question.
   Then read that one archetype file.

3. Pick a TIER from OS-Setup/tiers/TIERS.md (default T1; the archetype suggests one).

3b. CONSULT THE LIBRARY. Read OS-Setup/reference/HOW-TO-PULL.md, then
   OS-Setup/reference/ecosystem/SELECTION.md. Pull the 2–4 ecosystem catalog files
   that match this project (e.g., coding-agents, sdks-adks, memory-context,
   optimizations, knowledge-systems). Choose the SMALLEST stack that ships the
   archetype. Write the choice + why into docs/decisions/0002-stack-selection.md.
   Then close those files (don't keep them in context).

4. Generate the complete project structure into THIS directory, using
   OS-Setup/templates/ (+ reference/OS_SETUP_v1.3_full.md for exact template bodies),
   adapted to the archetype + tier + chosen stack.
   Fill every placeholder with project-specific content. No {{PLACEHOLDER}} may remain.

5. Copy OS-Setup/validators/* into orchestrator/scripts/ and run preflight.sh.
   It must pass before you declare setup complete.

6. Bake in failure prevention: for every failure mode in OS-Setup/failure-modes/
   that applies to this archetype, ensure the corresponding validator + rule is wired
   into the project (pre-commit hook + CI + the orchestrator's review protocol).

7. Generate wave-1 task files in work/wave-1/ ready to paste into OpenCode CLI workers.

When done, print:
  - The folder tree you created
  - Detected archetype + chosen tier (and why)
  - The first wave's task files, ready to dispatch
  - Which failure-mode validators are active
  - The exact command to start

MY BRIEF:
"""
<paste PDF text / scope / one line here>
"""

MY CONTEXT (optional — fill what you know):
- Deadline:            <e.g. 48h hackathon / 2-week internship / open-ended>
- Who will see it:     <just me / professor / interviewer / customers / team>
- Orchestrator model:  <Claude Code / Kimi — interchangeable>
- Worker tool:         <OpenCode CLI / Cursor / MiniMax / Codex>
- Tech preference:     <or "you choose">
- Must NOT do:         <hard constraints / out of scope>
```

---

## How archetype detection works

The orchestrator reads your brief + context and matches signals:

| Signal in brief/context | Likely archetype |
|---|---|
| "hackathon", "48 hours", "demo day", speed emphasis | `hackathon` |
| "internship", "report", "presentation", "mentor/professor" | `internship` |
| "take-home", "assessment", "interview", "evaluate my code" | `job-take-home` |
| "paper", "experiments", "ablations", "baselines", metrics | `research-ml` |
| "NER", "OCR", "extraction", "pipeline", documents | `nlp-pipeline` |
| "internal tool", "ERP", "admin", "for our team" | `internal-tool` |
| "customers", "multi-tenant", "billing", "SaaS", "PMF" | `saas-product` / `startup-mvp` |
| "CLI", "library", "package", "npm/pip" | `cli-tool` |
| "ETL", "warehouse", "analytics", "dashboard" | `data-pipeline` |
| none clear | ask ONE question, default `internal-tool` at T1 |

Each archetype file tells the orchestrator: which tier to default to, which folders to include/skip, which failure-modes are highest-risk, what "done" means, and what the deliverables are.

---

## If you have NO brief yet (just an idea)

Paste the prompt above with a one-line idea. The orchestrator will run the
`interviewer` protocol — ask you 3–4 multiple-choice questions — then proceed.
You never have to write a spec yourself; you answer questions.

---

## Re-running on an existing project

Point the orchestrator at OS-Setup and say "audit this existing project against
OS-Setup and add what's missing." It will:
- Detect the archetype from existing code
- Run all validators (find drift, broken refs, stale processes, embarrassing artifacts)
- Report gaps and offer to fix them
- NOT overwrite your code — only add scaffolding + fix violations you approve
