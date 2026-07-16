# Host capabilities ↔ Adaptoid

> Coding hosts (Grok Build, Claude Code, Cursor, Codex, …) already ship workflow power.  
> Adaptoid is the **project harness** around them — not a second IDE.

## Map (use host feature → Adaptoid contract)

| Host feature (e.g. Grok Build) | What you do in the host | Adaptoid role |
|---|---|---|
| **Plan mode** | Propose approach before code | Must match `PROJECT-INTENT` + SDLC stage 1–3 |
| **Subagents** | Parallel test/research workers | Two-tier: orchestrator plans; workers stay in `writes` box |
| **Skills / slash commands** | Reusable workflows | Prefer host skills; project rules in AGENTS.md |
| **Hooks** | Scripts on edit/tool | Session-start orient (Claude); preflight before ship |
| **MCP servers** | Linear, Sentry, DB, … | List in `adaptoid.config.yaml` mcp_servers; OAP policy |
| **AGENTS.md** | Per-repo conventions | **Generated** cold-start (Core host emit) |
| **Memory** | Persist across sessions | **HANDOFF.md** + events (replace-not-append) |
| **Code search / multi-file edit** | Grep + refactor | Stay in task `writes` / `forbid` (FM-13) |
| **Git integration** | Stage/commit/PR | Evidence of “done”; publish_gate before push |
| **Deep reasoning** | Hard problems | Still require command evidence after thinking |
| **Web search** | Docs/packages | Prefer cited reality over memory |
| **Terminal / streaming** | Build & test live | Acceptance commands + preflight |
| **Headless / CI** | Script in pipelines | `validators/preflight.sh`, `make ship-check` |
| **Code review** | Line feedback pre-PR | `review-protocol` + status-claims check |
| **Sandbox** | Untrusted code | See `protocols/sandboxing.md` when needed |
| **Background tasks** | Long builds | Don’t claim done until exit code known |
| **Theming** | UX only | Out of harness scope |

## Efficiency rule

If the host already does it → **use the host**.  
Adaptoid only adds: **intent, handoff, SDLC gates, validators, multi-host emit**.

## One sentence

**Host = hands. Adaptoid = mission rules + proof of done.**
