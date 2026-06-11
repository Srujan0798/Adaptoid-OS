---
name: code-review
version: "1.0.0"
description: Review code for correctness, style, security, and performance
verification_gates: [evidence, cross-check]
cost_estimate_usd: 0.10
capabilities:
  tools: [Read, Grep]
---

# Skill: Code Review

## Purpose
Catch bugs, style violations, security issues, and performance anti-patterns.

## Trigger
Worker submits code in a report.

## Checklist
- [ ] Types / lint pass
- [ ] No silent failures (bare except, swallowed errors)
- [ ] No secrets committed
- [ ] Blast radius checked (remote calls, file deletions)
- [ ] Tests included and passing
- [ ] Evidence provided (test output, lint output)

## Output
`work/reviews/wave-*/<task>.review.md`
