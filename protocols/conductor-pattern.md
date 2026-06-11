# Protocol — Conductor Pattern (parallel specialized sessions + review gates)

> Load for high-velocity work. The pattern behind ~10× engineering throughput: many isolated agent sessions running in parallel, each in a specialized role, gated by structured reviews so parallelism doesn't become chaos. Verified from garrytan/gstack (MIT) + the Conductor workflow.

## The core idea
Instead of one agent doing everything sequentially, run **10–15 isolated sessions in parallel**, each with a narrow specialized role and a clear "when to stop." A structured sprint framework keeps them coordinated. Throughput scales with parallelism because the work is decomposed and the roles are specialized.

## The sprint spine
```
Think → Plan → Build → Review → Test → Ship → Reflect
```
Each stage feeds the next (the plan's test plan is what QA consumes; review flags what ship verifies). This sequence is what prevents parallel chaos — every session knows its role and its handoff.

## Specialized roles (skills), not generalists
The leverage comes from specialization. Representative role-skills (gstack-style; adapt to your stack):
- **Planning:** office-hours (interrogate the ask) · ceo-review (scope challenge) · eng-review (lock architecture) · design-review · devex-review · autoplan (chain them)
- **Build:** design-consultation/shotgun/html · implement
- **Review:** staff-review (auto-fix obvious) · investigate (root-cause) · security (OWASP+STRIDE) · cross-model review (second model audits the first)
- **Test:** qa (real browser, generate regression tests) · benchmark (Core Web Vitals)
- **Ship:** ship (sync/test/audit/PR) · land-and-deploy (merge/CI/verify) · canary (post-deploy monitor)
- **Meta:** learn (persistent memory) · retro (per-area retrospective) · spec (vague → executable) · careful/freeze/guard (safety + edit locks)

## Review gates (route work to the right reviewer)
| Building | Plan-stage gate | Live audit gate |
|---|---|---|
| UI / web / mobile | design-review | design-review (live) |
| API / CLI / SDK / docs | devex-review | devex-review (live) |
| architecture / perf / tests | eng-review | staff-review |
| anything | autoplan (auto-detect) | — |

Gates are the quality counterweight to speed: parallel build, but nothing ships without passing its matched review.

## How it maps to OS-Setup's two-tier model
- **Orchestrator (Claude/Kimi)** = the conductor. Owns the sprint spine, assigns roles, runs the gates.
- **Workers (OpenCode windows / isolated sessions)** = the parallel players, each a specialized role on a disjoint slice (FM-13 keeps writes disjoint).
- **Review gates** = OS-Setup's `/review` + `verifier` sub-agent + the matched specialist review.
- **Persistent memory across sessions** = `events.jsonl` + HANDOFF + (optional) a GBrain-style shared KB.

## When to use / not use
- **Use** when work decomposes into 5+ independent slices and velocity matters (hackathon crunch, big feature wave, migration).
- **Don't** for a small single-file change — the coordination overhead isn't worth it (Anthropic's "start simple" rule).

## The discipline that makes it safe
1. Disjoint write sets per session (FM-13; `check_dispatch_disjoint.sh`).
2. Every session has an explicit STOP condition (its acceptance contract).
3. Gates are mandatory, not optional — speed without review gates is how parallel work ships bugs at scale.
4. One conductor owns state; sessions are stateless hands (kernel TWO-TIER).

## Velocity note (honest)
gstack reports very high LOC/day via this pattern. Treat LOC as a rough proxy, not a goal — the real win is *parallelized specialized work behind mandatory review gates*. Optimize for shipped, reviewed features, not lines.

`verified: 2026-05 ⚡ (garrytan/gstack)`
