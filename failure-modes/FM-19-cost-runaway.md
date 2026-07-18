# FM-19 — Cost / token runaway

**Symptom.** Session burns budget on loops, huge context pastes, multi-agent crews for tiny work, or endless tool retries. “Still working” with no outcome.

**Root cause.** No cost ceiling; progressive disclosure ignored; subagents spawned for greenfield; always-on mega-prompts.

**Prevention.**
- Cost ceiling in AGENTS / config; stop and ask when approaching it.
- Skills on demand (`.agents/skills`), thin AGENTS.md.
- Subagents only for large explore / parallel tests — not empty greenfield.
- One outcome per turn; verify-before-done ends the loop.

**Detection.** Human budget alarms; session token logs; “no acceptance progress after N turns.”

**Recovery.** Compact: rewrite HANDOFF, drop chat history dependency, resume from files only.
