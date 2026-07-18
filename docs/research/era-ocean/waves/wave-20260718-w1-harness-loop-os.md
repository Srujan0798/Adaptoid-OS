# Wave W1 — Harness Engineering + Loop Engineering + LLM-as-OS

**Wave id:** `wave-20260718-w1-harness-loop-os`  
**Date:** 2026-07-18  
**Scope:** Intellectual core of Adaptoid — portable harness, outer loops, and LLM-as-OS framing for coding agents.  
**Mode:** Read-only research synthesis. One slice of an ocean — **not** complete coverage.

> **Honesty contract:** This wave samples high-signal public writing (Karpathy, Cherny via quotes/talks, Osmani, Ronacher, Huntley, Trivedy/LangChain, Steinberger/OpenClaw discourse, secondary commentary). It does **not** claim to map the full agentic ecosystem, private lab harnesses, or every elite shop’s internal loop stack. Treat estimates as directional.

---

## Executive thesis — what the elite 1% do differently

**2025 was the year agents became real products. 2026 is the year the competitive edge moved outside the model.**

The elite pattern is not “better prompting.” It is:

1. **Treat the model as a jagged ghost, not a junior employee.**  
   Karpathy’s framing: LLMs are *summoned ghosts* with superpowers and cognitive deficits (amnesia, hallucination, jagged skill spikes). You do not “hire” them; you *harness* them. Taste and judgment stay human.

2. **Agent = Model + Harness.**  
   Everything that is not weights is harness: system prompts, tools, filesystems, sandboxes, hooks, skills, subagents, verification back-pressure. A decent model in a great harness beats a great model in a bad harness. (Trivedy / Osmani / HumanLayer consensus.)

3. **Stop being the person who prompts; write the loop that prompts.**  
   Cherny (Claude Code): *“I don’t prompt Claude anymore… My job is to write loops.”*  
   Steinberger (OpenClaw): design loops that prompt agents.  
   Osmani names the discipline **loop engineering** — one floor *above* harness engineering.

4. **Two loops, not one.**  
   Ronacher’s clarity:  
   - **Agent loop** (inner): ReAct — tool → observe → tool → “done.”  
   - **Harness loop** (outer): queue/work stays alive after the model would have stopped; reinject, fresh session, or handoff.  
   Elite practice invests disproportionately in the **outer** loop: done-conditions, fresh context, durable state on disk, maker≠checker.

5. **Software factory, not chat.**  
   Osmani / Cursor line: the job is building the *factory that builds the software* — specs, isolation (worktrees), automations, skills, connectors, subagent verification, external memory. Coding generation is cheap; **verification, invariants, and intent debt** are the scarce resources.

6. **Vibe coding → agentic engineering.**  
   Karpathy (AI Ascent 2026): vibe coding was the prototype; agentic engineering is the discipline (spec, diff review, eval loops, outsource thinking never understanding). Software 3.0 = programs written in English orchestrating a new computer (LLM ≈ CPU, context ≈ memory).

**What the 1% optimize for that the 99% skip:**

| Elite habit | Median habit |
|---|---|
| Encode every failure into harness rules (`AGENTS.md`, hooks, tests) | Retry the same prompt harder |
| Fresh context + filesystem state (Ralph-style) | One endless chat that rots |
| Maker / checker split; mechanical or second-model done signal | Self-graded “looks good” |
| Spec + invariants + red/green tests as back-pressure | Vague English goals |
| Autonomy slider + human review bandwidth as the real ceiling | Full auto, hope |
| Portable loop design across Claude Code / Codex / host | Tool fandom |

**Adaptoid-shaped implication:** Adaptoid’s value is not “another agent.” It is a **portable mission OS** — harness + outer SDLC loops + evidence gates — so any host/model can be swapped while the *compounding* artifacts (rules, done criteria, wave state, verification) survive.

---

## Concept dictionary (precise definitions)

### Stack layers (bottom → top)

| Layer | Definition | Primary job |
|---|---|---|
| **Weights / Model** | Frozen (or fine-tuned) LLM intelligence | Propose tokens, tool calls, plans |
| **Prompt engineering** | Crafting instructions *inside* a turn or system message | Local behavior shaping |
| **Context engineering** | What enters the window: files, retrieval, skills front-matter, compaction, offloading | Maximize signal per token; fight context rot |
| **Agent loop (inner)** | ReAct-style: reason → tool → observe → until model exits | Single-session problem solving |
| **Harness** | All non-model code/config: tools, FS, sandbox, hooks, MCP, subagents, observability | Turn intelligence into a work engine |
| **Loop engineering (outer)** | System that finds work, dispatches agents, checks, records, decides next — *replaces the human as prompter* | Multi-session autonomy under constraints |
| **Factory model** | Org-level view: fleets of agents + QC + specs + envs | Parallel software production |
| **LLM-as-OS / Software 3.0** | LLM as CPU-like substrate; context as RAM; apps as partial-autonomy products with GUIs and autonomy sliders | Ecosystem framing, not a product name |

### Named patterns

| Term | Meaning |
|---|---|
| **Harness engineering** | Discipline of treating scaffolding as a living artifact; every agent slip becomes a permanent rule (Osmani after Trivedy). |
| **Loop engineering** | Designing recursive goals + automations so the system prompts agents (Osmani, Cherny, Steinberger). |
| **Ralph / Ralph Wiggum loop** | Huntley: outer `while` loop (often fresh context each iteration) that re-feeds a goal until done; state on disk. Pure form: `while :; do cat PROMPT.md \| agent; done`. |
| **Agentic engineering** | Post–vibe-coding craft: specs, review, evals, understanding retained by humans (Karpathy 2026 framing). |
| **Vibe coding** | English-first, low-review generation; code as free/ephemeral (Karpathy 2025 coinage). Still valid for throwaways; insufficient for long-lived systems. |
| **Jagged intelligence / ghosts** | Superhuman in some pockets, foolish in others; not animal-shaped minds (Karpathy). |
| **RLVR** | Reinforcement Learning from Verifiable Rewards — 2025 training stage that produced reasoning-like behavior on checkable domains (Karpathy year-in-review). |
| **Context rot** | Performance degrades as the window fills; harnesses compact, offload, reset. |
| **Autonomy slider** | Product affordance for how much the agent owns (Cursor / Karpathy LLM-app properties). |
| **Intent debt** | Unwritten project intent filled by agent guesses each cold start; skills/`AGENTS.md` pay it down (Osmani). |
| **Orchestration tax** | Human review bandwidth is the real limit on parallel agents (Osmani). |
| **Maker ≠ checker** | Generator and evaluator split (often different model/session); stop-conditions not self-graded. |
| **Sprint contract / done condition** | Explicit, preferably verifiable “done” before generation; `/goal`-style loops. |
| **Partial autonomy app** | Karpathy: GUI + context eng + multi-call orchestration + human audit (Cursor archetype). |

### Thesis slogans (use carefully)

- **“2025 was agents; 2026 is harnesses/loops”** — useful marketing of a real shift (productized agents → outer-loop competition). Not a scientific periodization; labs still co-train model+harness.
- **“I don’t prompt; I write loops”** — Cherny; means outer automation + routines, not “prompts are dead.”
- **“If you’re not the model, you’re the harness.”** — Trivedy.

---

## Primary sources (links)

### Karpathy — LLM-as-OS, Software 3.0, agentic shift

| Source | URL | Why it matters |
|---|---|---|
| YC AI Startup School — Software 3.0 (Jun 2025) | https://www.youtube.com/watch?v=LCEmiRjPEtQ | LLM ≈ OS; Software 1.0/2.0/3.0; partial autonomy apps; context as working memory |
| Unofficial transcript (Donna Magi) | https://www.donnamagi.com/articles/karpathy-yc-talk | Searchable text of the talk (verify against video) |
| 2025 LLM Year in Review | https://karpathy.bearblog.dev/year-in-review-2025/ | RLVR, ghosts vs animals, Cursor as LLM app, Claude Code as local ghost, vibe coding |
| AI Ascent 2026 — Vibe Coding → Agentic Engineering | https://www.youtube.com/watch?v=96jN2OCOfLs | Discipline on top of vibes; understanding vs outsourced thinking |
| Related essays | https://karpathy.bearblog.dev/animals-vs-ghosts/ · verifiability · space of minds | Psychology of models |

### Cherny / Claude Code — loops over prompts

| Source | URL | Why it matters |
|---|---|---|
| Quote cascade (widely attributed to Boris Cherny, head of Claude Code) | e.g. https://x.com/rohanpaul_ai/status/2063289804708835412 (clips); echoed in Ronacher/Osmani | Canonical loop-engineering quote |
| The New Stack summary | https://thenewstack.io/loop-engineering/ | Industry framing of loop engineering + Cherny/Steinberger |
| Note | Direct long-form Cherny essay not located this wave | Prefer primary talk clips when citing exact wording |

### Osmani — harness, loop, factory

| Source | URL | Why it matters |
|---|---|---|
| Agent Harness Engineering (2026-04-19) | https://addyosmani.com/blog/agent-harness-engineering/ | Full harness stack; ratchet habit; skill-issue reframe |
| O’Reilly Radar reprint | https://www.oreilly.com/radar/agent-harness-engineering/ | Same essay, durable home |
| Loop Engineering (2026-06-07) | https://addyosmani.com/blog/loop-engineering/ | Five primitives + state; Codex ↔ Claude Code map |
| Factory Model (2026-02-25) | https://addyosmani.com/blog/factory-model/ | Factory mental model; verification bottleneck; TDD as back-pressure |
| Related | long-running agents, agent skills, orchestration tax, intent debt (linked from above) | Depth on each primitive |

### Ronacher — cautionary loop philosophy

| Source | URL | Why it matters |
|---|---|---|
| The Coming Loop (2026-06-23) | https://lucumr.pocoo.org/2026/6/23/the-coming-loop/ | Agent vs harness loop; where loops work vs fail; software-as-organism; opt-out difficulty; Pi/harness future |

### Huntley — Ralph loop (primitive outer loop)

| Source | URL | Why it matters |
|---|---|---|
| Ralph Wiggum as a “software engineer” | https://ghuntley.com/ralph/ | Original Ralph pattern (2025-07) |
| Everything is a Ralph loop | https://ghuntley.com/loop/ | Generalization; agent ≈ small loop of tokens+tools |

### Trivedy / LangChain — harness anatomy

| Source | URL | Why it matters |
|---|---|---|
| The Anatomy of an Agent Harness | https://www.langchain.com/blog/the-anatomy-of-an-agent-harness/ | Agent=Model+Harness; FS, bash, sandbox, memory, context rot, Ralph, co-evolution model↔harness |

### Steinberger / OpenClaw

| Source | URL | Why it matters |
|---|---|---|
| “Design loops that prompt your agents” | https://x.com/steipete/status/2063697162748260627 | Canonical Steinberger line |
| OpenClaw (project discourse) | Community / GitHub references via secondary writeups | Personal-agent / multi-agent harness experiment; not deeply audited this wave |

### Anthropic (adjacent, high quality)

| Source | URL | Why it matters |
|---|---|---|
| Harness design for long-running apps (cited heavily by Osmani) | https://www.anthropic.com/engineering/harness-design-long-running-apps | Lab-grade long-horizon harness (fetch full detail in a later wave) |

### Odysseus (named in mission — clarification)

| Source | URL | Why it matters |
|---|---|---|
| Odysseus / odysius (PewDiePie self-hosted AI workspace, ~2026-05-31) | e.g. HN https://news.ycombinator.com/item?id=48346693 ; GitHub mirrors | **Not** an “elite coding-agent harness” in the Cherny/Osmani sense. Local-first multi-purpose agent workspace / ChatOS-class product. Relevant as *personal LLM-OS surface*, weak as *coding SDLC harness* reference. |

### Secondary / synthesis (use as maps, not gospel)

- https://thenewstack.io/loop-engineering/
- https://cobusgreyling.substack.com/p/loop-engineering
- HumanLayer “skill issue” harness posts (linked from Osmani)
- Martin Fowler / Böckeler harness engineering overview (linked from Osmani)

---

## Patterns that compound (for a portable harness like Adaptoid)

These are **portable** — they should not depend on Claude Code vs Codex vs Cursor as the host.

### 1. Outer loop with durable state on disk

- Goal / PRD / wave file outside the chat.
- Fresh or compacted context per iteration (Ralph insight: continuous session ≠ continuous progress).
- Progress ledger the next iteration *must* read.
- **Adaptoid fit:** `HANDOFF.md`, wave files, EXECUTION state — *replace, never append blindly*; evidence or it didn’t happen.

### 2. Explicit done conditions (mechanical > social)

- Prefer binary signals: tests, lint, typecheck, preflight scripts, ship-check.
- LLM-as-judge only when mechanical verification is impossible (research, porting review) — and never as sole gate for load-bearing code.
- **Adaptoid fit:** `validators/preflight.sh`, `make ship-check`, SDLC loop protocols.

### 3. Maker ≠ checker

- Separate implementer session/subagent from reviewer/evaluator.
- Done-check not performed by the same trajectory that wants to stop.
- **Adaptoid fit:** two-tier Brain/Hands; adversarial review skills; wave researchers vs builders.

### 4. Failure → harness ratchet

- Every real failure becomes: rule in `AGENTS.md` / skill, hook, test, or blast-radius policy.
- Never “hope the next model version fixes it” as the default.
- **Adaptoid fit:** kernel principles, anti-hallucination rules, policies/default.yaml.

### 5. Context engineering as first-class product surface

- Progressive disclosure (skills front-matter, not full tool dump).
- Compaction + tool-output offload + optional full session reset with handoff brief.
- Private host context (local filesystem, secrets, repo) beats pure cloud AGI theater for intermediate takeoff (Karpathy on Claude Code).
- **Adaptoid fit:** INDEX.md load tables, session start protocol, stay-in-the-box file lists.

### 6. Factory primitives (Osmani’s five + state)

| Primitive | Portable form |
|---|---|
| Automations | Cron / scheduled triage / wave runners |
| Worktrees / isolation | Git worktrees, sandboxes, non-colliding paths |
| Skills | `SKILL.md` / project instruction files / packs |
| Plugins / connectors | MCP, CLIs, issue trackers — with blast-radius gates |
| Sub-agents | Role-scoped workers with narrow tools |
| State | Markdown ledgers, Linear/GitHub, HANDOFF |

### 7. Where loops *earn* their keep (Ronacher alignment)

**High ROI loops:** porting/mechanical transform, performance search, security scanning, research exploration, throwaway experiments, CI triage.  
**Low ROI / high risk unattended loops:** core invariants, persisted formats, taste-heavy architecture, “lasting” systems without strong tests and human architectural ownership.

### 8. Autonomy slider + human judgment retained

- Elite practice does not mean full abdication (Ronacher’s warning + Karpathy “never outsource understanding”).
- Design for legibility: diffs, evidence trails, rollback, small blast radius by default.
- **Adaptoid fit:** FM-style blast radius, remote/money/humans pause for confirmation.

### 9. Model–harness co-evolution awareness

- Models are post-trained *into* lab harnesses; switching tools changes behavior.
- Portable harnesses must not assume one vendor’s apply_patch / tool dialect is universal — abstract at the mission layer.

### 10. Spec quality is the multiplier

- Ambiguous specs multiply errors across parallel agents (factory model).
- Invest in architecture docs, invariants, and acceptance criteria *before* fan-out.

---

## What to IGNORE (hype)

| Hype | Why ignore / demote |
|---|---|
| **“Prompts are dead”** | Loops still *contain* prompts; the unit of design moved up, not away. |
| **“AGI endgame = cloud swarms only”** | Karpathy: intermediate jagged world favors local context + developer machine. |
| **Benchmarks as AGI proof** | RLVR + benchmaxxing → jagged spikes; trust production harness evals. |
| **Model brand wars as strategy** | Harness + verification dominate observed quality for many tasks. |
| **Unattended “ship to main” as default** | Amplifies defensive spaghetti and unowned organisms (Ronacher). |
| **Infinite agent fan-out without review bandwidth** | Orchestration tax; human ceiling remains. |
| **Token-unlimited Ralph without cost caps** | Steinberger-class burn rates; always set max iterations, $ ceilings, escalation. |
| **Odysseus-as-coding-elite-reference** | Wrong category for SDLC harness research (local ChatOS/workspace). |
| **“Software engineering is dead”** | Huntley-style provocation; elite consensus is opposite: engineering (specs, invariants, verification) becomes *more* load-bearing. |
| **Doc theater loops** | Adaptoid law: each loop must be a real SDLC gate with evidence, not ritual markdown. |

---

## Gaps (what this wave did not cover)

Honest incomplete list — candidates for later waves:

1. **Full Anthropic long-running harness engineering post** — cited widely; deep read + diagram extract pending.
2. **Primary Boris Cherny full talk transcript** — currently quote-level; need durable primary artifact.
3. **OpenClaw architecture deep dive** — stars/hype high; design review of actual loop/harness code not done here.
4. **OpenAI Codex app automations + harness team million-line claims** — secondary mentions only.
5. **HumanLayer, Dex Horthy, Böckeler full texts** — referenced via Osmani, not re-read end-to-end.
6. **Simon Willison agentic loops essay** — foundational one-liner only.
7. **Terminal Bench 2.0 methodology** — harness-sensitivity claim accepted from secondary; need numbers/methods.
8. **Enterprise factory deployments** (Stripe/Square/etc. product posts) — not audited.
9. **Security adversarial loops** (attackers looping against software; curl maintainer load) — Ronacher raises; operational patterns thin here.
10. **Academic multi-agent orchestration literature** vs industry bash-loop practice — not bridged.
11. **Eval harness design** (unit/integration/agent-eval) as product surface — light treatment.
12. **Non-coding LLM-as-OS apps** (general productivity) — out of Adaptoid hot path this wave.
13. **Chinese / non-English elite harness discourse** — not searched.
14. **Private internal harnesses** at labs — by definition invisible.

**Coverage estimate for this intellectual slice:** maybe ~5–15% of *public high-signal* writing on harness/loop/OS for coding agents; <<1% of the total agentic ocean. Do not treat as finished map.

---

## Distilled adopt / watch / refuse (for later product waves)

| Stance | Item |
|---|---|
| **Adopt (conceptual — already Adaptoid-shaped)** | Outer SDLC loops; evidence gates; replaceable state files; blast radius; maker≠checker; failure→rule ratchet |
| **Watch** | Productized `/loop` `/goal` primitives in hosts; skills format convergence; model–harness co-training lock-in |
| **Refuse** | Unverified unattended merge culture; doc-only “loops”; equating self-hosted ChatOS with coding harness excellence |

---

## Wave meta

- **Files written:** this document; `sources/INDEX.md` entry for W1.
- **Files not touched:** core product, kernel, adaptor, templates (mission constraint).
- **Next research angles (suggestions only):** Anthropic long-running harness post full extract; OpenClaw architecture; Cherny primary talk; Terminal Bench harness ablations; adversarial security loops.

*End of wave W1. Ocean remains larger than the map.*
