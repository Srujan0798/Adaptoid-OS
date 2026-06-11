# Protocol — Runtime Context Check (primary persistence)

> Load at every major phase boundary. This is the PRIMARY persistence mechanism: the agent validates and refreshes context before acting, rather than trusting that files/daemons kept things current. Git hooks/daemons are optional enhancers, never dependencies (works air-gapped/sovereign).

## When to run (every major phase boundary)
- Before PLAN, before DISPATCH, before each REVIEW, before MERGE, before SHIP, before any context handoff, at session start (`wake()`).

## What to check (the pre-phase ritual)
1. **Refresh state.** Re-read the small set of truth files: `HANDOFF.md`, `plan/EXECUTION.md`, the active wave's spec, last N `events.jsonl` entries. Don't act from chat memory (FM-04/FM-14).
2. **Detect staleness.** Is HANDOFF.md older than the last merge commit? Is EXECUTION's active wave consistent? (runs `validate_state.sh` — FM-01).
3. **Detect contradictions.** Do two sources disagree (a metric, a status, a config)? If so, resolve to the single source of truth before proceeding (FM-05).
4. **Detect missing artifacts.** Does a referenced file/spec/contract actually exist? (`check_references.sh` — FM-03).
5. **Detect stale processes.** About to run a job? `check_processes.sh` first (FM-02).
6. **Detect config drift.** Critical params still match the lock? (`check_config.sh` — FM-06).
7. **Pull, then act.** Only after the above is clean does the phase proceed.

## Why runtime-check over daemon-enforced
- **Robust + sovereign.** Works with no git, no daemon, no network. Pure local / air-gapped fine.
- **Agent-native.** The agent already reasons about context; making validation an explicit pre-phase step fits naturally and self-heals.
- **No hidden process.** Daemons that "keep things in sync" fail silently and become a dependency. Runtime checks fail LOUD, in the agent's view, exactly when it matters.

## Optional enhancers (enable if helpful, never required)
- **Git hooks** — pre-commit runs the validators; pre-push runs publish_gate. Good for teams.
- **Local daemon / file-sync** — auto-commit context, Obsidian-git sync, workspace persistence. Good for long-running 24/7 agents.
- **Watch mode** — re-run preflight on file change. Good for tight loops.

These accelerate; they don't replace the runtime check. If a daemon is down, the agent still validates correctly.

## Self-healing on failure
- Stale HANDOFF → regenerate from EXECUTION + events + git log.
- Drift (FM-01/FM-05/FM-12) → regenerate the derived artifact from its source.
- Stale process (FM-02) → kill + restart clean.
- Context full (FM-04) → `/handoff` then `/clear`, reload kernel + active spec.

## One-line implementation hook
`orchestrator/hooks/session-start.sh` and the orchestrator's phase transitions call `validators/preflight.sh` (fast subset) + re-read the truth files. The pre-phase check is cheap and prevents the expensive failures.
