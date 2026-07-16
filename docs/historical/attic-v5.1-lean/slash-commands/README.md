# Slash Commands — Named, Typed, Cost-Capped Workflows

> The orchestrator's user-facing API. Every command is a contract: inputs, outputs, cost ceiling, verification gates.

## Default Commands

| Command | Purpose | Cost Cap | Verification |
|---|---|---|---|
| `/adaptoid/plan` | Generate wave plan from intent | $0.50 | schema + evidence |
| `/adaptoid/build` | Dispatch wave tasks to workers | $2.00 | evidence + acceptance |
| `/adaptoid/review` | Review worker reports | $0.50 | cross-check |
| `/adaptoid/qa` | Run QA suite + acceptance | $1.00 | acceptance + regression |
| `/adaptoid/retro` | Post-wave retrospective | $0.25 | schema |
| `/adaptoid/done` | Mark wave shipped, update HANDOFF | $0.10 | state consistency |
| `/adaptoid/help` | List available commands | $0.01 | none |

## Power Commands

| Command | Purpose | Context |
|---|---|---|
| `/adaptoid/conductor` | Launch parallel sprint workspaces | high-velocity phases |
| `/adaptoid/evolve` | Trigger GEPA prompt evolution | benchmark-driven optimization |
| `/adaptoid/audit` | Run full verification + security audit | compliance checkpoints |

## Rules
1. Every command has a YAML contract in `slash-commands/adaptoid/<name>.yaml`.
2. Cost caps are hard ceilings — the orchestrator stops before exceeding.
3. Commands are versioned. Breaking changes bump the minor version.
