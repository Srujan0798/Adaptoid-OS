# ERA-OCEAN Partial E — Grok Build + Google Antigravity (host capabilities)

**Wave:** `wave-20260718-0841-E`  
**Agent:** E (host CLIs — xAI Grok Build · Google Antigravity)  
**Status:** **INCOMPLETE** (primary docs + news scraped; no local `grok`/`agy` install; no full Antigravity desktop/SDK deep-read; no source tree of `xai-org/grok-build`)  
**Written:** 2026-07-18  
**Scope:** Host capabilities for harness — **plan · skills · worktrees · headless · ACP** — plus **elite deltas for multi-host emit**. Research-only.

> Coverage honesty: still **≪ 1%** of agentic surface. Do not treat this partial as product integration or as a complete host matrix.

---

## 0. Honesty / coverage gaps

| Gap | Why it matters |
|-----|----------------|
| No local install of `grok` or `agy` in this wave | Runtime UX, permission prompts, actual worktree paths, ACP handshake failures unmeasured |
| Antigravity docs are SPA-heavy; some pages return thin HTML to scrapers | Plugin schema, headless flags, worktree CLI surface may lag official UI docs |
| Grok Build OSS dump (`xai-org/grok-build`) not tree-walked | Tool port lineage (Codex/OpenCode), upload remnants, prompt templates only via secondary (Willison) |
| Subagent isolation semantics (file write scopes, MCP inheritance) not proven with tests | Elite claim “one agent one worktree” needs host-specific evidence |
| No dual-host CI matrix run (Claude + Grok + agy on same repo) | Multi-host emit is design, not measured interop |
| Privacy/retention story for Grok Build is mid-July 2026 crisis → OSS; policy may still move | Production trust claims need re-verify |
| Antigravity **ACP** not confirmed as first-class (Grok has explicit `grok agent stdio`) | Do not assume ACP parity across hosts |

**What is solid:** docs.x.ai/build primary pages (overview, modes, skills/plugins, headless/ACP, hooks, worktrees, AGENTS.md); x.ai news (CLI launch, grok-build-0.1, Grok 4.5); Google transition blog + I/O 2026 Antigravity ecosystem; antigravity.google CLI features (plugins, sandbox, slash commands, subagents) via docs scrape; Adaptoid `host_emit.py` + `HOST-CAPABILITIES.md` as internal baseline.

---

## 1. Positioning (two different host species)

| Dimension | **Grok Build** (xAI) | **Antigravity CLI** (`agy`) (Google) |
|-----------|----------------------|--------------------------------------|
| **One-liner** | Terminal coding agent (TUI + headless + ACP) | Terminal surface of **Antigravity** agent platform (shared server-side harness) |
| **Install** | `curl -fsSL https://x.ai/cli/install.sh \| bash` | Product download / CLI install paths on antigravity.google |
| **Binary / stack** | Rust-heavy OSS harness (~mid-Jul 2026 Apache 2.0 dump) | Go rewrite (Google: snappier than Gemini CLI) |
| **Default model** | Grok 4.5 (Build default); also `grok-build-0.1` API SKU earlier | Gemini 3.x class (I/O: 3.5 Flash as high-speed agent engine) |
| **Auth** | SuperGrok / X Premium Plus / `XAI_API_KEY`; browser login | Google account / AI Pro·Ultra / Cloud enterprise paths |
| **Instruction files** | `AGENTS.md` family + Claude/Cursor compat + `.grok/rules/` | Skills/rules via plugins; Gemini CLI legacy migration |
| **Extensibility unit** | Skills + plugins + hooks + MCP + marketplaces | **Plugins** = skills + agents + rules + MCP + hooks monorepo unit |
| **Embed / automation** | `grok -p` · `grok agent stdio` (**ACP**) | Headless print mode (community: `agy -p`); Managed Agents API for cloud harness |
| **Platform scope** | CLI (+ API models; Office plugins narrative for 4.5) | Desktop 2.0 + CLI + SDK + Managed Agents + Gemini Enterprise |
| **Closest peers** | Claude Code / Codex CLI | Gemini CLI successor; peer of Claude Code as *platform*, not just TUI |

**Species rule for Adaptoid:** Grok Build ≈ **repo coding harness peer** (like Claude Code / Codex). Antigravity ≈ **platform + managed harness** with a CLI face — pin **platform** name, never “Gemini CLI” as product identity after Jun 18 2026 consumer cutover.

---

## 2. Grok Build — host capabilities (primary)

**Primary:** https://docs.x.ai/build/overview  
**Launch:** https://x.ai/news/grok-build-cli (2026-05-25)  
**Related news:** grok-build-0.1 API (2026-05-29); Grok 4.5 (2026-07-16)

### 2.1 Surfaces

| Surface | Mechanism | Harness use |
|---------|-----------|-------------|
| Interactive TUI | `grok` in project cwd | Human plan/act loop |
| Headless | `grok -p "…"` · `--output-format plain\|json\|streaming-json` | Scripts, CI, bots |
| ACP | `grok agent stdio` (JSON-RPC stdin/stdout) | Embed in IDEs / orchestration apps |
| Session ops | `--session-id` / `--resume` / `--continue`; `/resume`, `/fork` | Multi-turn automation |
| Inspect | `grok inspect` | Dump discovered config sources, instructions, skills, plugins, hooks, MCP — **debug gold** |

### 2.2 Plan

- Launch marketing: **plan → review → approve**; plan as editable artifact; diffs after approve.
- Docs (`/build/modes-and-commands`): **Plan mode** via `/plan [description]`, view with `/view-plan`.
- Behavior: edits to the **session plan file** auto-approved; **other file writes still need approval**.
- Clarifying questions before edits allowed while planning.
- `Shift+Tab` cycles session modes; `--always-approve` / `permission_mode` in `~/.grok/config.toml` for autonomy.

**Harness map:** Plan mode = soft SDLC gate 1–3. Adaptoid still needs **external evidence** (preflight) after host “approved plan.”

### 2.3 Skills · plugins · hooks · MCP

Discovery (docs `/build/features/skills-plugins-marketplaces`):

| Kind | Paths |
|------|-------|
| Skills | `./.grok/skills/` (walk to root), `~/.grok/skills/`, plugin `skills/`, `[skills] paths` in config |
| Plugins | `./.grok/plugins/`, `~/.grok/plugins/`, marketplaces, `--plugin-dir` |
| Hooks | `~/.grok/hooks/`, project `.grok/hooks/` (**requires `/hooks-trust` or `--trust`**), plugins |
| User skills (AAIF-shaped) | `~/.agents/skills/`, `~/.agents/commands/` |

- User-invocable skills become slash commands (`/<skill-name>`; qualified `/local:commit` on collision).
- Unified extensions modal: `/skills` `/plugins` `/hooks` `/mcps` `/marketplace`.
- **Claude Code zero-config compat:** reads Claude marketplaces, plugins, skills, MCPs, agents, hooks, and `CLAUDE.md` / `Claude.md` / `CLAUDE.local.md` / `.claude/rules/` alongside `.grok/`.
- **AGENTS.md family:** `AGENTS.md`, `Agents.md`, `AGENT.md`; nested precedence; also `.grok/rules/`, `.claude/rules/`, `.cursor/rules/` for compat. `grok inspect` shows token cost per rules file.
- Hooks: PreToolUse is **only blocking** event; fail-open on timeout/crash unless explicit deny. Events include SubagentStart/Stop, Pre/PostCompact, SessionStart/End. Also reads Claude + Cursor hook files.

### 2.4 Worktrees

**Primary:** https://docs.x.ai/build/features/worktrees

- Worktree session = isolated git checkout so parallel agents cannot overwrite each other.
- Live under `~/.grok/worktrees/<repo>/<name>`; start from current HEAD **including uncommitted changes**.
- CLI: `-w, --worktree [<NAME>]`; manage via `grok worktree <list|show|rm|gc>`.
- Settings: `new_session_worktree_mode` / `fork_worktree_mode` = ask | always | never.
- Agent Dashboard: Ctrl+W toggles worktree for new agents; subagents can launch in own worktrees (launch post + docs).
- Landing changes = ordinary git (worktree is real checkout).

**Harness map:** First-class productization of “one agent ↔ one worktree.” Aligns Adaptoid FM-13 / SHIP worktree rows.

### 2.5 Headless

| Flag | Role |
|------|------|
| `-p, --single` | One-shot prompt |
| `-m` | Model |
| `-s` / `-r` / `-c` | Session id / resume / continue |
| `--cwd` | Working directory |
| `--output-format` | plain · json · streaming-json |
| `--always-approve` | Skip tool prompts |
| `--no-auto-update` | CI hygiene |

Sessions stored under `~/.grok/sessions`. Streaming JSON = newline-delimited events for orchestration.

### 2.6 ACP (Agent Client Protocol)

- Entry: `grok agent stdio`.
- JSON-RPC over stdin/stdout; methods: `initialize` → `authenticate` → `session/new` → `session/prompt`.
- Assistant text streams as `session/update` chunks (`agent_message_chunk`).
- Client capabilities include `fs.readTextFile` / `writeTextFile` / `terminal`.
- Auth: cached token or `xai.api_key` when `XAI_API_KEY` set; `_meta.headless` on authenticate.

**Harness map:** Strongest **embed API** among this pair. Adaptoid multi-host orchestration can treat Grok as a **stdio agent process**, not only a human TUI.

### 2.7 Background / loop / multi-agent

- Subagents: independent child sessions in parallel (`/tasks`, Ctrl+B tasks pane).
- `/loop [interval] <prompt>` — recurring agent turns (min 60s; expire 7d; max 50 scheduled).
- Monitors: line-based event streams into conversation.
- Prompt queue while turn running (`/queue`).
- `/fork` branches session into peer agent.

### 2.8 Models & maturity signals

| Item | Note |
|------|------|
| Grok 4.5 | Default in Grok Build; API `$2/M in · $6/M out`; coding + agentic claims; Cursor co-training mention |
| grok-build-0.1 | Earlier fast coding SKU (~100+ TPS, $1/$2) |
| Custom models | `~/.grok/config.toml` OpenAI-compatible `base_url` |
| Privacy crisis → OSS | Mid-Jul 2026: directory upload backlash; retention default off; Apache 2.0 open source (Willison 2026-07-15) |
| Tool lineage | OSS tools ported/inspired from Codex + OpenCode (secondary) |

Treat as **high velocity, verify-before-prod** host.

---

## 3. Google Antigravity — host capabilities (primary + migration)

**Platform:** https://antigravity.google/  
**CLI features:** https://antigravity.google/docs/cli/features  
**Plugins:** https://antigravity.google/docs/cli/plugins  
**Transition:** https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ (2026-05-19)  
**I/O ecosystem:** https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/

### 3.1 Platform surfaces (not just a CLI)

| Surface | Role |
|---------|------|
| **Antigravity 2.0 desktop** | Multi-agent command center; parallel agents; scheduled tasks; ecosystem integrations |
| **Antigravity CLI (`agy`)** | Go TUI; lightweight terminal surface of **shared agent harness** |
| **Antigravity SDK** | Programmatic same harness; host on own infra |
| **Managed Agents (Gemini API)** | Cloud isolated Linux env; Interactions API; Antigravity harness + Gemini 3.5 Flash co-opt |
| **Gemini Enterprise Agent Platform** | Cloud identity / enterprise workload path |

**Hard cutover (consumers):** Jun 18 2026 — Gemini CLI / free + AI Pro/Ultra consumer Code Assist stop; enterprise Gemini CLI retained longer on paid/Cloud keys. **No 1:1 feature parity at cutover** (Google explicit).

### 3.2 Plan / permissions (CLI)

- Slash **/permissions** — autonomy levels: `request-review` · `always-proceed` · `strict`.
- Fine-grained allow/deny command lists in `~/.gemini/antigravity-cli/settings.json`.
- **/diff** interactive viewer to review changes and steer.
- Desktop/community: plan/quest-style multi-agent orchestration more productized in 2.0 UI than pure CLI docs (thin on “plan mode” name vs Grok/Cursor).

**Harness map:** Plan is **platform-distributed** (desktop orchestration + CLI permissions), not necessarily a single `/plan` twin. Adaptoid should not require Antigravity-specific plan files; keep portable plan markdown in repo.

### 3.3 Skills · plugins · hooks · MCP

**Plugin = deployable monorepo unit** (docs features page):

```text
~/.gemini/antigravity-cli/
├── plugins/
│   └── <plugin_name>/
│       ├── plugin.json         # required
│       ├── mcp_config.json     # optional
│       ├── hooks.json          # optional
│       ├── skills/             # optional
│       ├── agents/             # optional subagents
│       └── rules/              # optional
└── import_manifest.json
```

- Plugins stage under home dir; agent auto-discovers.
- Continuity from Gemini CLI: Agent Skills, Hooks, Subagents, Extensions → **Plugins**.
- Slash: `/skills`, `/mcp`, `/tasks`, `/agents`.
- Migration path imports Gemini CLI extensions (community/Google migration guides).

**Harness map:** Plugin packing is the **Google unit of multi-host emit** for skills+MCP+hooks+subagent defs. Portable skills under `.agents/skills/` still needed for non-Google hosts.

### 3.4 Worktrees / isolation

- Official CLI features page emphasizes **async subagents** + **terminal sandbox**, not a Grok-style `~/.…/worktrees/` first-class section (docs incomplete here).
- Secondary/community: Antigravity/desktop **worktree mode** for parallel agents; tutorial writeups describe git worktrees to avoid collisions; migration notes call out **session TTL** and **parallel file-state isolation** as gotchas.
- Terminal Sandbox (native OS: nsjail / sandbox-exec / AppContainer) — opt-in `enableTerminalSandbox` — blast-radius control for shell, not git isolation.

**Harness map:** Treat worktree as **operator law** (Adaptoid FM-13) even when host UX is weaker than Grok’s first-class worktrees. Do not assume `agy` auto-worktrees without verified CLI flag.

### 3.5 Headless

- Product positioning: CLI for fast local + **SSH + headless** vs desktop visual workspace.
- Community (Reddit / plugins): `agy -p` print/headless mode; known footguns — **`-p` must be last**, non-TTY hang unless stdin detached (`< /dev/null`).
- Managed Agents API = true server-side headless with persistent isolated env (different product surface than local CLI).

**INCOMPLETE:** official flag matrix for `agy` headless not fully captured this wave — re-read install/reference docs before CI claims.

### 3.6 ACP

- **Not confirmed** as Antigravity CLI first-class protocol equivalent to `grok agent stdio`.
- Embed paths: **SDK** + **Managed Agents API** + shelling `agy` as subprocess (community: Claude skill/plugin delegates to `agy` for cheap execution).
- Do **not** list Antigravity under ACP parity column until primary docs say so.

### 3.7 Subagents / background

- Async subagents: research, builds, validate without blocking main conversation.
- Main agent decides subagent **tools/permissions** (incl. MCP + write).
- `/agents` panel; approvals via detail view or Fast Path (`ctrl+k` approve, `ctrl+j` teleport).
- `/tasks` for background task monitor/terminate.
- Desktop 2.0: dynamic subagents + scheduled tasks (I/O).

---

## 4. Capability matrix (this partial — mid-2026 snapshot)

| Capability | Grok Build | Antigravity CLI / platform | Adaptoid portable rule |
|---|---|---|---|
| **Project law** | AGENTS.md + Claude/Cursor compat + `.grok/rules/` | Rules in plugins; GEMINI.md legacy | Always emit **AGENTS.md**; dual-emit host native |
| **Plan** | First-class `/plan` + plan file auto-approve | Permissions + /diff + desktop orchestration | Mandatory SDLC 1–3; host plan ≠ ship evidence |
| **Skills** | `.grok/skills` + plugins + `~/.agents/skills` | Plugin `skills/` + `/skills` | Prefer `.agents/skills/` (agentskills.io) |
| **Hooks (hard)** | PreToolUse block; trust gate for project hooks | Plugin `hooks.json` | SessionStart + preflight; soft ≠ hard |
| **MCP** | Client + extensions modal | Plugin `mcp_config.json` + `/mcp` | Allowlist only; FM-20 write/network |
| **Subagents** | Parallel + worktree launch | Async + permission inheritance | Research/test; **disjoint writes** |
| **Worktrees** | **First-class** (`-w`, `~/.grok/worktrees/…`) | Partial / desktop / community | Parallel risk → worktree (FM-13) |
| **Headless/CI** | `grok -p` + json/streaming-json | `agy -p` (footguns) + Managed Agents | Stage 6 preflight in CI |
| **ACP / embed** | **`grok agent stdio`** | SDK / API / subprocess (no ACP proof) | Capability shape: stdio agent vs cloud env |
| **Sandbox** | Local-first; permission_mode | Terminal Sandbox OS-native opt-in | MCP write ≥ blast-radius r3 |
| **Open / BYOK** | Multi-model config.toml; OSS harness | Google account / Cloud | Never hardcode unstable host brand IDs |

*Qualitative — re-verify before product claims.*

---

## 5. Elite deltas for multi-host emit

### 5.1 Current Adaptoid baseline (internal)

| Artifact | Today |
|----------|--------|
| `adaptor/host_emit.py` | Hosts: `agents`, `claude`, `cursor`, `codex`, `grok` — **no `antigravity`/`agy`** |
| Emit targets | AGENTS.md (agents/codex/grok/cursor) · CLAUDE.md + session-start hook · `.cursor/rules/adaptoid.mdc` |
| `core/HOST-CAPABILITIES.md` | Matrix rows for Claude/Cursor/Codex/Grok; Antigravity absent as column |
| Skills path | Prefer `.agents/skills/` (portable) |

### 5.2 Elite deltas (research → emit candidates)

> Status: **research candidates only**. Not shipped. Incomplete validation.

| # | Delta | Why (host evidence) | Emit sketch | Priority |
|---|-------|---------------------|-------------|----------|
| D1 | **Keep thin AGENTS.md as universal** | Grok walks AGENTS + Claude + Cursor rules; multi-host community already dual-reads | Always write AGENTS.md; never invent third proprietary law file | **Keep** |
| D2 | **Claude-compat dual emit is free Grok win** | Grok reads CLAUDE.md / `.claude/rules` / Claude skills with zero config | Emitting CLAUDE.md + AGENTS.md already multiplies Grok coverage | **Keep / document** |
| D3 | **Add `antigravity` host ID (stable alias `agy`)** | Gemini→Antigravity brand break; hardcoding “gemini-cli” is footgun | `HOSTS += antigravity`; emit optional plugin skeleton under `.gemini/antigravity-cli/plugins/adaptoid/` or document install path — **do not** write into `~` from engine | **Watch → design** |
| D4 | **Skills: dual layout, single source** | Grok: `.grok/skills` + `~/.agents/skills`; Antigravity: plugin `skills/`; industry: agentskills.io | Generate skills only under `.agents/skills/`; optional host-specific **symlinks or emit copies** to `.grok/skills` / plugin pack | **Adopt candidate** |
| D5 | **Plugin pack as optional “Google monorepo unit”** | Antigravity plugins bundle skills+agents+rules+MCP+hooks | New template: `core/hosts/antigravity.plugin/` with `plugin.json` + rules pointing at AGENTS principles | **Watch** |
| D6 | **Hooks trust semantics differ** | Grok project hooks need `/hooks-trust`; fail-open PreToolUse | Emit hook scripts + **README “must trust”**; never claim hooks fire without human trust step | **Document** |
| D7 | **Worktree ops as playbook law, not only Claude row** | Grok first-class; Antigravity weaker in CLI docs | HOST-CAPABILITIES: add Antigravity column; playbook: “if host lacks auto-worktree, operator creates worktree before parallel agents” | **Adopt candidate** |
| D8 | **Headless contracts as capability shapes** | Grok: streaming-json + ACP; agy: `-p` footguns; Managed Agents: cloud env | Encode **shapes** in HOST-CAPABILITIES: `stdio-acp` · `cli-print` · `cloud-managed` — not brand lists | **Adopt candidate** |
| D9 | **ACP adapter only where proven** | Grok has official ACP sample; Antigravity does not | Product orchestration may spawn `grok agent stdio`; treat agy as shell skill until ACP docs exist | **Keep boundary** |
| D10 | **Plan artifact portability** | Grok plan file is session-local; Cursor saves `.cursor/plans/` | Adaptoid plan stays in repo markdown (HANDOFF / plans/) independent of host plan UX | **Keep** |
| D11 | **Privacy / blast-radius default for Grok** | Jul 2026 upload incident; retention flipped off; OSS response | Emit `.gitignore` for secrets; never recommend `always-approve` as default in cold-start; point `/privacy` | **Adopt candidate** |
| D12 | **Subagent cost routing pattern** | Community: Claude design + `agy` execute under shared AGENTS.md | Elite: maker≠checker across **hosts**, not only models — harness may shell peer CLI | **Watch** (security: two trust domains) |
| D13 | **`grok inspect` as preflight helper** | Lists rules/skills/MCP discovery + tokens | Optional script note: “on Grok host, run `grok inspect` after emit” | **Watch** |
| D14 | **Never pin Gemini CLI paths in templates** | Consumer cutover complete Jun 18 2026 | Archive any gemini-cli emit; platform name = Antigravity | **Adopt** (docs hygiene) |
| D15 | **Soft vs hard enforcement unchanged** | Both hosts have soft rules + harder hooks/sandbox | Preflight remains source of ship truth; host plan approve ≠ done | **Keep** |

### 5.3 Multi-host emit target map (desired end-state, incomplete)

```text
repo/
  AGENTS.md                    # universal (all hosts)
  CLAUDE.md                    # Claude + Grok-compat free
  .agents/skills/*/SKILL.md    # portable skills source of truth
  .cursor/rules/adaptoid.mdc   # Cursor soft rules
  .claude/hooks/…              # Claude hard SessionStart
  .grok/                       # OPTIONAL thin Grok project hooks/skills copies
  plugins/adaptoid/ OR docs    # OPTIONAL Antigravity plugin pack (not ~/.gemini write)
  HOST-CAPABILITIES.md         # matrix including Grok + Antigravity columns
```

Engine rule: **write only into project tree**; never mutate user home plugin dirs without explicit operator step.

### 5.4 What not to do (elite negative space)

- Do not claim Grok ACP ≈ Antigravity embed without primary ACP docs.
- Do not treat Managed Agents cloud env as drop-in for local preflight evidence.
- Do not append host-specific walls into AGENTS.md (thin always-on; skills for procedures).
- Do not ship “always-approve / always-proceed” defaults in generated cold-starts.
- Do not hardcode SuperGrok / AI Ultra as required — document auth options.

---

## 6. Sources

| # | URL | Role |
|---|-----|------|
| 1 | https://docs.x.ai/build/overview | **Primary** — Grok Build surfaces, install, headless, multi-model |
| 2 | https://docs.x.ai/build/modes-and-commands | **Primary** — Plan mode, permission modes, slash surface, `/loop` |
| 3 | https://docs.x.ai/build/features/skills-plugins-marketplaces | **Primary** — skills/plugins/hooks discovery + Claude/AGENTS compat |
| 4 | https://docs.x.ai/build/cli/headless-scripting | **Primary** — `-p`, output formats, **ACP** `grok agent stdio` |
| 5 | https://docs.x.ai/build/features/worktrees | **Primary** — worktree isolation paths and lifecycle |
| 6 | https://docs.x.ai/build/features/hooks | **Primary** — PreToolUse deny, fail-open, trust |
| 7 | https://docs.x.ai/build/features/project-rules | **Primary** — AGENTS.md discovery precedence + `grok inspect` |
| 8 | https://docs.x.ai/build/features/background-tasks | **Primary** — `/loop`, monitors, queue, subagent tasks |
| 9 | https://x.ai/news/grok-build-cli | **Primary news** — plan/review/approve, subagents+worktrees, headless, ACP (2026-05-25) |
| 10 | https://x.ai/news/grok-build-0-1 | News — coding SKU API beta |
| 11 | https://x.ai/news/grok-4-5 | News — Grok 4.5 default model, pricing, Build default (2026-07-16) |
| 12 | https://simonwillison.net/2026/Jul/15/grok-build/ | Secondary — OSS Apache 2.0, privacy incident, tool lineage |
| 13 | https://github.com/xai-org/grok-build | Source dump (not deep-read this wave) |
| 14 | https://antigravity.google/ | Platform home |
| 15 | https://antigravity.google/docs/cli/features | **Primary** — plugins layout, sandbox, slash cmds, subagents |
| 16 | https://antigravity.google/docs/cli/plugins | **Primary** — plugins & skills (thin scrape) |
| 17 | https://antigravity.google/docs/cli-overview | CLI vs desktop positioning (headless mention) |
| 18 | https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ | **Primary** — Gemini CLI → Antigravity; Jun 18 2026 cutover |
| 19 | https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/ | I/O — Antigravity 2.0, CLI, SDK, Managed Agents, 3.5 Flash |
| 20 | https://antigravity.google/product/antigravity-cli | Product surface (plugins/MCP/skills/hooks) |
| 21 | Community secondary: Reddit `agy` headless as Claude subagent; Medium migration guides | Headless footguns; skills/subagents migrate patterns |
| 22 | Internal: `adaptor/host_emit.py`, `core/HOST-CAPABILITIES.md` | Emit baseline for elite deltas |

Prior ocean anchors (W1 hosts): S-20260718-037…046 in `docs/research/era-ocean/sources/INDEX.md`.

---

## 7. Incomplete follow-ups (next partial / local proof)

1. Local: install `grok`, run `grok inspect` in this kit repo; capture discovery list.
2. Local: install `agy`; document exact headless flags and non-TTY behavior.
3. Read full Antigravity plugin schema + migration doc (`gcli-migration`) end-to-end.
4. Tree-walk `xai-org/grok-build` for worktree + ACP + permission implementation truth.
5. Confirm whether Antigravity implements or plans ACP.
6. Draft (not merge) `antigravity` host template + HOST-CAPABILITIES column if still proven.
7. Dual-host smoke: same skill under Claude + Grok + agy with preflight evidence.
8. Re-check Grok retention/privacy defaults post-OSS dump.

---

## 8. One-page executive (for elite merge later)

1. **Hosts converge on plan · skills · hooks · subagents · headless · MCP** — differentiator is isolation depth (worktrees), embed protocol (ACP), and platform vs CLI scope.
2. **Grok Build** is a full peer coding harness with **first-class plan, worktrees, headless JSON, and ACP** — best xAI field for Adaptoid multi-host tests; treat privacy history as permanent blast-radius lesson.
3. **Antigravity** is Google’s **agent platform** (desktop + CLI + SDK + Managed Agents); CLI plugins are the monorepo emit unit; consumer Gemini CLI identity is dead after Jun 18 2026.
4. **Multi-host emit elite path:** thin AGENTS.md + `.agents/skills` source of truth + host duals (CLAUDE.md free Grok-compat; optional Antigravity plugin pack) + capability **shapes** (stdio-acp / cli-print / cloud-managed) — never brand-locked paths.
5. **This partial is incomplete** until local installs and Antigravity ACP/worktree primary docs close the gaps.

```
Ocean: open
Partial E: written · INCOMPLETE
Host trench: Grok Build + Antigravity
Claim full host map: FORBIDDEN
```
