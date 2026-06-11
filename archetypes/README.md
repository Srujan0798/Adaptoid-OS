# Archetypes — The Adaptation Engine

> An archetype tells the orchestrator HOW to adapt OS-Setup to your specific kind of project. Load exactly ONE at project creation.

## Why archetypes
A 48-hour hackathon and a compliance-bound SaaS need opposite things. Forcing both into one template either over-builds the hackathon or under-builds the SaaS. The archetype encodes the right trade-offs per context.

## Each archetype file specifies
1. **Signals** — words/context that indicate this archetype
2. **Default tier** — T0–T4 (see `tiers/TIERS.md`)
3. **What to emphasize** — the few things that actually matter here
4. **What to skip** — what would be over-building for this context
5. **Folders included / omitted** — concrete structure delta
6. **Highest-risk failure modes** — which FM-NN validators to wire in first
7. **Definition of done** — what "shipped" means here
8. **Deliverables** — the final artifacts that matter

## The archetypes
| File | For |
|---|---|
| `hackathon.md` | 24–72h build, demo-day, speed > polish |
| `internship.md` | Mentor/professor-reviewed, report + presentation |
| `job-take-home.md` | Interview assessment, impress a reviewer |
| `research-ml.md` | Experiments, ablations, paper, reproducibility (DRO-FairML type) |
| `nlp-pipeline.md` | Extraction/OCR/NER document pipelines (rfq2boq type) |
| `internal-tool.md` | Team-internal app/ERP (swa-erp type) |
| `saas-product.md` | Multi-tenant, customers, production, compliance |
| `startup-mvp.md` | PMF-seeking, fast but real, founder-led |
| `cli-tool.md` | Library / CLI / package |
| `data-pipeline.md` | ETL / warehouse / analytics |
| `_TEMPLATE.md` | Add a new archetype |

## Selection
The orchestrator matches your brief+context to signals (see `00-INVOCATION.md`). On a tie or ambiguity it asks ONE multiple-choice question. Default if truly unknown: `internal-tool` at T1.

## Mixing
Real projects can blend (e.g., an internship building a research-ml pipeline). The orchestrator picks the PRIMARY archetype for structure and pulls specific emphases from a secondary. It states which it chose and why.
