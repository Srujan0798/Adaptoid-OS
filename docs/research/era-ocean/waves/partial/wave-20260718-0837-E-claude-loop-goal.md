# Research wave partial — 20260718-0837-E — Claude `/loop`+`/goal` · migrations · workflows · Codex long-run

> Status: **INCOMPLETE** · Coverage of agentic world: still **≪1%**  
> Agent: **E** (ERA-OCEAN partial) · Research-only · **Write path:** this file only  
> Do not treat this partial as exhaustive or as product integration.

## Focus (assigned trench)

Deep primary-source extract on:

1. Claude Code official **`/goal`** and **`/loop`** contracts
2. Claude Code **dynamic workflows** (`code.claude.com/docs/en/workflows`)
3. Anthropic **AI code migration** harness (Jul 16 2026 blog)
4. Loop engineering taxonomy (Claude Code team blog)
5. Codex **Goals / scheduled tasks / long-running work** official pages + cookbook

Extract for Adaptoid: **loop+goal contracts**, **migration harness patterns**, **elite multi-day agent patterns**.

---

## Platforms / sources hit this partial

| # | Source | Role |
|---|---|---|
| 1 | https://code.claude.com/docs/en/goal | **Primary** — `/goal` contract |
| 2 | https://code.claude.com/docs/en/scheduled-tasks | **Primary** — `/loop`, cron, routines compare |
| 3 | https://code.claude.com/docs/en/workflows | **Primary** — dynamic workflows / JS harness |
| 4 | https://code.claude.com/docs/en/commands | Commands surface (`/goal`, `/loop` alias `/proactive`) |
| 5 | https://code.claude.com/docs/en/best-practices | Verification ladder incl. `/goal` + Stop hooks |
| 6 | https://code.claude.com/docs/en/glossary | Verification loop as prerequisite for `/goal` |
| 7 | https://claude.com/blog/getting-started-with-loops | Loop taxonomy (turn / goal / time / proactive) |
| 8 | https://claude.com/blog/ai-code-migration | **Primary** — Jul 16 2026 large migrations |
| 9 | https://github.com/anthropics/code-migration-kit-with-claude-code | Starter kit templates (rulebook, daemon, prompts) |
| 10 | https://learn.chatgpt.com/docs/long-running-work | Codex long-running + Goal mode |
| 11 | https://learn.chatgpt.com/docs/automations | Codex scheduled tasks |
| 12 | https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex | Codex Goals architecture (May 9 2026) |
| 13 | https://learn.chatgpt.com/use-cases/follow-goals | Codex “Follow a goal” use case |
| 14 | https://developers.openai.com/blog/run-long-horizon-tasks-with-codex | 25h long-horizon runbook pattern |
| 15 | Secondary: VentureBeat / community posts on `/goal` evaluator (Haiku) | Confirm evaluator story; prefer official docs |

---

## A. Claude Code `/goal` — completion-condition contract

### What it is

- **Command:** `/goal [condition|clear]` (aliases for clear: `stop`, `off`, `reset`, `none`, `cancel`)
- **Min version:** Claude Code **v2.1.139+**
- **Semantics:** Sets a **session-scoped completion condition**. After each turn, a **small fast model** (default **Haiku**) judges whether the condition holds. **No → start another turn** (reason becomes guidance). **Yes → clear goal**, record achieved entry.
- **One active goal per session.** Setting a new goal **replaces** the previous.
- Setting a goal **starts a turn immediately** with the condition as the directive (no separate prompt required).
- Indicator: `◎ /goal active` with elapsed runtime; bare `/goal` shows condition, turns, token spend, last evaluator reason.

### Evaluation mechanics (critical honesty)

- `/goal` is a **wrapper around a session-scoped prompt-based Stop hook**.
- Evaluator **does not run tools or read files independently** — it only judges what Claude **already surfaced in the transcript**.
- Therefore conditions must be **demonstrable via Claude’s own output** (e.g. “all tests in `test/auth` pass” works because Claude runs tests and the result lands in conversation).
- Evaluation tokens billed on small-fast model; typically negligible vs main turns.
- **Unavailable** if trust dialog not accepted, `disableAllHooks`, or `allowManagedHooksOnly` in managed settings — fails loud, not silent.

### Effective condition shape (official)

Up to **4,000 characters**. Strong conditions include:

| Element | Meaning |
|---|---|
| **One measurable end state** | test result, build exit code, file count, empty queue |
| **A stated check** | how Claude proves it (`npm test` exits 0, `git status` clean) |
| **Constraints** | what must not change (e.g. no other test files modified) |
| **Optional turn/time bound** | e.g. `or stop after 20 turns` |

### Lifecycle / resume / headless

| Action | Behavior |
|---|---|
| `/goal clear` | Remove before condition met |
| `/clear` | Also removes active goal |
| Session resume (`--resume` / `--continue`) | **Active** goal restored; **turn count, timer, token baseline reset** |
| Achieved/cleared | **Not** restored |
| `claude -p "/goal …"` | Runs loop to completion in one invocation; use `--output-format stream-json --verbose` so multi-turn goals don’t look stuck |
| Ctrl+C | Stops non-interactive goal early |

### Permissions pairing

- Goal **does not change permissions**. Default mode still prompts for disallowed tools.
- For unattended goals: pair with **auto mode**.

### Fit examples (official)

- Migrate module until call sites compile + tests pass
- Implement design doc until acceptance criteria hold
- Split large file until under size budget
- Drain labeled issue backlog until queue empty

---

## B. Claude Code `/loop` — time-interval contract

### What it is

- **Bundled skill** `/loop` (alias **`/proactive`**)
- **Cadence-driven**, not condition-driven: next turn starts when a **time interval elapses**
- Stops when **you stop it**, Claude decides work is done (self-paced mode), or **7-day expiry**
- **Session-scoped** scheduled tasks; restored on `--resume`/`--continue` if unexpired

### Invocation matrix

| You provide | Example | Behavior |
|---|---|---|
| Interval + prompt | `/loop 5m check the deploy` | Fixed cron schedule |
| Prompt only | `/loop check the deploy` | Claude **self-pacing** (1m–1h) from observations |
| Interval only / nothing | `/loop` or `/loop 15m` | Built-in **maintenance prompt**, or **`.claude/loop.md`** / `~/.claude/loop.md` |

Units: `s`/`m`/`h`/`d` (seconds rounded up to nearest minute; cron min granularity 1m). Odd intervals (e.g. 7m) rounded to clean cron step.

### Built-in maintenance prompt (bare `/loop`)

Order of work:

1. Continue unfinished work from conversation  
2. Tend current branch PR (review comments, failed CI, merge conflicts)  
3. Cleanup (bug hunts, simplification) when nothing pending  

Does **not** start new initiatives outside that scope; irreversible actions only if already authorized in transcript.

### `loop.md` contract

| Path | Scope |
|---|---|
| `.claude/loop.md` | Project (wins if both exist) |
| `~/.claude/loop.md` | User default |

- Plain Markdown, no required structure; **truncated at 25,000 bytes**
- Edits take effect **next iteration**
- Ignored if you pass a prompt on the command line
- **Not** a multi-task list — single default prompt

### Self-paced stop semantics

- Claude may call **`ScheduleWakeup` with `stop: true`**
- If iteration ends without reschedule/stop: fallback wakeup ~20m later; loop ends if that doesn’t reschedule either
- Fixed-interval loops run until you stop or **7-day expiry**
- `Esc` clears pending wakeup for `/loop` (not for NL-scheduled cron tasks)

### Scheduler internals

| Detail | Spec |
|---|---|
| Tools | `CronCreate`, `CronList`, `CronDelete` |
| Max tasks / session | **50** |
| Fire timing | Between turns; queues if Claude mid-response |
| Jitter (recurring) | Up to 30m after scheduled time (or half interval if sub-hourly) |
| One-shot jitter | Up to 90s early if scheduled at :00 or :30 |
| Expiry | Recurring auto-expire **7 days** after creation |
| Disable | `CLAUDE_CODE_DISABLE_CRON=1` |
| Provider caveats | On Bedrock / GCP Agent Platform / Foundry: no-interval → fixed **10m**; bare `/loop` may only show usage (no maintenance / no `loop.md`) |

### Three-way compare: keep session running

| Approach | Next turn when | Stops when |
|---|---|---|
| **`/goal`** | Previous turn finishes | Model confirms condition met |
| **`/loop`** | Time interval elapses | You stop, Claude ends (self-paced), or 7d |
| **Stop hook** | Previous turn finishes | Your script or prompt decides |

**Auto mode** alone = approve tools within a turn; **does not** start a new turn. Complements `/goal`.

### Scheduling that outlives a session (Claude)

| Mode | Runs on | Machine on? | Open session? | Min interval | Local files |
|---|---|---|---|---|---|
| **Cloud Routines** | Anthropic cloud | No | No | 1 hour | No (fresh clone) |
| **Desktop scheduled tasks** | Your machine | Yes | No | 1 minute | Yes |
| **`/loop`** | Your machine | Yes | Yes | 1 minute | Yes (session) |

---

## C. Loop engineering taxonomy (Claude team)

Definition (official team language): **loops = agents repeating cycles of work until a stop condition is met.**

| Loop type | Trigger | Stop | Best for | Primitive |
|---|---|---|---|---|
| **Turn-based** | User prompt | Claude judges done / needs context | Short exploratory tasks | Skills for verification |
| **Goal-based** | Manual prompt / `/goal` | Goal achieved **or** max turns | Verifiable exit criteria | `/goal` |
| **Time-based** | Interval | Cancel, or external work complete | Recurring / poll external systems | `/loop`, `/schedule` (routines) |
| **Proactive** | Event or schedule, no human RT | Per-task goal met; routine until off | Recurring well-defined streams | Compose auto mode + workflows + `/goal` + `/schedule` |

Example proactive composition (blog):

```text
/schedule every hour: check #project-feedback for bug reports.
/goal: don't stop until every report found this run is triaged, actioned, and responded to.
When fixing a bug, use a workflow to explore three solutions in parallel worktrees
and have a judge adversarially review them.
```

### Quality + cost (loop system design)

- Clean codebase patterns; encode “good” as skills  
- Second agent for review (`/code-review`) — maker ≠ checker  
- Pilot dynamic workflows on small slice first  
- Prefer scripts for deterministic steps  
- Don’t poll faster than the watched signal changes  
- Usage surfaces: `/usage`, bare `/goal`, `/workflows` agent token breakdown  

---

## D. Dynamic workflows — harness writes the harness

### What it is

- **JS script** Claude writes; runtime orchestrates **subagents at scale** in background  
- Min version **v2.1.154+**; paid plans + API/Bedrock/GCP/Foundry  
- Plan lives in **code** (loops, branching, intermediate vars), not Claude’s context  
- Intermediate results in **script variables**; conversation gets final answer  

### Who holds the plan

| | Subagents | Skills | Agent teams | **Workflows** |
|---|---|---|---|---|
| Next step decided by | Claude turn-by-turn | Claude + prompt | Lead agent | **The script** |
| Intermediate state | Context window | Context window | Shared task list | **Script vars** |
| Repeatable unit | Worker def | Instructions | Team def | **Orchestration itself** |
| Scale | Few per turn | Same | Handful of peers | **Dozens–hundreds / run** |

### Trigger paths

- Keyword **`ultracode`** (or “use a workflow”) in **human-origin** prompts only  
- Pre-v2.1.160 keyword was `workflow`  
- **`/effort ultracode`**: xhigh effort + auto-plan workflows for substantive tasks (v2.1.203+)  
- Bundled: **`/deep-research`** (fan-out search, cross-check claims, cited report)  
- Save: `/workflows` → `s` → `.claude/workflows/` (project) or `~/.claude/workflows/` (personal)  

### Runtime constraints

| Constraint | Why |
|---|---|
| No mid-run user input (except permission prompts) | Stage-signoff = separate workflows |
| Script itself: no FS/shell | Agents do I/O; script coordinates |
| ≤ **16 concurrent** agents (fewer on small CPUs) | Local resource bound |
| ≤ **1,000 agents total / run** | Anti-runaway |
| Resume | Same session; completed agents cached; in-flight agents restart |
| Exit Claude mid-run | Next session starts workflow **fresh** |
| Large workflow warning | >25 agents or >1.5M projected tokens (advisory; ultracode suppresses) |

### Script shape (portable idea)

```javascript
export const meta = { name: 'audit-routes', description: '…' }
const found = await agent('List every .ts file under src/routes/.', { schema: … })
const audits = await pipeline(found.files, file =>
  agent(`Audit ${file} …`, { label: file }),
)
return audits.filter(Boolean)
```

`agent()` = one subagent; `pipeline()` = one per list item. Subagents run in **`acceptEdits`** and inherit tool allowlist.

### Example workflow shapes (elite multi-file / multi-day)

- Fan-out audit + **adversarial verify** each finding  
- **Loop-until-done:** `tsc --noEmit` until pass or two no-progress rounds  
- Parallel migrate per file in **isolated copies**  
- Per-file review → merge ranked summary  
- Research fan-out + synthesize  
- Search until list stops growing (flaky tests)  

---

## E. Jul 2026 migration harness — “fix the process, not the code”

**Primary:** *How Anthropic runs large-scale code migrations with Claude Code* (Jul 16, 2026)

### Proof points (reported)

| Case | Scale | Stack / notes |
|---|---|---|
| Bun Zig → Rust (Jarred Sumner) | ~1M LOC in <2 weeks; suite green in CI pre-merge; 19 post-merge regressions fixed | Fable 5 + Opus 4.8 + dynamic workflows; ~5.9B uncached input + 690M output tokens (~$165k API) |
| Python → TS (Mike Krieger) | ~165k LOC TypeScript over a weekend | Hundreds of agents, 8 phase gates, 3 adversarial review rounds, parity harness of 7 scenarios; main port ~27M tokens |

**Core insight:** *You don’t fix the code. You fix the process (loop) that produced the code.*

### Why migrations suit agents

1. **Parallel** independent units (files/crates)  
2. **Old code is the spec**  
3. **Built-in referee** (tests / compiler / parity)  
4. **Queue writes itself** from failures  
5. **Consistency** via growing rulebook + adversarial review  

### Prerequisite: the Judge

Before migrating:

1. Categorize tests (externalizable vs internal-only)  
2. Rewrite portable assertions; adversarial agents check for weakened asserts  
3. Validate judge: pass on original; **fail on deliberately broken** code  

No ported suite? Build a **parity harness** (Mike: 7 real-world scenarios, any behavior delta = bug).

### Six steps (generalized)

| Step | Purpose | Harness pattern |
|---|---|---|
| **1** Rulebook + dependency map + gap inventory | Policy before bulk work | Rulebook **before** gap inventory; joint audit; skeptic reviewers |
| **2** Stress-test rules | Shakedown cruise | 3-file translate w/ rulebook vs “senior engineer”; **throw out code**; only keep rules |
| **3** Translate everything | Mechanical queue | Done = **file exists on disk**; batch scripts; `// TODO(port):` for unknowns; implementer on smaller models; **adversarial dual reviewers** + third on disagreement; rulebook grows, code not hand-patched against rules |
| **4** Compile | Error list as queue | Orchestrator + parallel fixers; classify systemic errors → loop fix |
| **5** Run / smoke | Crashes as queue | Group by root cause |
| **6** Match behavior | Parity / suite | Fixer agents vs both codebases; **build daemon** serializes rebuild; overnight self-designed E2E loop |

**Compiler-in-loop decision:** Mike ran TS compiler **inside** every loop (seconds). Jarred **banned** cargo from the translate loop (minutes) and deferred to compile step.

**Mike’s meta-loop:** full end-to-end migration → revise rules/workflow → **discard output** → rerun; shipped third run.

### Best practices (portable elite)

- Don’t follow guide blindly — plan *this* migration with Claude  
- Humans watch **patterns**, not individual failures (fixers burn those)  
- Adversarial review + **mechanical** verification  
- **Model routing:** small models for high-volume implement; largest for reviewers + rule writers  
- Front-load human hours on rulebook + stress test  
- Queue **mechanical + resumable** (disk is truth)  
- **Review loop results, not code**  

### Related artifacts

- Starter kit: https://github.com/anthropics/code-migration-kit-with-claude-code (generalized template, not the exact ports)  
- Code-modernization plugin (legacy/framework upgrades, not full language ports)  
- Dynamic workflows blog + docs  

---

## F. Codex Goals / scheduled tasks / long-running (official)

### Goal = completion contract (not unbounded autonomy)

From cookbook + long-running docs:

- **Goal:** persistent objective on a **thread** — what must be true, how checked, constraints  
- **Prompt:** do next thing → wait  
- **Goal:** work → check evidence → continue or complete  
- Lifecycle: `/goal`, `/goal pause`, `/goal resume`, `/goal clear`; progress row on desktop  
- Min version noted in cookbook: **Codex 0.128.0+**; may need `features.goals = true`  
- Goal mode **does not expand sandbox**; same approval/sandbox policy  

**Strong Goal six-part contract (cookbook):**

1. Outcome  
2. Verification surface  
3. Constraints  
4. Boundaries (allowed files/tools)  
5. Iteration policy  
6. Blocked stop condition  

Architecture notes (cookbook):

- Goal = **thread-scoped persisted state**, not global memory / project instructions  
- Continuation **event-driven** at safe idle boundaries  
- Plan-only work doesn’t continue; no-tool continuation turn suppresses next auto-continue (anti-spin)  
- Budget limit ≠ completion — stop, summarize, name next step  
- Model may mark complete **only with evidence**; pause/resume/clear/budget transitions user/system-controlled  

**Official long-running guidance:**

- Outcome + constraints + definition of done  
- Same chat for related work; separate chats for parallel independent work  
- Prefer `/plan` first if outcome unclear, then `/goal`  
- Parallel goals: use **worktrees** so two chats don’t write the same files  
- Prevent sleep while running (desktop)  

**Follow-a-goal use case:** multi-hour independent work; checkpoints + progress log; migrations / refactors / prototypes / eval-driven prompt optimization.

### Scheduled tasks (Codex Automations)

| Aspect | Spec |
|---|---|
| Surfaces | ChatGPT web **Scheduled** + desktop; **not** CLI/IDE management UI |
| Local | Desktop needs machine on + app running; project on disk |
| Worktrees | Optional isolate for Git repos |
| In-chat schedule | Reuses chat context (minute-based follow-up loops) |
| Standalone | New chat each run; findings in Scheduled inbox |
| Skills | Prefer skills for durable shareable workflows; `$skill-name` on desktop |
| Security | Unattended; `approval_policy = "never"` when org allows; start narrow sandbox |

### Long-horizon durable memory (Codex blog, Feb 2026)

25h design-tool experiment (GPT-5.3-Codex Extra High): ~13M tokens, ~30k LOC.

**File stack pattern:**

| Artifact | Role |
|---|---|
| Spec markdown | Goals, non-goals, hard constraints, deliverables, “done when” |
| `plans.md` | Milestones + acceptance + validation commands + stop-and-fix |
| `implement.md` | Runbook: follow plan, scoped diffs, validate after each milestone, update docs |
| Documentation/status log | Live audit trail |

Loop shape: **plan → edit → tools (test/build/lint) → real feedback → externalized state (repo/files/worktrees) → steer**.

App primitives: parallel project threads, skills, automations, git worktrees.

---

## G. Cross-host contracts — side-by-side

| Dimension | Claude Code | Codex |
|---|---|---|
| Completion contract | `/goal` + Haiku evaluator on **transcript** | `/goal` + evidence audit in **thread state** |
| Time / poll | `/loop` + session cron; routines/desktop for durable | Scheduled tasks (web/desktop); in-chat minute loops |
| Multi-agent harness | Dynamic workflows (JS, up to 1k agents/run) | Skills, worktrees, parallel chats; less “script owns loop” in official docs |
| Multi-session multi-day | Progress files / git / feature JSON (see W2 Anthropic eng post); workflows not cross-session resume | Durable project markdown + worktrees + scheduled return-to-chat |
| Maker ≠ checker | Separate evaluator model; adversarial workflow agents; Stop hooks | Evidence-based completion; auto-review for approvals |
| Weakness honesty | Evaluator **cannot independently re-run checks** | Continuation can still drift if verification surface vague |

---

## H. Elite patterns for multi-day agents (extract)

### 1. Separation of concerns (trigger vs stop)

| Concern | Own with |
|---|---|
| **What starts the next cycle** | Interval (`/loop`, schedule) vs turn-end (`/goal`, Stop hook) vs event (channels/webhooks) |
| **What ends the work** | Verifiable condition + external referee (tests, compiler, parity, benchmark) |
| **Who grades done** | **Not** the implementer alone — small evaluator, second agent, or mechanical script |

### 2. Completion contracts (portable Goal shape)

```
DONE when: <measurable end state>
PROOF: <command / artifact / diff that must appear in evidence>
CONSTRAINTS: <must not regress>
BOUNDARIES: <scope of files/tools>
BUDGET: <turns / time / tokens>
BLOCKED: <when to stop and report>
```

### 3. Migration / multi-day factory OS

1. **Judge first** (parity harness / portable tests)  
2. **Rulebook before mass translate**  
3. **Stress-test rules; discard code**  
4. **Mechanical queue** (`done` = artifact on disk)  
5. **Implement small / review large models**  
6. **Adversarial dual review** + rulebook growth over one-off patches  
7. **Phase gates** (compile → smoke → parity)  
8. **Serialize expensive ops** (build daemon)  
9. **Human attention on patterns**, not individual red items  
10. Optional meta-loop: full pipeline dry-run, **throw away**, refine process, rerun  

### 4. Multi-session bridge (compose with W2 Anthropic harness)

Even with `/goal`, sessions die. Elite multi-day still needs **disk truth**:

- progress / status log  
- git history  
- feature or milestone list with `passes` only after E2E  
- init/smoke script  
- rulebook / plans.md / implement.md  

`/goal` keeps **one session** grinding; disk artifacts keep **the project** grinding across sessions.

### 5. Host primitive composition (proactive multi-day)

```
schedule/routine  →  wake agent
goal contract     →  keep turning until verified
workflow script   →  fan-out + adversarial check
auto permissions  →  unattended tool use (blast radius deliberate)
worktrees         →  isolate parallel agents
mechanical referee→  compiler / suite / parity / benchmark
```

### 6. Anti-patterns named by sources

| Failure | Mitigation |
|---|---|
| Agentic laziness / early victory | Separate evaluator; hard goal condition; feature `passes` only after E2E |
| Self-preferential bias | Adversarial second agent / dual reviewers |
| Goal drift after compaction | Durable files; short goals; rulebook as source of truth |
| Vague goals | Measurable outcome + stated check + constraints |
| Evaluator blindness (Claude) | Force Claude to **run** the check so transcript holds evidence |
| Runaway workflows | Size guidelines; pilot slice; pause/stop in `/workflows` |
| Concurrent write thrash | Worktrees / isolated copies |
| Fixing code not process | Pattern → rulebook sentence → regenerate batch |

---

## I. Adaptoid delta (research → later product)

| Concept | Verdict | Notes |
|---|---|---|
| Goal as completion contract language | **Adopt (language)** | Aligns acceptance / SHIP gates; name “Goal-compatible DoD” |
| Separate evaluator / maker≠checker | **Adopt (already principle)** | Maps to evidence laws + dual agents |
| `/loop` vs `/goal` distinction | **Adopt (playbook)** | Cadence ≠ completion |
| Mechanical disk queue + resumable batches | **Watch → likely adopt for multi-day** | Fits HANDOFF/progress patterns |
| Dynamic workflow JS runtime | **Watch** | Host-native; Adaptoid stays portable mission layer |
| Migration six-step factory | **Watch** | High value for ports; not every T0 task |
| Evaluator that only reads transcript | **Honesty gap** | Prefer Stop-hook **scripts** for deterministic gates when stakes high |
| 7-day loop expiry / budget stops | **Adopt as cost discipline** | Bound forgotten loops |
| Codex six-part Goal template | **Adopt as prompt template** | Outcome/verify/constraints/boundaries/iteration/blocked |

**This partial: research corpus only — no Core product edits.**

---

## J. Gaps / incomplete (mandatory honesty)

**What this partial did well**

- Full official `/goal` + `/loop` pages  
- Full workflows constraints + migration blog process  
- Codex Goals cookbook architecture + scheduled + long-running docs  

**What remains incomplete**

- Did **not** re-scrape Anthropic Nov 2025 long-running eng post (covered in W2)  
- Did **not** open migration kit every prompt file line-by-line  
- Claude **Routines** deep API (only compared in scheduled-tasks table)  
- Managed Agents / Dreams not in this trench  
- Codex `prompting#goal-mode` page not fully fetched beyond long-running/use-case/cookbook  
- No live CLI verification of versions on this machine  
- Community failure modes (cost blowups, false “goal met”) only lightly secondary  
- OpenClaw / DeepSeek / Kimi / eval science still open ocean  
- Product integration of these contracts into Adaptoid Core **not done**  

**Coverage claim:** still **≪1%** of agentic surface. Ocean open.

---

## Sources (canonical list)

1. https://code.claude.com/docs/en/goal  
2. https://code.claude.com/docs/en/scheduled-tasks  
3. https://code.claude.com/docs/en/workflows  
4. https://code.claude.com/docs/en/commands  
5. https://code.claude.com/docs/en/best-practices  
6. https://code.claude.com/docs/en/glossary  
7. https://claude.com/blog/getting-started-with-loops (Jun 30, 2026)  
8. https://claude.com/blog/ai-code-migration (Jul 16, 2026)  
9. https://github.com/anthropics/code-migration-kit-with-claude-code  
10. https://learn.chatgpt.com/docs/long-running-work  
11. https://learn.chatgpt.com/docs/automations  
12. https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex (May 9, 2026)  
13. https://learn.chatgpt.com/use-cases/follow-goals  
14. https://developers.openai.com/blog/run-long-horizon-tasks-with-codex (Feb 23, 2026)  
15. Related (not deep this partial): Anthropic “Effective harnesses for long-running agents”; dynamic workflows product blog  

---

## Honesty footer (mandatory)

- Ocean still open. Coverage ≪1%.  
- This is **partial agent E** research notes, not a complete map of agentic systems.  
- Never claim finished, complete, or “mapped 100%”.  
- Evidence for “done” on product work still requires local commands + outputs — blog claims are **reported**, not re-run here.

**Ocean still open. Next wave candidates:** OpenClaw/Odysseus architecture · DeepSeek/Kimi agent docs · Claude Routines deep · Terminal-Bench vs product DoD · wire Goal/loop contracts into elite draft only after more waves.
