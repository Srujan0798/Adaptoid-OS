# Archetype — Startup MVP (pre-PMF)

**Signals.** "startup", "MVP", "find product-market fit", "first customers", "founder", "validate the idea", move-fast-but-real.

**Default tier.** T2, with T4 business docs. Real enough to charge for; lean enough to pivot.

## Emphasize
- **Speed to a usable product** that real users can try this week.
- **Instrumentation for learning.** Analytics on the core funnel from day 1 — you're learning, not just shipping.
- **Reversible decisions.** Don't lock into expensive architecture before PMF. Boring, swappable tech.
- **The business layer.** `STARTUP_ROADMAP.md` (vision, ICP, GTM, pricing experiments), `STAKEHOLDER_UPDATE.md`.
- **A pivot-able core.** Clean domain model; thin everything else, so a pivot rewrites the edges not the heart.

## Skip (until PMF)
- Full compliance (do the minimum legal; defer SOC2)
- Multi-region, k8s, heavy SRE
- Exhaustive test coverage on features that may get cut
- Premature scale optimization

## Folders
- T2 base + `STARTUP_ROADMAP.md`, `ROADMAP.md`, `docs/business/{STAKEHOLDER_UPDATE,pricing,demo_video_script}.md`, `Procfile`, analytics wiring.
- Defer `docs/compliance/` full set; keep a stub.

## Highest-risk failure modes
- **FM-08 scope creep** — the startup killer. Build only what tests a hypothesis. Everything else → BACKLOG.
- **FM-09 false status** — don't tell yourself/investors it works when it doesn't; instrument and look.
- **FM-04 context bloat** — fast iteration = many sessions; keep handoffs tight.
- **FM-07 artifacts/secrets** — customer-facing; no leaks.

## Definition of done (per wave)
- A hypothesis is testable with real users (the feature + the analytics to measure it)
- Core funnel instrumented
- Ships behind a flag if risky

## Deliverables
- The MVP (deployed, usable)
- `STARTUP_ROADMAP.md` kept live (what we learned → next experiment)
- Weekly `STAKEHOLDER_UPDATE.md`
