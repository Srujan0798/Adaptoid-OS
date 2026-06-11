# Protocol — Event Sourcing

> Load when designing session persistence, debugging a past run, or proving what happened. Every state mutation is an immutable event; current state is a *derived view*. The event log is the single source of truth — HANDOFF.md, EXECUTION.md, and dashboards are projections of it.

## The model

```
Traditional:  State[n+1] = f(State[n], Input)        — overwrite previous state
Event log:    Event[n+1] = g(State[n], Input)        — append event, never edit
              State[n+1] = replay(Event[1..n+1])     — derive state by folding events
```

Core invariants (non-negotiable):
1. **Append-only.** Events are never deleted, never modified. Corrections append new events.
2. **Deterministic replay.** Same event sequence → same reconstructed state, every time.
3. **Hash chained.** Each event embeds the previous event's hash (`prev_hash`). Genesis chains from 64 zeros. Any edit to history breaks the chain at the *next* event — tamper evidence by construction (FM-17).
4. **Total order per stream.** One JSONL file per wave-task; lines are strictly ordered.

## What this buys you

| Capability | How |
|---|---|
| Crash / compaction recovery (FM-15) | `replay_session.sh` + `wake.sh` rebuild orchestrator state from events |
| Tamper detection (FM-17) | `audit_chain.sh` verifies hash continuity; modified history breaks the chain |
| "What actually happened" forensics | The log records decisions as they occurred, not as later remembered (FM-09) |
| Time-travel debugging | Replay events up to any point to reconstruct the state at that moment |
| New-session handoff (FM-14) | HANDOFF.md is a projection; if it's stale, the event log is authoritative |

## Event format (as emitted by `validators/emit_event.sh`)

```json
{"ts": "2026-06-12T09:00:00Z", "id": "evt-178120784982", "type": "task.dispatched",
 "wave": "wave-1", "task": "01-backend", "prev_hash": "sha256:…", "file": "work/wave-1/01-backend.md",
 "hash": "sha256:…"}
```

- `type` — dot-namespaced event type (see table below)
- `prev_hash` — hash of the previous event in this stream (genesis = 64 zeros)
- `hash` — SHA-256 of this event line (computed over everything before the hash field)
- arbitrary `key=value` pairs become payload fields

## Recommended event types

| Type | When | Payload suggestions |
|---|---|---|
| `intent.parsed` | brief → typed PROJECT-INTENT | archetype, tier |
| `task.dispatched` | worker task file written | file, owner |
| `task.completed` / `task.failed` | worker report accepted/rejected | result, evidence |
| `verify.passed` / `verify.failed` | a verification gate ran | gate, layers, evidence |
| `route.blocked` | route sentinel rejected a transition | from, to, rule |
| `policy.denied` | OAP refused a tool call | tool, policy |
| `state.committed` | durable state written + hashed | file, state_hash |
| `checkpoint.saved` | CHECKPOINT.md written before /compact | reason |
| `rollback.executed` | recovery to a prior checkpoint | to_checkpoint, reason |
| `human.approval` | HITL gate decision | action, decision |
| `lesson.recorded` | memory-bank LESSON written | file |

Emit at every major action. The discipline is cheap (one shell call); the forensics are priceless.

## State reconstruction

```
wake.sh         — at session start: kernel + HANDOFF + EXECUTION + replay of recent events
replay_session.sh — after crash/compaction: full replay of a wave-task stream
audit_chain.sh  — before claiming session integrity: verify chain continuity
```

Replay rule: **never trust a projection over the log.** If HANDOFF.md disagrees with events.jsonl, the log wins and the projection gets regenerated (FM-12 applied to session state).

## Snapshots (long streams)

For streams that grow large, write a periodic snapshot event (`checkpoint.saved` with a state summary or a pointer to CHECKPOINT.md). Replay then starts from the latest snapshot instead of genesis. Keep the raw events — snapshots accelerate replay, they do not replace history.

## Retention

- Hot: current + previous wave streams stay as-is.
- Archive: completed-wave streams may be compressed and moved to `orchestrator/memory/session/archive/` — *after* `audit_chain.sh` passes on them. Never archive a broken chain; investigate it.

## Integration map

| Concern | Protocol / tool |
|---|---|
| State hashing of durable files | `protocols/vault-mmu.md` (`state.committed` events carry the VaultMMU hash) |
| Pre-execution route blocking | `protocols/route-sentinel.md` (blocked routes emit `route.blocked`) |
| Tool-call policy denials | `protocols/oap-security.md` (denials emit `policy.denied`) |
| Context refresh at phase boundaries | `protocols/runtime-context-check.md` |
| Token-limit checkpointing | `failure-modes/FM-15-context-compaction.md` |
