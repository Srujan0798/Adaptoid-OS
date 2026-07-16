# Protocol — SDLC Loop (efficient, not theater)

> Load when planning a wave or when “what do we do next?” is unclear.  
> Source alignment: classic SDLC stages (planning → maintain) + Agile increments.  
> Ref: [GFG SDLC overview](https://www.geeksforgeeks.org/software-engineering/software-development-life-cycle-sdlc/).

## Point

Loop engineering is **waste** if you only re-read docs.  
It is **useful** if each loop is a real SDLC gate with **evidence**, then ship or fix.

Adaptoid default = **Agile SDLC**: short waves that each touch plan → build → test → (optionally) deploy, not one giant waterfall unless the tier demands it.

## The 7 stages → Adaptoid

| # | SDLC stage | Adaptoid artifact | Done means (evidence) |
|---|---|---|---|
| 1 | Planning & feasibility | `PROJECT-INTENT.md` scope + tier | Goal, IN/OUT, falsification written |
| 2 | Requirements | Intent success criteria + HANDOFF next | Stakeholder needs as testable bullets |
| 3 | Design | `plan/` or task `writes` lists | Architecture notes; no freehand scope |
| 4 | Development | code under task `writes` | Diff exists; stays in box |
| 5 | Testing | unit/integration/acceptance cmds | Commands run + exit 0 pasted |
| 6 | Deployment | ship only after preflight | `preflight.sh` green; blast-radius ok |
| 7 | Maintenance | next wave HANDOFF | Bugs/enhancements = new tasks, not silent scope |

## Anti-waste rules (GFG “common mistakes” → harness)

1. **Docs are not the goal** — intent + handoff only; no SRS novel unless T3.  
2. **Test early** — every build task has `acceptance:` before coding.  
3. **Non-functionals in intent** — security/perf as success criteria when real.  
4. **No overengineering in wave-1** — smallest vertical slice.  
5. **Feedback loop** — rewrite HANDOFF after every wave (replace, never append).  
6. **Security is continuous** — OAP policy + publish_gate; not a phase you skip.

## Methodology pick (one line)

| When | Model |
|---|---|
| Hackathon / spike T0 | Compressed: Plan → Build → Demo-test (skip heavy design) |
| Default product T1–T2 | **Agile waves** (this protocol) |
| Compliance T3+ | Explicit design gate + audit trail (events.jsonl) |
| Ops-heavy | DevOps: CI (`preflight`, headless host) after every merge |

## Per-wave mini-loop (default)

```
PLAN   → intent + task briefs (disjoint writes)
BUILD  → implement only writes
TEST   → acceptance + preflight
SHIP?  → blast-radius check; else next wave
MAINT  → HANDOFF rewrite
```

Never start BUILD without PLAN evidence.  
Never claim SHIP without TEST evidence.

## Host features (use the tool; don’t reimplement)

Coding hosts (e.g. Grok Build / Claude Code / Cursor) already provide: plan mode, subagents, skills, hooks, MCP, search, git, terminal, review, sandbox.  
Adaptoid **does not replace** them — it **orients** them with AGENTS.md + intent + validators.

See `core/HOST-CAPABILITIES.md`.
