# Templates

> The files the orchestrator generates into a new project, adapted to archetype + tier. These are SOURCES — the orchestrator fills placeholders, never copies verbatim with `{{...}}` left in.

## The deep reference
The complete, filled examples of every template (CLAUDE.md kernel, HANDOFF, HIERARCHY, TASK/REPORT/WORKER, Makefile, mcp.json, pyproject, CI, ROLE, core/*, skills, agents, hooks, recipes, specs, PRD/ARCHITECTURE/EXECUTION, docs, evals) live in:

**`../reference/OS_SETUP_v1.3_full.md`** — §4 has every template verbatim.

This folder is intentionally thin: rather than duplicate 600 lines of templates (which would themselves drift — FM-05), the orchestrator reads the reference for exact template bodies and applies the structure below.

## What gets generated where
| Project path | Template source | Notes |
|---|---|---|
| `CLAUDE.md` + `KIMI.md` | reference §4.1 | identical content; embed the kernel laws |
| `AGENTS.md` | alias of CLAUDE.md | Cursor/Codex compat |
| `HANDOFF.md` | reference §4.2 | session continuity (FM-14) |
| `HIERARCHY.md` | reference §4.3 | repo map + ownership |
| `work/TASK_TEMPLATE.md` | reference §4.5 | self-contained brief format |
| `work/REPORT_TEMPLATE.md` | reference §4.6 | requires evidence block (FM-09) |
| `work/WORKER_PROMPT.md` | reference §4.7 | universal worker prefix |
| `.specify/memory/constitution.md` | kernel/PRINCIPLES.md + project rules | adds to, never contradicts, the 12 laws |
| `.specify/specs/wave-N/*` | reference §4.23 + protocols/eval-driven-dev | spec/plan/tasks/contracts |
| `plan/{PRD,ARCHITECTURE,EXECUTION}.md` | reference §4.12 + archetype | EXECUTION row = one per wave + commit hash (FM-01) |
| `orchestrator/**` | reference §4.4, 4.13, core/* | ROLE, core, commands, skills, agents, hooks, recipes, rules |
| `Makefile` | reference §4.8 | dev/test/lint/dispatch/ship targets |
| `mcp.json` | reference §4.9 | domain MCP servers |
| `pyproject.toml` / `package.json` | reference §4.10 | language config |
| `.github/workflows/*` | reference §4.12 | ci/test/security (+ tier extras) |
| `.pre-commit-config.yaml` | reference §4.11 | wires validators as hooks |
| `evals/*` | reference §4.23–24 | eval-driven dev |

## Always copy the validators
On generation, copy `OS-Setup/validators/*.sh` → the project's `orchestrator/scripts/` and wire them:
- pre-commit: `validate_state`, `check_references`, `publish_gate`, `check_silent_failures`
- CI: `preflight.sh`
- review protocol: run `preflight.sh` before every `/merge` and `/ship`
- before any long run: `check_processes.sh`
- before `/dispatch`: `check_dispatch_disjoint.sh`

## Generation order
See `INDEX.md` § "Generation order."
