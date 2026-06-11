# Protocol — Eval-Driven Development

> Load when defining capabilities or building anything AI/agent-flavored. Per Anthropic "Demystifying evals for AI agents" (Jan 2026).

## Core idea
Define the capability as TESTS before the agent/system can fulfill it. Tests evolve: capability evals (low pass-rate, "can we?") → regression suite (high pass-rate, "did we break it?").

## Structure (evals/)
- `tasks/NNN-*.task.yaml` — one test: input, execution, outcome verification, grader, trials, lifecycle stage
- `graders/` — code-based (deterministic), llm_judge (rubric), human_review
- `trials/` — multiple attempts per task (non-determinism)
- `transcripts/` — full records; READ THESE, don't trust scores blindly
- `outcomes/` — final environmental states
- `reports/` — pass@k / pass^k summaries

## Two metrics
- **pass@k** — succeeds in ≥1 of k attempts → capability presence
- **pass^k** — ALL k attempts succeed → production reliability

| Stage | target |
|---|---|
| Capability eval | pass@5 ≥ 50% |
| Regression suite | pass@3 ≥ 95% |
| Production blocker | pass^10 ≥ 99% |

## The 6 anti-patterns (reject evals that do these)
1. **Brittle grading** — rejecting `96.12` vs `96.124`; hardcoded tool-call sequences. Grade the OUTCOME, not the path.
2. **Ambiguous specs** — agent can't reasonably complete.
3. **Class imbalance** — only "should happen" cases; never "should refuse/not happen".
4. **Shared state pollution** — trials leak into each other. Each trial fresh.
5. **Bypasses** — agent "passes" by cheating (edits DB directly, hardcodes the answer).
6. **Saturation** — 100% pass = no signal; add harder tasks.

When pass^k = 0%: the task is probably broken, not the agent. Read the transcript.

## Lifecycle
- **Early:** 20–50 tasks from real failures (mine HALL_OF_SHAME + support tickets), not hundreds.
- **Growth:** promote capability evals → regression as they hit 95%; add harder ones on saturation.
- **Production:** run on every commit; combine with monitoring, A/B, user feedback (Swiss Cheese).
- **Always:** read transcripts weekly; calibrate LLM-graders vs humans quarterly.

## Frameworks
Harbor (containerized, Terminal-Bench compatible) · Braintrust (prod observability) · Langfuse (self-hosted) · Phoenix (open-source tracing) · LangSmith. The framework matters less than the task quality.

## For non-AI projects
"Evals" = the acceptance contracts in `.specify/specs/*/contracts/`. Same discipline: define done as runnable tests first; pass^k ≈ seed/flake stability (FM-10).
