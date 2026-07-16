# Protocol — Context Budget (anti-forgetting)

> Load when context feels full, before /clear, or before adding to an always-loaded file. Directly fights FM-04.

## Budgets
- Always-loaded kernel (CLAUDE.md + KIMI.md + HANDOFF.md + HIERARCHY.md): **≤ 8K tokens** combined. Warn at 8K, fail at 12K.
- Per-task working context: **≤ ~30K tokens**.
- Session before /clear: **≤ ~100K tokens**.

## The 5 techniques
1. **Progressive disclosure.** Don't read all of `orchestrator/core/` or this OS-Setup folder at startup. Kernel only; pull specific files on trigger.
2. **@-reference, don't paste.** Point at `@plan/PRD.md`; let the tool fetch on demand instead of pasting whole files.
3. **Compact to disk.** Decisions → ADRs. State → HANDOFF.md. Events → events.jsonl. The chat is scratch; files are memory.
4. **Sub-agents for exploration.** Spawn `codebase-explorer` in its own context; receive only the summary, not the 40 files it read.
5. **/clear between unrelated tasks.** Don't carry wave-1's conversation into wave-2.

## The "would removing this cause a mistake?" test (Boris)
Before adding a line to CLAUDE.md/kernel: if removing it wouldn't cause an error, it belongs in a lazy-loaded `protocols/` or `docs/` file, not the kernel.

## When context is clearly full
1. `/handoff` — write a compact "where we are" to HANDOFF.md (use the `caveman` compression style).
2. `/clear`.
3. Reload: kernel + HANDOFF.md + current wave spec + last N events. Nothing else.

## Signs of bloat (act on these)
- You're re-reading a file you read earlier this session.
- You contradicted an earlier decision.
- Responses slow / quality drops.
- You're quoting whole files when a line would do.

Run `validators/context_budget.sh` to measure.
