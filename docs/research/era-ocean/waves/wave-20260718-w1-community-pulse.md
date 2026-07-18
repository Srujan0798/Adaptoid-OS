# Wave W1 — Community pulse (live practitioner signal)

| Field | Value |
|---|---|
| Wave | `20260718-w1-community-pulse` |
| Focus | What practitioners say works **now** for agent harnesses (not vendor decks) |
| Surfaces | HN, Reddit (`r/ClaudeAI`, related), X/Twitter, YC/founder narrative |
| Date (UTC) | 2026-07-18 |
| Coverage honesty | **Incomplete snapshot.** ≪1% of agentic surface. Selection-biased toward loud threads and power users. |

---

## Method (what was actually scraped)

- **HN:** harness / long-running agents / parallel agents / AGENTS.md eval / SWE-bench gaming / early-stopping / “loop engineering”
- **Reddit:** Claude Code levels, worktrees, portable harnesses (Agentsmith / Citadel / Lanes)
- **X:** agent harness anatomy, skills taxonomy, cost/token burn, AGENTS.md botfiles
- **YC / founder:** W25 “95% AI code” claim; Spring 2026 app asks for coding-agent session; Linzumi (S26) multi-agent chat product

This is **practitioner pulse**, not a systematic survey. Quotes and themes below are recurring across independent threads, not single anecdotes elevated to gospel.

---

## 1. Recurring complaints

### 1.1 False done / early stopping

- Agents **declare victory before the task is done**. Reasoning models alone do not fix this.
- Practitioners treat early stopping as a **harness bug**, not a model bug.
  - Common fix: **TODO lists re-injected every turn** (Claude Code pattern); explicit open-task tools; stop-hooks that refuse “done” without verify.
  - HN: mini-agent demos show early stopping; “TODOs always performed best” among experiments (hypothesis tracking, etc.).
- Related: **tests-pass ≠ merge-ready**. METR / HN: many SWE-bench-passing PRs would not be merged (taste, structure, maintainability). Functional correctness is a weak “done.”

### 1.2 Cost runaway / token burn

- Parallel agent fleets and unattended loops **burn tokens silently**.
  - X anecdotes: multi-week loops left running; “guardrail” thrash; incomplete context causes **stronger models to hunt harder** (more tools, more retries → higher $).
  - Cost pattern: incomplete context does not get cheaper with a better model—it gets more expensive.
- Long sessions hit rate limits / subscription ceilings mid-task; multi-model handoffs used as damage control (Claude burn → GPT finish).
- Elite practice frames cost as **loop design**: vague tasks + fat context dumps + max-effort on small asks + inherited context across agents.

### 1.3 Context rot / instruction decay

- Named problem: **context rot** — irrelevant files / long transcripts poison long-horizon reasoning.
  - HN products/comments: agents spend large fractions of time searching; naive RAG/stuffing worsens rot; specialized retrieval subagents claim large reductions.
- **CLAUDE.md / AGENTS.md wall:** long instruction files get silently ignored (community consensus often ~80–150 lines; top rules win, bottom rules die).
  - Reddit 5-level post (high engagement): 145 lines → ignore bottom; trim to ~77 → compliance returns.
- LLM-generated AGENTS.md often **hurts** (documents the obvious → more rot). Human, non-obvious, struggle-derived rules win when anything does.
- arXiv/HN AGENTS.md study: human files ~+4% avg (inconsistent across models); auto-generated ~−3%. Practitioners reframe: 4% on public repos is still material; real value is domain knowledge not in the repo.

### 1.4 Parallel collisions / multi-agent chaos

- Multiple agents on the **same working tree** step on each other’s files. Community slogan: **stop sharing one checkout**.
- Orchestration without isolation → merge hell; with worktrees, conflict rates can be low (one public claim: ~3% across large fleets—single-source, treat as anecdote).
- Multi-agent without L3/L4 foundations (skills + hooks) is repeatedly called a mess (“don’t skip levels”).
- Review load: parallel agents turn ICs into EM+IC hybrids; every agent feels like a **brand-new coworker** with no trust history → review tax dominates.

### 1.5 Benchmark theater / “gaming”

- **SWE-bench Verified saturated / contested** (~93.9% claimed; OpenAI/HN: flawed tests, contamination, helper-name memorization).
- Bench-specific harnesses (debug agents, multi-attempt orchestration) inflate leaderboard without generalizing.
- Terminal-bench / exploit papers: adversarial gaming of agent benchmarks is now explicit discourse.
- Community shift: **SWE-bench Pro / Terminal-Bench / live private evals**; ignore marketing deltas between 70% and 90% on Verified.

### 1.6 Other frequent pains

- **Permission stalls:** agent waits on a prompt while tokens/time burn.
- **Mock vs real:** AGENTS.md + skills pass mock tests, fail real automation (“never follow instructions” when stakes rise).
- **Slop / review complacency:** uncomfortable-truths thread — humans become complacent reviewers under volume.
- **Harness churn:** Manus/LangChain/Anthropic reportedly re-architect harnesses as models improve — outer scaffolding has short half-life if it duplicates model strengths.

---

## 2. Recurring wins (what people say actually works)

### 2.1 Tight AGENTS.md / CLAUDE.md (not encyclopedias)

- Keep **short**, high-signal, non-obvious.
- Split by concern (architecture / conventions / boundaries) rather than one megafile.
- Put **why / intentional weirdness / gotchas**, not directory trees the agent can grep.
- Symlink / dual-name: `AGENTS.md` ↔ `CLAUDE.md` / `GEMINI.md` for multi-host.

### 2.2 Skills (progressive disclosure, on-demand protocols)

- Skills = task-scoped markdown (+ scripts, datasets) loaded when relevant — not always-on system prompt bulk.
- Taxonomy seen in the wild: knowledge, verification, data, automation, scaffolding, review, CI/CD, runbooks, infra ops — **one responsibility each**.
- Verification skills called the biggest unlock: simulate usage, assert, check logs — not just generate.
- Skills evolve: every failure becomes harness memory.
- Shared skill spec across Codex/Claude emerging; public AGENTS.md + skills for community tuning.

### 2.3 Hooks (enforce, don’t plead)

- PostToolUse: per-file typecheck/lint after edit (avoid 200-error dumps).
- Stop hooks: quality gates before “done.”
- SessionStart: load campaign context.
- Pattern: move from **telling** the agent to validate → **infrastructure** that validates.

### 2.4 Git worktrees + isolation

- One agent per worktree/branch/directory; optional tmux session per agent.
- VS Code extensions (tmux-worktree, Lanes, etc.) productize the click-path.
- Multi-host fleets: Claude Code + OpenCode + Codex side by side on different features.

### 2.5 Verify loops / deterministic outer harness

- Consensus on HN “harness that can do anything”: **deterministic scaffold + LLM only at decision leaves**.
- Outer layer names in play: **loop engineering**, flow engineering, tool-response engineering, agentic exoskeleton.
- Plan → implement → verify → ship; failing test first for bugs; real project checks before done (Agentsmith-style).
- Regex/static tests for “taste” patterns agents keep violating (stronger than prompt bans).
- Handoff at ~25–30% context remaining rather than death spiral at 100%.

### 2.6 TODO / plan as first-class harness state

- Dynamic TODOs re-injected at context head; survive compaction as compact session summary.
- Plan mode: write plan file, sometimes wipe planning context, hold plan at system level during implement.
- Filesystem as living memory: `plans/<task>/plan.md`, campaign files, changelog folders for session resume.

### 2.7 Parallel lifestyle (when isolated)

- Simon Willison-style parallel agents + Jesse Vincent-style advanced multi-agent workflows widely referenced.
- Elite move: same task to N agents → compare diffs → mix-and-match (tooling still immature).

---

## 3. Named tools / harnesses people actually use

| Name | Role in community talk |
|---|---|
| **Claude Code** | Default serious coding agent; reference harness architecture |
| **OpenAI Codex / Codex CLI** | Daily driver pair with Claude; multi-rig setups |
| **OpenCode** | OSS coding agent; high HN engagement; multi-model |
| **Cursor / Copilot / Zed Agent** | IDE-native; often “for everything else” or lighter work |
| **Pi** (pi.dev) | Minimalist extensible harness; Armin-adjacent discourse |
| **Aider / Roo / Cline / Augment** | Historical/ongoing alternatives; settlement debates |
| **mini-SWE-agent** | ~100-line agent proving loop > complexity |
| **OpenRig** | Multi-harness (Claude Code + Codex) via tmux topology |
| **Zot** | “Yet another coding agent harness” Show HN |
| **Agent-harness-kit (AHK)** | Multi-agent scaffolding |
| **Agentsmith** | Portable plan→verify→ship OS over CLAUDE/AGENTS.md |
| **Citadel** | Open harness embodying 5-level Claude Code maturity |
| **GSD (get-shit-done)** | Cited as stack addition for structure |
| **Beads** | Lightweight multi-context task survival |
| **Serena** | OSS efficiency / symbol tools for agents |
| **MCP** | Ubiquitous external tool surface |
| **claude-code-router** | Route non-Anthropic models through Claude Code |
| **Worktree + tmux extensions** | Lanes, vscode-tmux-worktree, etc. |
| **Linzumi** (YC S26) | Team chat → many coding agents |
| **WarpGrep / retrieval subagents** | Context-rot mitigation narrative |
| **Grok Build** | Mentioned in reviews (worktree sub-agents); lower community share than Claude/Codex in this scrape |

**Framing that stuck:** coding agent = **(harness + model)** pair. Harness = loop + tools + permissions + memory − weights.

---

## 4. YC / founder narrative (if any)

- **W25 signal (widely repeated):** ~**25% of YC Winter 2025** batch allegedly have **~95% AI-generated** codebases (Jared Friedman / TechCrunch amplification). Treat as **directional founder lore**, not audited metric.
- **Application shift (Spring 2026):** YC asks applicants to attach a **coding agent session** (markdown/transcript from Claude Code or similar) — signal that *how you drive agents* is part of founder skill assessment.
- **Productization of multi-agent ops:** e.g. **Linzumi** (S26) — team chat to command dozens of coding agents (kickoff / review / ship).
- Founder mental model: agents as leverage; bottleneck moves to **specs, review, and harness reliability**, not typing speed.
- Caution from HN: “AI writing most code” ≠ quality or maintainability; review and understanding remain non-outsourceable.

---

## 5. “1% elite” practices (mentioned repeatedly)

These appear across independent high-engagement threads (Reddit 5-levels, HN harness/loop threads, X architecture threads):

1. **Harness > model for controllable gains** — invest in loop, gates, memory, permissions; models swap.
2. **Graduate by ceiling, don’t skip levels** — prompt → tight AGENTS.md → skills → hooks → orchestration.
3. **Verify is infrastructure** — hooks/tests/stop-gates; not “please run tests” in prose.
4. **Worktree isolation as default** for any parallel work.
5. **TODO / plan re-injection** against early stopping and compaction amnesia.
6. **Deterministic outer loop** — scripts and gates own progress; LLM only for judgment nodes (“loop engineering”).
7. **Skills as products** — single-responsibility, progressive disclosure, versioned, shared across org.
8. **Human AGENTS.md from struggle logs** — never auto-dump repo README into agents.md.
9. **Context budget discipline** — hand off early; compact hierarchy (micro → snip → summarize → collapse); retrieval subagents over stuffing.
10. **Evidence of done** — real suite, taste tests, human merge criteria; distrust bench scores and agent self-reports.
11. **Permission + cost ceilings** — no unattended infinite retry; kill switches; serial writes / parallel reads.
12. **Multi-model / multi-harness deliberately** — write with one, refine with another; or Claude Code + Codex in one rig.
13. **Filesystem as memory** — campaign files, plans, changelogs outlive context windows.
14. **Empiricism in project rules** — “verify, research, back with data” encoded so agents can’t vibe-ship.

---

## 6. Implications for Adaptoid (watch / adopt / refuse — draft only)

| Signal | Lean | Note |
|---|---|---|
| Tight AGENTS.md + non-obvious domain rules | **Adopt** | Already in cold-start; keep short; resist encyclopedia growth |
| Skills + progressive disclosure | **Adopt / deepen** | Align with modular protocols, not one mega-prompt |
| Hooks / stop-gates / ship-check | **Adopt** | Evidence-or-it-didn’t-happen matches community elite |
| Worktree / blast-radius isolation | **Adopt** | Parallel without collisions |
| Loop engineering as real SDLC gates | **Adopt** | Explicitly reject doc-theater loops |
| Multi-agent fleets without L3/L4 | **Refuse** | Community reports chaos |
| Bench-chasing harnesses | **Refuse / watch** | Gaming is real; private evals > leaderboard |
| Unattended infinite agent loops | **Refuse** | Cost + false done risk |
| Auto-generated AGENTS.md as default | **Refuse** | Net negative in study + practice |
| Outer deterministic scaffold over pure chat | **Adopt** | Matches Adaptoid “mission OS” thesis |

---

## 7. Gaps / what this wave did **not** cover

- Non-English communities; Discord/Slack private guilds; internal company playbooks  
- Systematic r/LocalLLaMA / r/MachineLearning depth  
- Full Karpathy / Boris Cherny / Addy Osmani primary essays (flagged for later waves)  
- Quantitative cost studies (only anecdotes)  
- Security / OAP / prompt-injection failure modes at scale  
- Enterprise SSO / compliance harness constraints  

**Honest coverage estimate after this wave:** still **≪ 1%** of the ocean. This is a **pulse**, not a map.

---

## 8. Top source threads (for re-open)

| ID | Surface | Why it matters |
|---|---|---|
| HN 48921077 | Towards a harness that can do anything | Loop engineering, deterministic outer harness |
| HN 46081704 | Effective harnesses for long-running agents | Pareto wall, cost of last 10%, AGENTS.md + trackers |
| HN 45489884 | Parallel coding agent lifestyle | Parallel ops, review tax |
| HN 47034087 | Evaluating AGENTS.md | Empirical + practice clash |
| HN 47910388 / 47341645 | SWE-bench death / unmergeable PRs | Benchmark gaming, false done |
| HN 46545620 | Claude Code in 200 LOC | Early stopping, TODO harness |
| Reddit 1s1ipep | 5 levels of Claude Code | Skills/hooks/worktrees maturity model |
| Reddit 1qzduim | Stop multi-agent same repo | Worktrees as social norm |
| Reddit 1uy69ma | Agentsmith portable harness | Plan→verify→ship |
| YC / TechCrunch W25 | 95% AI code narrative | Founder market belief |
| X (architecture / skills / cost) | Harness anatomy + token burn | Live power-user discourse |

Detail registry: `docs/research/era-ocean/sources/INDEX.md`.
