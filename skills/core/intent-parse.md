---
name: intent-parse
version: "1.0.0"
description: Parse natural language brief into structured ProjectIntent
verification_gates: [schema, evidence]
cost_estimate_usd: 0.05
capabilities:
  tools: [Read, Write]
  files:
    - PROJECT-INTENT.md
    - schemas/ProjectIntent.schema.json
---

# Skill: Intent Parse

## Purpose
Turn a vague project brief into a schema-validated `ProjectIntent`.

## Trigger
User says "I want to build X" or pastes a PDF brief.

## Steps
1. Read `schemas/ProjectIntent.schema.json`
2. Extract stakeholders, success criteria, constraints from brief.
3. Infer archetype and tier.
4. Write `PROJECT-INTENT.md` with YAML frontmatter.
5. Run `validators/check_intent.sh` to validate.

## Output
`PROJECT-INTENT.md` with all required fields populated.
