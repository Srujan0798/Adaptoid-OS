# Hidden Gems Protocol

> Discover, evaluate, and integrate high-leverage but under-hyped tools and patterns.

## Purpose

Systematically scan the agentic-AI ecosystem for lesser-known tools, SDKs, and patterns, evaluate them against Adaptoid criteria, and add the winners to the ecosystem catalog without letting hype drive the stack.

## Evaluation criteria (score 1–5 each)

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| **Harness fit** | Adds complexity with no verification gain | Improves one of speed / safety / verifiability | Directly improves safety, speed, AND verifiability |
| **Verifiability** | No reproducible demo or eval | Core claim reproducible from docs | Core claim has an automated eval in `tests/evals/` |
| **Documentation quality** | Sparse / marketing-only | Solid docs + examples | Docs + examples + architecture + failure modes |
| **Active maintenance** | Dormant / deprecated | Active, single maintainer | Active, multiple maintainers, clear roadmap |
| **Differentiation** | Incremental clone of known tool | Meaningful niche improvement | Step-change for a real Adaptoid workflow |

**Total score** = sum of the five criteria (range 5–25). A candidate must score **≥ 15** and **≥ 4 on Harness fit** to be cataloged.

## Process

1. **Scan** — monitor repositories, papers, release notes, and practitioner notes.
2. **Reproduce** — run the tool's core claim in a sandbox under `examples/scratchpad/`.
3. **Score** — fill the 1–5 rubric; record evidence and a reproducible command.
4. **Catalog** — add to `reference/ecosystem/hidden-gems.md` with `last-verified:` frontmatter.
5. **Refresh** — re-run `STALE_CHECK.sh` monthly; archive entries that fall below threshold.

## Required `PROJECT-INTENT.md` / `adaptoid.config.yaml` fields

```yaml
super_adaptoid:
  loaded:
    - hidden-gems
  hidden_gems:
    enabled: false
    catalog: reference/ecosystem/hidden-gems.md
    scratchpad: examples/scratchpad/
    stale_days: 90
    minimum_score: 15
    required_harness_fit: 4
```

## Failure modes addressed

- **FM-06 — Config Revert:** tool choices are declared in config; no silent stack changes.
- **FM-12 — Stale Derived Docs:** catalog entries carry `last-verified:` and are checked by `STALE_CHECK.sh`.
- **FM-15 — Context Compaction:** evaluations produce compact ADRs; full evidence stays in `examples/scratchpad/`.

## Relationship to the Kernel

Applies `kernel/PRINCIPLES.md` (law 2 — simplicity first; law 5 — evidence) and `kernel/ANTI-HALLUCINATION.md`.

## Validator

```bash
[ -f reference/ecosystem/hidden-gems.md ] || echo "Note: hidden-gems catalog not initialized"
bash reference/ecosystem/STALE_CHECK.sh 90 reference/ecosystem/
bash validators/check_references.sh
bash validators/context_budget.sh
bash validators/dogfood.sh
```
