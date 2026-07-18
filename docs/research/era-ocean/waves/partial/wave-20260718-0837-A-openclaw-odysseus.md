# ERA-OCEAN Partial A — OpenClaw + Odysseus + OpenCode

**Wave:** `wave-20260718-0837-A`  
**Agent:** A (local/self-hosted agent harnesses)  
**Status:** INCOMPLETE (web + GitHub primary; no local installs, no source deep-read of full trees)  
**Written:** 2026-07-18  
**Scope:** OpenClaw, Odysseus, OpenCode as local/self-hosted agent harnesses — architecture, skills/MCP/memory, vs Claude Code coding harness, elite concepts for portable mission OS (Adaptoid).

---

## 0. Honesty / coverage gaps

| Gap | Why it matters |
|-----|----------------|
| No local `docker compose` / `openclaw onboard` / `opencode` run in this wave | Runtime behavior, latency, failure modes, actual skill injection quality unmeasured |
| Odysseus internals only via README, ROADMAP, THREAT_MODEL, secondary reviews | Agent loop, exact OpenCode wrap, skill store layout not fully verified from code |
| OpenClaw docs are excellent but huge (70k+ commits; monorepo) | Many subsystems (ACPX, canvas, nodes, cron, plugin hooks) only sampled |
| OpenCode monorepo packages/ not fully enumerated | Desktop app, console, SDK details thin |
| “Hermes” appears in comparisons as sibling to OpenClaw | Out of primary trio; cited only where sources pair it |
| Star counts / maturity numbers from secondary sources may lag | Treat popularity stats as soft signals |
| Claude Code comparison is from public product shape + OpenCode compatibility surface, not Anthropic internal harness docs | Not a reverse-engineer of Claude Code |

**What is solid:** official READMEs, docs sites, VISION, THREAT_MODEL, ROADMAP, architecture pages for Gateway/agent/skills/MCP, OpenCode agents/skills/MCP/rules docs, independent writeups (Pinokio, gavinj.net).

---

## 1. Positioning map (three different species)

| Dimension | **OpenClaw** | **Odysseus** | **OpenCode** |
|-----------|--------------|--------------|--------------|
| **One-liner** | Personal always-on assistant Gateway | Self-hosted multi-app AI **workspace** | Open-source **coding agent** (TUI/desktop/IDE) |
| **Primary surface** | Messaging channels + CLI + companion apps | Browser UI / PWA (`:7000`) | Terminal TUI, desktop app, VS Code SDK |
| **Interaction** | Async + sync; cron, heartbeats, DMs | Sync sessions you open | Sync coding sessions in a repo |
| **Product is…** | The **agent loop** + channel reach | Bundled apps (chat, docs, email, research, cookbook…) | Build/plan coding agents + tools |
| **License (reported)** | MIT | AGPL-3.0-or-later | MIT |
| **Runtime home** | Node Gateway daemon (`~/.openclaw`) | Docker-first FastAPI stack + services | Bun/Node CLI + local state |
| **Model posture** | Consumer of any provider endpoint | **Manages** local serving (Cookbook) + APIs | Consumer; multi-provider; “Zen” curated list |
| **Closest Claude product** | “Personal Claude” via WhatsApp/Telegram — **not** Claude Code | Claude Desktop / Codex-style **workspace UI**, local-first | **Claude Code** (open alternative) |
| **Repo (primary)** | https://github.com/openclaw/openclaw | https://github.com/pewdiepie-archdaemon/odysseus (also `odysseus-dev/odysseus`) | https://github.com/anomalyco/opencode |
| **Docs** | https://docs.openclaw.ai | README + `docs/setup.md` + GitHub pages | https://opencode.ai/docs |

**Key ecosystem relation (from Pinokio comparison + Odysseus feature list):**  
Odysseus is described as wrapping **OpenCode** as its coding/agent component inside a larger workspace — agent core is a *module*, not the whole product. OpenClaw is the opposite: the agent loop *is* the product; apps emerge via skills/MCP/channels.

---

## 2. OpenClaw — architecture

### 2.1 Control plane: single Gateway

- Long-lived **Gateway** owns messaging surfaces (WhatsApp/Baileys, Telegram/grammY, Slack, Discord, Signal, iMessage, WebChat, plus many more listed in README).
- Control clients (macOS app, CLI, web UI, automations) connect over **WebSocket** (default `127.0.0.1:18789`).
- **Nodes** (macOS/iOS/Android/headless) also WS with `role: node`, device pairing, explicit caps/commands (canvas, camera, screen, location…).
- One Gateway per host for provider sessions (e.g. one Baileys session).
- Canvas host served on same port under `/__openclaw__/canvas/` and A2UI paths.
- Install path: `npm i -g openclaw` → `openclaw onboard --install-daemon` (launchd/systemd).

### 2.2 Agent runtime

- **Embedded agent runtime** (not merely shelling out): model discovery, tool wiring, prompt assembly, session store, channel delivery share one surface.
- Workspace is required `cwd` (`agents.defaults.workspace`, often `~/.openclaw/workspace`).
- Bootstrap files injected into system prompt “Project Context” on first turn of a session:

  | File | Role |
  |------|------|
  | `AGENTS.md` | Operating instructions + “memory” |
  | `SOUL.md` | Persona, boundaries, tone |
  | `TOOLS.md` | User tool conventions (does **not** enable tools) |
  | `IDENTITY.md` | Name/vibe/emoji |
  | `USER.md` | User profile |
  | `HEARTBEAT.md` | Heartbeat-specific |
  | `BOOTSTRAP.md` | One-time first-run ritual (deleted after) |
  | `MEMORY.md` | Root long-term memory if present |

- Sessions: per-agent SQLite `~/.openclaw/agents/<agentId>/agent/openclaw-agent.sqlite`; setup attestation in shared `~/.openclaw/state/openclaw.sqlite`.
- Multi-agent routing: channels/accounts/peers → isolated agents (workspaces + sessions).
- **Queue / steer:** mid-run messages can steer after current tool batch (`/queue steer` default); followup/collect/interrupt modes exist.
- **Sandbox:** host tools full power for `main` session by default; `agents.defaults.sandbox.mode: "non-main"` sandboxes non-main (Docker default; SSH/OpenShell backends). Group safety defaults deny browser/canvas/nodes/cron for sandboxed sessions.
- **DM security:** pairing codes + allowlists; `openclaw doctor` surfaces risky DM policies. Explicit opt-in for open DMs.
- Explicitly **rejects** “manager-of-managers / nested planner trees as default architecture” and heavy orchestration layers that duplicate agent/tool infra (VISION.md guardrail).

### 2.3 Skills / MCP / memory

**Skills**

- AgentSkills-shaped: directory + `SKILL.md` (YAML frontmatter + markdown body).
- Precedence: workspace `skills/` > `.agents/skills` > `~/.agents/skills` > `~/.openclaw/skills` > bundled > plugin/extra dirs.
- Gating via `metadata.openclaw.requires` (bins, env, config), OS filters, installer specs (brew/node/go/uv/download).
- **Snapshots** at session start; watcher can refresh mid-session; token budget for skills prompt block.
- **ClawHub** registry (`clawhub.ai`): install/update/verify; Skill Workshop queues agent-drafted skill proposals for human approval.
- Per-agent skill allowlists (`agents.list[].skills` replaces defaults entirely when set).
- Bundled `coding-agent` skill is **opt-in** and can drive Claude/Codex/OpenCode CLIs when present.
- Codex CLI skills are *not* auto-roots; migrate via `openclaw migrate codex`.

**MCP**

- Dual role:
  1. **`openclaw mcp serve`** — OpenClaw *as* MCP server: exposes Gateway channel conversations (list/read/send/events/approvals) to Codex, Claude Code, etc.
  2. **Client registry** — `mcp.servers` in OpenClaw config; project into embedded runtime and other adapters; tool filters, OAuth, probe/doctor.
- Goal: pragmatic MCP without duplicating plugin/ClawHub/ACP paths.
- Session-scoped bundled MCP runtimes reaped after idle TTL; one-shot runs clean up stdio trees.

**Memory**

- File/markdown workspace memory (`MEMORY.md`, `AGENTS.md` as operating memory).
- **Plugin slot:** only one memory plugin active at a time; multiple options ship; converging on one default path (VISION).
- Secondary sources: skills can be auto-written from experience (“learns you over time”) — treat as product narrative until plugin code audited.
- Channel + cron + heartbeats give *continuity* that pure coding harnesses lack.

### 2.4 Plugin model (elite)

- Core stays lean; capabilities as plugins.
- Prefer **bundle-style** plugins (skills, MCP, config) over code plugins when possible — smaller interface, better security boundary.
- Code plugins for runtime hooks, providers, channels, tools.
- Plugin hooks into agent loop: `before_model_resolve`, `before_prompt_build`, `before_tool_call` / `after_tool_call`, compaction, message send/receive, session lifecycle, install gates, etc.
- Terminal block semantics for tool/message guards.

### 2.5 Ops / identity

- `openclaw doctor --fix` for config migrations (no silent old-key aliases).
- Chat operator commands: `/status`, `/new`, `/reset`, `/compact`, `/think`, `/verbose`, `/trace`, `/usage`, `/restart`, `/activation`.
- Remote: Tailscale preferred; SSH tunnel alternative; pairing for non-loopback.

---

## 3. Odysseus — architecture

### 3.1 What it is

- Self-hosted **AI workspace**: chat, agents, deep research, documents, email (IMAP/SMTP), notes/tasks/calendar (CalDAV), gallery, compare models, Cookbook (hardware-aware model recommend/download/serve).
- **Docker-first:** `docker compose up -d --build` → `http://localhost:7000`; first admin password in logs.
- Stack (from tree + threat model + Pinokio): FastAPI app (`app.py`), **ChromaDB**, **SearXNG**, **ntfy**, `mcp_servers/`, services/integrations, Python + JS frontend.
- License: **AGPL-3.0-or-later** (copyleft — important for Adaptoid packaging/forks).
- Positioning vs OpenClaw (Pinokio): Odysseus = **sync dashboard you open**; OpenClaw = **async daemon that reaches you**. Odysseus competes more with **Claude Desktop / Codex UI**, not with OpenClaw’s channel daemon niche.

### 3.2 Agent / tools

- Features claim: local/API models, **tools, MCP, files, shell, skills, memory**.
- Pinokio: agent core **wraps OpenCode** — coding agent is a component inside the suite.
- Threat model roles:

  | Capability | Admin | Non-admin |
  |------------|-------|-----------|
  | Chat, browser, docs, research, memory, images | yes | yes |
  | Shell, files, email, MCP tools, calendar, vault, model serving | yes | no |

- Internal tool loopback: random `INTERNAL_TOOL_TOKEN`, `internal-tool` reserved user, agent tools hit admin-gated HTTP routes in-process after `owner_is_admin_or_single_user`.
- **Prompt injection:** `untrusted_context_message` wraps web, email, memories, skills, notes as **data** not system instructions; system preamble policy. ROADMAP still flags skill/tool injection audit as high priority.
- Known gaps (THREAT_MODEL): no shell/filesystem sandbox; SSRF via chat `base_url` (PR noted); coarse token scopes.

### 3.3 Skills / MCP / memory

- Skills: SKILL.md-style (aligned with ecosystem); ROADMAP: agent mode **context bloat** from tools + skills + memory + documents hurts small local models — needs slimmer prompts / tool selection.
- Memory: **ChromaDB** vector store (workspace memory), plus files; treated as untrusted for injection.
- MCP: `mcp_servers/` in repo; MCP tools admin-only (`mcp__*` prefix blocked for non-admins).
- Deep Research: multi-step research with self-hosted SearXNG (no third-party search API required if local models used) — strong local-first narrative.
- Cookbook: scans hardware, recommends models, download/serve via vLLM/llama.cpp (and roadmap SGLang) — **model ops as product surface**.

### 3.4 Maturity / UX signal (secondary)

- ROADMAP is frank: “I don’t know what I’m doing, help”; high priority on bugs, install matrix, Cookbook reliability, email performance, provider probing.
- Review (gavinj.net): best-in-class **web workspace UI** and model compare/cookbook; weaker **personable agent identity**, Gmail-depth integrations, channel presence vs Hermes/OpenClaw-class daemons. Suggests hybrid: Odysseus workbench + always-on assistant layer.

---

## 4. OpenCode — architecture

### 4.1 What it is

- Open-source **AI coding agent** (Anomaly / opencode.ai): TUI-first, also desktop app (beta) and VS Code SDK.
- Install: `curl -fsSL https://opencode.ai/install | bash` or npm `opencode-ai`, brew, nix, docker, etc.
- Project init: `opencode` in repo → `/init` → generates **`AGENTS.md`** (commit to git).
- Provider-agnostic; OpenCode Zen curated models; `/connect` for keys.
- Undo/redo of agent file changes; optional `/share` conversations.
- Claude Code compatibility: reads `CLAUDE.md`, `.claude/skills` unless `OPENCODE_DISABLE_CLAUDE_CODE*`.

### 4.2 Agents (primary + subagent)

| Agent | Mode | Role |
|-------|------|------|
| **build** | primary (default) | Full tools — implementation |
| **plan** | primary | Analysis; edits/bash default **ask** (restricted) |
| **general** | subagent | Multi-step research/tasks; full tools except todo |
| **explore** | subagent | Fast read-only codebase search |
| **scout** | subagent | External docs / dependency repos in managed cache |
| compaction / title / summary | hidden primary | System utilities |

- Switch primary with **Tab**; invoke subagents via `@` or Task tool.
- Child sessions navigable (parent/child keybinds).
- Config: `opencode.json` and/or markdown agents in `~/.config/opencode/agents/` or `.opencode/agents/`.
- Per-agent: model, prompt, temperature, **steps** (max iterations cost ceiling), color, mode, permissions.
- **Permissions model:** `allow` | `ask` | `deny` per tool class (`edit`, `bash`, `skill`, `task`, MCP globs, etc.); bash command globs; last matching rule wins.
- `permission.task` controls which subagents an agent may spawn.

### 4.3 Skills / MCP / memory (coding-shaped)

**Skills**

- On-demand via native **`skill` tool** — agents see name/description catalog; load full SKILL.md when needed (context thrift).
- Discovery paths: `.opencode/skills`, `~/.config/opencode/skills`, Claude-compatible `.claude/skills`, `.agents/skills` (project + global).
- Frontmatter: name, description, optional license/compatibility/metadata.
- Permission patterns on skill tool (`allow`/`deny`/`ask`).

**MCP**

- First-class in `opencode.json` `mcp`: **local** (command array + env) and **remote** (URL + headers + OAuth, DCR).
- Tools merge with built-ins; can disable globally or per-agent via tool globs (`mymcp_*`).
- Explicit warning: MCP **eats context** — be selective (GitHub MCP called out as heavy).
- CLI: `opencode mcp auth|list|logout|debug`.

**Rules / “memory”**

- **`AGENTS.md`** project + global (`~/.config/opencode/AGENTS.md`); not long-lived personal memory like OpenClaw `MEMORY.md` + channels.
- `instructions` in config: extra files, globs, remote URLs.
- Session undo/redo and compaction agents are session-scoped, not life-long personal graph.

### 4.4 Relation to Claude Code

OpenCode is the **closest open harness twin** to Claude Code among the three:

| Concern | Claude Code (product shape) | OpenCode |
|---------|----------------------------|----------|
| Primary job | Repo coding agent | Same |
| Plan vs build | Plan mode / restricted write | Explicit **plan** primary agent + permissions |
| Project rules | `CLAUDE.md` / rules | `AGENTS.md` + Claude fallbacks |
| Skills | Agent skills directories | SKILL.md multi-root + skill tool |
| MCP | Client | Client (local/remote/OAuth) |
| Subagents | Task-style specialization | general/explore/scout + custom |
| Host lock-in | Anthropic product + models (with flexibility) | Multi-provider, open source |
| Persistence | Session + project rules | Same class; no multi-channel personal OS |

OpenClaw/Odysseus **differ from Claude Code** more deeply: they are not IDE/TUI coding products first — they are **personal OS / workspace OS**.

---

## 5. Cross-cut comparison (harness traits)

| Trait | OpenClaw | Odysseus | OpenCode | Claude Code (ref) |
|-------|----------|----------|----------|-------------------|
| **Host** | Own devices + Gateway | Self-host Docker/native | Dev machine TUI/desktop | Cloud product + local CLI |
| **Blast radius default** | Full host for main; sandbox non-main | Admin = shell/files; no OS sandbox yet | Permission ask/allow/deny | Approval + project sandbox norms |
| **Skill packaging** | SKILL.md + ClawHub + Workshop | SKILL.md + workspace | SKILL.md on-demand skill tool | Skills ecosystem |
| **MCP** | Server *and* client registry | Client (admin tools) | Client first-class | Client |
| **Memory** | Workspace MD + memory plugin slot | ChromaDB + files | AGENTS.md / session | Project rules / session |
| **Channels** | First-class (20+ apps) | Workspace-centric; mobile PWA | None (coding surface) | None |
| **Model ops** | Point at endpoints | Cookbook + serve | Point at providers | Anthropic-centric + options |
| **Identity** | SOUL/IDENTITY/USER ritual | Weaker identity per reviews | Agent personas via config | Product persona |
| **Copyleft risk** | MIT | **AGPL** | MIT | Proprietary |
| **SDLC / gates** | Doctor, hooks, exec approvals | Threat model + role gates | Plan mode, steps, permissions | Plan + permissions |

---

## 6. Elite concepts for portable mission OS (Adaptoid)

Extracted patterns worth **stealing as design law**, not reimplementing as clones:

### A. Surfaces vs harness (product species clarity)

1. **Three product species, one mission OS glue:**  
   - *Channel daemon* (OpenClaw) = ambient Hands.  
   - *Workspace suite* (Odysseus) = human mission cockpit.  
   - *Coding harness* (OpenCode/Claude Code) = repo-scoped implementer.  
   Adaptoid should **compose** these roles via contracts, not become a 4th monolithic UI.

2. **Gateway as single control plane** — one long-lived process owns sessions, tools, events, health; clients are thin. Portable OS: define a **session/event protocol** independent of model vendor.

3. **Nodes with caps** — devices declare role + allowed commands; pairing is device-identity based. Maps to Adaptoid blast-radius + remote node policies.

### B. Skills as portable mission units

4. **SKILL.md as the interchange format** (AgentSkills) — OpenClaw, OpenCode, Odysseus all converge. Adaptoid skills should ship as `SKILL.md` trees loadable by any host that speaks AgentSkills.

5. **Precedence stack** — workspace > project agent > personal > managed > bundled. Matches Adaptoid kit vs generated project vs user overrides.

6. **Gating skills on reality** — require bins/env/config before injection; don’t advertise skills that can’t run. Adaptoid: skill eligibility = tool policy ∩ environment.

7. **Skill snapshots + watchers** — freeze skill set per session for determinism; refresh on explicit events. Prevents mid-turn skill thrash.

8. **Skill Workshop (human gate on agent-authored skills)** — agents propose reusable skills; humans approve. Aligns with Adaptoid “never silent compound” / proof of done.

9. **Registry + verify envelope** (ClawHub pattern) — install/update/verify provenance; install policy command fail-closed. Portable OS needs **skill trust** not just skill files.

10. **On-demand skill load (OpenCode)** vs **prompt catalog (OpenClaw)** — dual modes: token-cheap lazy load for coding; always-on catalog for personal assistant. Adaptoid: lazy for large libraries; pin critical mission skills.

### C. Memory that is not a RAG gimmick

11. **Bootstrap ritual files** (SOUL, IDENTITY, USER, BOOTSTRAP) — identity is **filesystem contract**, not chat history. Adaptoid HANDOFF/PRINCIPLES kinship.

12. **Single active memory plugin slot** — avoid dual memory brains fighting. One write path, many read projections.

13. **Untrusted-context wrapping** (Odysseus) — emails, web, memories, skills as **data-role** with explicit policy. Adaptoid anti-hallucination / prompt-injection law.

14. **Replace-not-append state** — OpenClaw doctor migrates config; bootstrap attestation prevents silent reseed. Matches Adaptoid HANDOFF rewrite discipline.

### D. Permissions & blast radius

15. **Plan vs Build as first-class agents** — not a vibe; permission matrix. Adaptoid Brain (plan/read) vs Hands (build/write).

16. **Permission last-match globs** for bash/MCP/skills — fine-grained, auditable. Prefer over binary tool on/off alone.

17. **Main vs non-main sandbox** — full power for owner primary session; sandbox strangers/groups. Channel products *require* this; coding harnesses less so.

18. **DM pairing codes** — untrusted inbound is default. Any Adaptoid remote channel must assume hostile senders.

19. **Admin vs non-admin tool classes** (Odysseus) — chat-for-all, shell-for-admin. Multi-user self-host patterns.

20. **Internal tool loopback token** — agent tools don’t bypass auth; in-process privilege still checks session owner.

### E. MCP strategy (don’t become MCP soup)

21. **MCP dual role** — expose your sessions *to* other harnesses (OpenClaw serve) *and* consume tools. Adaptoid as MCP server for “mission state” is a power move.

22. **Context budget discipline** — OpenCode warns MCP blows context; OpenClaw filters tools per server. Adaptoid: MCP allowlists per pack/mission.

23. **Probe/doctor before save** — validate MCP servers at config time. Fail closed on broken tools mid-mission.

24. **Avoid hierarchy frameworks as default** — OpenClaw VISION refuses manager-of-managers. Prefer **flat agents + task subagents + queues**, not org-chart frameworks.

### F. Model ops as mission infrastructure

25. **Cookbook / hardware-aware serving** — portable OS that runs local must treat VRAM fit and serve reliability as first-class (not “user figures out Ollama”).

26. **Blind model compare** — eval is part of the workspace, not external spreadsheet. Adaptoid eval gates kinship.

27. **Provider idle vs run timeouts** — separate model-stream watchdog from agent wall clock (OpenClaw). Local models need different defaults than cloud.

### G. Continuity & ambient agency

28. **Cron + heartbeat + channels** — personal OS value is *between* IDE sessions. Coding harness alone is incomplete for mission OS.

29. **Steering queues** — don’t only interrupt; inject guidance after tool batch. Human-in-loop without killing work.

30. **Hybrid deployment** (reviewer consensus): Odysseus-class **cockpit** + OpenClaw-class **reach** + OpenCode-class **repo Hands**. Adaptoid is the **mission rules + SDLC gates + proof** layer that survives model and host swap.

### H. Legal / packaging

31. **AGPL workspace vs MIT harnesses** — shipping Odysseus-derived UI may force AGPL compliance; OpenClaw/OpenCode patterns safer to reimplement under MIT. Prefer **concept transfer** over code copy for AGPL surfaces.

---

## 7. Sources (URLs)

### Primary

- OpenClaw repo: https://github.com/openclaw/openclaw  
- OpenClaw README (raw): https://raw.githubusercontent.com/openclaw/openclaw/main/README.md  
- OpenClaw VISION: https://raw.githubusercontent.com/openclaw/openclaw/main/VISION.md  
- OpenClaw docs home: https://docs.openclaw.ai  
- OpenClaw architecture: https://docs.openclaw.ai/concepts/architecture  
- OpenClaw agent runtime: https://docs.openclaw.ai/concepts/agent  
- OpenClaw agent loop: https://docs.openclaw.ai/concepts/agent-loop  
- OpenClaw skills: https://docs.openclaw.ai/tools/skills  
- OpenClaw MCP CLI: https://docs.openclaw.ai/cli/mcp  
- OpenClaw site: https://openclaw.ai  
- ClawHub: https://clawhub.ai  
- Odysseus repo: https://github.com/pewdiepie-archdaemon/odysseus  
- Odysseus README (raw main): https://raw.githubusercontent.com/pewdiepie-archdaemon/odysseus/main/README.md  
- Odysseus ROADMAP (dev): https://raw.githubusercontent.com/pewdiepie-archdaemon/odysseus/dev/ROADMAP.md  
- Odysseus THREAT_MODEL (dev): https://raw.githubusercontent.com/pewdiepie-archdaemon/odysseus/dev/THREAT_MODEL.md  
- Odysseus site: https://pewdiepie-archdaemon.github.io/odysseus/  
- OpenCode repo: https://github.com/anomalyco/opencode  
- OpenCode site: https://opencode.ai  
- OpenCode docs intro: https://opencode.ai/docs  
- OpenCode agents: https://opencode.ai/docs/agents  
- OpenCode MCP: https://opencode.ai/docs/mcp-servers  
- OpenCode skills: https://opencode.ai/docs/skills  
- OpenCode rules: https://opencode.ai/docs/rules  
- AgentSkills spec (referenced by OpenClaw): https://agentskills.io  

### Secondary / ecosystem

- Pinokio: Odysseus vs OpenClaw+Hermes: https://beta.pinokio.co/posts/01kt59fmhj9qyjeam6vandy6p2  
- gavinj.net Odysseus review: https://www.gavinj.net/post/odysseus-review-local-first-ai-workspace  
- HN: Odysseus self-hosted workspace: https://news.ycombinator.com/item?id=48346693  
- Medium overview (Odysseus): https://medium.com/data-science-in-your-pocket/pewdewpie-odysseus-the-biggest-youtuber-dropped-an-ai-workspace-28136b87a87b  

---

## 8. Elite bullets for merge (copy-ready)

- **Species split is the architecture:** OpenClaw = ambient channel agent OS; Odysseus = local AI workspace/cockpit; OpenCode = Claude-Code-class repo harness. Adaptoid should **orchestrate**, not clone all three UIs.
- **SKILL.md + precedence + eligibility gating + human-approved workshop** is the portable skill stack; ClawHub-style verify is the trust layer.
- **OpenCode’s on-demand `skill` tool** is elite for token economy; OpenClaw’s session skill snapshot is elite for personal-assistant stability — Adaptoid wants both modes.
- **Bootstrap identity files (SOUL/IDENTITY/USER/MEMORY)** beat chat-memory folklore; make identity a versioned FS contract.
- **Gateway + nodes + pairing + main/non-main sandbox** is the security shape for anything reachable from chat apps.
- **Plan/Build primary agents + permission globs + task subagent ACL** is the clean Brain/Hands model OpenCode shares with Claude Code — lift this into mission packs.
- **MCP as bidirectional bridge** (expose mission sessions *and* consume tools) > MCP-as-junk-drawer; always filter tools and budget context.
- **Untrusted-context wrapping** for web/email/memory/skill text is non-negotiable on self-hosted multi-tool workspaces.
- **Local model Cookbook + blind compare** make self-host honest; without hardware-aware serving, “local-first” is cosplay.
- **Reject nested manager hierarchies as default**; prefer flat agents, queues/steering, and SDLC gates with evidence.
- **AGPL Odysseus UI concepts vs MIT harness patterns:** transfer ideas, reimplement under Adaptoid license posture; don’t silently vendor AGPL.
- **Hybrid future (elite consensus):** cockpit (Odysseus-class) + reach (OpenClaw-class) + Hands (OpenCode-class) + **Adaptoid mission rules / SDLC proof** as the portable OS layer that survives host and model swaps.

---

## 9. Suggested next research (not done here)

1. Install OpenClaw + capture real `openclaw.json` schema excerpts for multi-agent + sandbox.  
2. Map Odysseus `src/` agent loop and confirm OpenCode wrap points in code.  
3. Diff OpenCode `packages/` agent runtime vs Claude Code public behavior (tools, compact, LSP).  
4. Hermes Agent docs cross-walk (Nous) for memory/channel patterns Pinokio groups with OpenClaw.  
5. ClawHub skill package format + verify envelope schema dump for Adaptoid skill registry design.

---

*End of partial A. Incomplete by design; ready for ERA-OCEAN merge.*
