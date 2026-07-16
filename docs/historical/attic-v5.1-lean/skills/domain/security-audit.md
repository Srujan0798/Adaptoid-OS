---
name: security-audit
version: "1.0.0"
description: Audit code and config for security vulnerabilities
verification_gates: [evidence, cross-check]
cost_estimate_usd: 0.20
capabilities:
  tools: [Read, Grep, Bash]
---

# Skill: Security Audit

## Purpose
Find vulnerabilities before they reach production.

## Trigger
Before any merge that touches auth, data access, or network.

## Checklist
- [ ] No hardcoded secrets
- [ ] Input validation on all endpoints
- [ ] SQL injection / XSS / CSRF checks
- [ ] Dependency vulnerabilities scanned
- [ ] OAP policy covers all new tools
- [ ] Evidence: scan output + PoC if applicable

## Output
`work/security.md`
