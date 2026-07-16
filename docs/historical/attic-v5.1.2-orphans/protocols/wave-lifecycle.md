# Protocol — Wave Lifecycle

> Load when starting/running any wave. A "wave" (= vertical slice) is one coherent end-to-end deliverable.

```
PLAN      /plan wave-N
          → .specify/specs/wave-N/{spec, plan, tasks, contracts}
          → contracts/ = runnable acceptance tests (written BEFORE code)

DISPATCH  /dispatch wave-N
          → for each task, write a self-contained brief to work/wave-N/0X-*.md
          → check disjoint write sets (FM-13) before writing
          → log dispatch to events.jsonl

EXECUTE   (human opens OpenCode worker windows, pastes WORKER_PROMPT + one brief each)
          → workers run in parallel, write code, write work/reports/wave-N/0X-*.report.md

REVIEW    /review work/reports/wave-N/0X-*.report.md
          → orchestrator RE-RUNS acceptance commands itself (never trusts the claim — FM-09)
          → spawn verifier sub-agent for independent check
          → APPROVE | REVISE (rewrite brief, redispatch) | REJECT (→ attic/, re-plan)

MERGE     /merge ...
          → post-merge-format hook; run wave tests
          → update EXECUTION.md (REPLACE the row, don't append — FM-01)
          → append to CHANGELOG [Unreleased]; update HANDOFF.md; log event

SHIP      /ship wave-N   (when all tasks merged)
          → full acceptance + eval + perf; regenerate derived docs (FM-12)
          → run validators/preflight.sh — must pass
          → tag wave-N-complete with commit hash in EXECUTION.md
          → bump CHANGELOG; set HANDOFF active wave = N+1
```

## Right-sizing a wave
- 4–8 tasks; each ≤ one worker session (≤ ~2h, ≤ ~50K worker context).
- A wave ends with a DEMO: something a user/reviewer can see work.
- Vertical (a usable feature), not horizontal (a layer nobody can use yet).

## Gates between phases
- Can't DISPATCH without contracts/ existing (acceptance defined first).
- Can't MERGE without acceptance re-run green by the orchestrator.
- Can't SHIP without preflight.sh green (all wired validators pass).

## When a wave stalls
- Repeated REVISE on one task → the brief is unclear. Rewrite it tighter (inline more context), or `/zoom-out`.
- Scope ballooning → `/scope-guard`; move extras to BACKLOG.
- Lost the thread → `/handoff`, `/clear`, reload kernel + this wave's spec.
