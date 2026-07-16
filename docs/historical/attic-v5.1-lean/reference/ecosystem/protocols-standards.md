# Ecosystem — Protocols & Standards (the universal layer — always relevant)

> These are the open standards every modern agent tool supports. Building on them = no lock-in, max portability. ALWAYS pull this file at setup.

## MCP — Model Context Protocol
Agent ↔ tools/data. The USB-C of agent tooling.
- Supported by: Claude, ChatGPT, Cursor, VS Code, JetBrains, Codex, Cline, Goose, ADK — everyone.
- 210+ tools in the wild.
- In OS-Setup projects: declared in `mcp.json`; gated by `orchestrator/hooks/mcp-security-gate.sh`.
- Common servers: filesystem, git, tavily (search), context7 (docs), sequential-thinking, playwright (browser), serena (code).
- `modelcontextprotocol.io` (corpus)

## A2A — Agent-to-Agent Protocol
Agent ↔ agent. Google + 50+ partners; ~24k★.
- Complements MCP (MCP = agent→tool; A2A = agent↔agent).
- Use when agents from DIFFERENT providers must coordinate.
- Built into Google ADK.
- `github.com/google/A2A` (corpus)

## agentskills.io — the Skill standard
The `SKILL.md` format (Anthropic-originated, now open). 40+ tools compatible.
- Folder = `SKILL.md` (YAML frontmatter: name, description, license, compatibility, metadata, allowed-tools) + optional `scripts/ references/ assets/`.
- Progressive disclosure: metadata (~100 tok) → full instructions (<5k) → resources on demand.
- 2026 additions: `allowed-tools`, `invocation` (claude/user/both), `subagent: true`.
- Commands unified into skills: `.claude/commands/X.md` and `.claude/skills/X/SKILL.md` both make `/X`.
- `agentskills.io/specification` (corpus)

## AGENTS.md / CLAUDE.md — the config standard
One markdown file, auto-loaded by every IDE (Claude Code, Cursor, Codex, Continue, Gemini CLI...).
- Write once; alias across (`CLAUDE.md` = `KIMI.md` = `AGENTS.md` = `.cursor/rules`).
- Boris rule: keep it SHORT ("would removing this cause a mistake?").
- In OS-Setup: the kernel laws are embedded here; detail goes to lazy-loaded `protocols/`.

## Why this matters for "beating everyone"
Build on standards → your project works in every tool, inherits every new MCP server and skill the community ships, and never needs a migration. Proprietary glue is the thing that makes projects rot. OS-Setup is standards-native by default.

`verified: 2026-05 (corpus, all stable standards)`
