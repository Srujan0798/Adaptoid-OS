# Ecosystem — Coding Agents (the surfaces you work in)

> All of these speak MCP + the agentskills.io `SKILL.md` standard, so skills/config port across them. Pick by workflow, not lock-in.

## Tier 1 — mainstream
| Tool | What it is | Pick when | Source |
|---|---|---|---|
| **Claude Code** | Anthropic agentic CLI/IDE/desktop/web; Skills, sub-agents, hooks, background agents, routines, auto-memory | default orchestrator; deepest Skills+MCP | code.claude.com (corpus) |
| **Cursor** | AI IDE; Composer, background agents, rules, MCP, worktrees | GUI-first, parallel tasks | cursor.com (corpus) |
| **OpenAI Codex** | OpenAI coding agent; CLI + cloud + IDE; Rust core | OpenAI-stack shops | github.com/openai/codex (corpus) |
| **Gemini CLI** | Google's open-source terminal agent; Skills support | Gemini-stack | geminicli.com (corpus) |
| **GitHub Copilot** | In-editor; agent skills support | existing GH workflow | (corpus) |

## Tier 2 — open-source / power
| Tool | Edge | Source |
|---|---|---|
| **Cline** | VS Code, plan/act mode, MCP | github.com/cline/cline (corpus) |
| **Aider** | terminal, repomap, /architect, strong git | github.com/Aider-AI/aider (corpus) |
| **Goose** | Block/Linux-Fdn, Rust, 70+ MCP, extensible | block.github.io/goose (corpus) |
| **OpenHands** | cloud agents, scales to thousands, 65k★ | openhands.dev (corpus) |
| **Amp** | Sourcegraph frontier agent, threads/sharing | ampcode.com (corpus) |
| **Continue** | source-controlled AI checks enforceable in CI (.continue/checks/) | github.com/continuedev/continue (corpus) |
| **oh-my-pi** | ⚡ terminal agent, hash-anchored edits, LSP, subagents — trending this month | github (oh-my-pi) ⚡ |
| **Kiro** | AWS, spec-driven dev native | kiro.dev (corpus) |
| **Factory** | "Droids", IDE→CI/CD task delegation | factory.ai (corpus) |
| **Roo Code** | "AI dev team in editor", multi-step | roocode.com (corpus) |

## How OS-Setup uses this for YOUR project
- **Orchestrator** = Claude Code OR Kimi (your interchangeable pair). These are the brains.
- **Workers** = OpenCode CLI (your choice) or any Tier-2 agent in parallel windows. The hands.
- The generated project's `AGENTS.md`/`CLAUDE.md`/`.cursor/rules` are kept identical so any surface above can drive it.

## Selection hints
- Solo + deep Skills/MCP → Claude Code.
- Need GUI + parallel agents → Cursor or Emdash/Mux (worktree managers).
- OpenAI/Gemini org → Codex / Gemini CLI.
- Want CI-enforced agent checks → Continue (`.continue/checks/`).
- Terminal minimalist → Aider or oh-my-pi.

`verified: 2026-05 (⚡ items this burst; rest corpus)`
