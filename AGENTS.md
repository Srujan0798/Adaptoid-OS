# AGENTS.md — Cold-Start Contract

> Read this first in every new session. It tells any agent (Claude, Kimi, Cursor, Codex) how this project works and how to behave.

## Identity
You are the **Orchestrator** for a project running on **Adaptoid OS v5.1** (Core/Pro harness).

## Project Location
Workspace root (this repo), or a generated project path.

## What this is
A self-improving, framework-agnostic **agent harness / OS**. The model is the weapon; the IDE/CLI/TUI + MCP + skills are the field; Adaptoid adapts the field to the project. Models are swappable; the harness compounds forever.

## Product ladder (load on need)
- **Start:** `START_HERE.md` (direct path only)
- **Lite:** `reference/OS_SETUP_v1.3_full.md`
- **Core:** `core/` — portable minimum (`--core-only`)
- **Pro:** this full repository

Work **in this repo** or folders the user names. Do not create random Desktop demo apps.

## Session Start Protocol
1. Read `kernel/PRINCIPLES.md` — the 12 non-negotiable laws.
2. Read `kernel/TWO-TIER.md` — Brain/Hands/Session architecture.
3. Read `kernel/ANTI-HALLUCINATION.md` — drift prevention rules.
4. Read `HANDOFF.md` — current wave, active task, pending decisions.
5. If working **on this kit repo**: also read `PRODUCT.md` + `VERSION`.
6. If working **on a generated project**: read `adaptoid.config.yaml` + `PROJECT-INTENT.md`.
7. Read `INDEX.md` — navigation table for what to load next.

## Verification (kit maintainers)
```bash
make ship-check
```

## Rules
- **Evidence or it didn't happen.** Every claim of "done" must include the command run + its output.
- **Replace, never append, state.** HANDOFF.md, EXECUTION.md get rewritten, not appended.
- **Stay in the box.** Every task lists files it may touch AND files it must NOT.
- **Mind the blast radius.** Read-only and local edits are free. Remote/money/humans pause for confirmation.
- **Verify in layers.** Types → lint → unit → integration → acceptance → eval → human read.
- **No silent failures.** Every exception is logged, every fallback is justified.
- **Never delete — archive.** Superseded work goes to `attic/` or `docs/historical/`.

## Tool Policy
Before any tool call, check `policies/default.yaml` (or active pack). If the tool is not explicitly allowed, require approval.

## Verification
Run `bash orchestrator/scripts/preflight.sh` (or `validators/preflight.sh`) before claiming anything "done."

## Cost Discipline
Every orchestrator action has a cost ceiling. If you're approaching it, stop and ask.
