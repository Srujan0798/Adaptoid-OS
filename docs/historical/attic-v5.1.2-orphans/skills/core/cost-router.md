---
name: cost-router
version: "1.0.0"
description: Route tasks to the cheapest model that can handle them
verification_gates: [schema]
cost_estimate_usd: 0.01
capabilities:
  tools: [Read]
---

# Skill: Cost Router

## Purpose
Minimize cost without sacrificing quality. Use small models for simple tasks, large models for complex ones.

## Trigger
Before every LLM call.

## Rules
- Classification / extraction → small model (e.g., gpt-4o-mini)
- Code generation / reasoning → large model (e.g., gpt-4o, kimi-k2.6)
- Verification / cross-check → different model family (e.g., Claude for Kimi output)
- Never exceed `cost_cap_usd` in slash-command YAML.

## Output
Selected model + estimated cost.
