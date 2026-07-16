---
name: evidence-collect
version: "1.0.0"
description: Bind every claim to a source the Adaptoid can re-fetch
verification_gates: [evidence]
cost_estimate_usd: 0.02
capabilities:
  tools: [Read, Bash]
---

# Skill: Evidence Collect

## Purpose
Ensure every claim has a source. No claim without evidence.

## Trigger
After any analysis, review, or verification step.

## Steps
1. For every claim, list the source (file, URL, command output).
2. If source is a command, run it and capture output.
3. If source is a file, record path + line number.
4. Store evidence in `memory-bank/evidence/`.

## Output
Evidence block appended to report.
