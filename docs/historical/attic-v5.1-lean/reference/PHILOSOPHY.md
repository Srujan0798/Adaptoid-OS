# 🜂 PHILOSOPHY.md

> *The soul of the Adaptoid. Five foundational thinkers / systems that
> shape every choice in the DevKit: Karpathy's LLM-as-OS, the gstack
> virtual-team pattern, the OpenClaw multi-channel gateway, the Hermes
> Closed Learning Loop, and the Netflix culture of freedom & responsibility.
> Read this first, before anything else, to understand what the Adaptoid
> is trying to be.*

---

## 0. Why a philosophy file

Most agentic systems ship a config, a CLI, and a README. They do not ship
a *worldview*. The result: every builder reinvents the same values from
scratch, every disagreement about a default comes back to first principles
that nobody wrote down, and every "the docs say X but I want Y" turns into
a fork.

Adaptoid-OS v2.0 ships its worldview. Not because the worldview is novel —
it is synthesized from public work by Karpathy, Garry Tan, Peter Steinberger,
Nous Research, and the Netflix culture memo — but because *codifying* the
worldview is the difference between a tool and a tradition. A tradition can
absorb new contributors; a tool can only absorb new features.

This file is the tradition. It is short, it is opinionated, and it is
binding on every layer below it.

---

## 1. The five pillars

| Pillar | Source | One-line thesis |
| --- | --- | --- |
| **LLM-as-OS** | Andrej Karpathy, Sept 2023 ("a more complete picture is emerging of LLMs not as a chatbot, but the kernel process of a new Operating System") + AIOS-Agent paper (Ge et al., 2023) | Treat the LLM as a kernel. Treat prompts/skills as programs. Treat tools as syscalls. Treat agents as apps. |
| **Conductor & Virtual Team** | Garry Tan (YC CEO), gstack, 2026; Conductor by Melty Labs | Run 10–15 parallel sprints, each in its own isolated workspace, with role-specialized skills acting as a CEO/CTO/QA virtual team. |
| **Multi-Channel Gateway** | Peter Steinberger, OpenClaw (247K stars), 2026 | A single sovereign process owns every channel (WhatsApp, Telegram, Discord, Slack, iMessage, …), routes to multiple isolated agents, isolates memory + auth + sandbox per agent. |
| **Closed Learning Loop** | Nous Research, Hermes Agent | The agent is not a one-shot tool. It is a *learning* system. Every trajectory crystallizes into a Skill. Every failure pattern strengthens a Skill. Every session compounds. |
| **Freedom & Responsibility** | Netflix Culture Memo (Patty McCord, Reed Hastings) | High autonomy, high alignment, low process. Context, not control. Highly aligned, loosely coupled. Pay top of market. Don't tolerate brilliant jerks. Disagree & commit. |

These five are the pillars. Everything else in the Adaptoid is a
*composition* of them.

---

## 2. Pillar I — LLM-as-OS (Karpathy)

### 2.1 The original

> "A more complete picture is emerging of LLMs not as a chatbot, but the
> kernel process of a new Operating System."
> — Andrej Karpathy, X / Twitter, Sept 28 2023

The full metaphor:

| OS concept | LLM equivalent |
| --- | --- |
| Kernel process | The LLM itself |
| RAM | Context window (10 Hz single-threaded) |
| Disk / ROM | The weights + RAG / memory store |
| Syscall | A function call / tool use / token output |
| User-space program | An agent / skill / prompt |
| Process table | The active plan (DAG of skills) |
| Process isolation | A workspace, a sandbox, an agentDir |
| I/O scheduler | The cost router, the conductor |
| Filesystem | The memory bank (Markdown + vector + graph) |
| Package manager | The skill registry |
| OS family | LLM family (Claude, GPT, Gemini, Llama) |
| Security model | Permission / route check / redaction |
| Audit log | OTel traces + memory bank history |

### 2.2 Why this matters for the Adaptoid

If the LLM is a kernel, then:

- **Skills are not prompts.** They are *user-space programs* — small,
  typed, versioned, with input contracts, output contracts, and a
  permission set.
- **Memory is not a chat log.** It is a *filesystem* — with directories,
  ACLs, mounting, and mount-time validation.
- **The plan is not free-form prose.** It is a *process table* — a DAG
  of typed skills with explicit dependencies.
- **The agent runner is not a chat loop.** It is a *kernel* — it
  schedules, dispatches, audits, kills, restarts.
- **Multi-agent is not a magic trick.** It is *multi-process* — with
  isolation, IPC (A2A), and shared resources (the memory bank).

The Adaptoid is, end-to-end, a small operating system for LLMs. The
folder structure is the filesystem. The Engine is the kernel. The
controller is the process scheduler. The Skills are programs. The
Memory bank is the disk. The Cost router is the I/O scheduler. The
RouteCheck is the permission check. The Trace contract is the audit log.

If you have ever written an OS, you already understand the Adaptoid.

### 2.3 The "10 Hz single-threaded" constraint

Karpathy notes the LLM runs at ~10 tokens/sec, single-threaded. This
is the *fundamental throughput limit* of the whole stack. The Adaptoid
is engineered around it:

- **Parallelism is achieved by process isolation**, not by making the
  LLM faster. 10–15 isolated workspaces, each running its own LLM
  call, in parallel (Conductor pattern, §3).
- **The bottleneck is moves between processes.** We minimize context
  bloat, maximize progressive disclosure, and aggressively checkpoint.
- **Caching is the only way to multiply 10 Hz.** LiteLLM response
  cache. Skill pre-loading. Memory bank as the "page cache".

### 2.4 The LLM-as-pressure-tester

Karpathy's second insight (March 2026, on No Priors): "I spent four
hours refining an argument with an LLM, felt it was bulletproof, then
asked it to argue the other side and was *immediately* convinced. The
LLM is not a truth machine, it's a *persuasion* machine." The Adaptoid
operationalizes this by *requiring* every high-stakes output to be
**adversarially cross-checked by a different model family** (see
`VERIFICATION-PROTOCOLS.md` §5).

This is the LLM-as-pressure-tester pattern. The Adaptoid does not trust
*one* model to argue for *and* against itself. It runs the second pass
on a different family (Claude ↔ GPT ↔ Gemini), with a different prompt
("find three reasons this is wrong"), and treats disagreement as a
*halt* signal.

---

## 3. Pillar II — Conductor & Virtual Team (gstack)

### 3.1 The original

> "I don't think I've typed like a line of code probably since December,
> basically, which is an extremely large change."
> — Andrej Karpathy, No Priors podcast, March 2026

> "How does one person ship like a team of twenty? Peter Steinberger
> built OpenClaw — 247K GitHub stars — essentially solo with AI agents."
> — Garry Tan, gstack README, 2026

The gstack pattern, distilled:

- 23 opinionated tools (skills), each a *role* in a virtual engineering
  team: CEO, CTO, Eng Manager, Designer, QA, Release Manager, Doc
  Engineer, …
- 6 enforced questions per `/office-hours` ("the question you forgot to
  ask yourself").
- 3-layer planning review: `/plan-ceo-review` (product), `/plan-eng-review`
  (technical), `/plan-design-review` (UX, with a 0-10 score and
  AI-content detection).
- `/design-consultation` builds a design system + `DESIGN.md` from zero.
- `/review` finds prod issues and *auto-fixes* them.
- **Conductor workspaces**: 10–15 parallel sprints, each in its own
  isolated workspace, with cross-sprint roll-up.
- Dual-AI cross-review: the worker's output is re-graded by a
  *different* model family.
- Real browser automation for end-to-end testing.

Numbers Garry Tan reports: 600K+ lines of production code in 60 days,
35% tests, 10–15 parallel sprints sustained, 1–2k LOC / day average,
140k LOC and 362 commits in a single `/retro` week.

### 3.2 What the Adaptoid takes from gstack

- **Slash commands as the primary trigger.** Not free-form chat. The
  Adaptoid ships `/adaptoid/plan`, `/adaptoid/build`, `/adaptoid/review`,
  `/adaptoid/qa`, `/adaptoid/release`, `/adaptoid/retro`, `/adaptoid/design`,
  `/adaptoid/research`. Each is a *named workflow* with a typed
  contract, not a free-form prompt.
- **The 6 enforced questions** as the canonical intake gate. Every
  plan starts with the 6 questions; missing any of them is a falsification
  hit.
- **The 3-layer planning review.** Plan = (product_review ∧ technical_review
  ∧ design_review). Each is a separate node with a separate model.
- **The virtual team.** Skills are not just programs; they are *roles*.
  `core.cto`, `core.ceo-review`, `core.qa`, `core.design-consultation`,
  `core.release-mgr` — each a typed skill with a persona, an
  anti-pattern list, and a contract.
- **The Conductor.** A new pattern, `core.conductor` + `workflows/parallel-sprint/`
  + the `conductor/` directory. 10–15 isolated workspaces, each running
  a sprint, with cross-sprint roll-up via the memory bank.
- **Real browser automation** in the verification layer.
  `core.browser-orchestrator` (Stagehand / Browser-Use) is a first-class
  citizen, not a bolt-on.

### 3.3 What the Adaptoid improves on gstack

- **gstack is Claude-Code-locked** (slash commands, AGENTS.md, sessions).
  The Adaptoid is harness-agnostic: same slash commands work in
  Claude Code, OpenAI Agents SDK, LangGraph, Cursor, Aider, Goose,
  Hermes Agent, OpenClaw.
- **gstack has no formal verification regime** beyond the 3-layer
  review. The Adaptoid has a 4-layer verification regime (schema,
  evidence, route, cross-check) plus a typed `WR-1..WR-12` and
  `H-1..H-12` anti-pattern catalog.
- **gstack has no formal memory bank** beyond the Claude-Code session
  history. The Adaptoid has a portable Markdown + SQLite FTS + graph
  memory bank with an ACL.
- **gstack has no formal "falsification" gate.** The Adaptoid requires
  every plan to enumerate, in advance, the conditions under which it
  is not valid.
- **gstack is solo-builder-tuned.** The Adaptoid is solo-AND-team-tuned
  (with multi-channel gateway, multi-agent bindings, RBAC).

---

## 4. Pillar III — Multi-Channel Gateway (OpenClaw)

### 4.1 The original

OpenClaw (Peter Steinberger, 247K stars, 2026) is a single local
process that:

- Hosts a **WebSocket gateway** that connects to every channel you use
  (WhatsApp via Baileys, Telegram via grammY, Discord, Slack, iMessage
  via `imsg` on macOS, Signal, Google Chat, MS Teams, Mattermost,
  Matrix, Feishu, LINE, Nostr).
- Hosts **N isolated agents** in a single process (or in N processes
  for hard isolation). Each agent has its own:
  - `workspace/` (the cwd by default; sandbox the boundary)
  - `agentDir/` (auth profiles, model registry, per-agent config)
  - `sessions/` (chat history + routing state)
  - `auth-profiles.json` (per-agent credentials — *never* shared)
  - `skills/` (per-agent vs `~/.openclaw/skills` shared)
- **Bindings** route inbound messages to the right agent:
  ```yaml
  bindings:
    - { agentId: ceo,         match: { channel: feishu,    accountId: admin    } }
    - { agentId: data-analyst, match: { channel: feishu,    accountId: analyst  } }
    - { agentId: product-lead, match: { channel: telegram,  accountId: product  } }
  ```
- **Skills metadata** for install + requirements:
  ```yaml
  metadata:
    openclaw:
      requires: [node>=20, pnpm]
      install:  [brew, npm, go, uv]
  ```
- **Daemon install** (`openclaw onboard --install-daemon`) + **Tailscale**
  remote access + **macOS/iOS/Android node pairing**.
- **Per-agent sandbox + tool policy.** Workspace is *not* a hard
  boundary; the sandbox + tool allow/deny list is.
- **macOS menu-bar app + Web Control UI + iOS/Android node + CLI + TUI.**

### 4.2 What the Adaptoid takes from OpenClaw

- **The single-sovereign-process pattern.** The Adaptoid ships an
  Adaptoid Gateway (in `multi-channel/gateway/`) that owns every
  channel + every agent.
- **The binding grammar.** A typed `Binding` (channel, accountId,
  matchPattern → agentId) is the routing primitive.
- **Per-agent isolation.** Each agent has its own `agentDir/`,
  `sessions/`, `auth-profiles.json`. Memory is physically partitioned.
- **The skills metadata convention.** `metadata.adaptoid.requires`
  + `metadata.adaptoid.install` are first-class fields in the
  `SKILL.md` frontmatter.
- **Tailscale-style remote.** The Adaptoid gateway can be exposed
  over a Tailscale / Wireguard / Cloudflare tunnel.
- **The "two deployment modes".** Single-gateway-multi-agent (default;
  resource-efficient) and dual-gateway (hard isolation for sensitive
  workloads). The Adaptoid lets the user pick.

### 4.3 What the Adaptoid improves on OpenClaw

- **OpenClaw is a single binary** (Node). The Adaptoid is a *protocol
  and a DevKit* — it composes OpenClaw-style gateways with MCP,
  A2A, the Agent Skills open standard, and the OTel-native observability
  layer.
- **OpenClaw's learning is implicit** (per-agent state). The Adaptoid
  has a formal Closed Learning Loop (Pillar IV) that crystallizes
  trajectories into Skills, regardless of gateway.
- **OpenClaw's verification is per-channel.** The Adaptoid has a
  4-layer cross-channel verification regime.
- **OpenClaw is built on one developer's taste.** The Adaptoid's
  defaults are derived from the entire ecosystem (see
  `references/landscape-map.md`).

---

## 5. Pillar IV — Closed Learning Loop (Hermes)

### 5.1 The original

Hermes Agent (Nous Research, mid-2026) is the first agent whose
*primary* design goal is learning, not execution. From the official
docs and the GEPA paper:

> "A closed learning loop — Agent-curated memory with periodic nudges.
> Autonomous skill creation after complex tasks. Skills self-improve
> during use. FTS5 session search with LLM summarization for
> cross-session recall. Honcho dialectic user modeling."

The four mechanisms, in order:

1. **Trajectory capture.** Every tool call (name, args, return value,
   latency, HTTP status, exit code), every user correction (explicit
   or implicit), every error + recovery. The trajectory is the
   raw material.
2. **Skill crystallization.** If the trajectory satisfies any of:
   - tool calls ≥ 5
   - error encountered and self-recovered
   - user gave corrective feedback
   Then Hermes compresses the trajectory into a `SKILL.md` (natural-
   language, not code) and writes it to `~/.hermes/skills/`.
3. **Self-improvement via DSPy + GEPA.** GEPA (Generalized
   Evolutionary Policy Adaptation) loads the current best strategy
   set, generates a *perturbed variant*, runs it, evaluates
   *fitness* (target-achievement × user-satisfaction × latency),
   and retains only above-threshold variants. DSPy handles the
   in-prompt optimization; GEPA handles the meta-search.
4. **Honcho dialectic user modeling.** A separate model maintains
   a *user persona* — preferences, expertise, communication style —
   that is updated after every session. The agent gets
   *personalized* over time without re-asking.

The 7-stage skill lifecycle:

```
1. TRIGGER     — trajectory satisfies one of the triggers above
2. DISTILL     — compress the trajectory to a SKILL.md
3. INDEX       — add to the FTS5 search index
4. SCOPE       — set the activation conditions ("when target is X
                  and Y, this skill applies")
5. PROGRESSIVE — L1 (frontmatter) loaded always;
                 L2 (body) loaded on match;
                 L3 (scripts/templates) loaded on demand
6. SELF-IMPROVE — Reviewer feedback / failure patterns / success
                   patterns fold back into the SKILL.md
7. PROMOTE     — when a skill reaches high fitness, it becomes a
                  default in the relevant workflow
```

### 5.2 What the Adaptoid takes from Hermes

- **The four-layer memory model.** Working (in-context) →
  Episodic (sessions, FTS5 + LLM-summarized) → Semantic (vector
  + graph) → Procedural (Skills). Adaptoid v1.0 had three layers;
  v2.0 has four.
- **The trajectory → skill crystallization pipeline.** Adaptoid
  ships `core.nudge-engine` (terminal-end prompt), `core.skill-crystallize`
  (trajectory → SKILL.md), and `core.skill-evolve` (DSPy/GEPA-style
  meta-search).
- **FTS5 session search with LLM summarization.** The Adaptoid's
  `memory-sync.sh search` is the FTS5 piece; `core.summarize-sessions`
  is the LLM piece.
- **Honcho-style user modeling.** `core.honcho-model` maintains a
  per-user persona in `memory-bank/user/`. Every plan is bound to
  it.
- **The "skill evolves from use" principle.** Every Adaptoid Skill
  has a `last_evolved` field alongside `last_verified`. The CI
  distinguishes "stale" (TTL expired) from "unevolved" (no feedback
  for N sessions).

### 5.3 What the Adaptoid improves on Hermes

- **Hermes is a single-agent system.** The Adaptoid composes Hermes-style
  learning *with* multi-agent bindings, durable execution, and the
  full verification regime.
- **Hermes's GEPA runs only on skills.** The Adaptoid runs GEPA-style
  evolution on the *whole plan* (per-node model choice, per-node
  cost cap, per-node verification cadence) — a much higher-leverage
  target.
- **Hermes is open-source but single-implementation.** The Adaptoid
  ships the *abstract* Closed Learning Loop and lets the user plug
  in DSPy / TextGrad / GEPA / ADAS / a homegrown loopper.

---

## 6. Pillar V — Freedom & Responsibility (Netflix)

### 6.1 The original

The Netflix Culture Memo (Patty McCord, Reed Hastings; 2009, updated
through 2024) distills a high-autonomy engineering culture into seven
aspects:

1. **Values are what we Value** — actual values are revealed by who
   gets rewarded, promoted, let go (not by what the wall poster says).
2. **High Performance** — great workplace ≠ great workforce. Hire,
   develop, and cut smart.
3. **Freedom & Responsibility** — give people the freedom to figure
   out the best way to do the work, and hold them responsible for
   the outcome. The opposite of process-heavy.
4. **Context, not Control** — set the context (strategy, metrics,
   constraints, principles) and let people decide the tactics. Don't
   command-and-control the daily execution.
5. **Highly Aligned, Loosely Coupled** — every team has the same
   strategic context; teams are decoupled in execution.
6. **Pay Top of Market** — high performers have options; keep them.
7. **Promotions & Development** — develop from within; promote
   based on demonstrated excellence.

The 9 valued behaviors (memorize these):

1. You make wise decisions (people, technical, business, creative)
   *despite ambiguity*.
2. You identify root causes, get beyond treating symptoms.
3. You think strategically, can articulate what you are and are not
   doing, why.
4. You smartly separate what *must* be done well now, and what can
   be improved later.
5. You build great teams. You attract and hire *brilliant* people.
6. You maintain *high standards*: bars rise with each hire.
7. You are *generously candid* in order to help the company.
8. You *disagree-and-commit*: dissent, then align.
9. You minimize *brilliant jerks*: a brilliant jerk is someone who
   is brilliant but makes others feel bad. Don't tolerate.

The *Keeper Test*: "Which of your people, if they told you they were
leaving for a similar role at a peer company, would you fight hard
to keep? If you wouldn't fight to keep them, why are they still
here?"

The *Brilliant Jerk* anti-pattern: brilliant jerks cost the company
disproportionately in morale, retention, and team velocity. A team
of 9 + 1 brilliant jerk produces less than a team of 9 high-perf
players.

### 6.2 What the Adaptoid takes from Netflix

- **Context, not control, in the Engine.** The Adaptoid Engine
  emits a typed plan, but the *tactics* (which skill, which model,
  which order) are decided at the controller level. The user sets
  the *strategy* (PROJECT-INTENT.md, profile, falsification) and
  the engine figures out the rest.
- **Highly aligned, loosely coupled in the multi-agent system.**
  Every agent in a Conductor sprint shares the same PROJECT-INTENT,
  the same falsification block, the same verification regime —
  but is free to pick its own skills, models, and order.
- **The 9 behaviors as the agent's code-of-conduct.** The
  Adaptoid's `AGENTS.md` "never" list is inspired by the Netflix
  behaviors, but specialized for the AI context. Examples:
  - "Wise decisions despite ambiguity" → the Adaptoid's
    route-check is for this.
  - "Identify root causes, get beyond symptoms" → the
    `FM-rationalized-failure` control.
  - "Disagree-and-commit" → the conductor's `falsification-check`
    halts on dissent; the human ack proceeds.
- **The Keeper Test, applied to Skills.** Every Skill has a
  `fitness_score` and a `keeper_test_pass` field. The CI fails
  if a Skill's keeper-test-pass is false for >30 days. Skills
  that wouldn't be fought-for get pruned.
- **Brilliant jerks, applied to models.** A model that gets the
  answer right 99% of the time but is *expensive* / *slow* /
  *fragile* is a brilliant jerk. The Adaptoid's cost router
  downgrades on cost-cap violation, even if the model is "smarter."

### 6.3 What the Adaptoid improves on Netflix

- **Netflix's "freedom" is human-only.** The Adaptoid extends it to
  *both* humans and AI agents, with explicit guardrails (the
  verification regime, the falsification block, the route-check).
- **Netflix's "context" is CEO memos.** The Adaptoid's context is
  a typed PROJECT-INTENT.md, validated by a JSON Schema, with
  inferred failure modes, and an enforced falsification block.
  Better than a memo.
- **Netflix's "alignment" is a culture.** The Adaptoid's alignment
  is the `meta` block in PROJECT-INTENT.md (`risk_tolerance`,
  `iteration_style`, `profile`) plus the `non_negotiables` list,
  which is hard-enforced by the controller.

---

## 7. The synthesis (how the five pillars compose)

The Adaptoid is what you get when you compose all five:

| Layer | Pillar | What the Adaptoid does |
| --- | --- | --- |
| Kernel | LLM-as-OS (Karpathy) | LLM is a kernel; skills are programs; memory is disk |
| Scheduler | Conductor (gstack) | 10–15 parallel sprints, each isolated, each a typed skill DAG |
| I/O | Multi-Channel (OpenClaw) | One gateway, many channels, many agents, full isolation |
| Learning | Closed Loop (Hermes) | Trajectory → skill → DSPy/GEPA evolution → Honcho user model |
| Culture | Freedom & Responsibility (Netflix) | Context not control; aligned not coupled; 9 behaviors as code-of-conduct |

The pillar interactions:

- The **Conductor** (Pillar II) runs *inside* the LLM-as-OS kernel
  (Pillar I). Each sprint is a process; the Conductor is the
  scheduler.
- The **Multi-Channel Gateway** (Pillar III) is *the user-space
  daemon* in the LLM-as-OS. It binds channels to processes.
- The **Closed Learning Loop** (Pillar IV) is *the kernel's
  background GC*: it consolidates trajectories into Skills,
  promotes high-fitness ones, prunes dead ones.
- The **Netflix culture** (Pillar V) is *the policy* the kernel
  enforces. Context not control = PROJECT-INTENT.md. Aligned not
  coupled = shared `meta` block.

---

## 8. The eight anti-patterns the Adaptoid refuses

Codified from the five pillars:

1. **"Trust the model."** (Pillar I) — LLM-as-kernel implies
   verification-first. The Adaptoid never trusts a single verifier
   for high-stakes decisions.
2. **"Free-form chat is fine."** (Pillar II) — gstack showed that
   slash-commands + typed workflows beat free-form. The Adaptoid
   refuses free-form for non-trivial work.
3. **"One agent, one channel."** (Pillar III) — OpenClaw showed
   that a single gateway + N agents + M channels is the *correct*
   shape. The Adaptoid ships the gateway.
4. **"Skills are static prompts."** (Pillar IV) — Hermes showed
   that skills *evolve*. The Adaptoid refuses static skills.
5. **"Just write the README."** (Pillar V) — Netflix culture says
   values are revealed by who gets rewarded, not by what the wall
   says. The Adaptoid's `non_negotiables` are *enforced*, not
   suggested.
6. **"Process is safety."** — Wrong. *Context* is safety, not
   process. The Adaptoid has high context (PROJECT-INTENT +
   falsification + verification) and low process (no mandatory
   ticketing, no required meetings).
7. **"Big team = big output."** — Wrong. gstack showed 1 person
   with the right harness ships like 20. The Adaptoid is solo-
   AND-team-tuned.
8. **"We're all-in on one vendor."** — The Adaptoid is open-
   standard-first (MCP, A2A, Skills, OTel) and vendor-agnostic
   (LiteLLM gateway; multiple model families for cross-check).

---

## 9. The four "we" statements

> "We are a kernel." — The Adaptoid treats the LLM as a kernel
> process. Skills are programs. Memory is disk. The controller is
> the scheduler.
>
> "We are a team." — The Adaptoid runs a virtual engineering team
> with 23+ roles, 10–15 parallel sprints, and a Conductor that
> orchestrates them.
>
> "We are a gateway." — The Adaptoid owns every channel, routes
> every message, and isolates every agent.
>
> "We are a learner." — The Adaptoid captures every trajectory,
> crystallizes every pattern, evolves every skill, and remembers
> every user.

These four "we"s are not slogans. They are the binding commitments
of the DevKit.

---

## 10. The reading list (the actual sources)

If you want to go deeper on the pillars, in this order:

1. **Karpathy, X / Twitter, Sept 28 2023** — the LLM-as-OS tweet.
2. **Ge et al., 2023, "LLM as OS, Agents as Apps: Envisioning
   AIOS"** (arXiv:2312.03815) — the academic version.
3. **Garry Tan, gstack README, 2026** — github.com/garrytan/gstack
4. **Augment Code, "Garry Tan's gstack hits 89.7K stars"** — the
   productivity numbers.
5. **OpenClaw docs, "Multi-agent routing"** — docs.openclaw.ai/concepts/multi-agent
6. **OpenClaw, "Configuration — agents"** — docs.openclaw.ai/gateway/config-agents
7. **OpenClaw security paper, 2026** — arXiv:2605.23330
8. **Nous Research, Hermes Agent docs** — hermes-agent.nousresearch.com
9. **Nous Research, "Hermes Agent Self-Evolution"** — github.com/NousResearch/hermes-agent-self-evolution
10. **mranand substack, "Inside Hermes Agent"** — mranand.substack.com
11. **NVIDIA, "Hermes Unlocks Self-Improving AI Agents"** — blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/
12. **Netflix Culture Memo (Patty McCord, Reed Hastings)** — jobs.netflix.com/culture
13. **Wharton, "Netflix Culture: Freedom and Responsibility"** — knowledge.wharton.upenn.edu

The synthesis in this file is *derived* from these sources. The
extraction notes (what each pillar contributes, what the Adaptoid
takes, what it improves on) are *judgments* — open to debate, and
designed to be debated. If you disagree with an extraction note,
open a PR. The philosophy is a living document.

---

## 11. TL;DR

> The Adaptoid is built on five pillars. **Karpathy's LLM-as-OS**
> makes it a kernel. **gstack's Conductor** makes it a team.
> **OpenClaw's multi-channel gateway** makes it a sovereign.
> **Hermes's Closed Learning Loop** makes it a learner. **Netflix's
> Freedom & Responsibility** makes it a culture. Each pillar has a
> clear contribution, a clear extraction, and a clear improvement.
> The DevKit that ships with this philosophy is the most synthesized
> agentic foundation in mid-2026. The remaining files in this
> repository are the *implementation* of the philosophy.

🜂
