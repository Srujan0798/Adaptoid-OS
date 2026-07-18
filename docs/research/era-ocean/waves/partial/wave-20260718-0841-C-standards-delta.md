# Partial Wave C — Standards Delta (2026-07-18-0841)

| Field | Value |
|---|---|
| Wave | `wave-20260718-0841-C-standards-delta` |
| Agent | ERA-OCEAN partial **C** (W4) |
| Category | Weekly-style **standards delta** — AGENTS.md · Agent Skills · MCP |
| Status | **PARTIAL / INCOMPLETE** — mid-2026 snapshot from official primaries only; not a full standards map |
| Coverage honesty | Primaries opened live. No exhaustive host matrix re-walk, no SDK tier re-score, no A2A deep dive, no full SEP catalog audit this session. |
| Files written | **Only** this file |

---

## Mission question

What changed **mid-2026** on the three portable rails — **AGENTS.md**, **Agent Skills (`SKILL.md`)**, **MCP** — that a **host-agnostic harness** must know before it claims portability?

---

## Executive delta (elite, one screen)

1. **Three rails, one foundation orbit.** AGENTS.md + MCP sit under **Agentic AI Foundation (AAIF) / Linux Foundation** project surfaces; Agent Skills is an open Anthropic-origin format with multi-host client gravity. Portable harnesses ship **policy file + skill packs + tool plane**, not host-private instruction filenames.
2. **AGENTS.md is social law, not schema.** Plain Markdown, **no required fields**, nested nearest-wins, chat overrides. ~**60k+** public repos (site claim). Stewarded by AAIF. Migration path still `AGENT.md` → `AGENTS.md` + symlink.
3. **Skills are context economics.** Progressive disclosure (metadata → body → scripts/refs) is the product; `name`/`description` contract + `skills-ref validate` are the compliance floor. `allowed-tools` remains **experimental**.
4. **MCP `2026-07-28` is the hard break.** RC locked **2026-05-21**; final target **2026-07-28**. Stateless core, no `initialize` handshake, no `Mcp-Session-Id`, explicit handles for app state, extensions first-class (Apps + Tasks), OAuth/OIDC hardening, Roots/Sampling/Logging deprecated. Dual-stack window is mandatory for any production client/server.
5. **Harness implication.** Adaptoid-class systems treat these as **SDLC surfaces**: AGENTS.md = mission policy, Skills = on-demand expertise packs, MCP = high-blast-radius tool plane (FM-20). Do not freeze on `2025-11-25` session semantics.

---

## 1. AGENTS.md — official primary

**Primary:** [https://agents.md/](https://agents.md/)  
**Stewardship:** Agentic AI Foundation (AAIF) under Linux Foundation — [aaif.io](https://aaif.io/) · project [aaif.io/projects/agents-md](https://aaif.io/projects/agents-md/)  
**Origin ecosystem:** Collaborative push including OpenAI Codex, Amp, Google Jules, Cursor, Factory (site About).

### What it is (stable contract)

- **"README for agents"** — dedicated, predictable place for build/test/style/security/PR instructions that would clutter human READMEs.
- **Format:** standard Markdown. **No required fields.** Any headings; agent parses the text you give.
- **Placement:** root `AGENTS.md`; monorepos use **nested** files per package/subproject.
- **Precedence law:** closest `AGENTS.md` to the edited file wins; **explicit user chat prompts override everything**.
- **Behavior expectation:** if you list test/lint commands, agents **will attempt** them and fix failures before finishing (site FAQ).
- **Adoption signal:** site claims **60k+** open-source projects with an `AGENTS.md` path (GitHub code search linked from home).

### Mid-2026 portable-harness must-knows

- **Do not invent a third proprietary instruction filename** without an adapter. Host-local files (`CLAUDE.md`, rules dirs) may dual-read; the **portable** unit is still `AGENTS.md`.
- **Nested > monolithic dump.** OpenAI monorepo cited with **88** AGENTS.md files at time of writing on the official page — monorepo harnesses must discover **nearest** file, not only root.
- **Content that compounds:** exact install/dev/test commands with flags; one-test patterns; PR title format; security gotchas; package-local names. Avoid dumping full style guides agents should get from linters.
- **Migration still first-class:** `mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`. Aider: `read: AGENTS.md` in `.aider.conf.yml`. Gemini CLI-class: `context.fileName: "AGENTS.md"` in settings JSON (site FAQ).
- **AAIF gravity:** AGENTS.md is a listed AAIF project alongside MCP, goose, agentgateway — instruction files are infrastructure, not a blog meme.

### Incomplete / not covered here

- Per-host discovery quirks (when a host prefers CLAUDE.md / `.cursor/rules` over AGENTS.md).
- Empirical quality of the 60k corpus (many thin scaffolds vs living policy).
- Conflict resolution when AGENTS.md and Skills disagree (chat still wins; harness policy may need explicit rank).

---

## 2. Agent Skills — agentskills.io

**Home:** [https://agentskills.io/home](https://agentskills.io/home)  
**Spec:** [https://agentskills.io/specification](https://agentskills.io/specification)  
**Repo / validate:** [github.com/agentskills/agentskills](https://github.com/agentskills/agentskills) · `skills-ref validate ./my-skill`  
**Clients:** [https://agentskills.io/clients](https://agentskills.io/clients) (large multi-vendor showcase; counts rise — treat as order of magnitude)

### What it is (stable contract)

A skill is a **directory** with required `SKILL.md` (YAML frontmatter + Markdown body) plus optional:

```
skill-name/
├── SKILL.md          # required
├── scripts/          # optional executables
├── references/       # optional on-demand docs
├── assets/           # optional templates/resources
└── ...
```

### Frontmatter (harness compliance floor)

| Field | Required | Constraints (spec) |
|---|---|---|
| `name` | Yes | ≤64 chars; `a-z0-9-` only; no leading/trailing/consecutive hyphens; **must match parent directory name** |
| `description` | Yes | ≤1024 chars; what **and when**; keyword-rich for discovery |
| `license` | No | Name or bundled license file |
| `compatibility` | No | ≤500 chars; env / product / network needs |
| `metadata` | No | Arbitrary string→string map (unique keys recommended) |
| `allowed-tools` | No | Space-separated pre-approved tools — **experimental** |

### Progressive disclosure (the real product)

1. **Discovery** — load only `name` + `description` (~100 tokens) for all skills at startup.  
2. **Activation** — load full `SKILL.md` body when task matches description (recommend **&lt;5k tokens / &lt;500 lines**).  
3. **Execution** — run scripts / read `references/` / use `assets/` only as needed.

Body has **no format restrictions**. Prefer step-by-step + examples + edge cases. Keep references **one level deep** from `SKILL.md` (no deep nested chains).

### Mid-2026 portable-harness must-knows

- **Skills ≠ always-on rules.** Rules/AGENTS.md = policy budget; Skills = optional expertise without context bloat. Wrong packing → silent token tax or never-activated skills.
- **Description is the trigger surface.** "Helps with PDFs" fails discovery; task + keyword rich descriptions succeed. Harness skill-emit must treat description quality as product.
- **Validate in CI:** `skills-ref validate` checks frontmatter + naming. Ship gate for generated skill packs.
- **`allowed-tools` is not portable yet.** Experimental; support varies. Do not assume host enforcement equals Adaptoid policy engine.
- **Client gravity is real:** showcase spans Claude Code, Claude, Codex, Cursor, Copilot/VS Code, OpenCode, Goose, Amp, Factory, JetBrains Junie, OpenHands, Roo, Kiro, enterprise data agents (Databricks, Snowflake, …), and many OSS CLIs. Portable skill packs pay off.
- **Community surface growing:** official Discord; open development on GitHub. Anthropic-origin open standard, ecosystem-owned evolution.

### Incomplete / not covered here

- Host-specific install paths (`~/.claude/skills`, `.cursor/skills`, plugins, marketplaces).
- Security of third-party skill marketplaces / supply chain (skill = untrusted instructions + scripts).
- Draft **"Skills over MCP"** extension on MCP draft overview (structured skills via tool plane) — named on draft home; not deep-read this session.

---

## 3. MCP — Model Context Protocol (latest RC + draft)

**Site / draft:** [https://modelcontextprotocol.io/specification/draft](https://modelcontextprotocol.io/specification/draft)  
**Changelog vs 2025-11-25:** [https://modelcontextprotocol.io/specification/draft/changelog](https://modelcontextprotocol.io/specification/draft/changelog)  
**RC blog (canonical narrative):** [https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)  
**AAIF companion (dev impact, 2026-07-16):** [aaif.io MCP 7-28 article](https://aaif.io/blog/introducing-mcp-7-28-for-ai-application-developers-what-goes-away-and-what-might-break/)  
**Extensions overview:** [https://modelcontextprotocol.io/extensions/overview](https://modelcontextprotocol.io/extensions/overview)  
**Schema repo:** [github.com/modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)

### Status clock (as of this wave)

| Milestone | Date / note |
|---|---|
| Previous finalized rev | **`2025-11-25`** (still latest **final** until ship day) |
| RC locked | **2026-05-21** |
| Final target | **2026-07-28** (`2026-07-28` protocol version) |
| Working name | "MCP 7-28" (AAIF community) |
| Character | **Largest revision since launch**; intentional **breaking** changes |

> AAIF ambassador write-up (2026-07-16): re-verify wording once final ships; SEPs cited as Final, revision as RC.

### 3.1 Stateless core — what a portable harness must rewire

**Gone (breaking):**

- `initialize` / `initialized` handshake (**SEP-2575**).
- Protocol-level session + `Mcp-Session-Id` (**SEP-2567**).
- Sticky-session assumption for horizontal Streamable HTTP.

**Now:**

- Every request is **self-contained**: protocol version, client capabilities, clientInfo travel in `_meta` keys (`io.modelcontextprotocol/...`).
- New **`server/discover`** for capability/version advertisement (clients MAY call up front; STDIO compat probe).
- App state = **explicit handles** returned by tools and passed as ordinary arguments (`basket_id`, `search_handle`, …) — visible to the model, not hidden in transport.
- Server-to-client mid-call work restructured: server-initiated requests only while processing a client request (**SEP-2260**); Multi Round-Trip Requests (**SEP-2322**) return `InputRequiredResult` / `resultType: "input_required"` with `inputRequests` + `requestState`; client retries original call with `inputResponses`.
- All results carry required **`resultType`**: `"complete"` | `"input_required"` (omit ⇒ treat as complete for older servers).
- Streamable HTTP: **`Mcp-Method` + `Mcp-Name` headers required** (**SEP-2243**); body/header mismatch rejected.
- List/read results: **`ttlMs` + `cacheScope`** (**SEP-2549**) for client/intermediary caching.
- W3C Trace Context in `_meta` documented (`traceparent`, `tracestate`, `baggage`) (**SEP-414**).
- SSE stream **resumability / Last-Event-ID redelivery removed** — broken stream ⇒ re-issue as **new request ID**.
- Subscriptions: GET + `resources/subscribe` replaced by **`subscriptions/listen`** long-lived POST-response stream with typed opt-ins.
- Removed: `ping`, `logging/setLevel`, `notifications/roots/list_changed`; per-request log level via `_meta` instead.
- Resource-not-found error: **`-32002` → `-32602`** (Invalid Params).

### 3.2 Extensions become first-class

**SEP-2133:** reverse-DNS extension IDs, `extensions` capability map, independent versioning, `ext-*` repos, Extensions Track in SEP process. Opt-in; disabled by default.

**Official / notable extensions (draft + RC):**

| Extension | Role |
|---|---|
| **MCP Apps** (`ext-apps`, SEP-1865) | Server-rendered interactive HTML UI in sandboxed iframe; tools declare UI templates for prefetch/security review; UI actions share JSON-RPC audit/consent path |
| **Tasks** (`io.modelcontextprotocol/tasks`, SEP-2663) | Long-running work as extension (was experimental core in 2025-11-25). Server may return task handle from `tools/call`; client drives `tasks/get`, `tasks/update`, `tasks/cancel`. **No `tasks/list`** (sessionless scoping). Server-directed creation when client advertises extension |
| **Skills over MCP** (named on draft overview) | Structured skill instructions discovered/consumed through MCP — watch; not deep-read here |
| Auth extensions | OAuth client credentials; enterprise-managed authorization (`ext-auth`) |

Anyone who shipped **2025-11-25 experimental Tasks** must migrate lifecycle.

### 3.3 Authorization hardening (OAuth / OIDC reality)

Six SEPs align HTTP MCP auth with production OAuth/OIDC:

- **MUST** validate `iss` on auth responses when present (**RFC 9207**, SEP-2468); future versions may reject missing `iss`.
- Declare OIDC **`application_type`** on Dynamic Client Registration (SEP-837) — fixes desktop/CLI localhost redirect defaults.
- Credentials bound to **issuer**; re-register on AS migration (SEP-2352).
- Refresh-token guidance for OIDC-style AS (SEP-2207); step-up scope accumulation (SEP-2350); `.well-known` discovery suffix clarity (SEP-2351).
- **DCR (RFC 7591) deprecated** as preferred registration path in favor of **Client ID Metadata Documents** (PR #2858); DCR remains for back-compat AS.

Local stdio still different threat model than internet-exposed Streamable HTTP — do not collapse them in harness policy.

### 3.4 Deprecations (annotation-only for now)

| Feature | Replacement direction |
|---|---|
| **Roots** | Tool params, resource URIs, server config/env — Roots never were real ACLs |
| **Sampling** | Host/agent or direct provider APIs — clear responsibility for model calls, cost, injection |
| **Logging** | `stderr` (stdio); **OpenTelemetry** for structured observability |
| HTTP+SSE (legacy transport) | Streamable HTTP (reclassified under lifecycle policy) |
| Sampling `includeContext` thisServer/allServers | omit or `"none"` |

**Lifecycle policy (SEP-2596):** Active → Deprecated → Removed with **≥12 months** between deprecation and earliest removal. Conformance suite + SDK tier system gate Standards Track Final (SEP-2484 / SDK tiers).

### 3.5 Tool contracts

- Full **JSON Schema 2020-12** for `inputSchema` / `outputSchema` (SEP-2106): composition, conditionals, `$ref`/`$defs`; input root still object; `structuredContent` any JSON value.
- **MUST NOT** auto-dereference external `$ref` URIs; bound depth/validation time.
- `tools/list` **SHOULD** be deterministic order (prompt-cache friendliness).

### 3.6 Security trust principles (draft — still non-negotiable)

Draft security section: user consent/control; data privacy; tool safety — **tool descriptions/annotations untrusted** unless server is trusted; hosts obtain consent before tool invoke. Protocol cannot enforce; implementors **SHOULD**.

Complementary (not re-walked this partial): official security best practices tutorial (confused deputy, token passthrough, local MCP compromise) — see prior ocean waves.

---

## 4. What a portable harness must do (checklist)

### AGENTS.md rail

- [ ] Emit/maintain root + nested AGENTS.md; discovery = **nearest wins**, chat overrides.
- [ ] Prefer executable commands over essay style guides.
- [ ] Dual-read host-local files only as adapters; never require a fourth invent-your-own policy file for "portability."

### Skills rail

- [ ] Ship skills as directories with valid `name`/`description`; CI via `skills-ref validate`.
- [ ] Keep SKILL.md under ~500 lines; progressive disclosure structure mandatory.
- [ ] Treat skill scripts as **code** (review, pin, quarantine) — same blast-radius class as tools.
- [ ] Do not depend on experimental `allowed-tools` for security boundaries.

### MCP rail (pre/post 2026-07-28)

- [ ] **Dual-support window:** clients/servers may speak `2025-11-25` and `2026-07-28` during migration.
- [ ] Stop assuming session stickiness; design tools with **explicit handles**.
- [ ] Plan for MRTR / `input_required` instead of open SSE elicitation holds.
- [ ] Gate MCP Apps UI templates (prefetch + sandbox review) before host render.
- [ ] Tasks: implement extension lifecycle if long-running work needed; drop reliance on `tasks/list` / experimental core API.
- [ ] Auth: validate `iss`, issuer-bound credentials, no token passthrough, audience-bound tokens.
- [ ] Observability: OTel + stderr — not protocol Logging as primary ops plane.
- [ ] Error handling: update `-32002` resource-miss matchers → `-32602`.
- [ ] Keep MCP write/network tools **high blast radius** (Adaptoid FM-20) regardless of protocol version.

---

## 5. Delta table (mid-2026 vs late-2025 mental model)

| Topic | Late-2025 / 2025-11-25 mental model | Mid-2026 must-know |
|---|---|---|
| Repo policy | Host-specific CLAUDE.md / rules | **AGENTS.md** as portable README-for-agents + nested precedence; AAIF project |
| Packaged workflows | Prompt snippets, custom slash commands | **SKILL.md** open format + progressive disclosure + multi-host clients |
| MCP transport session | `initialize` + `Mcp-Session-Id` + sticky LB | **Stateless** self-contained requests; `server/discover` |
| Cross-call state | Hidden in session | **Explicit tool handles** |
| Long-running work | Experimental Tasks in core | **Tasks extension**; poll/update/cancel; no list |
| Interactive UI | Mostly not standardized | **MCP Apps** extension (sandboxed HTML) |
| Roots / Sampling / Logging | Core features | **Deprecated**; migrate off |
| Auth | Uneven remote story | OAuth/OIDC hardening + CIMD preferred over DCR |
| Tool schema | Limited schema dialect | Full **JSON Schema 2020-12** |
| Protocol evolution | Ad-hoc breaks | **Lifecycle policy** + extensions track + conformance |

---

## 6. Sources (primaries)

| ID | Source | URL |
|---|---|---|
| P1 | AGENTS.md official | https://agents.md/ |
| P2 | AAIF home / projects | https://aaif.io/ · https://aaif.io/projects/agents-md/ |
| P3 | Agent Skills home | https://agentskills.io/home |
| P4 | Agent Skills specification | https://agentskills.io/specification |
| P5 | Agent Skills clients | https://agentskills.io/clients |
| P6 | MCP draft specification | https://modelcontextprotocol.io/specification/draft |
| P7 | MCP draft changelog | https://modelcontextprotocol.io/specification/draft/changelog |
| P8 | MCP 2026-07-28 RC blog | https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ |
| P9 | MCP extensions overview | https://modelcontextprotocol.io/extensions/overview |
| P10 | AAIF MCP 7-28 developer impact (2026-07-16) | https://aaif.io/blog/introducing-mcp-7-28-for-ai-application-developers-what-goes-away-and-what-might-break/ |

Secondary (context only, not re-validated end-to-end this partial): prior ocean wave `wave-20260718-w1-hosts-models-standards.md` §2; MCP security best practices tutorial.

---

## 7. Incomplete — explicit non-claims

- Did **not** re-fetch every SEP PR body; relied on RC blog + draft changelog + AAIF summary.
- Did **not** measure SDK Tier 1 readiness vs 2026-07-28 RC on the wire.
- Did **not** deep-read Skills-over-MCP extension schema or Apps security sandbox formal model.
- Did **not** map A2A / agentgateway / goose AAIF siblings beyond name recognition.
- Did **not** produce Adaptoid code changes — research trench only.
- Final MCP wording may still drift until **2026-07-28** ship; re-open P6–P8 after final publish.

---

## 8. One-line product cut for Adaptoid

**Portable mission OS = AGENTS.md (policy) × Skills (expertise packs) × MCP (tool plane with dual-version + handle-first + high blast-radius gates).** Everything else is host adapter.
