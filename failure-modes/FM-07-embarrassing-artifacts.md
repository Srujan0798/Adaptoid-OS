# FM-07 — Embarrassing Artifacts Committed

**Symptom.** The repo contains files that should never be seen by the reviewer/professor/customer: cheat sheets, "defense guides," AI-orchestration prompts, vendor chat dumps, secrets, or `Co-Authored-By: <AI>` where unwanted.

**Real incident.** ⚡LIVE during this folder's build: `DRO-FairML/MEETING_CHEAT_SHEET.md` reappeared after a prior cleanup. Earlier the same project had `CHEAT_SHEET.md`, `DEFENSE_GUIDE.md`, `ORC_PROMPT.md`, `PROFESSOR_REVIEW_PROMPT.md`, `session-ses_*.md`, and an `agents/` briefing dir — all committed, all needing removal before the professor could browse the repo.

**Root cause.** Working artifacts (prep notes, AI prompts, conversation dumps) were written into the repo root and committed alongside real code. No gate distinguished "private working file" from "publishable artifact."

**Blast.** The reviewer sees you used a cheat sheet / AI prompts → credibility damage, possible integrity flag. Secrets leaked → security incident.

**Prevention rule.**
- Working artifacts go in `attic/` or a gitignored `scratch/`, never the tracked root.
- If a doc must exist (FAQ, formulas), it's framed as legitimate engineering documentation, not "cheat sheet for the meeting."
- A publish gate scans before every commit and before any push.

**Validator.** `validators/publish_gate.sh`:
- Fails on filenames matching: `*cheat*`, `*defense*guide*`, `*ORC_PROMPT*`, `*REVIEW_PROMPT*`, `*_simulator*`, `session-*`, `kimi-export*`, `*viva*`.
- Fails on content markers: AI-orchestration prompt phrasing, `Co-Authored-By` (configurable), `BRUTAL`/`merciless` reviewer language.
- Runs `detect-secrets`/`gitleaks` for keys.

**Wire-in.** Pre-commit hook (blocks), pre-push, CI `security.yml`.

**Fix when it fires.** Move the file to `attic/` (untracked) or delete; if it's a real doc, rebrand it professionally; rotate any leaked secret.
