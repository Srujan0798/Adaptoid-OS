# Self-Improvement Protocol — GEPA + Hermes

> The "compound eternally" flywheel. The system improves its own harness over time.

## GEPA — Genetic-Pareto Prompt Evolution

1. **Mutate** — rephrase, add context, restructure, compress, decompose, add examples, temperature sweep
2. **Evaluate** — run mutated prompt on benchmark
3. **Select** — Pareto-frontier for accuracy, latency, tokens, cost, robustness
4. **Replace** — promote winning prompt to production

## Hermes — Learning Loop Agent

After every wave:
1. **Analyze traces** — what worked, what failed, where did verification catch it?
2. **Crystallize** — write/update `SKILL.md` entries
3. **Write lesson** — append to `memory-bank/lessons/`
4. **Propose validator** — if a new failure mode was observed, propose FM + validator

## Bootstrap Rule
Self-improvement only runs when:
- All preflight checks pass
- The wave is marked SHIPPED
- At least one lesson was generated

## Safety
- GEPA mutations are sandboxed — never promoted without passing the full verification suite
- Hermes proposals are reviewed by the orchestrator, not auto-merged
