---
name: blast-radius-check
description: >
  Use before destructive, production, money, network-write, or MCP write actions. Classify r0–r5 and pause for human if high.
---

# Blast radius check

| Tier | Examples | Action |
|---|---|---|
| r0–r1 | read files, local edit | free |
| r2 | git commit local | free after tests |
| r3 | push, PR, network write | confirm |
| r4–r5 | prod deploy, secrets, money, `rm -rf` | **stop — human** |

MCP write/network is often **unsandboxed** (esp. Codex) → treat as ≥ r3.
See `protocols/blast-radius.md` + `policies/default.yaml`.
