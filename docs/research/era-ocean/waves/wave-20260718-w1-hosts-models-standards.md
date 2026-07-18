# Wave W1 — Hosts, Models, Standards (mid-2026)

| Field | Value |
|---|---|
| Wave ID | `wave-20260718-w1-hosts-models-standards` |
| Date (UTC) | 2026-07-18 |
| Researcher | Wave-1 (Grok Build subagent) |
| Scope | Official docs + top hosts / models / standards for **coding agents** |
| Coverage honesty | **≪ 1%** of the agentic surface. Snapshot, not map. |
| Product link | Distill later into `elite/` + `ADAPTATION.md` only when proven |

> **Method:** Live web scrape of official docs, foundation announcements, and cross-checked secondary sources (July 2026). Bullets are **harness-relevant** (what compounds for multi-host mission OS), not marketing.

---

## Executive read (for Adaptoid)

1. **Three rails are de facto infrastructure:** `AGENTS.md` (repo policy), **Agent Skills** (`SKILL.md` progressive disclosure), **MCP** (tool/data plane) — all Linux Foundation / open-standard direction.
2. **Hosts are converging on the same surface:** plan → act → tools → hooks → skills → subagents → headless/CI → MCP. Differentiator = harness quality + model pairing + blast-radius UX, not feature list.
3. **Model = weapon, host = field, harness = mission rules.** Vendor lock is real on *loop quality* (Claude Agent SDK ≈ Claude Code loop; Codex pairs with GPT-5.x-Codex; Antigravity is Google’s server-side harness). Portable layer = AGENTS.md + Skills + MCP + evidence gates.
4. **Gemini CLI → Antigravity CLI** is the sharpest host rename of 2026: consumer Gemini CLI cut over June 18, 2026.
5. **Windsurf → Devin Desktop; Continue → acquired by Cursor.** Host churn is product strategy, not research trivia.
6. **MCP 2026-07-28 RC** is the largest protocol break since launch (stateless core, extensions, Tasks, Apps, auth hardening). Plan for dual-support windows.

---

## 1. HOSTS

### 1.1 Claude Code (Anthropic)

**Primary:** https://code.claude.com/docs/en/overview · product https://claude.com/product/claude-code

- **Multi-surface one engine:** Terminal CLI, VS Code/Cursor extension, JetBrains, Desktop app, Web (`claude.ai/code`), mobile/remote control — same CLAUDE.md, settings, MCP across surfaces.
- **Harness knobs that matter:** `CLAUDE.md` + auto-memory; **skills** (packaged workflows); **hooks** (pre/post shell); **sub-agents / agent teams / background agents**; scheduled **Routines** (cloud) vs local scheduled tasks.
- **Unix composability:** `claude -p` headless, pipe stdin, CI (GitHub Actions / GitLab), Slack route-to-PR, Chrome debug — treat as scriptable runtime, not only chat.
- **Programmable twin:** **Claude Agent SDK** = same tools/loop/context as Claude Code, Python + TypeScript — build products on the *production loop*, not a toy reimplementation.
- **Research signal (not marketing):** Anthropic economic research on ~400k Claude Code sessions (Oct 2025–Apr 2026) frames autonomy + expertise returns; enterprise lore (long autonomous runs) is real but **verify-in-loop** remains the reliability gate.
- **Harness implication:** Best reference implementation of “mission OS on a host.” Map Adaptoid gates → Claude hooks + skills + CLAUDE.md/AGENTS.md dual-read.

### 1.2 Cursor Agent

**Primary:** https://cursor.com/docs · best practices https://cursor.com/blog/agent-best-practices (Jan 2026)

- **Explicit harness model:** Instructions (system + rules) × Tools (edit/search/terminal/MCP) × **Model** — Cursor retunes harness **per frontier model** (different models need different tool bias).
- **Plan Mode as first-class SDLC gate:** research → clarify → editable Markdown plan (save under `.cursor/plans/`) → approve → build. Restart-from-plan beats fix-forward.
- **Rules vs Skills:** Rules = always-on project policy (`.cursor/rules/`); Skills = dynamic `SKILL.md` + hooks (e.g. stop-hook grind loops until tests/`DONE`). Skills were nightly-channel earlier in 2026 — verify channel maturity before depending.
- **Parallel / multi-agent product motion:** Cursor 3 pushes task-assignment and multi-agent supervisory workflows; background agents + browser tools for visual verify.
- **Context hygiene as operator skill:** new conversation on task boundaries; `@Past Chats` selective recall; let agent search rather than dump files.
- **Harness implication:** Closest public write-up of “harness engineering” language. Align Adaptoid Plan/Act/Evidence with Plan Mode + rules/skills split. Continue.dev **acquired by Cursor** → OSS Continue path is absorption risk.

### 1.3 OpenAI Codex CLI

**Primary:** https://developers.openai.com/codex/cli (also ChatGPT Learn mirrors)

- **Terminal loop + cloud handoff:** local repo inspect/edit/run; `codex exec` for CI; `codex cloud` to move work to sandboxed cloud env and apply back; `codex resume` for session continuity.
- **AGENTS.md native:** `/init` scaffolds AGENTS.md; skills + plugins extend workflows; MCP client (`codex mcp`); can run **as MCP server** (`codex mcp-server`) for Agents SDK orchestration.
- **Subagents default-path:** specialized parallel workers with merge-back into main session (CLI, IDE extension, ChatGPT desktop).
- **Control surface:** model + reasoning effort + permissions/sandbox/writable roots; dedicated **`/review`** (findings without mutating tree); image + web search context.
- **Model coupling:** GPT-5.x / GPT-5.x-Codex lineage tuned for long-horizon agentic coding, context compaction, Windows agentic reliability; Terminal-Bench leadership claims need date-stamped verification.
- **Harness implication:** Strongest **policy + sandbox** story among Big-3 CLIs. Treat Codex as both host *and* callable tool (MCP) inside higher-level multi-agent products.

### 1.4 Grok Build (xAI)

**Primary:** https://docs.x.ai/build/overview · launch https://x.ai/news/grok-build-cli (May 2026)

- **Surfaces:** Interactive TUI (`grok`), headless (`grok -p`, streaming JSON), **Agent Client Protocol (ACP)** embed in other apps.
- **Extensibility stack (aligns with industry):** instructions, skills, plugins, hooks, MCP; `grok inspect` dumps discovered config sources for the cwd — operational gold for harness debugging.
- **Model flexibility:** custom models via `~/.grok/config.toml` (OpenAI-compatible base URLs); powers on **Grok 4.5** / coding-oriented API models (e.g. earlier `grok-build-0.1` fast coding SKU).
- **Maturity/trust:** Early beta → rapid open-source release of Grok Build (Apache 2.0, mid-Jul 2026) after retention/privacy pressure; treat as **high velocity, verify-before-prod**.
- **Harness implication:** Another terminal-native peer to Claude Code/Codex with ACP + multi-model. Good test target for “host-agnostic AGENTS.md/skills/MCP” claims. Subagent parallelism (community reports up to multi-agent Heavy-style runs) — confirm against current docs before hardcoding.

### 1.5 Gemini CLI → Antigravity CLI (Google)

**Primary:** https://antigravity.google/ · migration https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ · CLI plugins https://antigravity.google/docs/cli/plugins

- **Hard cutover:** June 18, 2026 — Gemini CLI stopped serving free / AI Pro / Ultra consumer tiers; **Antigravity CLI** is the terminal successor; enterprise Gemini Code Assist paths retained longer on Gemini CLI OSS repo.
- **Platform not tool:** Antigravity 2.0 = desktop + CLI + **server-side harness** + Managed Agents in Gemini API + Google Cloud / Gemini Enterprise Agent Platform.
- **Feature continuity (names change):** Agent Skills, Hooks, Subagents, Extensions → **Plugins** (bundle skills, background subagents, rules, MCP defs, event hooks).
- **Ops reality:** Shared backend for multi-agent / background async; session TTL and parallel file-state isolation called out as migration gotchas.
- **Harness implication:** Google is selling **agent runtime + managed execution**, not just a CLI. Adaptoid should treat `agy` as peer host with plugin packing = skills+MCP+hooks monorepo unit.

### 1.6 Cline

**Primary:** https://cline.bot/ · docs https://docs.cline.bot · GitHub `cline/cline`

- **Open coding agent runtime:** IDE extension (huge Marketplace install base), CLI (`npm i -g cline`), **SDK** for embed — Apache-2.0, BYOK / local weights.
- **Plan / Act as UX law:** plan alignment, then execute; step approval or auto-approve; checkpoints + one-click undo — human-in-the-loop as product default.
- **MCP marketplace + “add a tool”:** first-class MCP client; can generate/install MCP servers from chat — self-extending tool plane.
- **Rules/skills + multi-agent:** `.clinerules`; coordinator/specialist teams; schedules/cron; Slack/Linear/CI headless.
- **Harness implication:** Best OSS reference for **permissioned Act loop + MCP marketplace**. Maps cleanly to Adaptoid blast-radius policies (approve write/network).

### 1.7 Aider

**Primary:** https://aider.chat/ · AGENTS.md: configure `read: AGENTS.md` in `.aider.conf.yml`

- **Git-native pair loop:** every edit tends toward commit-quality diffs; polyglot leaderboard culture (model ranking discipline).
- **BYOK / model-agnostic:** OpenAI, Anthropic, DeepSeek, Ollama, OpenAI-compatible — quality tracks the model hard.
- **Lower “agent product” surface:** fewer subagent/orchestration features than Claude Code/Cline/OpenCode; wins on **structured refactor correctness** for terminal power users.
- **Cadence risk:** slower release cadence vs OpenCode/Cline in mid-2026 comparisons — still valuable as harness control (git as transaction log).
- **Harness implication:** Use as **diff/commit evidence pattern** reference. AGENTS.md opt-in shows poly-host instruction file is necessary but not sufficient without discovery conventions.

### 1.8 OpenCode

**Primary:** https://opencode.ai/

- **Most-starred open coding agent class (community rankings mid-2026):** terminal + desktop + IDE extension; LSP-aware; multi-session parallel agents; shareable session links.
- **Provider freedom:** 75+ providers via Models.dev; free models + Copilot/ChatGPT login bridges; local models; curated **Zen** model list for agentic quality.
- **Privacy-first positioning:** claims no storage of code/context — enterprise-sensitive envs.
- **MCP + permissions:** config-driven MCP and permission policies (`ask` defaults); sub-agents / background agent experiments in 2026 release notes.
- **Harness implication:** Default OSS multi-host testbed for Adaptoid instruction packs. Star counts ≠ reliability; still the community gravity well for BYOK agents.

### 1.9 Windsurf → Devin Desktop (Cognition)

**Primary:** https://devin.ai/desktop/ · “Windsurf is now Devin Desktop”

- **Cascade → multi-agent command center:** IDE fork heritage + cloud Devin agents; local vs cloud agent sessions; kanban-style multi-session UX.
- **Corporate chaos:** Windsurf founders/parts → Google; product path → Cognition/Devin branding — **host identity unstable**.
- **Harness implication:** Track as **cloud agent + IDE hybrid**, not as stable open standard. Prefer portable layers over Windsurf-specific config deep investment.

### 1.10 Continue (acquired by Cursor)

**Primary:** https://www.continue.dev/ (acquisition notice)

- **Was:** OSS VS Code/JetBrains agent with Chat / Autocomplete / Edit / Agent modes and **per-mode model routing**.
- **Now:** Acquired by Cursor; community OSS may linger as foundation, but strategic roadmap is Cursor’s.
- **Harness implication:** Do not build new product dependencies on Continue as independent host. Archive learnings: granular model routing per agent mode.

### Host matrix (harness dimensions)

| Host | AGENTS.md / rules | Skills | MCP | Subagents | Headless/CI | Open / BYOK |
|---|---|---|---|---|---|---|
| Claude Code | CLAUDE.md (+ ecosystem AGENTS.md) | Yes | Yes | Yes | Yes | Proprietary host; 3P providers on some surfaces |
| Cursor | Rules + AGENTS ecosystem | Yes | Yes | Yes / multi | Yes | Proprietary IDE; multi-model |
| Codex CLI | AGENTS.md first-class | Yes | Client + server | Yes | Yes | ChatGPT/OpenAI account |
| Grok Build | Instructions / AGENTS-style | Yes | Yes | Yes (claims) | Yes | SuperGrok / API; multi-model config |
| Antigravity | Skills/plugins (Gemini.md legacy) | Yes | Yes | Yes | Yes | Google account / Cloud |
| Cline | .clinerules | Yes | Yes + marketplace | Yes | Yes | OSS BYOK |
| Aider | AGENTS.md via conf | Limited | Limited | Weak | Scriptable | OSS BYOK |
| OpenCode | Config + ecosystem | Yes | Yes | Yes | Yes | OSS BYOK |
| Windsurf/Devin | Proprietary | Partial | Yes | Cloud multi | Cloud | Proprietary |
| Continue | Config | Partial | Yes | Limited | Limited | Acquired |

*Matrix is qualitative mid-2026 — re-verify before shipping product claims.*

---

## 2. STANDARDS

### 2.1 AGENTS.md

**Primary:** https://agents.md/ · stewarded by **Agentic AI Foundation (AAIF)** under Linux Foundation (donated late 2025 with OpenAI/ecosystem push)

- **README for agents:** plain Markdown, **no required fields**; predictable path for build/test/style/security/PR rules that would clutter human READMEs.
- **Discovery & precedence:** root + **nested** AGENTS.md (closest to edited file wins); user chat overrides all. OpenAI monorepo cited with dozens of nested files.
- **Adoption signal:** 60k+ public repos with AGENTS.md path (site claim, mid-2026). Native or configurable across Codex, Cursor, Claude ecosystem, Aider, Gemini/Antigravity configs, Copilot, etc.
- **What works in practice:** exact commands with flags; testing “how to run one test”; security gotchas; monorepo package-local files. Avoid dumping full style guides (use linters).
- **Harness implication:** **Single portable policy file** Adaptoid already uses. Keep dual CLAUDE.md/AGENTS.md strategy or symlink patterns; never invent a third proprietary instruction filename without adapter.

### 2.2 Agent Skills (agentskills.io)

**Primary:** https://agentskills.io/home · spec https://agentskills.io/specification · GitHub `agentskills/agentskills`

- **Unit of capability:** directory with required `SKILL.md` (YAML frontmatter + Markdown body); optional `scripts/`, `references/`, `assets/`.
- **Frontmatter contract:** required `name` (dir-matching, kebab-case) + `description` (what **and when**); optional license, compatibility, metadata, experimental `allowed-tools`.
- **Progressive disclosure (context economics):**
  1. Metadata ~100 tokens at startup for all skills  
  2. Full SKILL.md on activation (recommend &lt;5k tokens / &lt;500 lines)  
  3. References/scripts on demand  
- **Cross-host adoption:** Anthropic-origin open standard; listed adopters span Claude Code, Codex, Cursor, Gemini/Antigravity, Copilot, OpenCode, Goose, JetBrains, enterprise data platforms, etc. (counts rise monthly — treat “40+” as order of magnitude).
- **Harness implication:** Skills = **optional expertise packs** without always-on context bloat. Adaptoid skill emit should validate with `skills-ref` and keep descriptions trigger-rich. Hooks/scripts inside skills = executable policy.

### 2.3 MCP — Model Context Protocol (latest)

**Primary:** https://modelcontextprotocol.io · GitHub `modelcontextprotocol/modelcontextprotocol` · RC blog https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/

- **Role:** JSON-RPC open standard for LLM apps ↔ tools/resources/prompts (the **USB-C of agent tools**). Anthropic-origin; foundation/open governance trajectory; ubiquitous client support in coding hosts.
- **Transports:** stdio (local) + Streamable HTTP (remote); production MCP is now an ops problem (auth, multi-tenant, scaling), not a demo.
- **2026-07-28 RC (final target date July 28, 2026) — largest break since launch:**
  - **Stateless protocol core:** remove initialize handshake + `Mcp-Session-Id`; self-contained requests; horizontal scale without sticky sessions.
  - **Routable headers:** `Mcp-Method` / `Mcp-Name`; list cache via `ttlMs` / `cacheScope`; W3C Trace Context in `_meta`.
  - **Extensions first-class:** reverse-DNS IDs; official **MCP Apps** (server-rendered sandboxed UI); **Tasks** lifecycle as extension (not experimental core).
  - **Auth hardening:** OAuth/OIDC alignment (iss validation, application_type, refresh, step-up scopes).
  - **Deprecations:** Roots, Sampling, Logging → tool params / provider APIs / OTel+stderr.
- **Harness implication:** Adaptoid FM-20 (MCP write/network = high blast radius) remains correct. Plan dual-support for pre- and post-2026-07-28 clients; prefer explicit tool handles over hidden session state; treat MCP Apps/Tasks as optional capability negotiation.

### 2.4 A2A — Agent2Agent (brief)

**Primary:** https://a2a-protocol.org · GitHub `a2aproject/A2A` · LF launch Jun 2025 · one-year milestones Apr 2026

- **What it is:** Google-origin protocol for **agent-to-agent** discovery, secure messaging, and collaboration across vendors/frameworks — complementary to MCP (tools/data), not a replacement.
- **Governance:** Linux Foundation project with AWS, Cisco, Google, Microsoft, Salesforce, SAP, ServiceNow (+ growth to 150+ orgs claimed by Apr 2026); cloud platform integrations expanding.
- **Harness implication:** Relevant when Adaptoid orchestrates **heterogeneous external agents** (enterprise mesh). For single-repo coding harness, AGENTS.md + Skills + MCP dominate day-to-day; watch A2A for multi-product agent handoff.

---

## 3. LABS / MODELS (coding-agent relevant)

### 3.1 Anthropic Claude

- **Coding-agent flagship stack:** Opus-class for long-horizon / hardest reasoning; Sonnet-class for balanced agent loops; rapid 4.x→5.x numbering in 2026 docs (e.g. Opus 4.8 / Sonnet 5 references on platform docs — always pin model IDs in harness config).
- **Claude Code is the RLHF of the loop:** model quality is inseparable from host harness; Agent SDK reuses that loop.
- **Managed Agents:** hosted stateful sessions with event history — productized autonomy beyond CLI.
- **Harness note:** Prefer explicit model pins + cost ceilings; long sessions need memory/skill discipline, not just bigger context.

### 3.2 OpenAI

- **GPT-5.x general + Codex-specialized line:** GPT-5.2-Codex / later 5.x-Codex / GPT-5.5 agentic coding narrative — long-horizon, compaction, Windows agentic, cybersecurity-sensitive capabilities with controlled rollout.
- **Codex surfaces share account context:** CLI, IDE, ChatGPT, cloud sandbox, computer use — model choice includes reasoning effort knobs.
- **Harness note:** Sandbox + permissions are first-class; good default for high-blast-radius automation if org already on ChatGPT Enterprise.

### 3.3 Google Gemini

- **Gemini 3.x Flash/Pro class** as Antigravity defaults (e.g. 3.5 Flash called out at I/O 2026) — speed/cost for agent steps; Pro-class for harder planning.
- **Tight coupling to Antigravity / AI Studio / Cloud Agent Platform** — model + managed harness + enterprise identity.
- **Harness note:** Consumer CLI migration proves Google will break host names; pin **platform** (Antigravity) not “Gemini CLI” in docs.

### 3.4 xAI Grok

- **Grok 4.5** (Jul 2026): coding + agentic + knowledge work; trained with Cursor collaboration narrative; large context lineage (earlier 4.3-class 1M context claims).
- **Coding SKUs:** `grok-build-0.1` (fast agentic coding API) + full Grok in Grok Build CLI; aggressive price/performance positioning.
- **Harness note:** Fast-moving open-source CLI + model train — great for multi-host tests; verify retention/privacy defaults after Jul 2026 policy changes.

### 3.5 DeepSeek

- **Role in agent loops:** cost-efficient strong coding models widely used via BYOK hosts (Cline, Aider, OpenCode, Continue-class tools); frequent “V3/V4/R1-class” naming in community — **confirm current ID on DeepSeek platform before pinning**.
- **Harness note:** Excellent secondary model for bulk agent steps / open-weight experiments; pair with stricter verify gates (tests) when replacing frontier closed models.

### 3.6 Moonshot Kimi

- **Kimi K3** frontier positioning (long-horizon coding, multimodal, huge context claims); **kimi-k2.7-code** as dedicated coding API SKU (256k context cited).
- **Open weights lineage:** K2.5/K2.6 open releases with agent-swarm narratives; K2 series sunset timeline on platform (migrate to K3).
- **Kimi Code CLI** positioned as preferred agent framework for Kimi models.
- **Harness note:** Competitive open/API option for agent swarms and cost; validate tool-calling reliability in *your* harness (not only chat benchmarks).

### 3.7 Open models in agent loops (pattern, not catalog)

- **Where they run:** Ollama, LM Studio, vLLM, OpenAI-compatible gateways inside Cline/OpenCode/Aider/Grok custom models.
- **What matters for harnesses:** reliable **tool calling**, instruction following under AGENTS.md, long-context degradation, and **eval on your repo** — leaderboards lag release cadence.
- **Practical pattern mid-2026:** frontier closed model for plan/architecture; open/cheap model for mechanical edits + test fix loops; never skip evidence gates when swapping models.

---

## 4. FRAMEWORKS (brief — harness builders)

Sources cross-check: Langfuse Jul 2026 framework survey; Alice Labs / community rankings.

### 4.1 LangGraph + DeepAgents (LangChain)

- **LangGraph:** graph-state production control — durable execution, HITL interrupts, memory; explicit edges for audit/rollback.
- **DeepAgents:** opinionated “deep agent” harness on LangGraph — planner, isolated subagents, filesystem abstraction, skill middleware, shell/HITL — batteries for long coding-style agents.
- **Harness implication:** Closest open framework analogue to multi-step SDLC graphs; use when Adaptoid-like gates need custom productization outside a vendor CLI.

### 4.2 Claude Agent SDK

- **Same loop as Claude Code** as a library (Python/TS): tools, permissions, hooks, in-process MCP, subagents.
- **Not** the raw Messages API — you inherit Anthropic’s production agent loop.
- **Harness implication:** Fastest path to “Claude Code inside our product”; lock-in is the loop quality itself.

### 4.3 OpenAI Agents SDK

- **Primitives:** agents, handoffs, guardrails, sessions; tracing; multi-model via LiteLLM-class bridges; Codex can be exposed as MCP tools.
- **Harness implication:** Good multi-agent orchestration layer when Codex/OpenAI is the worker; thin abstraction, frequent 0.x iteration — pin versions.

### 4.4 PydanticAI

- **Type-safe Python agents:** tools/IO as types; validation shifts errors left; durable execution + OTel in 2.x; multi-provider.
- **Harness implication:** Best when harness correctness = schema correctness (structured outcomes, eval harnesses).

### 4.5 CrewAI

- **Role-based crews + Flows:** fast multi-agent prototypes; Flows add deterministic branching around autonomous crews.
- **Harness implication:** Great for role theater demos; production needs Flow discipline + external eval — not a substitute for SDLC evidence gates.

### 4.6 Microsoft Agent Framework

- **Successor to AutoGen + Semantic Kernel agent investment (1.x):** graph workflows, middleware, YAML declarative agents, Python + .NET, Foundry deploy, OTel.
- **AutoGen maintenance mode** for new features — migrate narrative is official.
- **Harness implication:** Default for enterprise Microsoft shops; pair with A2A/MCP as ecosystem protocols.

### 4.7 Mastra

- **TypeScript-first:** agents + graph workflows (then/branch/parallel), RAG, evals, 40+ model routing, HITL suspend/resume; Apache-2.0 core.
- **Harness implication:** Leading TS product framework alongside Vercel AI SDK agent abstractions (`ToolLoopAgent` / `HarnessAgent` wrapping Claude Code or Codex loops).

---

## 5. Cross-cutting patterns (elite extract candidates)

| Pattern | Why it compounds | Adaptoid relevance |
|---|---|---|
| Plan → approve → Act | Reduces wrecked repos | Already core; keep as host-agnostic gate |
| AGENTS.md nested precedence | Monorepo truth | Keep; document closest-wins |
| Skills progressive disclosure | Context budget | Emit valid SKILL.md; trigger-rich descriptions |
| Hooks as policy | Format/lint/security without prompt hope | Map FM / validators to hooks |
| Subagents with isolated context | Parallel research without poisoning main thread | Orchestrator/subagent model |
| MCP as tool plane + blast radius | One integration, many hosts | FM-20; dual MCP version support |
| Headless `-p` / CI agents | Automation without GUI | ship-check, preflight, routines |
| Model-specific harness tuning | Same tools, different prompts | Don’t assume one system prompt fits all models |
| Evidence or it didn’t happen | Agents lie confidently | Tests, logs, command output in HANDOFF |
| Host churn (rename/acquire) | Gemini→Antigravity, Windsurf→Devin, Continue→Cursor | Depend on standards not brand |

---

## 6. Explicit non-claims / gaps (honesty)

This wave **did not**:

- Run Terminal-Bench / SWE-bench locally or verify every vendor score.
- Audit every MCP SEP or implement 2026-07-28 clients.
- Inventory all 60k AGENTS.md files or all skills registries.
- Deep-dive Copilot, Devin cloud internals, Amazon Q, Jules, Amp, Factory, Kiro, Zed, etc.
- Produce legal/compliance review of Grok Build open-source dump or retention policies.
- Map pricing accurately (prices move weekly).

**Coverage remains ≪ 1%.** Next waves should rotate: community (HN/Reddit), benchmarks, security/OAP, Karpathy/Boris loop engineering primaries, enterprise multi-agent case studies.

---

## 7. Suggested adopt / watch / refuse (research-only)

| Stance | Item | Note |
|---|---|---|
| **Adopt (already aligned)** | AGENTS.md, Skills, MCP client discipline, Plan/Act, evidence gates | Stay compatible with agents.md + agentskills.io |
| **Watch** | MCP 2026-07-28 final; A2A production meshes; Antigravity enterprise; Grok Build OSS evolution | Breaking changes + host renames |
| **Watch** | Claude Agent SDK / Codex-as-MCP / DeepAgents as product runtimes | Overlap with Adaptoid Core mission |
| **Refuse (for now)** | Host-proprietary-only instruction formats as *sole* source of truth | Always keep portable AGENTS.md |
| **Refuse** | Treating star counts or single vendor blog scores as proof of done | Evidence from our validators only |

---

## 8. Source index pointer

Full URL registry appended in:

`docs/research/era-ocean/sources/INDEX.md` → section **W1 Hosts/Models/Standards**.
