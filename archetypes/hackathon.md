# Archetype — Hackathon

**Signals.** "hackathon", "24/48/72 hours", "demo day", "MVP by tomorrow", "judges", speed emphasis, throwaway-ok.

**Default tier.** T0→T1 (lean). Never above T1 — observability/compliance are wasted here.

## Emphasize
- **The demo path.** One end-to-end happy path that works on stage. Nothing else matters as much.
- **Visible progress fast.** Wave-1 = a clickable/runnable thing in hours, not a foundation nobody sees.
- **Fallbacks for the demo.** Pre-recorded data, seeded DB, offline mode — so a flaky wifi doesn't kill the demo.
- **A crisp story.** README top = what it does + the 30-second pitch + how to run the demo.

## Skip (over-building here)
- Multi-tier auth/RBAC (one hardcoded user is fine)
- Compliance docs, SLOs, observability, audits
- Exhaustive test taxonomy (keep `tests/` = a few smoke + the demo path)
- Multi-Dockerfile, prod compose, Procfile
- `deliverables/paper|patent`

## Folders
- Include: `CLAUDE.md`/`KIMI.md`, `plan/PRD.md` (one page), `work/`, `src/`, `tests/` (smoke only), `README.md`, `demo/`
- Omit: `.specify/` heavy specs (a one-line acceptance per task is enough), `docs/operational`, `docs/compliance`, `evals/` (unless the project IS an agent)
- Keep `validators/preflight.sh` but only the fast checks.

## Highest-risk failure modes
- **FM-09 false status** — "it works" on stage when it doesn't. Demo the real path before claiming.
- **FM-02 stale process** — don't run three half-broken servers at once.
- **FM-11 silent failures** — a swallowed error mid-demo = white screen. Fail loud in dev, fallback gracefully in demo mode.

## Definition of done
The demo happy path runs start-to-finish on the presenter's machine, twice in a row, with the seeded/offline fallback ready.

## Deliverables
- Working demo (the app)
- 1-page README with run instructions + pitch
- Optional: 60-second `demo/script.md`
