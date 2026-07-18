# Failure-Modes Library

> The reason OS-Setup exists. Each file is ONE real failure observed across actual projects (rfq2boq, swa-erp, DRO-FairML), with its root cause and an executable prevention.
>
> This is not theory. Every FM here was caught happening — several were caught **live** during the forensic scan that built this folder (see notes marked ⚡LIVE).

## How to use
- **Proactively:** before a risky operation, skim the relevant FM and run its validator.
- **Reactively:** when you see a symptom, open the matching FM, apply the fix, and ensure its validator is wired into the project so it can't recur silently.
- **At setup:** the orchestrator wires every applicable FM's validator into the new project's pre-commit + CI + review protocol.

## Format of each FM file
```
Symptom          — what you observe
Real incident    — where it actually happened
Root cause       — the actual mechanism (not the surface)
Blast            — what it costs if unprevented
Prevention rule  — the discipline
Validator        — the script that enforces it
Wire-in          — where the validator runs (hook/CI/review)
```

## The library (grows only)

| FM | Title | Class |
|---|---|---|
| FM-01 | State drift (duplicate/contradictory state files) | State |
| FM-02 | Stale process with wrong params | Process |
| FM-03 | Broken references (links to deleted files) | Integrity |
| FM-04 | Context bloat → forgetting | Context |
| FM-05 | Metric inconsistency (same fact, two values) | Truth |
| FM-06 | Config revert (param silently changed) | Config |
| FM-07 | Embarrassing artifacts committed | Publish |
| FM-08 | Scope creep / over-building | Scope |
| FM-09 | False status / misframing | Truth |
| FM-10 | Flaky tests (pass alone, fail in suite) | Test |
| FM-11 | Silent failures (swallowed errors) | Reliability |
| FM-12 | Stale derived docs (README with old numbers) | Truth |
| FM-13 | Parallel collisions (two workers, one file) | Concurrency |
| FM-14 | Lost handoff (cold new session) | Continuity |
| FM-15 | Context compaction (token limit → lost state) | Context |
| FM-16 | Wrong route (hallucinated DAG transitions) | Routing |
| FM-17 | Tampered state / undetected context drift | Integrity |
| FM-18 | Unauthorized tool call / destructive action | Security |
| FM-19 | Cost / token runaway | Cost |
| FM-20 | MCP / tool trust & injection | Security |

## Meta-rule
Every CRITICAL bug found in production or audit → add a new FM file here + a regression test + a validator. The library only grows. (This is the Hermes-style self-evolution loop.)
