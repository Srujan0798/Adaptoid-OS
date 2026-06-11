# Adaptoid OS v4.0 — Eternal Agentic Harness

> **What this is.** A self-improving, framework-agnostic operating system for agentic AI that treats harness engineering — the control stack surrounding the LLM — as the primary optimization target. It compounds its own reliability forever through runtime validation, persistent living memory, and a sovereign meta-core that hovers above every framework without being captured by any.
>
> **Why a folder, not one file.** A single giant markdown bloats the context window. Agents read it once, then forget the middle, then contradict it. This folder uses **progressive disclosure**: the agent loads only the small kernel always, and pulls in the specific protocol / failure-mode / archetype it needs, when it needs it. This is the actual fix for "the agent forgets everything."
>
> **Version.** v4.0 — Jun 2026. The Eternal Agentic Harness. Supersedes v3.x (kept in `CHANGELOG.md`).

---

## 60-second start

**Option A — Orchestrator-driven (Claude/Kimi):**
1. Open Claude Code or Kimi in an empty folder where you want the project.
2. Paste the contents of [`00-INVOCATION.md`](00-INVOCATION.md).
3. Paste your project brief (PDF text, one paragraph, or one line — anything).
4. The orchestrator detects the **archetype**, picks a **tier**, and generates the full project structure.
5. You open OpenCode CLI worker windows and start shipping.

**Option B — Engine-driven (sovereign, no AI needed):**
```bash
python3 ~/Desktop/OS-Setup/adaptor/engine.py \
  --brief "Convert RFQ PDFs to structured BOQ" \
  --output ./my-project
```
The engine detects archetype, consults the ecosystem library, generates structure, copies validators, and runs preflight — all locally, no network, no AI session required.

That's it. The agent does the rest by reading this folder.

---

## What makes v4.0 different from a normal "starter template"

| Normal template | Adaptoid OS v4.0 |
|---|---|
| Static files you copy | **Adapts** to archetype + tier — via executable engine |
| One big README agents forget | **Progressive disclosure** — kernel always, rest on demand |
| Hopes agents don't make mistakes | **18 failure-modes** — real failures with executable preventions |
| Detects drift but you fix it | **Self-healing validators** — `--fix` auto-resolves drift, stale processes, config revert, artifacts |
| Generic | **11 archetypes** — hackathon, internship, research, SaaS, internal-tool... |
| Trusts agent claims | **Evidence-required** — nothing is "done" without a runnable proof |
| Session dies = lost state | **Durable session log** — `events.jsonl` + `wake.sh` rebuilds context after crash |
| Static ecosystem catalog | **Freshness-enforced library** — stale entries flagged automatically |
| Hopes the kit is correct | **Dogfood** — the kit validates itself before you use it |
| No philosophy | **Three Pillars** — LLM-as-OS, Freedom & Responsibility, Harness Engineering |
| Free-form intent | **Typed PROJECT-INTENT.md** — schema-validated, machine-parseable |
| No route safety | **Route Sentinel** — pre-execution wrong-route blocking |
| No state integrity | **VaultMMU** — SHA-256 hash chain, tamper detection |
| No tool policy | **OAP Security** — deterministic policy enforcement before every tool call |
| Static workflows | **5 core workflows + 3 domain playbooks** — parameterized execution patterns |
| No command surface | **Slash commands** — named, typed, cost-capped orchestrator API |

---

## Folder map

```
OS-Setup/
├── README.md              ← you are here
├── INDEX.md               ← full file map (the agent's navigation table)
├── 00-INVOCATION.md       ← the exact paste-prompt + how adaptation works
├── CHANGELOG.md
│
├── kernel/                ← ALWAYS loaded (small, non-negotiable)
│   ├── PRINCIPLES.md          the 12 laws
│   ├── TWO-TIER.md            orchestrator vs workers; Brain/Hands/Session
│   └── ANTI-HALLUCINATION.md  the rules that stop the specific failures
│
├── failure-modes/         ← ★ the prevention library (load the one you risk)
│   ├── README.md
│   └── FM-01 … FM-15.md       each: symptom · root cause · prevention · validator
│
├── archetypes/            ← ★ the adaptation engine (load the one that matches)
│   ├── README.md
│   └── <archetype>.md         hackathon, internship, research-ml, saas, ...
│
├── protocols/             ← load on demand for a specific operation
│   ├── wave-lifecycle.md  dispatch-protocol.md  review-protocol.md
│   ├── eval-driven-dev.md blast-radius.md  context-budget.md
│   ├── runtime-context-check.md  primary persistence (sovereign/air-gapped)
│   ├── conductor-pattern.md      high-velocity parallel sessions
│   └── verification.md
│
├── tiers/TIERS.md         ← T0–T4 sizing
│
├── adaptor/               ← ★ the executable Adaptoid Engine
│   ├── engine.py              RUN the adaptation (sovereign, no network)
│   ├── ADAPTOR_ENGINE.md      the transform mechanism
│   ├── OUTPUT_SPEC.md         executable-first artifact spec
│   └── EXAMPLE-given-brief-to-output.md
│
├── templates/             ← the files the orchestrator generates
│   └── root/ orchestrator/ work/ specify/ plan/ docs/ evals/ ci/
│
├── validators/            ← ★ executable scripts that PREVENT + HEAL failures
│   ├── preflight.sh           runs all checks (passes --fix/--dry-run through)
│   ├── dogfood.sh             OS-Setup validates itself
│   ├── emit_event.sh          append to durable session log (events.jsonl)
│   ├── replay_session.sh      reconstruct context from events.jsonl
│   ├── wake.sh                crash recovery — rebuild orchestrator state
│   └── validate_*.sh          one per failure mode (all support --fix)
│
├── workflows/             ← parameterized workflow definitions (YAML)
│   ├── core/                    quick-prototype, parallel-execution, long-horizon
│   ├── verification-heavy.yaml  self-improving.yaml
│   └── reference/               domain playbooks (startup-mvp, data-science, hackathon-48h)
│
├── slash-commands/        ← named, typed, cost-capped orchestrator API
│   └── adaptoid/                plan, build, review, qa, retro
│
├── memory-bank/           ← living folder memory (Anti-Forgetting Triad)
│   ├── FACT.template.md         verified truths with TTL
│   ├── LESSON.template.md       post-mortems + crystallized patterns
│   ├── ADR.template.md          architecture decision records
│   └── facts/ decisions/ lessons/ sessions/ evidence/ snapshots/
│
├── philosophy/            ← the Three Pillars
│   ├── LLM-as-OS.md             Karpathy mental model
│   ├── freedom-responsibility.md Netflix culture → agents
│   └── harness-engineering.md   2026 consensus: harness > model
│
├── schemas/               ← machine-readable specs
│   ├── ProjectIntent.schema.json
│   └── AdaptoidConfig.schema.json
│
├── setup/                 ← local-first harness template
│   ├── AGENTIC_OS_PROFILE.md
│   └── harness/                 Docker Compose + Makefile (optional)
│
├── reference/             ← ★ the DevKit LIBRARY (pull-on-demand, like books)
│   ├── HOW-TO-PULL.md          how the orchestrator consults the library
│   ├── mental-models.md        LLM-as-OS + freedom-and-responsibility
│   ├── ecosystem/             the agentic-AI catalog (last 6 months + leaders)
│   │   ├── INDEX.md               card catalog
│   │   ├── SELECTION.md           archetype → recommended stack (decision engine)
│   │   ├── STALE_CHECK.sh         flag stale catalog entries
│   │   ├── coding-agents.md       Claude Code, Cursor, Codex, Cline, Aider, Goose...
│   │   ├── sdks-adks.md           Claude SDK, OpenAI Agents SDK, Google ADK, LangGraph...
│   │   ├── protocols-standards.md MCP, A2A, agentskills.io, AGENTS.md
│   │   ├── skills-catalog.md      the 1000+ skill universe + sources
│   │   ├── tools-compendium.md    280+ tools, 20 categories
│   │   ├── skills-registry.md     USRI / OpenClaw / Skills.sh
│   │   ├── memory-context.md      Letta, agentmemory, headroom, codegraph...
│   │   ├── optimizations.md       caching, compression, indexing, parallelism...
│   │   ├── knowledge-systems.md   Obsidian, NotebookLM, RAG, markitdown
│   │   ├── orchestration-multiagent.md  patterns, ADK graph, Ruflo, swarms
│   │   ├── personal-agents.md     OpenClaw, Hermes, nanobot
│   │   ├── people.md              Karpathy, Boris, Willison, Anthropic, Pocock, YC
│   │   └── compatibility-adapters.md  LangGraph, CrewAI, AutoGen, etc.
│   └── OS_SETUP_v1.3_full.md  previous single-file version (exact template bodies)
```

## The DevKit library (what makes this "universal")
`reference/ecosystem/` is a curated catalog of the agentic-AI frontier — trending repos from the last 6 months (headroom, codegraph, agentmemory, oh-my-pi...), the SDK/ADK landscape (Claude SDK, OpenAI Agents SDK, Google ADK 2.0, LangGraph, DSPy), the 1000+ skill universe, memory/context/optimization tooling, and the practitioners whose discipline is baked in (Karpathy, Boris Cherny, Anthropic, Willison, Pocock, YC). The orchestrator **pulls from it like a reference shelf** — reads the card catalog, opens the 2–4 books that match your archetype, picks the smallest winning stack, records an ADR, closes the books. A project generated by OS-Setup therefore starts from the *collective frontier*, auto-selected for its problem — not from scratch.

---

## The core loop (what the agent actually does)

```
read kernel/  →  detect archetype  →  pick tier  →  generate structure from templates/
     →  run validators/preflight.sh  →  dispatch wave-1  →  workers execute
     →  review (evidence required)  →  merge  →  ship  →  next wave
     →  on ANY anomaly: consult failure-modes/  →  add the matching validator
```

Read [`INDEX.md`](INDEX.md) next if you're an agent. Read [`00-INVOCATION.md`](00-INVOCATION.md) if you're a human starting a project.
