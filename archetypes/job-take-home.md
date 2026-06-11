# Archetype — Job Take-Home / Assessment

**Signals.** "take-home", "coding assessment", "interview project", "evaluate my code", "submit by", a reviewer who will judge code quality not just function.

**Default tier.** T1, polished. Small surface, high finish.

## Emphasize
- **Reviewer experience.** The reviewer spends ~20 min. README must make it trivial: what, why, how-to-run, how-to-test, design decisions, trade-offs, what you'd do with more time.
- **Clean, idiomatic code.** Matches the language's conventions. No dead code, no commented-out blocks, no TODOs left in.
- **Tests that demonstrate thinking.** Not 100% coverage theater — the RIGHT tests (edge cases, the tricky bits) with clear names.
- **Visible decisions.** A short `DECISIONS.md` or README section: "I chose X over Y because…" Reviewers reward judgment.
- **Runs first try.** `make test` / one command. If it doesn't run, function doesn't matter.

## Skip
- Over-engineering for scale they didn't ask for (anti-signal to reviewers)
- Speculative abstractions, plugin systems, config frameworks
- Deployment infra unless the prompt asks
- Heavy docs beyond the README + DECISIONS

## Folders
- Minimal, clean: `src/`, `tests/`, `README.md`, `DECISIONS.md`, `Makefile`, language config, CI (shows you know CI).
- Omit: `.specify/` heavy, `docs/operational`, `deliverables/`, `orchestrator/` apparatus can be hidden in a branch — the submitted tree should look hand-crafted, not agent-scaffolded.

## Highest-risk failure modes
- **FM-07 embarrassing artifacts** — CRITICAL. No AI-orchestration files, no `CLAUDE.md` cruft, no `Co-Authored-By` if the assessment expects your own work. Run `publish_gate.sh` hard. Consider building with the apparatus in a gitignored dir.
- **FM-08 scope creep** — reviewers penalize over-engineering. Do exactly what's asked, well.
- **FM-09 false status** — the README claims must match reality; reviewers WILL run it.
- **FM-10 flaky tests** — a flaky suite in a take-home is an instant red flag.

## Definition of done
- One command runs it; one command tests it; both green on a fresh clone
- README answers what/why/run/test/decisions/trade-offs/next
- Code reads like a senior engineer wrote it by hand
- Zero agent/AI scaffolding visible in the submitted tree

## Deliverables
- The clean repo (or zip)
- README + DECISIONS
