# Partial Wave B — DeepSeek + Moonshot Kimi (agent / coding APIs)

| Field | Value |
|---|---|
| Wave ID | `wave-20260718-0837-B-deepseek-kimi` |
| Partial | **B** (DeepSeek + Moonshot/Kimi only) |
| Date (UTC) | 2026-07-18 |
| Researcher | ERA-OCEAN agent B (Grok Build subagent) |
| Scope | Official product + API docs: DeepSeek agent/coding surfaces; Moonshot Kimi (`kimi-k3`, `kimi-k2.7-code`, tool/agent loops); open-weight deployment notes |
| Method | Primary docs via live page fetch (`api-docs.deepseek.com`, `platform.kimi.ai`, HF model cards) |
| Coverage honesty | **≪ complete.** Snapshot of official rails only — not evals, not regional China endpoints, not every host plugin, not infra ops for 1T/1.6T self-host. |
| Product link | Distill later into `elite/` + `ADAPTATION.md` only when proven in Adaptoid gates |

> **Method note:** Bullets are **harness-relevant** (tools, context, coding agents, open-weight loops). Marketing benchmarks quoted only when they expose a harness pattern (e.g. preserve-thinking, dynamic tools).

---

## Executive read (for Adaptoid)

1. **Both vendors sell “weapon + host sockets,” not a full mission OS.** DeepSeek and Kimi ship OpenAI- and Anthropic-compatible chat APIs + first-class host integration recipes (Claude Code, OpenCode, Codex, Kimi Code CLI). The **agent loop stays on the client**; the model emits `tool_calls` + optional `reasoning_content`.
2. **The elite shared contract is `reasoning_content` re-injection under tool use.** Drop CoT on a tool turn → 400 / broken multi-step agents. Non-tool multi-turn may *drop* CoT (DeepSeek) or *always keep* it (Kimi K2.7 Code). Harness must branch on this rule per model SKU.
3. **Kimi’s dynamic tool loading is the strongest published anti–tool-bloat pattern** among open Chinese API vendors: start with `search_tools` + core tools, inject full schemas via `role: system` + `tools` mid-conversation (K3 only). Maps cleanly to Adaptoid progressive tool disclosure / MCP skill loading.
4. **Open weights are real product strategy, not side notes.** DeepSeek-V4 (MIT) and Kimi-K2.7-Code (Modified MIT) ship HF weights + vLLM/SGLang paths. That enables **self-hosted agent loops** with the same OpenAI-shaped client contract — Adaptoid can treat “official API vs local OpenAI-compat” as a deployment mode, not a rewrite.
5. **Cost/context knobs are first-class harness inputs:** 1M context (DeepSeek V4, Kimi K3) vs 256K coding SKUs; automatic prefix/context cache; Flash/highspeed for subagents; effort `max` for coding hosts.

---

## 1. DEEPSEEK — official API & agent surface

### 1.1 Identity & dual wire format

**Primary:** https://api-docs.deepseek.com/ · pricing https://api-docs.deepseek.com/quick_start/pricing/

| Param | Value |
|---|---|
| OpenAI base | `https://api.deepseek.com` |
| Anthropic base | `https://api.deepseek.com/anthropic` |
| Current models | `deepseek-v4-pro`, `deepseek-v4-flash` |
| Legacy (retire **2026-07-24 15:59 UTC**) | `deepseek-chat` → V4-Flash non-thinking; `deepseek-reasoner` → V4-Flash thinking |

- **Harness implication:** One provider, two SDKs. Hosts that only speak Anthropic (Claude Code) and hosts that only speak OpenAI both plug in with env/base_url swaps — no custom protocol.
- **Context:** **1M** standard for both V4 models; **max output 384K**. Thinking default-on; dual thinking / non-thinking.
- **Pricing shape (per 1M tokens, official table):** cache-hit input is orders of magnitude cheaper than miss (Flash $0.0028 hit vs $0.14 miss; Pro $0.003625 vs $0.435); output Flash $0.28 / Pro $0.87. Concurrency: Flash 2500 / Pro 500. **Stable system + tool prefixes + multi-turn append = money and latency.**

### 1.2 Thinking mode + multi-turn tool loop (critical)

**Primary:** https://api-docs.deepseek.com/guides/thinking_mode/ · tools https://api-docs.deepseek.com/guides/tool_calls/

- Toggle: OpenAI `thinking: {type: enabled|disabled}` (+ SDK often via `extra_body`); Anthropic maps effort via `output_config.effort`.
- Effort: `reasoning_effort` `high` \| `max`. Defaults `high`; **complex agent hosts (Claude Code, OpenCode) auto-map to `max`**. Compat: `low`/`medium` → `high`, `xhigh` → `max`.
- Thinking mode **ignores** `temperature` / `top_p` / presence/frequency penalties (no error if set — silent no-op). Don’t build sampling-based gates on thinking turns.
- CoT returns as `reasoning_content` sibling of `content`.
- **Context concatenation rules (elite):**
  - **No tool call** between user turns: prior `reasoning_content` **need not** be resent (API ignores if sent).
  - **Any tool call** in a turn: that assistant’s `reasoning_content` **must** be passed on **all subsequent** requests in the conversation — omit → **HTTP 400**.
- Official sample loop: `while True` create → append full assistant message → if `tool_calls` execute → append `role: tool` with `tool_call_id` → continue until no tools. Multi-sub-turn reasoning *inside one user question* is the designed pattern (date tool then weather tool before final answer).
- **Harness implication:** Adaptoid tool runtime must treat “assistant message serialization” as **full object dump** (`content` + `reasoning_content` + `tool_calls`), not content-only. Model-specific policy table: DeepSeek = *conditional* preserve CoT.

### 1.3 Tool calls + `strict` schema mode

**Primary:** https://api-docs.deepseek.com/guides/tool_calls/

- Classic OpenAI tools array; **model does not execute tools** — client must.
- **`strict` mode (beta):** `base_url=https://api.deepseek.com/beta`; each function `strict: true`; server validates JSON Schema; requires all properties in `required`, `additionalProperties: false` for objects. Supported schema surface: object/string/number/integer/boolean/array/enum/anyOf + `$def`/`$ref` (recursive ok). String: `pattern` + limited `format` (email/hostname/ipv4/ipv6/uuid); no min/maxLength. Array: no min/maxItems.
- Parallel tool calls historically advertised (legacy FC notes: up to 128 functions, parallel).
- **Harness implication:** Prefer strict tools for high-blast-radius Adaptoid actions (shell, git write, payments). Schema constraints = free policy layer before your own validators.

### 1.4 Context caching (disk prefix units)

**Primary:** https://api-docs.deepseek.com/guides/kv_cache/

- **Default on**, zero client API for cache create/TTL.
- Hits require **full match of a persisted cache prefix unit** (SWA-era behavior differs from naive “byte prefix”).
- Persist triggers: (1) request boundaries (end of user input + end of model output), (2) common-prefix detection across requests, (3) fixed token intervals on long I/O.
- Multi-round chat that **appends** after shared prefix hits; forked divergences after shared stem need a second request before stem becomes its own unit.
- Response `usage`: `prompt_cache_hit_tokens` / `prompt_cache_miss_tokens`.
- **Harness implication:** Pin system prompt, tool defs, and long static packs at the **front**; mutate only the tail. Measure hits in ship-check / cost dashboards.

### 1.5 Coding / agent host integrations (official)

**Primary:** https://api-docs.deepseek.com/quick_start/agent_integrations/claude_code/ · V4 notes https://api-docs.deepseek.com/news/news260424/

Documented / claimed agent sockets:

| Host | Integration pattern |
|---|---|
| **Claude Code** | `ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic` + DeepSeek key as `ANTHROPIC_AUTH_TOKEN`; model `deepseek-v4-pro[1m]`; **Haiku tier + `CLAUDE_CODE_SUBAGENT_MODEL` → `deepseek-v4-flash`**; `CLAUDE_CODE_EFFORT_LEVEL=max` |
| **Claude Desktop (dev mode)** | Name mapping: `claude-opus*` → V4-Pro; `claude-haiku*` / `claude-sonnet*` → V4-Flash |
| **OpenCode / OpenClaw / in-house DeepSeek agents** | V4 release: “seamlessly integrated… already driving our in-house agentic coding” |
| **GitHub Copilot** (docs mention) | Listed among supported agent tools on quickstart |

- **Native Web Search in Claude Code path:** when the host decides search is needed, DeepSeek API runs search + summary LLM turns → **extra token cost** called out explicitly.
- FIM completion (beta) + chat prefix completion (beta) on pricing feature matrix — **FIM non-thinking only** (useful for IDE completion hosts, not full agent loops).
- **Harness implication:** Official recipe encodes **two-tier model routing** (Pro main, Flash subagent) — same Brain/Hands cost discipline as Adaptoid TWO-TIER. Steal the env matrix as a pack template for multi-host BYOK.

### 1.6 Open weights loop (DeepSeek-V4)

**Primary:** https://api-docs.deepseek.com/news/news260424/ · HF https://huggingface.co/collections/deepseek-ai/deepseek-v4 · e.g. https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro

- **Open-sourced preview:** V4-Pro **1.6T total / 49B active**; V4-Flash **284B / 13B active**; tech report PDF on HF; **MIT** weights (per model card / secondary confirmations).
- Structural claims relevant to long agent context: token-wise compression + **DSA (DeepSeek Sparse Attention)** for 1M-context efficiency.
- Marketing: open-source SOTA agentic coding; integrated with Claude Code / OpenClaw / OpenCode.
- **Harness implication:** Self-host path = same OpenAI-shaped loop + local vLLM/SGLang (ecosystem). Treat open weights as **blast-radius / data-residency mode**, not a different agent architecture. Verify tool-call templates on local engines — they lag official API edge cases (`strict`, Anthropic shim).

### 1.7 Gaps / honesty (DeepSeek)

- No first-party “DeepSeek Agent SDK” equivalent to Claude Agent SDK in the scraped docs — **you own the loop**.
- Historical instability notes on older FC (looped/empty calls) still circulate; V4 claims agent polish — **verify with evals**, don’t trust release copy.
- Did not fully scrape rate-limit isolation, Anthropic Messages parity matrix, or every agent_integrations subpage beyond Claude Code.

---

## 2. MOONSHOT KIMI — official API, coding SKUs, agent products

### 2.1 Platform identity & model ladder

**Primary:** https://platform.kimi.ai/docs/overview · models https://platform.kimi.ai/docs/models · index https://platform.kimi.ai/docs/llms.txt

| Model | Role | Context | Notes |
|---|---|---|---|
| **`kimi-k3`** | Flagship (2.8T params claimed) | **1M** | Always reasons; `reasoning_effort` currently **only `"max"`**; native vision; recommended for Claude Code / knowledge work |
| **`kimi-k2.7-code`** | Dedicated coding / long-horizon SE | **256K** | Thinking **always on**; ~30% less thinking tokens vs K2.6 (vendor); multimodal tool demos |
| **`kimi-k2.7-code-highspeed`** | Same as 2.7-code, speed SKU | **256K** | ~180 tok/s (up to ~260 short context); resource-limited / may fluctuate |
| **`kimi-k2.6`** | General agent + vision | **256K** | Thinking optional; supports Preserved Thinking via `thinking.keep` |
| **`kimi-k2.5`** | Prior multimodal agentic | **256K** | Sunset path for new users; full sunset **2026-08-31** with moonshot-v1 series |

- Global OpenAI-compat base: `https://api.moonshot.ai/v1` · env `MOONSHOT_API_KEY`.
- Anthropic-compat for hosts: `https://api.moonshot.ai/anthropic`.
- **Harness implication:** Pick **K3 for 1M mission context / dynamic tools**; pick **K2.7-Code for coding-agent throughput**; highspeed for interactive CLI feel. Don’t assume one param set across SKUs.

### 2.2 Thinking / Preserved Thinking (SKU matrix)

**Primary:** https://platform.kimi.ai/docs/guide/use-kimi-k2-thinking-model

| Field | K3 | K2.7-Code | K2.6 | K2.5 |
|---|---|---|---|---|
| `reasoning_effort` | `"max"` only | n/a | n/a | n/a |
| `thinking.type` | always on (API shape differs) | **only `enabled`** | enabled default / can disable | enabled default / can disable |
| Preserved thinking | must re-send full assistant msg | **always on, cannot disable** | opt-in `thinking.keep="all"` | **not supported** |

- Multi-step tool rules: keep in-loop `reasoning_content`; `max_tokens` ≥ 16k recommended so CoT+answer aren’t truncated; **do not set temperature** on K2.7-Code / K2.6 thinking (fixed 1.0 / top_p 0.95 — other values **error**); prefer streaming for large CoT payloads.
- OpenAI SDK often lacks typed `reasoning_content` → use `hasattr` / `getattr` or raw HTTP.
- **K2.7-Code tool constraints:** `tool_choice` only **`auto` \| `none`** (forced named tool / `required` can conflict with reasoning); multi-step **must** retain reasoning in context or error.
- **Harness implication:** Model adapter layer needs a **ThinkingPolicy** enum: `conditional_preserve` (DeepSeek), `always_preserve` (K2.7-Code), `opt_in_preserve` (K2.6), `always_reason_effort_max` (K3). One size fits none.

### 2.3 Tool calling + agent loop (official recipe)

**Primary:**  
- Tool guide: https://platform.kimi.ai/docs/guide/use-kimi-api-to-complete-tool-calls  
- Build agent: https://platform.kimi.ai/docs/guide/use-kimi-k3-to-setup-agent  
- Tool choice: https://platform.kimi.ai/docs/guide/use-tool-choice  
- Best practices: https://platform.kimi.ai/docs/guide/kimi-k3-tool-calling-best-practice  

Elite patterns from official agent sample:

- **Stage the mission:** Retrieve → Analyze → Deliver (tools for retrieval/determinism; model for judgment). Don’t restate tool behavior in long system prompts — put args in JSON Schema.
- **Schema hygiene:** `additionalProperties: false` + complete `required` lists.
- **Loop mechanics:** append **complete** assistant message (preserve `reasoning_content`); every tool result carries matching `tool_call_id`; **cap rounds** (`MAX_TOOL_ROUNDS = 8` in sample) — iterative loop, not recursive stack; on tool failure return error JSON as tool content and **continue sibling calls**; treat `finish_reason=length` as hard failure, not final answer.
- **tool_choice:** first turn `"required"` to force retrieval/search; then `"auto"`. Changing tool_choice **does not** invalidate prefix cache (per K3 best practices).
- Function name regex (API tool-use docs): `^[a-zA-Z_][a-zA-Z0-9-_]{2,63}$`; parameters root must be JSON Schema subset (**MFJS**).

### 2.4 Dynamically loaded tools (elite harness concept)

**Primary:** https://platform.kimi.ai/docs/guide/use-dynamic-tool-loading · best practices above

- Problem named in docs: **Tool Definition Bloat** — all schemas every request → tokens + wrong-tool selection.
- Pattern:
  1. Top-level `tools` = only `search_tools` + small always-on core set.
  2. System prompt advertises searchable domains/tags.
  3. Optional first-turn `tool_choice: "required"`.
  4. On search hits, inject **full** tool defs via mid-history message: `{ "role": "system", "tools": [ ... ] }` — **no `content` on that message** (content+tools → 400).
  5. Dynamic tools coexist with global tools; visibility starts at injection position.
- Client-owned retention: server does **not** remember dynamic tools; re-send for cache-friendly continuity or drop to shrink context (cache miss risk after edit point).
- **K3 only** — other models (e.g. K2.6) → tokenization failure.
- **Harness implication:** Highest-value import for Adaptoid. Map to MCP server catalogs / skill registries: **search → inject → act**, not “dump 200 tools in every Brain call.”

### 2.5 Official tools = Formula runtime

**Primary:** https://platform.kimi.ai/docs/guide/use-official-tools

- Platform runs tools as **Formulas** (URI `moonshot/<name>:latest`): declaration + sandboxed Python implementation; host schedules isolation/billing.
- Discovery: `GET /formulas/{uri}/tools` → OpenAI-shaped tools array.
- Execution: `POST /formulas/{uri}/fibers` with `{name, arguments}`; success → `context.output` or **encrypted_output** (pass ciphertext back as tool result for protected tools like web-search).
- Catalog (docs table): `web-search`, `fetch`, `code_runner`, `excel`, `date`, `convert`, `memory`, `quickjs`, `base64`, `rethink`, …  
  **Caveat:** docs warn web-search path is being updated / may be temporarily unreliable.
- **Harness implication:** Two-plane design — **Chat Completions (decide)** + **Formula fibers (execute platform tools)** + **local functions (execute your tools)**. Same shape as Adaptoid Hands with mixed MCP/local executors.

### 2.6 Multimodal tools (coding + vision agents)

**Primary:** https://platform.kimi.ai/docs/guide/kimi-k2-7-code-quickstart

- Official sample: tool returns **list of multimodal content blocks** (`video_url` + `text`) as `role: tool` content — not only strings.
- Agent loop watches video clips via ffmpeg, feeds base64 video back into the model mid-loop.
- Limits: images ≤ ~4K res; video ≤ 1080p; large media → **Files API** not giant request bodies; base64 images only (URL images not supported on vision path in this guide); request body soft cap ~100M.
- **Harness implication:** Tool result type system must allow **structured multimodal content**, not `str` only — affects logging, redaction, and evidence store.

### 2.7 Context caching (automatic)

**Primary:** https://platform.kimi.ai/docs/guide/use-context-caching-feature-of-kimi-api

- Automatic for all models; no cache IDs/TTL APIs.
- Best for fixed front matter: system rules, knowledge packs, **stable tool defs**.
- Guidance vs RAG: caching for frequent fixed context; RAG for huge unfixed corpora.
- Multi-turn: put large fixed content **early** in `messages`.
- Dynamic tool injection notes: append new tool system messages at end to preserve prefix cache; editing earlier tool decls can break hits.
- **Harness implication:** Same discipline as DeepSeek — immutable prefix packs. Aligns with Adaptoid “replace, never append state” *for session files*, but **append-only tails** for model messages.

### 2.8 Coding agent products & host sockets

| Product / host | URL / docs | Harness signal |
|---|---|---|
| **Kimi Code CLI** | https://www.kimi.com/code · platform guide https://platform.kimi.ai/docs/guide/kimi-code-cli | First-party terminal agent; `/login` to platform API key; model picker; recommended framework for K2.7-Code on HF card |
| **Claude Code + Kimi** | https://platform.kimi.ai/docs/guide/claude-code-kimi | Full env matrix: `ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic`, models `kimi-k3[1m]` or 2.7-code; **`ENABLE_TOOL_SEARCH=false`** (not supported on endpoint); **`CLAUDE_CODE_AUTO_COMPACT_WINDOW`** must match context (1048576 vs 262144); effort `max`; clean stale `~/.claude/settings.json` env overrides |
| **Codex CLI** | https://platform.kimi.ai/docs/guide/codex-kimi | Official K3 path |
| **OpenCode** | https://platform.kimi.ai/docs/guide/open-code | Built-in auth to Kimi platform |
| **Hermes / OpenClaw** | platform guides | Agent product demos for K3 multimodality |
| **GitHub Copilot** | product news / secondary | K2.7-Code called out as **first open-weight model in Copilot** model picker (Jul 2026 era) — distribution win for open weights |

- K2.7-Code in Claude Code: **Tab → Thinking on** required; WebSearch without thinking → `400 invalid thinking`; WebFetch may be unavailable on Anthropic shim — use MCP scrape instead.
- **Harness implication:** Host integrations fail on **tier model env completeness** (haiku/subagent/fable) and **compact window mismatch**. Adaptoid multi-host packs should ship complete env matrices per model+host pair, not a single `MODEL=` line.

### 2.9 Open weights loop (Kimi K2.7 Code)

**Primary:** https://huggingface.co/moonshotai/Kimi-K2.7-Code · deploy notes on card

- **1T MoE / 32B active**, 256K context, MLA attention, MoonViT 400M, native INT4 path like K2-Thinking.
- License: **Modified MIT**.
- Deploy engines: **vLLM, SGLang, KTransformers**; transformers `>=4.57.1,<5`.
- Forces thinking + preserve_thinking; Instant mode **not** supported; temp 1.0 / top_p 0.95 recommended for local.
- Agent evals (vendor table, treat as claims): Kimi Code Bench, Program Bench, MCP Atlas / MCPMark, long-horizon “Claw 24/7” via OpenClaw harness.
- **Harness implication:** Self-host coding agent = Kimi Code CLI or OpenAI-compat server + your loop. Preserve-thinking is non-optional in the model’s product design — don’t strip CoT to save tokens without measuring task fail rate.

### 2.10 Gaps / honesty (Kimi)

- K3 dynamic tools are the crown jewel but **K3-only** — coding SKU 2.7 may not get the same injection API; confirm before designing around it for code agents.
- Official tool free-tier + rate limits under load; web-search docs self-flag as outdated.
- Partial mode, JSON mode, Batch, MoonPalace debugger, pricing pages not fully extracted this wave.
- China vs global endpoint differences (`platform.moonshot.ai` vs `platform.kimi.ai` / `api.moonshot.ai`) need a dedicated geo wave.

---

## 3. CROSS-CUT — harness concepts (DeepSeek ∩ Kimi)

| Concept | DeepSeek | Kimi | Adaptoid adopt posture |
|---|---|---|---|
| Client-owned tool loop | Yes (canonical samples) | Yes (MAX_TOOL_ROUNDS sample) | **Adopt** as Core runtime invariant |
| Dual OpenAI + Anthropic wire | Yes | Yes (Claude Code path) | **Adopt** for multi-host BYOK |
| Reasoning re-injection | Conditional on tool turns | Always (K2.7) / full msg (K3) | **Adopt** per-model policy table |
| Automatic context cache | Disk prefix units + hit metrics | Auto prefix; cache-aware dynamic tools | **Adopt** prefix discipline + cost telemetry |
| Strict / schema tools | `strict` beta | Schema + MFJS + additionalProperties false | **Adopt** for high blast-radius tools |
| Dynamic tool inventory | Not documented as first-class | **K3 dynamic system.tools** | **Watch → pilot** on Brain tool plane |
| Official host recipes | Claude Code, OpenCode, … | Claude Code, Codex, OpenCode, Kimi Code CLI | **Adopt** env pack templates |
| Open weights + local loop | V4 MIT 1M-context MoE | K2.7-Code Modified MIT 256K | **Watch** for air-gapped Hands |
| Subagent model tiering | Flash for subagents / Pro main | Highspeed code SKU; compact window per model | **Adopt** TWO-TIER cost map |
| Multimodal tool results | Not deep-scraped this wave | First-class video/image tool content | **Watch** for visual verify agents |
| Platform-hosted tools | Web search via Claude Code integration | Formula fibers (code_runner, fetch, …) | **Watch** vs MCP-only purity |

---

## 4. Elite 10% bullets (distill candidates)

1. **Full assistant message append is the real protocol.** If your harness strips to `{role, content}`, thinking+tool models will die mid-mission.
2. **Tool Definition Bloat is a solved problem in public docs (Kimi K3):** search → inject complete schemas → act. MCP marketplaces that dump every server’s tools every turn are doing it wrong.
3. **Cache is a first-class harness design constraint**, not a billing footnote. Immutable prefixes (system + tools + long packs); mutate only the tail.
4. **Two-tier models are industry default for agent hosts:** Pro/K3/main for judgment; Flash/highspeed/subagent for cheap fan-out. Encode in pack config.
5. **Host compact windows must equal model context** (`CLAUDE_CODE_AUTO_COMPACT_WINDOW` 1M vs 256K). Wrong value = silent quality death or hard context errors.
6. **Open weights do not remove the need for a harness.** They only move the same OpenAI-shaped loop on-prem; vLLM tool templates and preserve-thinking still need proof.
7. **Cap tool rounds and treat truncation as failure.** Official Kimi agent sample is more honest than most frameworks about infinite tool loops and `finish_reason=length`.
8. **Disable host features the endpoint doesn’t support** (`ENABLE_TOOL_SEARCH=false` on Kimi Anthropic shim). Feature flags are part of the harness, not optional polish.
9. **Strict tool schemas are free safety.** DeepSeek strict beta + Kimi `additionalProperties: false` = validate before execute.
10. **Weapon ≠ host ≠ mission OS.** Both vendors optimize the weapon and publish host plugs; Adaptoid’s edge remains SDLC gates, evidence, blast-radius policy, and multi-host instruction packs.

---

## 5. Sources (URLs)

### DeepSeek (primary)
- https://api-docs.deepseek.com/
- https://api-docs.deepseek.com/quick_start/pricing/
- https://api-docs.deepseek.com/guides/tool_calls/
- https://api-docs.deepseek.com/guides/thinking_mode/
- https://api-docs.deepseek.com/guides/kv_cache/
- https://api-docs.deepseek.com/quick_start/agent_integrations/claude_code/
- https://api-docs.deepseek.com/news/news260424/
- https://api-docs.deepseek.com/api/create-chat-completion/
- https://huggingface.co/collections/deepseek-ai/deepseek-v4
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro

### Moonshot / Kimi (primary)
- https://platform.kimi.ai/docs/overview
- https://platform.kimi.ai/docs/llms.txt
- https://platform.kimi.ai/docs/models
- https://platform.kimi.ai/docs/guide/kimi-k2-7-code-quickstart
- https://platform.kimi.ai/docs/guide/kimi-k3-tool-calling-best-practice
- https://platform.kimi.ai/docs/guide/use-dynamic-tool-loading
- https://platform.kimi.ai/docs/guide/use-kimi-k3-to-setup-agent
- https://platform.kimi.ai/docs/guide/use-kimi-api-to-complete-tool-calls
- https://platform.kimi.ai/docs/guide/use-kimi-k2-thinking-model
- https://platform.kimi.ai/docs/guide/use-official-tools
- https://platform.kimi.ai/docs/guide/use-context-caching-feature-of-kimi-api
- https://platform.kimi.ai/docs/guide/claude-code-kimi
- https://platform.kimi.ai/docs/guide/kimi-code-cli
- https://platform.kimi.ai/docs/guide/use-tool-choice
- https://huggingface.co/moonshotai/Kimi-K2.7-Code
- https://www.kimi.com/code (Kimi Code product / CLI install root)

### Secondary (distribution / corroboration only)
- OpenRouter / Cloudflare Workers AI model cards for K2.7-Code context & agentic feature claims
- GitHub Copilot announcement material re: K2.7-Code open-weight picker (confirm in GH docs before product claims)

---

## 6. Next scrapes (not done this partial)

- DeepSeek Anthropic Messages parity + rate_limit isolation pages
- Full agent_integrations tree (OpenCode, Copilot, OpenClaw exact env)
- Kimi Codex CLI + OpenCode + Hermes guides line-by-line
- Kimi Partial Mode, JSON Mode, Batch, pricing/limits
- Self-host tool-call templates for vLLM/SGLang on V4 + K2.7-Code
- Geo split: moonshot.cn vs kimi.ai global

---

*End partial B. Coverage remains ≪ complete. Do not mark Era Ocean finished.*
