# Archetype — SaaS Product

**Signals.** "customers", "multi-tenant", "subscription/billing", "sign up", "production", "uptime", "compliance", external paying users.

**Default tier.** T3 (T4 if pre-PMF startup — see `startup-mvp.md`).

## Emphasize
- **Multi-tenancy + isolation** from the data model up (tenant_id everywhere, row-level security).
- **Auth done right.** Sessions/JWT, password reset, MFA-ready, rate limiting, account lockout.
- **Observability.** Logs, metrics, traces, error tracking, dashboards, alerts (SLOs).
- **Compliance** per domain: GDPR/DPDP/HIPAA/SOC2 — data deletion, audit trails, DPA.
- **Reliability.** Health checks, graceful degradation, backups, incident playbook, zero-downtime deploys.
- **Billing correctness.** Money as decimal, idempotent webhooks, reconciliation.

## Skip
- Nothing structural — this is the heaviest archetype. But still: no speculative features beyond the roadmap (FM-08).

## Folders
- Full T3: multi-Dockerfile, `docker-compose.{dev,prod}.yml`, `docs/operational/` (full), `docs/compliance/`, `prometheus.yml`, `.github/workflows/{ci,test,security,perf_regression,docs_sync,audit}.yml`, `schema/db_struct.sql`, `Procfile`.
- `evals/` if any AI features.

## Highest-risk failure modes (all of them, but especially)
- **FM-07 embarrassing artifacts / secrets** — a leaked key in a customer product is an incident. `publish_gate.sh` + gitleaks hard-block.
- **FM-11 silent failures** — a swallowed error in billing/auth = lost money or security hole.
- **FM-02 stale process / FM-13 collisions** — in prod-adjacent work, controlled.
- **FM-01 state drift / FM-12 stale docs** — runbooks must be current or on-call fails.

## Definition of done (per wave)
- Feature works for a tenant; isolation verified (tenant A can't see tenant B)
- Security review passed (auth, injection, secrets)
- Observability wired (logs/metrics/alerts for the new surface)
- Perf budget met; CI incl. security + perf green
- Rollback plan documented

## Deliverables
- Running multi-tenant product
- Operational runbook, incident playbook, SLOs
- Compliance docs current
