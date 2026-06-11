# Skills Registry

> Universal Skill Registry Interface (USRI) for Adaptoid OS.

## Schema (USRI v1)

```yaml
skill:
  name: "string"
  version: "semantic"
  description: "string"
  author: "string"
  tags: ["string"]
  verification_gates: ["schema", "evidence", "cross-check"]
  capabilities:
    tools: ["Read", "Write", "Bash"]
    mcp_servers: ["filesystem", "git"]
  cost_estimate_usd: 0.10
  example_prompt: "string"
```

## Sources
- **OpenClaw ecosystem:** 5,700+ skills
- **Skills.sh registry:** 85,000+ signed portable bundles
- **Adaptoid core:** 20+ curated skills in `skills/`

## Rule
Every skill used in a project must have a USRI entry. Custom skills are first-class but must be documented.
