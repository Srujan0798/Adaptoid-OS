---
name: worktree-parallel
description: >
  Use when ≥2 agents might edit overlapping paths. One task → one git worktree → disjoint writes → merge after tests.
---

# Worktree parallel (FM-13)

1. Parallel BUILD only if `writes` sets are disjoint **or** each agent has its own worktree.
2. Prefer host worktree isolation (Claude `--worktree`, Grok/Codex worktrees).
3. Merge only after TEST evidence on each branch/worktree.
4. Single writer for `HANDOFF.md` on the primary tree.
