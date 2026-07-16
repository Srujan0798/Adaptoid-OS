# HANDOFF — Adaptoid OS kit (this repo)

> **Replace, never append.** Cold sessions for kit maintainers start here.

## Status
- **Active wave:** wave-1
- **Active task:** maintenance / dogfood lessons only
- **Release:** v5.1.0 product complete (see `VERSION`)
- **Last updated:** 2026-07-16
- **Branch:** `main`

## Goal (one line)
Keep the portable harness (Lite / Core / Pro) shippable: any host, any model, finishable projects.

## Done so far
- Core package + host emission (`agents`, `claude`, `cursor`, `codex`, `grok`)
- Conductor runtime (wake, init-wave, dispatch stub/shell, HANDOFF rewrite)
- Benchmarks + 50 harness calibration cases + `make ship-check`
- CI workflow validates dogfood + tests + bench + cal smoke
- Real dogfood: hackathon whiteboard brief → shell PASS reports

## Next (ordered)
1. External dogfood on real user projects (collect FMs only with evidence)
2. Optional: deeper host hooks when a host's lifecycle events are needed
3. Do **not** expand multi-channel / enterprise without demand

## Pending decisions
- None blocking v5.1

## Blockers
- None

## Evidence links
- `PRODUCT.md` — definition of done
- `make ship-check` — release gate
- `CHANGELOG.md` — v5.1 entries
- `core/README.md` — Core ladder

## Do NOT
- Bloat kernel beyond ~2K tokens
- Add multi-channel/enterprise “for completeness”
- Claim model quality wins without harness evidence
