# Archetype — Internal Tool / ERP

**Signals.** "internal tool", "ERP", "admin panel", "for our team", "operations", "workflow", "CRUD-heavy", a known set of internal users. (swa-erp type.)

**Default tier.** T1→T2. Real users (your team) but not external customers, so polish < reliability.

## Emphasize
- **Domain model first.** Get the entities + lifecycle right (e.g., project: Lead→Quote→…→Closed). Everything hangs off the data model.
- **RBAC from the start.** A handful of real roles; enforce server-side.
- **Audit log.** Every mutation: who/when/what-before/after. Internal tools need accountability.
- **Vertical slices.** Each wave ships a usable feature end-to-end (API + UI), not a horizontal layer nobody can use yet.
- **Boring, reliable stack.** Postgres + a mature web framework. No exotic tech.

## Skip (until needed)
- Multi-tenancy (single org install)
- Client/vendor portals (later wave)
- Mobile apps
- Marketing/GTM
- AI features inside the tool (keep it operational)

## Folders
- Full T1: `src/{backend,frontend}`, `tests/`, `.specify/`, `plan/`, `docs/`, `orchestrator/`.
- T2 adds: `docs/operational/` (runbook, observability) once it has daily users.
- `deliverables/` only if there's a report/handoff requirement.

## Highest-risk failure modes
- **FM-01 state drift** — EXECUTION.md duplicate-wave bug appeared HERE (swa-erp). `validate_state.sh` blocking.
- **FM-13 parallel collisions** — multi-worker waves editing shared models; disjoint write sets enforced at dispatch.
- **FM-06 config revert** — DB URL / auth settings asserted.
- **FM-04 context bloat** — keep CLAUDE.md short; the apparatus is large, load lazily.

## Definition of done (per wave)
- The wave's feature works end-to-end for a real user role
- `pytest tests/wave-N/` green; CI green
- Lifecycle/permissions enforced server-side
- EXECUTION.md has exactly one row per wave with the commit hash

## Deliverables
- The running tool (docker-compose up)
- Per-wave demo (a user flow that works)
- Runbook for whoever operates it
