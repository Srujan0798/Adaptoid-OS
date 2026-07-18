# Partial D — Community LIVE pulse (HN · Reddit · X)

| Field | Value |
|---|---|
| Wave partial | `wave-20260718-0837-D-community-live` |
| Agent | D (community live) |
| Focus | Live practitioner signal: loop engineering, false done, worktrees, AGENTS.md failures |
| Surfaces | HN (`news.ycombinator.com`), Reddit (agent harness / Claude Code / Codex), X (semantic + keyword) |
| Captured | 2026-07-18 (session “NOW” scrape) |
| Output scope | **This file only** |
| Coverage honesty | **Incomplete by design.** Opportunistic multi-query scrape, not a census. Loud power-user threads dominate; silent successful workflows under-sample. X is hype-saturated (“leaked Anthropic PDF” meme cluster). Reddit/HN better for failure modes; X better for circulating doctrine slogans. |

---

## Method (what was actually queried)

### Hacker News
- `site:news.ycombinator.com` agent harness, Claude Code, Codex, AGENTS.md
- Parallel agents, worktrees, false done / early stop, loop engineering / backpressure / Ralph loop
- Representative threads (not exhaustive crawl of front page)

### Reddit
- Agent harness, Claude Code, Codex comparisons
- Worktree isolation posts, harness rebuild notes, false-done / premature-success threads
- Subreddits in hit set: `r/ClaudeAI`, `r/ClaudeCode`, `r/AI_Agents`, `r/vibecoding`, `r/LangChain`, related

### X
- `x_semantic_search`: loop engineering, false done, worktrees, AGENTS.md failures
- `x_keyword_search` (Latest): loop engineering / false done / worktrees / AGENTS.md + Claude|Codex|Cursor|harness|agent
- `x_keyword_search` (Latest): worktree collisions / fail
- Note: semantic search returns engagement-weighted history; keyword Latest skews to low-view same-day noise + doctrine reposts

**Not done:** full thread comment dumps, Algolia date-bounded HN export, subreddit top-of-week API, Discord/Slack private channels, Chinese/Japanese communities.

---

## Executive snapshot (recurring for elite harness)

| Theme | Community consensus (live) | Elite-harness implication |
|---|---|---|
| False done / nodding loop | Self-grade = broken; premature success is the default failure | External verifier + evidence gate; never trust agent “done” |
| Worktrees | Parallel without isolation = file clobber; worktrees = default answer | One agent ↔ one worktree/branch; orchestrator enforces, not prompts |
| AGENTS.md | Short human rules help; fat/auto files rot; markdown alone is “pray” | Structured harness coercion > prose hopes; progressive disclosure |
| Loop engineering | Discover → isolate → verify → persist → schedule | Outer system prompts agent; timer + budget + authz |
| Harness > model theater | Same model ±20 pts by harness; dual-tool power users common | Invest in gates/skills/hooks; multi-host AGENTS portability |
| Ceremony skepticism | AGENTS/SKILLS/delegation can sacrifice understanding | Ceremony only if it is a real SDLC gate with proof |

---

## 1. Recurring FAILS (elite harness must defeat)

### 1.1 False done / premature success / “nodding loop”

**Signal strength:** High (HN + Reddit + X doctrine cluster all hit this).

- Agents declare victory without running tests, or after tests that do not match merge criteria.
- Self-review bias: same agent grades its own work → always “yes.”
- X circulating “five broken loops” taxonomy (viral July 2026): **Blind / Tangled / Nodding / Amnesiac / Manual**. Nodding = never says no to itself. Manual = human presses Start (not a loop).
- Reddit: “false done is the most common failure”; “premature success announcements”; architecture threads asking how to prevent false done without blocking legitimate work.
- Harness rebuild lesson (r/ClaudeCode): **“Done” must be a defined terminal state** (`done` | `blocked` | `needs-input`) **with evidence**, not trailing “I could also…”.

**Elite anti-pattern fix (community-derived):**
- Second agent / external verifier; never self-grade.
- Stop-hooks / policy gates refuse “done” without verify artifact.
- Cadence-style tools explicitly marketed as “won’t let LLM grade its own work.”
- Tests-pass ≠ ship-ready (taste, structure, maintainability remain human/critic gates).

### 1.2 Tangled parallel / shared checkout collisions

**Signal strength:** High, operationally concrete.

- Reddit slogan thread: *Stop running multiple Claude Code agents in the same repo* — merge conflicts, reverts, clobber.
- HN Kanban/agent fleets: same-checkout parallel cards overwrite files; worktree-per-task is the fix productized by several tools.
- X: worktree isolation is the default parallel story (“six agents, six trees”); also reports of **Codex UI regressions** dropping Worktree/Local so new tasks land on shared main → collisions return.
- Reddit failure: Claude Code **confused about main vs worktree path** — edits main checkout almost every long worktree session for some users.
- PSA class: subagent worktrees from wrong base (`origin/…`); harness flipping `core.bare` and breaking ordinary git until noticed.
- HN security note: worktrees share `.git`; malicious process / hook escape risk vs full clone/container boundary.

**Elite anti-pattern fix:**
- Isolation is **infrastructure**, not AGENTS.md advice.
- One agent · one worktree · one branch · optional tmux session.
- Abort trees for subagents (child hang must not hostage parent forever).
- Intent continuity is **not** solved by worktrees alone (X debate: worktrees isolate files, not goals — need STATE/intent graph + disk memory).

### 1.3 AGENTS.md / CLAUDE.md failures

**Signal strength:** High, nuanced (not “delete all instructions”).

| Failure mode | Live evidence |
|---|---|
| **Pray mode** | HN: CLAUDE.md is hope; structured harness config (e.g. opencode.json `instructions` + coerced agents) actually forces subagent use |
| **Length rot** | Fat files → bottom rules ignored; community still trims hard |
| **Anti-pattern claim** | X (citing swyx thread): persistent instruction files can trap agents refining stage-0 for hours; prefer /plan /goal /skill or nothing |
| **Mock ≠ real** | X same-day: AGENTS.md + skills pass mock tests, fail on real automation (“never follow instructions”) |
| **Layering** | Reddit harness rebuild: your file does **not** replace system prompt; it layers; write to override, not restate |
| **Auto-gen / LLM-written** | Prior study echoes still in HN: auto AGENTS can hurt; human struggle-derived rules win |
| **Cross-host drift** | Codex often “better at following agents.md”; Claude freestyles more (HN); users dual-run and commonize AGENTS.md |
| **Ceremony tax** | HN: AGENTS.md, SKILLS.md, delegation frameworks may sacrifice understanding for ostensible progress |

**Elite anti-pattern fix:**
- Short, non-obvious rules; progressive skills; structured coercion where host allows.
- Policy hooks **block** dangerous tools (not “please don’t”).
- Per-session brief for task context; root AGENTS for stable project law only.
- Treat AGENTS.md as **one layer**, not the harness.

### 1.4 Broken / hollow loops (loop engineering fails)

**Signal strength:** Medium–high (doctrine heavy on X; practice heavy on HN).

Five-failure frame (X viral, treat as mnemonic not paper):
1. **Blind** — no discovery; waits for human to hand work
2. **Tangled** — shared dir parallelism destroys
3. **Nodding** — self-approve
4. **Amnesiac** — results only in context window; morning amnesia
5. **Manual** — no timer/trigger; script waiting for a person

Related live fails:
- Infinite/nonsense message loops (Gemini CLI loop detection; over-detect on newer models)
- Goal drift, permission creep, understanding debt, premature success (X “Claude loop manual” meme cluster)
- Permission stalls / too many dumb questions mid-loop
- Unattended autonomy without authorization (budget, verifier, fixed env) = failure moving faster
- Compounded false affirmatives at scale (fallback makes tests pass; review still fails)

### 1.5 Cost, review tax, benchmark theater

- Parallel fleets burn tokens; ceiling becomes **human review bandwidth**, not agent count.
- Power users: Claude for architecture / complex; cheaper agent for grind (token efficiency).
- SWE-bench-style scores contested as harness-gamed; “same model, different tool” can swing ~20 points (Reddit CLI comparison claim).
- Model-vendor harnesses co-trained with models; DIY harness hard to match CC/Codex depth (Reddit).

### 1.6 Worktree / isolation rough edges (not pure win)

- Pain finding “the real file” among many worktrees (HN).
- Git DB contention / hook escape (HN).
- Path confusion to main (Reddit).
- Product regressions removing worktree UX (X/Codex issue pointer).

---

## 2. Recurring WINS (what elite operators report)

### 2.1 Loop engineering as outer system

Canonical Discover → Isolate → Verify → Persist → Schedule (X + loop-engineering articles circulating June–July 2026):

| Stage | Live practice |
|---|---|
| Discover | Own work: failing CI, open issues — not morning paste |
| Isolate | Git worktrees / separate checkouts |
| Verify | **Second agent** or deterministic gates; never self-grade |
| Persist | Disk state (`STATE.md`, plans, memory/) not only context |
| Schedule | Timer / automation / Ralph-style outer loop |

HN “Backpressure is all you need” + Ralph-loop lineage: outer automation for container, build, unit, integration, user-path; agent iterates until **evidence** of done; human owns PR quality bar.

### 2.2 Worktrees + multi-host fleet

- Worktree + tmux as default parallel lifestyle (Reddit how-to; VS Code tmux-worktree extensions).
- Multi-model: Claude Code + Codex + OpenCode side by side on different features.
- Shared AGENTS.md across harnesses for dual-sub (X same-day practice).
- Writer ≠ judge: implement agent and verify agent split.

### 2.3 Structured harness coercion > markdown hope

- OpenCode / structured config forces agent graph; AGENTS.md as `instructions` attachment, not sole control plane (HN).
- Hooks as control flow: PreToolUse **block**, not log-only (Reddit rebuild).
- Policy gate before tool calls (HN Show-class posts).
- DAG of subagents, not flat for-loop await-all; abort trees.

### 2.4 Short AGENTS + skills + progressive disclosure

- Workspace-first: AGENTS.md + TOOLS.md + memory/ (OpenClaw / similar HN discussion).
- Skills on-demand vs always-on encyclopedia.
- Human-written gotchas > LLM-generated SOPs.
- Some operators still succeed with thin workflow AGENTS + ROADMAP + milestone files — **minimal** ceremony.

### 2.5 Explicit terminal states + evidence

- Force end-of-turn: done | blocked | needs-input + proof.
- Gate irreversible actions (delete, push, external) on explicit recent intent.
- Real project checks / QA loop before done (not only unit green).

### 2.6 Dual-tool & host selection

| Observation | Source class |
|---|---|
| Claude Code often preferred for complex architecture / mature plugins | Reddit 2026 tool polls |
| Codex stronger agents.md adherence + token/rate headroom for many | HN + Reddit |
| Same model swings hard by harness | Reddit CLI bakeoff narrative |
| Power users keep **two** agents warm | Multiple Reddit threads |

### 2.7 Spec-driven + plan mode

- Spec / plan file first; implement in isolation; critic pass.
- Human-designed interfaces / narrow write surface so agents cannot break what they cannot touch (HN).
- Kanban / markdown-spec orchestration for multi-agent queues (with worktree isolation).

---

## 3. Loop-engineering doctrine (X cluster — use carefully)

**Honesty:** A large July 2026 X cluster amplifies “Anthropic engineer leaked N-page loop PDF” content. Treat as **meme-propagated doctrine**, not verified employer docs. The *ideas* still match independent HN/Reddit practice:

1. Stop prompting the agent; build the system that prompts it.
2. Uncontrolled autonomy is not authorized; authorization = recurring task + objective verifier + fixed budget + working environment.
3. Failure file: goal drift, self-review bias, premature success, understanding debt, permission creep.
4. Verify sits in the center; hand back to human when gates fail.
5. Counter-thread: pure unbounded loops hide why they broke → prefer **structured graphs** you can see, control, and stop (graph vs loop debate).

**Older still-cited signal:** Whitmore (2023) — loops multiply nondeterminism (~5–15% fail per loop step); intense guardrails required. Still directionally aligned with 2026 practice complaints.

---

## 4. Source index (URLs)

### Hacker News
- https://news.ycombinator.com/item?id=47936579 — Ask HN: Claude Code getting worse? AGENTS.md vs structured harness (OpenCode)
- https://news.ycombinator.com/item?id=47938417 — Good vs bad AGENTS.md; harness dumps file into context
- https://news.ycombinator.com/item?id=47940443 — Why OpenCode harness vs CLAUDE.md hope
- https://news.ycombinator.com/item?id=46743908 — Claude Code swarms / multi-agent ceremony skepticism
- https://news.ycombinator.com/item?id=47357042 — “Shall I implement it? No” — Codex vs Claude agents.md adherence; critic agents
- https://news.ycombinator.com/item?id=48632144 — Symlinks CLAUDE.md ↔ AGENTS.md
- https://news.ycombinator.com/item?id=46844822 — Opinionated minimal coding agent harness; workspace AGENTS/TOOLS/memory
- https://news.ycombinator.com/item?id=47295537 — SWE-CI; harness matters for eval; AGENTS.md for dense context?
- https://news.ycombinator.com/item?id=47640521 — Open weights + harness; AGENTS/ROADMAP as thin workflow
- https://news.ycombinator.com/item?id=48558502 — Policy gate before tool calls; CLAUDE.md/AGENTS.md not enough alone
- https://news.ycombinator.com/item?id=45489884 — Parallel coding agent lifestyle; worktree caveats (git DB, security)
- https://news.ycombinator.com/item?id=47218318 — Parallel agents + tmux + markdown specs; worktree tip
- https://news.ycombinator.com/item?id=48272984 — Subagents in worktrees + feedback loop
- https://news.ycombinator.com/item?id=47282777 — Claude Code passion / agentic mode control debate
- https://news.ycombinator.com/item?id=46060508 — Gemini CLI loop detection / stuck loops
- https://news.ycombinator.com/item?id=48345090 — Backpressure; Ralph loop; outer QA; multi-worktree scale
- https://news.ycombinator.com/item?id=47220440 — Agents wrong often; parallel worktrees as new “flow”
- https://news.ycombinator.com/item?id=46737630 — Unrolling the Codex agent loop (OpenAI)
- https://news.ycombinator.com/item?id=44533004 — Kanban multi-agent; false affirmatives; worktree isolation
- https://news.ycombinator.com/item?id=48771515 — Flow state vs multi-worktree agent lifestyle

Related external from HN comments:
- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://opencode.ai/docs/config/
- https://jamesanglin.com/blog/claude-code-worktrees
- https://github.com/smogili1/circuit
- https://github.com/openai/codex

### Reddit
- https://www.reddit.com/r/ClaudeAI/comments/1qzduim/stop_running_multiple_claude_code_agents_in_the/ — worktree isolation manifesto
- https://www.reddit.com/r/ClaudeCode/comments/1ueuh0h/what_i_learned_about_claude_code_by_rebuilding/ — harness rebuild: layering, hooks, abort trees, DAG, explicit done
- https://www.reddit.com/r/ClaudeCode/comments/1tnbo0a/am_i_using_worktrees_wrong_or_is_claude_code_just/ — worktree path confusion to main
- https://www.reddit.com/r/claudeskills/comments/1uwmzsu/psa_claude_code_creates_subagent_worktrees_from/ — wrong-base worktrees / bare repo footgun
- https://www.reddit.com/r/ClaudeCode/comments/1tbcfmi/impressions_two_weeks_after_moving_from_claude/ — harness importance; CC vs Codex limits
- https://www.reddit.com/r/vibecoding/comments/1s2ftie/i_compared_all_6_major_cli_coding_agents/ — harness swings scores; dual-agent pattern
- https://www.reddit.com/r/AI_Agents/comments/1uselz0/which_coding_ai_tool_are_you_actually_using_in/ — custom harness + MCP/skills; Omnigent meta-harness
- https://www.reddit.com/r/AI_Agents/comments/1slczzz/which_coding_ai_tool_are_you_actually_using_in/ — 2026 tool poll
- https://www.reddit.com/r/LangChain/comments/1tu9lxt/how_can_deep_agents_compete_with_claude_code/ — model+harness co-training
- https://www.reddit.com/r/LLMDevs/comments/1srwj77/architecture_review_needed_preventing_false_done/ — false done architecture
- https://www.reddit.com/r/ClaudeAI/comments/1ul639o/claude_constantly_not_doing_what_it_should/ — false done + keep CLAUDE.md short
- https://www.reddit.com/r/ClaudeCode/comments/1u41kmx/cadence_a_tool_that_wont_let_claude_or_other_llms/ — no self-grade tooling
- https://www.reddit.com/r/ClaudeAI/comments/1to8l0j/building_the_harness_around_our_coding_agents/ — eight failure modes → harness pillars

Related longform (from Reddit/search adjacency):
- https://levelup.gitconnected.com/your-claude-md-wont-save-you-the-fence-around-your-coding-agent-will-cc309d5a54a5 — rulebook vs fence; CLAUDE.md alone insufficient
- https://www.linkedin.com/pulse/building-harness-around-our-coding-agents-eight-failure-karl-wirth-2lmte — eight pillars (context, provenance, capability, workflow, restraint, verification, UI, coordination)
- https://www.heyuan110.com/posts/ai/2026-03-31-harness-claudemd-guide/ — fat CLAUDE.md can make agent dumber

### X (posts — durable URLs)
- https://x.com/sjwhitmore/status/1645811222661718021 — early agent loop nondeterminism / guardrails (2023, still cited conceptually)
- https://x.com/RaoulDukeDegen/status/2077353734154392047 — AGENTS.md anti-pattern claim (swyx sacred cow)
- https://x.com/phosphenq/status/2070967048193159344 — agent loop broken → structured graph
- https://x.com/Sprytixl/status/2073723542332456997 — five broken loops (Blind/Tangled/Nodding/Amnesiac/Manual)
- https://x.com/DataChaz/status/2070415564510785812 — Discover/Isolate/Verify/Persist/Schedule loop PDF meme
- https://x.com/Degen_calls_sol/status/2075972702607655131 — verify-centered loop; premature success / self-review bias
- https://x.com/DrOptix_/status/2078384163489513520 — AGENTS.md mock pass, real fail (2026-07-18)
- https://x.com/guneysol/status/2078390254864675118 — Orwell rules into CLAUDE/AGENTS for less slop
- https://x.com/Bartek95058577/status/2078398038716928215 — Codex vs Claude agents.md / overengineering (same-day)
- https://x.com/Dmitr_AI/status/2078024185700344283 — multi-agent worktree parallel + writer≠judge
- https://x.com/AndyThinkMode/status/2077234648074330526 — Codex worktree UX regression → shared checkout collisions
- https://x.com/milinpaul/status/2076550150286348602 — two sessions same folder collide; worktrees don’t
- https://github.com/openai/codex/issues/32927 — (linked) Worktree/Local missing from Codex macOS composer

---

## 5. Implications for an elite harness (Adaptoid-shaped)

Map community LIVE signal → harness laws (not prescriptions beyond evidence):

1. **Evidence or it didn’t happen** — matches false-done / nodding-loop panic; require verifier + command output.
2. **Replace, never append, state** — amnesiac loop fix; disk memory over context-only.
3. **Stay in the box / blast radius** — restraint + hooks; permission creep is a named loop killer.
4. **Worktree isolation as default parallel** — tangled-loop fix; enforce in orchestrator.
5. **AGENTS.md as thin law, skills as progressive protocols** — avoid encyclopedia rot and stage-0 thrash.
6. **Second-opinion / non-self-grade** — structural, not prompt.
7. **Budget + schedule + authorization before autonomy** — else “manual” or runaway.
8. **Multi-host portable instructions** — community already dual-runs CC + Codex; shared AGENTS/skills win.
9. **Graph/stoppability** — unbounded retry loops without visible control are out of fashion among sophisticated posters.
10. **Ceremony only if SDLC gate** — HN skepticism of AGENTS/SKILLS theater without better outcomes.

---

## 6. Honesty / gaps / next scrape

| Gap | Why it matters |
|---|---|
| No full HN Algolia date window or comment graph | May miss quieter high-signal threads |
| Reddit is search-hit biased | Hot failures over quiet stable setups |
| X meme-cluster contamination | “Leaked PDF” posts inflate loop-engineering language without primary docs |
| No Discord / private eng Slack | Where much harness craft actually lives |
| No quantitative rates | “High signal” is qualitative recurrence, not prevalence |
| Worktree success rates | Contradictory: “just works” vs “edits main every time” — unresolved |
| AGENTS.md as anti-pattern vs must-have | Live split; likely **length + coercion mechanism** mediate |
| Chinese / EU / enterprise forums | Not sampled |

**Partial D status:** LIVE pulse captured; recurring wins/fails extracted; sources linked. **Not** a complete community survey. Suitable as input to ERA-OCEAN elite synthesis, not as sole decision evidence.

---

*End partial D — `wave-20260718-0837-D-community-live`*
