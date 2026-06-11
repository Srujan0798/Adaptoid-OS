# Kernel — Two-Tier Architecture (Brain / Hands / Session)

> Always loaded. The shape of every project built with OS-Setup.

## The two tiers

```
TIER 1 — ORCHESTRATOR  (Claude Code OR Kimi — interchangeable)
  Plans. Dispatches. Reviews. Merges. Owns project state.
  ONE at a time. If one model is down, the other reads the same files and continues.
        │  writes task brief → work/<wave>/<task>.md
        ▼
TIER 2 — WORKERS  (OpenCode CLI / Cursor / MiniMax / Codex — many, parallel)
  Each takes ONE self-contained brief. Executes. Writes code. Writes a report.
  Stateless across tasks. Uses ITS OWN skills, not the orchestrator's.
        │  writes report → work/reports/<wave>/<task>.report.md
        ▼
  Back to orchestrator: review → merge.
```

**Hard rule:** the orchestrator never writes feature code; workers never plan. The bridge is the `work/` folder. Nothing else passes between tiers.

## Anthropic's Brain / Hands / Session mapping (Apr 2026)

| Primitive | Our equivalent | Why it matters |
|---|---|---|
| **Brain** (model + harness) | the orchestrator (Claude/Kimi) | can crash and resume |
| **Hands** (sandboxes, tools) | OpenCode worker windows, MCP servers | disposable; replace freely |
| **Session** (durable log) | `orchestrator/memory/session/<wave>-<task>.events.jsonl` | the ONE thing that must survive |

Three failure modes, three recoveries:
- **Brain crash** → reopen Claude/Kimi → reads HANDOFF.md + events.jsonl → resumes.
- **Hand crash** → that worker window dies → open a new one with the same brief.
- **Session lost** → the only fatal one. That's why state lives in files, never only in the chat.

## Why interchangeable orchestrators

You use Claude Code and Kimi interchangeably. So:
- `CLAUDE.md` and `KIMI.md` at the project root have **identical content**.
- `AGENTS.md` is an alias for the same (Cursor/Codex compat).
- Switching mid-project requires zero migration — both read the same `orchestrator/` apparatus.

## Why workers are stateless

Workers forget everything between tasks BY DESIGN. This is a feature: it forces every task brief to be self-contained, which is what makes parallel dispatch safe. A brief that needs "remember what we discussed" is a broken brief. See `protocols/dispatch-protocol.md`.
