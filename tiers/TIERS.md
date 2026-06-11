# Tiers — Sizing the Build

> Pick the smallest tier that fits. Bigger tier = more files = more discipline = more overhead. Additive: T4 ⊇ T3 ⊇ T2 ⊇ T1 ⊇ T0.

| Tier | Use when | Adds |
|---|---|---|
| **T0 — Minimum** | Throwaway script, weekend hack, spike | CLAUDE.md + work/ + plan/PRD (one page) + src/ + a smoke test. ~10 files. |
| **T1 — Standard** | Internal tool, MVP, small team (DEFAULT) | Full kernel-driven structure: orchestrator/, .specify/, plan/, docs/, tests/ taxonomy, evals/, validators/, CI (ci+test+security). ~90 files. |
| **T2 — Production** | Real users, on-call, observability matters | + docs/operational/ (observability, SLOs, incident playbook), docs/audits/<date>/, HALL_OF_SHAME.md, BACKLOG.md, perf_regression + docs_sync CI, prometheus.yml, docker-compose.dev.yml, workflows/ + memory/states/. |
| **T3 — Enterprise/Compliance** | Regulated (GDPR/DPDP/HIPAA/SOC2), audited | + docs/compliance/ + certificates, multi-Dockerfile split, docker-compose.prod.yml, audit.yml, schema/db_struct.sql, secrets management. |
| **T4 — Startup/Customer-facing** | Seeking PMF, external customers | + STARTUP_ROADMAP.md, ROADMAP.md, docs/business/ (STAKEHOLDER_UPDATE, pricing, demo script), Procfile, deliverables/, analytics wiring. |

## How tier is chosen
1. The archetype suggests a default tier.
2. The user's context (deadline, audience) can bump it up or down.
3. When unsure, go LOWER. You can always add T2+ folders later; you can't easily un-bloat.

## Tier-down rule
If the project stalls under its own weight (too many docs to maintain, too much ceremony), DROP a tier. The structure serves shipping, not the reverse.

## What NEVER changes across tiers (always present)
- The kernel (PRINCIPLES, TWO-TIER, ANTI-HALLUCINATION) baked into CLAUDE.md/KIMI.md
- `work/` bridge (task + report templates)
- At least the fast `validators/preflight.sh`
- HANDOFF.md (even T0 benefits from a 5-line "where we are")
