# Host capabilities matrix (mid-2026)

> Mission law is host-agnostic. **Enforcement depth is not.**  
> Stage activation rules: **`SHIP-SYSTEM.md`**. Proceeding style: **`HOST-OPERATING-PLAYBOOK.md`**.

## Portable layers (all hosts)

| Layer | Path / standard | Load |
|---|---|---|
| Project law | `AGENTS.md` ([agents.md](https://agents.md/)) | Every session |
| Procedures | `.agents/skills/*/SKILL.md` ([agentskills.io](https://agentskills.io)) | On demand |
| External tools | MCP (allowlisted in config) | When needed |
| Evidence gates | `orchestrator/scripts/preflight.sh` | Before done |

## Host × capability

| Capability | Claude Code | Cursor | Codex | Grok Build | Adaptoid rule |
|---|---|---|---|---|---|
| Project law | `CLAUDE.md` + AGENTS | `.mdc` + AGENTS | Nested AGENTS | AGENTS + Claude-compat | Always emit **AGENTS.md**; dual-emit host native |
| Plan mode | ✓ | ~ Agent planning | ~ Goal/plan | ✓ plan→approve | **Mandatory** SDLC 1–3 |
| Subagents | ✓ + worktrees | ~ background | ✓ | ✓ parallel | Research/test; disjoint writes |
| Git worktrees | ✓ CLI/hooks | manual | ✓ desktop | ✓ | Parallel risk → worktree (FM-13) |
| Agent Skills | ✓ `.claude/skills` | ✓ | ✓ | ✓ + Claude skills | Prefer `.agents/skills/` |
| Hooks (hard) | ✓✓ PreToolUse… | soft rules | ✓ | ✓ | SessionStart + preflight; soft ≠ hard |
| Sandbox | OS/perms | local machine | **shell yes; MCP no** | local-first | MCP write ≥ blast-radius r3 |
| MCP | ✓ | ✓ | STDIO/HTTP/OAuth | ✓ | Allowlist only; pin versions |
| Headless/CI | `claude -p` | limited | CLI + Actions | `grok -p` | Stage 6 preflight in CI |

## Soft vs hard (critical)

| Control | Soft (may ignore) | Hard (always fires) |
|---|---|---|
| Cursor `.mdc` / long AGENTS prose | ✓ | — |
| Claude/Codex/Grok hooks | — | ✓ when configured |
| Adaptoid validators / preflight | — | ✓ **source of ship truth** |

**Never** treat rules text as sufficient for secrets, prod, or money — require hooks + human + preflight.

## Skills vs AGENTS

| File | Job |
|---|---|
| `AGENTS.md` | Short always-on law (build/test/style/secrets) |
| `SKILL.md` | How-to procedures loaded when relevant |
| `SHIP-SYSTEM.md` | Which stage needs which tool + evidence |

Keep AGENTS thin (Codex ~32 KiB budget). Push procedures into skills.
