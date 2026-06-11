# Memory Bank — Living Folder Memory

> The Anti-Forgetting Triad: folder-based persistent memory + mandatory bootstrap reading + verification gates that detect drift.

## Structure

```
memory-bank/
├── facts/          — verified truths (TTL: 90 days default)
├── decisions/      — ADRs (Architecture Decision Records)
├── lessons/        — post-mortems + crystallized patterns
├── sessions/       — per-session distilled context
├── evidence/       — receipts, outputs, screenshots
└── snapshots/      — checkpoint dumps before compaction
```

## Rules
1. **Markdown is the source of truth.** Human-editable, machine-parseable, grep-friendly.
2. **Every entry has a `verified:` date.** Stale entries trigger `memory-sync.sh --rotate`.
3. **Facts decay.** TTL defaults: facts 90d, decisions 365d, lessons 180d. Refresh or archive.
4. **Bootstrap reading.** Every new session reads the most recent 5 facts + 3 decisions + 2 lessons.

## Templates
- Use `FACT.template.md` for facts
- Use `LESSON.template.md` for lessons
- Use `ADR.template.md` for decisions
