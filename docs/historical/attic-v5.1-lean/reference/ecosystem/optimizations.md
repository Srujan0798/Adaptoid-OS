# Ecosystem — Optimizations (cost, speed, reliability — pull for every project)

> The compounding wins the best agentic engineers use. Most are cheap to adopt and pay back immediately.

## Token / cost
1. **Prompt caching** (Anthropic/OpenAI). Cache the stable prefix (kernel, system, tool defs). 5-min TTL on Anthropic — structure sessions to stay warm; batch within the window. Huge cost cut on repeated context.
2. **Tool-output compression** — `headroom` ⚡ (60–95% reduction before the LLM sees RAG/tool results).
3. **Code indexing** — `codegraph` ⚡ so the agent reads 5 files not 500.
4. **Progressive disclosure** — load kernel always, everything else on trigger (this whole OS-Setup). The structural version of context economy.
5. **caveman skill** — ~75% reduction on summaries/handoffs.
6. **markitdown** ⚡ — convert messy docs once, cheaply, instead of re-parsing.

## Speed
7. **Parallel workers / worktrees** — Emdash, Mux, or just multiple OpenCode windows on disjoint files (FM-13 keeps them safe). Linear → parallel is the biggest wall-time win (saw 30h→10h on DRO-FairML by parallelizing).
8. **Sub-agents for exploration** — Opus orchestrator + Haiku/cheaper sub-agents for read-heavy investigation; only the summary returns to main context.
9. **Background agents** — long tasks run async (Claude Code background, OpenHands, ADK Cloud Run); you check back.
10. **Auto mode** — skip permission prompts for r0/r1 (read/local) actions; pause only at r2+ (blast-radius.md).

## Reliability
11. **Eval-driven dev** — pass@k/pass^k; capability evals → regression suite (protocols/eval-driven-dev.md).
12. **Swiss-cheese verification** — stack the layers (protocols/verification.md).
13. **Durable session log** — `events.jsonl` so a crash resumes, not restarts (FM-14).
14. **Config-as-law + runtime assertion** — kills the wrong-param run (FM-02/FM-06) that wasted hours.
15. **Deterministic tests** — seed everything; run suite twice shuffled (FM-10).

## Quality
16. **CLAUDE.md short** (Boris) — the model follows a tight contract better than a sprawling one.
17. **Plan → code → verify** — never skip plan on multi-file changes (Karpathy).
18. **Surgical diffs** — touch only what's asked; reviewers + future-you benefit.
19. **One-source-of-truth metrics** — generated, never hand-typed (FM-05/FM-12).

## The compounding thesis
Each is a few % to a few ×. Stacked, a project that uses prompt-caching + indexing + compression + parallelism + eval-gates runs ~an order of magnitude cheaper/faster/more-reliably than a naive one. That gap IS the "beat everyone" edge — not a secret model, just disciplined use of the ecosystem.

`verified: 2026-05 (headroom/codegraph/markitdown ⚡; caching/parallel/eval patterns corpus + Anthropic posts)`
