# FM-14 — Lost Handoff (cold new session)

**Symptom.** A new session (or a switch from Claude to Kimi, or after a crash) starts with no idea what wave is active, what's been shipped, what's in flight. It re-derives wrongly, or asks the user to re-explain everything.

**Real incident.** The entire reason `HANDOFF.md` exists. Across long multi-session projects, every fresh session risked starting cold; without a handoff file the orchestrator would re-read everything (FM-04 bloat) or guess (hallucinate).

**Root cause.** Session state lived only in the chat. When the chat ended/compacted/switched models, the state was gone. No durable, compact "where we are" record.

**Blast.** Wasted re-orientation, wrong assumptions, duplicated work, user frustration ("I already told you this").

**Prevention rule (Brain/Hands/Session — kernel TWO-TIER).**
- `HANDOFF.md` always reflects current truth: active wave, last dispatched, last merged, open decisions, next action. Updated after every merge.
- `orchestrator/memory/session/<wave>-<task>.events.jsonl` is the append-only durable log.
- New session protocol: read HANDOFF.md → kernel → current wave spec → last N events. THEN act.
- Claude↔Kimi switch needs zero migration (identical CLAUDE.md/KIMI.md).

**Validator.** `validators/check_handoff.sh`:
- Fails if HANDOFF.md's "active wave" disagrees with EXECUTION.md (overlaps FM-01).
- Fails if HANDOFF.md wasn't updated since the last merge commit (stale handoff).
- Confirms `events.jsonl` exists for the active wave.

**Wire-in.** Session-start hook prints HANDOFF.md head. `/merge` updates HANDOFF.md. `replay_session.sh` reconstructs from events on demand.

**Fix when it fires.** Regenerate HANDOFF.md from EXECUTION.md + recent events + git log; then proceed.
