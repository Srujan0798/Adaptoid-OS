# Archetype — Internship Project

**Signals.** "internship", "mentor", "professor", "company project", "report", "presentation", "evaluation at the end", a real org (e.g., SWA Consultancy) but you're the builder being assessed.

**Default tier.** T1→T2. Real enough to be useful; documented enough to be presented; not full enterprise.

## Emphasize
- **A real, working deliverable.** It must actually run and do the thing the org wanted.
- **A defensible writeup.** `deliverables/report/` — problem, approach, architecture, results, limitations. You must be able to explain every line you "wrote."
- **A presentation.** `deliverables/slides/` — what/why/how/results, 12–15 slides.
- **Reproducibility.** Mentor can clone and run it. `make demo` works on a fresh machine.
- **Honest limitations.** A documented limitation reads as rigor; a hidden one reads as a gap when found.

## Skip
- Multi-tenancy, billing, marketing/GTM
- Heavy compliance unless the org's domain requires it
- Customer-facing polish beyond a clean internal UI

## Folders
- Include full T1 + `deliverables/{report,slides}`, `docs/` (architecture, decisions, runbook), `evals/` if it's an AI/ML deliverable.
- `STAKEHOLDER_UPDATE.md` (for the mentor) — light, periodic.

## Highest-risk failure modes
- **FM-07 embarrassing artifacts** — NO cheat sheets / AI prompts / "defense guides" in the repo the mentor browses. (This burned a past project — `MEETING_CHEAT_SHEET.md`.) Run `publish_gate.sh` before every push.
- **FM-09 false status** — don't claim results you can't reproduce in front of the mentor.
- **FM-05 metric inconsistency** — the report, slides, and README must state the SAME numbers from one generated source.
- **FM-12 stale derived docs** — README results must match the latest run, not an old one.

## Definition of done
- Deliverable runs on a fresh clone via documented steps
- Report + slides complete, numbers all from one source
- You can explain/derive every key piece without notes
- Repo is clean of working artifacts and AI scaffolding

## Deliverables
- The working system
- `deliverables/report/report.pdf`
- `deliverables/slides/`
- Clean, browsable repo
