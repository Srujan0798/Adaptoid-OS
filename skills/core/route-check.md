---
name: route-check
version: "1.0.0"
description: Validate proposed DAG transitions against static map
verification_gates: [schema, evidence]
cost_estimate_usd: 0.01
capabilities:
  tools: [Read]
  files:
    - adaptoid.config.yaml
---

# Skill: Route Check

## Purpose
Prevent wrong-route errors (FM-16) by validating every transition before execution.

## Trigger
Before any state transition or tool dispatch.

## Steps
1. Read `adaptoid.config.yaml` `dag_transitions`.
2. Check if `source → target` is in `allowed_next`.
3. Check retry count < `max_retries`.
4. If invalid, emit `WRONG_ROUTE_BLOCKED` event and halt.

## Output
`ALLOW` or `BLOCK` with reason.
