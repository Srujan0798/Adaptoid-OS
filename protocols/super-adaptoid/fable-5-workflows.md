# Fable 5 Workflows Protocol

> The v5.0 workflow library for long-horizon, multi-agent, and self-improving tasks.

## Purpose

Provide a curated, composable set of workflows that encode the best practices for the five recurring v5.0 story types: research, build, review, launch, and evolve.

## The Five Fables

| Fable | Trigger | Pattern |
|---|---|---|
| Fable 1 — Deep Research | open-ended question | three-stage research with falsification |
| Fable 2 — Build & Ship | typed intent available | planner → coder → reviewer loop |
| Fable 3 — Critical Review | report/code exists | multi-critic cross-verification |
| Fable 4 — Launch & Grow | public release | positioning → content → checklist playbook |
| Fable 5 — Evolve | post-ship or anomaly | closed learning loop + evolution engine |

## Relationship to Workflows

Concrete YAML implementations live in `workflows/`. This protocol defines the narrative structure and success criteria for each Fable.
