# FM-15 — Context Compaction (orchestrator token limit)

> **Symptom:** Orchestrator hits token limit mid-wave. Loses context. Makes wrong decisions. Session dies. You have to say "continue" and it resumes from a cold guess.
>
> **Observed in:** DRO-FairML session — Claude hit usage limits 3+ times. Each time the orchestrator lost its place, required manual "continue," and re-read files it had already processed.

## Root cause
The orchestrator's context window fills with:
1. Full file contents from multiple `Read` calls
2. Tool outputs (grep results, file listings, diffs)
3. Prior conversation history
4. No explicit checkpoint before compaction

When `/compact` or the model's limit kicks in, the agent loses the "current state" — what wave, what task, what decisions are pending, what was already verified.

## Prevention

### 1. Checkpoint before compaction
Before `/compact` or before context feels full, write `orchestrator/memory/CHECKPOINT.md`:
```markdown
# Checkpoint — YYYY-MM-DD HH:MM UTC

## Current state
- Active wave: wave-N
- Active task: NN-name
- Phase: plan | dispatch | review | merge | ship
- Last completed: <what just finished>
- Pending: <what must happen next>

## Decisions in this session (not yet in ADRs)
- <decision 1>
- <decision 2>

## Verified truths this session
- <fact 1> (from <file> line <n>)
- <fact 2>

## Risks flagged
- <risk 1>
```

### 2. Compaction protocol
```
Context feels full → STOP
  ↓
Write CHECKPOINT.md (above)
  ↓
Run `/compact` or `claude --clear`
  ↓
Reload: kernel/ → HANDOFF.md → CHECKPOINT.md → active wave spec
  ↓
Resume from pending item
```

### 3. Size guardrails
- `context_budget.sh` monitors kernel size (FM-04)
- Orchestrator calls `emit_event.sh` before every major action — events.jsonl survives compaction
- Wave specs live in `.specify/specs/wave-N/` — re-read the one active spec, not all specs

## Validator
`context_budget.sh` (FM-04) catches kernel bloat before it causes compaction.
`validators/replay_session.sh` rebuilds context from events.jsonl after compaction.

## Fix when it happens
1. Do NOT act from chat memory after compaction
2. Read `orchestrator/memory/CHECKPOINT.md` (or recreate from events.jsonl)
3. Re-read HANDOFF.md + active wave spec
4. Confirm: "Resuming wave-N task-NN. Pending: <X>. Correct?"
5. Only then proceed
