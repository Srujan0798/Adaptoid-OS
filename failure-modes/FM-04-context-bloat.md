# FM-04 — Context Bloat → Forgetting

**Symptom.** The agent contradicts a decision it made earlier. Re-asks something already answered. Loses the thread mid-task. Quality degrades the longer a session runs. The user says "it forgets everything."

**Real incident.** The explicit motivation for rebuilding OS-Setup as a folder. Single 1500-line `OS_SETUP.md` files, 14KB `HIERARCHY.md`, sprawling per-wave prompt folders — the orchestrator read them once, then the middle fell out of context, then it improvised against its own rules.

**Root cause.** Two mechanisms:
1. **Front-loading.** Stuffing everything into always-loaded files (one giant CLAUDE.md / one giant setup file) fills the window with detail that's irrelevant most of the time.
2. **Context never compacted.** Long sessions accumulate dead exploration; the signal-to-noise collapses.

**Blast.** The model violates its own constitution, re-does work, hallucinates file contents it "remembers wrong." Every other failure mode gets more likely as context bloats.

**Prevention rule.**
- **Progressive disclosure.** Kernel always (~2K tokens). Everything else loaded on trigger only. This whole folder is built that way.
- **Short kernel.** CLAUDE.md ≤ ~3K tokens. Boris's test: "would removing this line cause a mistake?" If no, cut.
- **/clear between unrelated tasks.** Don't carry wave-1's chat into wave-2.
- **Compact to disk.** Decisions → ADRs; state → HANDOFF.md; events → events.jsonl. The chat is scratch, the files are memory.

**Validator.** `validators/context_budget.sh`:
- Sums tokens (≈ chars/4) of always-loaded files (CLAUDE.md + KIMI.md + HANDOFF.md + HIERARCHY.md). Warns > 8K, fails > 12K.
- Flags any single doc > 500 lines that is auto-loaded (should be lazy).

**Wire-in.** Run at session start and before adding anything to an always-loaded file.

**Fix when it fires.** Move detail from kernel files into `protocols/` or `docs/` (lazy-loaded). Run `/handoff` then `/clear`. Reload only kernel + current spec.
