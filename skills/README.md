# Skills — Reusable Agent Capabilities

> Every skill is a contract: inputs, outputs, verification gates, cost ceiling.

## Structure

```
skills/
├── core/           — framework-agnostic capabilities
│   ├── intent-parse.md
│   ├── route-check.md
│   ├── evidence-collect.md
│   ├── cost-router.md
│   └── memory-write.md
└── domain/         — specialized capabilities
    ├── code-review.md
    ├── data-analysis.md
    ├── security-audit.md
    └── deploy-checklist.md
```

## Skill Format (USRI v1)

```yaml
skill:
  name: "route-check"
  version: "1.0.0"
  description: "Validate proposed DAG transitions against static map"
  verification_gates: [schema, evidence]
  cost_estimate_usd: 0.01
  capabilities:
    tools: [Read]
  example_prompt: |
    Check if transition from {{source}} to {{target}} is valid
    according to adaptoid.config.yaml dag_transitions.
```

## Rule
Every skill used in a project must have a USRI entry in `skills/` or `reference/ecosystem/skills-registry.md`.
