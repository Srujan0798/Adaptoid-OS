# Wave partial C — LangGraph + DeepAgents · Claude Agent SDK demos · OpenAI Agents SDK orchestration

| Field | Value |
|---|---|
| Wave | `wave-20260718-0837-C-langgraph-deepagents` |
| Agent | ERA-OCEAN partial **C** |
| Date (UTC) | 2026-07-18 |
| Status | **Partial research draft** — ocean open; not product doctrine |
| Scope | LangGraph runtime + Deep Agents harness; Claude Agent SDK demos patterns; OpenAI Agents SDK multi-agent orchestration; framework-vs-host-harness decision rules for Adaptoid |
| Files touched | **This file only** |
| Coverage honesty | **≪ 1%** of each stack. Primary docs scraped 2026-07-18; APIs and demos churn weekly. **No claim** of production benchmarks, private lab harnesses, or full demo code review. |

> **Honesty contract:** This is a **scrape + synthesis** slice, not a finished map. LangChain’s own comparison page was last drafted **2026-04-16** (they invite issue reports if products changed). Claude demos are explicitly **local-only, not production**. OpenAI Agents SDK surface is dual-homed (platform docs + `openai.github.io/openai-agents-python`). Treat version pins, release tags, and “managed vs self-host” claims as **verify-before-adopt**.

---

## Mission question

What **elite, portable patterns** do the three big “build agents in code” ecosystems encode — and **when should Adaptoid use a framework runtime vs lean on the host harness** (Claude Code / Codex / Grok Build / Cursor / Antigravity) that already ships the production coding loop?

---

## Executive thesis (for Adaptoid)

1. **Three layers keep getting conflated.** LangChain’s product taxonomy is the cleanest public vocabulary:
   - **Framework** = agent loop abstractions + model/tool integrations (LangChain, OpenAI Agents SDK, Vercel AI SDK, …)
   - **Runtime** = durable execution, streaming, HITL interrupts, persistence (LangGraph, Temporal, Inngest, …)
   - **Harness** = opinionated batteries: planning, FS, subagents, context offload, skills (Deep Agents, Claude Agent SDK, Manus-class systems)

2. **Deep Agents is not “LangGraph with marketing.”** It is an **agent harness on top of** LangGraph (via LangChain `create_agent` building blocks). LangGraph alone is the low-level **orchestration runtime**. Choosing wrong layer = either reimplementing Claude-Code-shaped tools by hand, or over-constraining with a graph when a host CLI would win.

3. **Claude Agent SDK ≈ Claude Code as a library.** Same tools/loop/context management as the CLI; demos show product shapes (research multi-agent, WebSocket chat, plan-mode UX, session V2). Vendor coupling is **model + loop quality**, not just an API client.

4. **OpenAI Agents SDK is deliberately thin.** Few primitives (Agent, tools, handoffs / agents-as-tools, guardrails, sessions, sandbox agents, tracing). Orchestration splits into **LLM-decided** vs **code-decided** — same tradeoff Adaptoid already makes with outer SDLC loops vs model ReAct.

5. **Adaptoid’s durable edge is above all three.** Mission rules, evidence gates, AGENTS.md / skills / MCP policy, HANDOFF replace-state, blast-radius, multi-host swap. Frameworks are **weapons and runtimes**; hosts are **fields**; Adaptoid is **mission OS**. Do not reimplement Claude Code or Deep Agents inside Core. **Steal patterns; keep portable contracts.**

---

## Layer map (shared vocabulary)

| Layer | Job | Examples (this wave) | Adaptoid analogue |
|---|---|---|---|
| Weights / model | Propose tokens + tool calls | Claude, GPT-5.x, Gemini, local tool-calling models | “Weapon” — swappable |
| Framework | Standard agent loop, tools, middleware | LangChain `create_agent`; OpenAI Agents SDK | Optional product stack for **generated** apps |
| Runtime | Durable graph, checkpoint, interrupt, stream | **LangGraph** | Outer loop persistence if product needs multi-day threads |
| Harness | Opinionated long-horizon agent | **Deep Agents**, **Claude Agent SDK**, coding CLIs | Host harness when *building the kit*; product harness when *shipping an agent product* |
| Host / field | Interactive + CI coding surface | Claude Code, Codex, Cursor, Grok Build, Antigravity | Primary execution surface for kit maintainers |
| Mission OS | Gates, evidence, multi-host rules | **Adaptoid Core** | Never replace with a vendor framework |

LangChain’s own “when to use” cut (paraphrased from official products page):

| Use | When |
|---|---|
| **LangChain** | Fast start; standard models/tools/loop; team conventions |
| **LangGraph** | Custom orchestration shape; durable/long-running; mix deterministic + agentic steps |
| **Deep Agents** | Long-horizon, multi-step, non-deterministic tasks needing planning + FS + subagents + context engineering out of the box |

---

## 1. LangGraph — agent **runtime** (not the full harness)

### Primary sources

- Docs: https://docs.langchain.com/oss/python/langgraph/overview  
- Persistence / interrupts: https://docs.langchain.com/oss/python/langgraph/persistence · https://docs.langchain.com/oss/python/langgraph/interrupts  
- GitHub: https://github.com/langchain-ai/langgraph  
- Stack fit: https://docs.langchain.com/oss/python/concepts/products  

### What it is (official claims, mid-2026)

- **Low-level orchestration framework and runtime** for long-running, stateful agents and workflows.
- **Not** an opinionated agent product: does not abstract prompts/architecture the way a harness does.
- Central capabilities called out in overview:
  - **Persistence** (survive failures; resume)
  - **Human-in-the-loop** (inspect/modify state)
  - **Memory** (thread short-term + cross-session long-term concepts)
  - **Streaming**
  - **Production deploy** path via LangSmith ecosystem
- Ecosystem pairing: LangChain components for models/tools are common but **not required**. Higher-level start → LangChain agents; batteries-included long-horizon → **Deep Agents**.

### Elite patterns (portable, not LangGraph-branded)

| Pattern | Mechanism | Why elites care | Adaptoid take |
|---|---|---|---|
| **Checkpoint + thread ID** | Checkpointer persists graph state; config carries `thread_id` | Resume after crash, pause, deploy restart | Outer loops need durable “where we were”; don’t invent a weaker checkpointer for product threads |
| **Interrupt as HITL syscall** | `interrupt()` saves state and waits for external input | Approval gates without killing the run | Map to Adaptoid blast-radius / human gates (FM-20 class), not chat “are you sure?” |
| **Store vs checkpointer** | Checkpointer = thread progress; store = cross-thread facts | Separates session RAM from long-term disk | Matches disk memory / HANDOFF vs ephemeral chat |
| **Custom graph when ReAct is wrong** | Explicit nodes/edges for deterministic + agentic mix | Open-ended agent loops lose on cost/latency for fixed pipelines | Use graph (or code) for **SDLC stages**; use agent only where non-determinism pays |
| **Subgraphs** | Nested orchestration | Modular multi-agent without prompt soup | Prefer few specialists + clear interfaces over mega-graph |
| **Honest durability caveat** | Community + vendor critiques: checkpoint ≠ Temporal-grade durable execution | Idempotency / side-effect replay can burn production | Treat money/side-effect tools as **non-replayable** unless you design for it |

### When LangGraph is the right tool

- You are **shipping an agent product** with multi-hour/day workflows, pause/resume, multi-tenant threads, and custom control flow.
- You need **typed streaming** and production tracing (often LangSmith) as first-class ops.
- The **agent loop itself is the product shape** (research pipeline, approval workflow, multi-actor system) — not “edit this monorepo.”

### When LangGraph is the wrong tool

- You are **maintaining Adaptoid kit or a normal app repo** and the host harness (Claude Code / Codex / Grok Build) already owns tools, FS, git, hooks, skills.
- You only need a **single ReAct loop + tools** — LangChain `create_agent` or OpenAI Agents SDK is lighter.
- You want Claude-Code-grade coding autonomy **without** reimplementing sandbox, permissions, and context engineering.

---

## 2. Deep Agents — batteries-included **harness** on LangGraph

### Primary sources

- Overview: https://docs.langchain.com/oss/python/deepagents/overview  
- Comparison vs Claude Agent SDK: https://docs.langchain.com/oss/python/deepagents/comparison (draft dated **2026-04-16** — re-verify)  
- GitHub: https://github.com/langchain-ai/deepagents (~26k★ at scrape; MIT)  
- JS: https://github.com/langchain-ai/deepagentsjs  
- From-scratch course (pattern pedagogy): https://github.com/langchain-ai/deep-agents-from-scratch  
- UI: https://github.com/langchain-ai/deep-agents-ui  
- Quickstarts: now under `deepagents/examples` (old `deepagents-quickstarts` repo **archived / moved**)  
- Productized coding agent on the harness: **Deep Agents Code (`dcode`)** — https://docs.langchain.com/oss/python/deepagents/code/overview  

### Positioning (official)

Deep Agents is marketed as an **open source agent harness**:

> Opinionated defaults for long-horizon, multi-step work; extensible without forking; model-agnostic; production path via LangGraph + LangSmith.

FAQ hierarchy (GitHub README paraphrase):

1. **LangGraph** = graph runtime  
2. **LangChain `create_agent`** = minimal harness  
3. **Deep Agents** = opinionated harness on top of that stack (filesystem, sub-agents, context management, skills, planning)

Layers **compose**: a custom LangGraph `CompiledStateGraph` can plug in as a Deep Agent sub-agent.

### Built-in capability clusters (elite “deep agent” DNA)

From official overview + from-scratch course — these three patterns are the **shared elite skeleton** across Manus / Claude Code / Deep Agents:

| Cluster | Built-ins (Deep Agents) | Pattern name |
|---|---|---|
| **Planning / recitation** | `write_todos` with pending / in_progress / completed in state | Task planning so the model re-grounds mid-run |
| **Context offload** | Virtual FS (`ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`, …); summarization; large tool-result eviction | Disk is memory; chat is cache |
| **Context isolation** | `task` tool → ephemeral subagents with fresh windows; return summary only | Subagent delegation |
| **Execution env** | Tools + MCP; pluggable backends; sandboxes (`execute`); QuickJS interpreter (`eval`) | Action surface with isolation knobs |
| **Steering** | LangGraph interrupts / HITL approval on sensitive tools | Human in the loop |
| **Memory / skills** | `AGENTS.md`-style memory always loaded; Agent Skills progressive disclosure (`SKILL.md`) | Intent debt reduction |
| **Streaming** | Typed streams + `stream.subagents` for nested work | Ops visibility |

**Security model (explicit):** Deep Agents follows **“trust the LLM”** — enforce boundaries at **tool/sandbox/permission** layers, not by hoping the model self-polices. Aligns with Adaptoid soft-vs-hard rules.

### Backends & permissions (production-relevant)

- FS backends: in-memory state, local disk, LangGraph store, composite, custom.
- Declarative **permissions** (allow/deny read/write path globs, first-match-wins). **Does not apply to sandbox backends** that expose shell `execute` — different threat model.
- Two sandbox connection patterns (LangChain blog + comparison page):
  1. **Agent inside sandbox** (Claude Agent SDK default shape)
  2. **Agent outside; sandbox as tool** (remote execute) — Deep Agents supports both; comparison claims Claude Agent SDK only the first (self-host path). **Managed** Anthropic agents may differ — re-verify.

### Deep Agents vs Claude Agent SDK (LangChain comparison — use carefully)

| Axis | Deep Agents (LangChain claim) | Claude Agent SDK (LangChain claim) |
|---|---|---|
| Model | Any tool-calling provider | Claude ecosystem (Anthropic / Bedrock / Vertex / Azure paths) |
| Execution backend | Pluggable | Local FS of the sandbox the agent runs in |
| Multi-tenancy | Built-in scoped threads / per-user sandboxes / RBAC story | Build yourself |
| Deploy | Managed Deep Agents in LangSmith **or** self-host image via `langgraph build` | Self-host server/auth/stream yourself; managed agents = separate product |
| License | MIT | SDK MIT; Claude Code proprietary |

**Bias warning:** This table is **vendor comparison from LangChain**, last noted draft **April 2026**. Treat as hypothesis; re-read Anthropic hosting + Managed Agents docs before architecture decisions.

### Deep Agents from scratch — pedagogical gold

Course reduces “deep” agents to implementable LangGraph lessons:

1. ReAct `create_agent` baseline  
2. TODO / `write_todos` planning  
3. Virtual filesystem in state  
4. Subagents + `task` isolation  
5. Full research agent composition  

**Adaptoid lesson:** You do not need the `deepagents` package to learn the patterns — but for product ship velocity, the package is the packaged form of those patterns.

### When to use Deep Agents

- Building a **multi-step product agent** (research, ops, document pipelines) that needs plan + FS + subagents **without** committing to Anthropic-only loop.
- Need **model swap** (frontier + open-weight + local) under one harness.
- Want LangGraph deploy/trace story (LangSmith) with harness defaults.

### When **not** to use Deep Agents (for Adaptoid)

- **Kit development / coding-agent work on this repo:** host harness wins (hooks, worktrees, native git UX, CLAUDE.md/AGENTS.md dual-read).
- You only need thin tool loop → OpenAI Agents SDK or LangChain `create_agent`.
- You need **Claude Code parity** and are already Anthropic-locked → Claude Agent SDK may be higher loop quality for coding (vendor co-training of model+harness).

---

## 3. Claude Agent SDK + demos — host harness as library

### Primary sources

- Agent SDK overview: https://code.claude.com/docs/en/agent-sdk/overview (also platform.claude.com / docs.claude.com mirrors)  
- Python: https://github.com/anthropics/claude-agent-sdk-python  
- TypeScript: https://github.com/anthropics/claude-agent-sdk-typescript  
- **Demos (exists, public):** https://github.com/anthropics/claude-agent-sdk-demos (~2.7k★ at scrape)  
- Related wave context: hosts/models research already notes SDK ≈ Claude Code programmable twin  

### What the SDK is

- Same **tools, agent loop, and context management** that power **Claude Code**, programmable in Python + TypeScript.
- Contrast with Client SDK: you do **not** write the tool-while loop; the harness runs it.
- Contrast with CLI: same capabilities; SDK for CI/CD, custom apps, production automation; CLI for interactive dev.
- Contrast with **Managed Agents**: hosted REST (Anthropic runs agent + sandbox) vs library-in-your-process.

### Built-in surface (capability checklist)

| Area | Examples |
|---|---|
| Tools | Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch, Monitor, AskUserQuestion, Agent, … |
| Hooks | PreToolUse, PostToolUse, Stop, SessionStart/End, UserPromptSubmit, … |
| Subagents | `AgentDefinition` / agents map; `parent_tool_use_id` for nested tracking |
| MCP | Local/server configs (e.g. Playwright) |
| Permissions | `allowed_tools`, `disallowed_tools`, permission modes, `canUseTool` |
| Sessions | Capture `session_id`, resume, fork |
| FS config | Skills, CLAUDE.md memory, plugins, setting_sources |

### Demo catalog patterns (`claude-agent-sdk-demos`)

> **Caveat (README):** demos are **for local development only** — not production/scale.

| Demo | Pattern for Adaptoid / products |
|---|---|
| **hello-world** | Minimal `query` / options; baseline smoke |
| **hello-world-v2** | **Session API V2** (`unstable_v2_*`): separate `send()` / `stream()` vs single `query()` generator; multi-turn + session persistence |
| **research-agent** | **Lead agent** decomposes → parallel **Researcher** subagents (WebSearch + Write to notes) → **Data Analyst** (charts) → **Report Writer** (PDF via Skill). Artifacts on disk (`files/research_notes|charts|reports`). **Hooks** for pre/post tool tracking; `parent_tool_use_id` links subagent tool calls. Structured `tool_calls.jsonl` + transcript |
| **simple-chatapp** | React + Express + **WebSocket** streaming conversation loop — product UI shell |
| **ask-user-question-previews** | `AskUserQuestion` with `previewFormat: "html"`; round-trip via WebSocket; **plan mode steering** toward clarify-before-act |
| **email-agent** | IMAP inbox + agentic search (domain vertical) |
| **excel-demo** | Spreadsheet artifact loop |
| **resume-generator** | Web search → structured document artifact (`.docx`) |

### Elite patterns distilled from demos + SDK docs

1. **Filesystem is the shared bus** between lead agent and subagents (notes → charts → report). Same as Deep Agents offload; same as Adaptoid HANDOFF/disk memory.  
2. **Lead owns topology; specialists own tools.** Researchers don’t write the final PDF; writer doesn’t search. Matches OpenAI “specialists excel at one task.”  
3. **Hooks = hard policy and observability.** Soft prompt rules without Pre/Post hooks are theater for audit/blast-radius.  
4. **Session resume is a first-class product API** (especially V2 stream split).  
5. **Plan / clarify UX** (AskUserQuestion + previews) is product harness, not model magic.  
6. **Slash commands / skills** package recurring missions (`/research`, `/competitive-analysis`) — map to Adaptoid skills / protocols.  
7. **Evidence logs:** tool_calls.jsonl is the right shape for “evidence or it didn’t happen.”

### When to use Claude Agent SDK

- Product or automation needs **Claude Code loop quality** (coding + general computer-use style work) inside your process.
- CI headless agents, custom UIs, multi-agent research products **on Anthropic models**.
- You already pay the Anthropic ecosystem tax and want **one harness** shared with interactive Claude Code.

### When not to

- Multi-provider model strategy as core requirement → Deep Agents / OpenAI Agents / host-agnostic skills layer.
- Adaptoid **kit** work: prefer host CLI + AGENTS.md; use SDK only if building a product *on* the loop.
- Need managed multi-tenant agent server out of the box without building hosting (evaluate Managed Agents / LangSmith separately).

---

## 4. OpenAI Agents SDK — thin framework + orchestration primitives

### Primary sources

- Platform agents guide: https://developers.openai.com/api/docs/guides/agents  
- Orchestration (platform): https://developers.openai.com/api/docs/guides/agents/orchestration  
- Python docs site: https://openai.github.io/openai-agents-python/  
- Multi-agent / orchestration: https://openai.github.io/openai-agents-python/multi_agent/  
- GitHub: https://github.com/openai/openai-agents-python · https://github.com/openai/openai-agents-js  
- Patterns examples: `examples/agent_patterns` in the Python repo  
- Evolution note: https://openai.com/index/the-next-evolution-of-the-agents-sdk/ (Apr 2026 — sandbox-aware harness direction)  
- Historical: Swarm → Agents SDK (Mar 2025 announcement lineage)

### Core design

**Few primitives:**

- **Agents** — LLM + instructions + tools  
- **Agents as tools / handoffs** — multi-agent coordination  
- **Guardrails** — parallel validation; fail fast  
- Plus: agent loop, MCP tools, sessions, HITL, tracing, **sandbox agents**, realtime/voice paths  

**Design principles (official):** enough features to be worth using; few enough to learn quickly; works OOTB; customizable.

**Agents SDK vs Responses API:**

| Use Responses API directly | Use Agents SDK |
|---|---|
| You own loop, tool dispatch, state | Runtime manages turns, tools, guardrails, handoffs, sessions |
| Short-lived model response | Multi-step artifacts / coordinated work |
| | Real workspace / resumable sandbox agents |

### Orchestration doctrine (elite, explicit)

Official split:

#### A. Orchestrating via LLM (open-ended)

Agent has tools + handoffs; plans autonomously.

| Pattern | Behavior | Best when |
|---|---|---|
| **Agents as tools** | Manager keeps conversation control; specialists via `Agent.as_tool()` | Manager owns final answer; combine specialist outputs; shared guardrails in one place |
| **Handoffs** | Triage routes; specialist becomes active agent for the turn | Specialist should speak to user; focused prompts; no manager narration tax |

Tactics listed by OpenAI:

1. Invest in prompts (tools, parameters, bounds)  
2. Monitor and iterate  
3. Allow introspect/improve (loops, critique, error feedback)  
4. **Specialists > generalists**  
5. Invest in **evals**

#### B. Orchestrating via code (deterministic)

- Structured outputs → code routes next agent  
- **Chains** (research → outline → draft → critique → improve)  
- **While** maker/checker until evaluator passes  
- **Parallel** (`asyncio.gather`) for independent work  

**Mix freely.** Same as Adaptoid: outer loop in code; inner loop in model.

### 2026 direction (sandbox harness)

“Next evolution” messaging pushes Agents SDK toward **long-horizon, filesystem/sandbox, memory, Codex-like tools** — convergence with Deep Agents / Claude Agent SDK shape. Treat as **trajectory**: the thin Swarm-era SDK is growing harness features; re-read sandbox agents docs before assuming “thin forever.”

### When to use OpenAI Agents SDK

- Multi-agent **product** logic with clean handoff/manager patterns and OpenAI (or multi-provider via models layer) stack.
- Want **guardrails + tracing + evals** integration with OpenAI ops suite.
- Prefer **Python-first orchestration** over learning a graph DSL.
- Sandbox-isolated coding/document agents under OpenAI’s client/workspace model.

### When not to

- Non-OpenAI coding host is primary (Claude Code day-to-day) — don’t force dual harnesses for the same job.
- Complex durable graph with many interrupts — LangGraph may fit better.
- Need maximum model portability + packaged deep-agent middleware today → Deep Agents.

---

## 5. Cross-cut comparison (framework / runtime / harness / host)

| Concern | LangGraph | Deep Agents | Claude Agent SDK | OpenAI Agents SDK | Host CLIs (CC/Codex/Grok/…) |
|---|---|---|---|---|---|
| Abstraction height | Low runtime | High harness | High harness (vendor) | Mid framework | High interactive harness |
| Durable threads | Core job | Via LangGraph | Sessions / hosting you build | Sessions + sandbox resume | Session/resume per product |
| Multi-model | Yes | Strong story | Claude-centric | OpenAI-centric + providers | Host-specific |
| Coding ergonomics | DIY | `dcode` + tools | **Best-in-class if Claude** | Growing sandboxes | **Best for humans-in-repo** |
| Multi-agent | Graphs/subgraphs | `task` subagents | Agent tool + demos | Handoffs + as_tool | Subagents / teams |
| HITL | Interrupts | interrupt_on | Permissions + AskUser | Guardrails + HITL APIs | Approval modes |
| MCP | Via LC stack | Yes | Yes | Yes | Yes |
| Skills / AGENTS.md | Partial / via apps | First-class | CLAUDE.md + skills | Skills tools trajectory | Native |
| Adaptoid fit | Generated long-run products | Generated deep agents | Anthropic product path | OpenAI product path | **Default for kit SDLC** |

---

## 6. Elite decision matrix for Adaptoid

### Rule 0 — Separate three products

| You are… | Default surface |
|---|---|
| Maintaining **Adaptoid kit** / generated project code in a repo | **Host harness** (Claude Code, Codex, Grok Build, Cursor, Antigravity) + Adaptoid gates |
| Shipping a **customer-facing multi-step agent app** | Framework/runtime/harness stack (pick one spine below) |
| Encoding **portable mission rules** | Adaptoid Core only (AGENTS.md, skills, protocols, evidence) — never vendor-lock kernel |

### Rule 1 — Framework vs host harness

| Signal | Prefer **host harness** | Prefer **framework/runtime/harness** |
|---|---|---|
| Primary user | Engineer in repo | End user / API / background worker |
| Success metric | Diff quality, tests, ship-check | Task completion, latency, multi-tenant SLOs |
| Tool surface | Git, FS, terminal, IDE | Domain tools + controlled sandbox |
| Session model | Worktrees, PRs, HANDOFF files | Thread IDs, checkpointers, sessions |
| Autonomy | Human review bandwidth limited | Product autonomy slider |
| Model strategy | Swap hosts/models weekly | Pin stack for supportability |

### Rule 2 — Pick a spine for agent **products** (not for kit)

| Spine | Choose if… |
|---|---|
| **Claude Agent SDK** | Claude loop quality is the moat; coding-like tools; Anthropic OK |
| **Deep Agents + LangGraph** | Multi-model; need packaged deep patterns + durable deploy story |
| **LangGraph alone** | Custom control flow; harness patterns DIY or minimal |
| **OpenAI Agents SDK** | Handoff/manager clarity; OpenAI ops/evals; Python-first thin core |
| **Host-only + scripts** | Internal automation; Ralph-style outer loops; no multi-tenant product |

### Rule 3 — Steal these patterns into Adaptoid **without** adopting packages in kernel

| Pattern | Source | Adaptoid encoding (conceptual) |
|---|---|---|
| TODO recitation | Deep Agents / from-scratch | Task lists in HANDOFF / wave state; not endless chat |
| Context offload to disk | All three | Artifacts + HANDOFF rewrite; context rot control |
| Subagent isolation | All three | Maker ≠ checker; sparse subagents; return summaries |
| Manager vs handoff | OpenAI | Orchestrator owns answer vs specialist owns conversation |
| Code vs LLM orchestration | OpenAI + LangGraph | SDLC stages in code; agent only where needed |
| Hooks as hard gates | Claude SDK demos | Soft rules + validators/hooks; FM-20 for high blast tools |
| Interrupt/HITL | LangGraph / Deep Agents | Explicit human gates; no silent money/remote |
| Tool allowlists + FS permissions | Deep Agents / Claude | Deny-by-default tools; path ACLs |
| Evals as training signal | OpenAI tactics | Golden tasks; ship-check; not vibes |
| Trust boundary at tools | Deep Agents security note | Sandbox + policy; never “model promised” |

### Rule 4 — What Adaptoid must **refuse**

- **Hardcoding** LangGraph / Deep Agents / Agents SDK as the only way to run Core.  
- Replacing **evidence gates** with framework “agent said done.”  
- Treating vendor comparison pages as neutral truth.  
- Deploying Anthropic demos’ patterns to production without auth, tenancy, and rate limits.  
- Assuming checkpoint resume is safe for **non-idempotent** side effects.

### Rule 5 — Adopt / watch / refuse (this wave)

| Item | Verdict | Notes |
|---|---|---|
| Deep-agent triad (plan, FS offload, subagents) | **Adopt (concept)** | Already aligned with elite/HARNESS waves |
| Host harness for kit SDLC | **Adopt (default)** | Confirmed by hosts wave |
| Deep Agents package in Core | **Watch / refuse for kernel** | Optional stack hint for *generated* agent products only |
| LangGraph as Core engine | **Refuse for kernel** | OK as generated-project backend |
| Claude Agent SDK for products | **Watch / adopt per product** | Strong coding harness; Anthropic coupling |
| OpenAI handoff vs as_tool doctrine | **Adopt (concept)** | Document in multi-agent playbooks |
| Managed LangSmith / Managed Claude agents | **Watch** | Hosting tradeoffs; re-verify 2026-Q3 docs |
| `dcode` as Claude Code competitor | **Watch** | Multi-model coding agent on Deep Agents |

---

## 7. Incomplete / unknown (honesty)

| Gap | Why it matters | Next scrape |
|---|---|---|
| Did not run any SDK against live APIs | No latency/cost/quality numbers | Optional eval wave with golden tasks |
| Did not read full demo source trees | Patterns from README + SDK docs only | Spot-read research-agent + chatapp implementations |
| LangChain comparison dated Apr 2026 | May lag Anthropic Managed Agents / hosting | Re-fetch comparison + Anthropic hosting |
| OpenAI sandbox agents depth | Trajectory only; not full sandbox client matrix | Sandbox agents + clients pages |
| Temporal/Inngest vs LangGraph durability debate | Checkpoint critique is real for payments/side effects | Durable execution critique wave |
| CrewAI, Google ADK, LlamaIndex, Mastra, PydanticAI, etc. | Out of this partial’s box | Other partials / later waves |
| Private enterprise harnesses | Invisible | Never claim completeness |
| Version pins | deepagents PyPI latest noted ~0.6.12 (Jun 2026) on GitHub releases UI; docs mention 0.7 alphas for some FS tools — **version churn** | Pin and re-check before scaffolding |

---

## 8. Sources (primary first)

### LangGraph / Deep Agents / LangChain

1. https://docs.langchain.com/oss/python/langgraph/overview  
2. https://docs.langchain.com/oss/python/langgraph/persistence  
3. https://docs.langchain.com/oss/python/langgraph/interrupts  
4. https://docs.langchain.com/oss/python/deepagents/overview  
5. https://docs.langchain.com/oss/python/deepagents/comparison  
6. https://docs.langchain.com/oss/python/concepts/products  
7. https://docs.langchain.com/oss/python/deepagents/code/overview  
8. https://github.com/langchain-ai/langgraph  
9. https://github.com/langchain-ai/deepagents  
10. https://github.com/langchain-ai/deepagentsjs  
11. https://github.com/langchain-ai/deep-agents-from-scratch  
12. https://github.com/langchain-ai/deep-agents-ui  
13. https://github.com/langchain-ai/deepagents-quickstarts (archived → examples in main repo)

### Claude Agent SDK / demos

14. https://code.claude.com/docs/en/agent-sdk/overview  
15. https://github.com/anthropics/claude-agent-sdk-demos  
16. https://github.com/anthropics/claude-agent-sdk-python  
17. https://github.com/anthropics/claude-agent-sdk-typescript  
18. Research-agent README (raw): `anthropics/claude-agent-sdk-demos` → `research-agent`

### OpenAI Agents SDK

19. https://developers.openai.com/api/docs/guides/agents  
20. https://developers.openai.com/api/docs/guides/agents/orchestration  
21. https://openai.github.io/openai-agents-python/  
22. https://openai.github.io/openai-agents-python/multi_agent/  
23. https://github.com/openai/openai-agents-python  
24. https://openai.com/index/new-tools-for-building-agents/  
25. https://openai.com/index/the-next-evolution-of-the-agents-sdk/

### Secondary / critique (not primary truth)

26. Durability critiques of checkpoint-style systems (e.g. Diagrid “checkpoints aren’t durable execution” class arguments) — use as risk checklist, not vendor ranking.

### Related Era Ocean waves (in-repo context, not external)

- `docs/research/era-ocean/waves/wave-20260718-w1-harness-loop-os.md`  
- `docs/research/era-ocean/waves/wave-20260718-w1-hosts-models-standards.md`  
- `docs/research/era-ocean/elite/ELITE-10-PERCENT.md`  

---

## 9. One-page summary for merge into elite distill

**Deep agents everywhere converge on:** plan/TODO · offload to filesystem · isolate with subagents · hard gates at tools · eval/monitor loops.

**LangGraph** = durable **runtime**. **Deep Agents** = multi-model **harness** on that runtime. **Claude Agent SDK** = Claude Code **as library** (+ demos of multi-agent research, streaming UI, plan UX). **OpenAI Agents SDK** = thin **framework** with explicit **handoff vs manager** orchestration + code-side loops.

**Adaptoid default:** host harness for kit SDLC; portable patterns (disk state, maker≠checker, hooks, sparse tools) in Core; optional framework spine only for **generated agent products**, never as kernel identity.

---

*End partial C. Coverage remains ≪1%. Do not mark Era Ocean complete.*
