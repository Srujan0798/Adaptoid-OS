# Example: Production SaaS Project

## Brief
Build a multi-tenant ERP for a manufacturing SME.

## Archetype
`saas-product`

## Tier
T3

## Waves
1. Foundation — auth, tenant isolation, DB schema
2. Core modules — inventory, orders, invoicing
3. Integrations — Shopify, QuickBooks, shipping APIs
4. Polish — compliance, audit logs, performance

## Generated Structure
Full OS-Setup structure with:
- `docs/decisions/` (ADRs for every major choice)
- `orchestrator/memory/session/` (events.jsonl per wave)
- `validators/` (all 18 FMs active)
- `memory-bank/` (facts, lessons, decisions)

## Outcome
- 12 weeks to production
- Zero critical bugs in first 30 days
- FM-01 (state drift) caught by validate_state.sh before merge
