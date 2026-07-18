# Research wave — 20260718-0827 — Cherny + long-running harness + Goals

> Status: **INCOMPLETE** · Coverage of agentic world: still **≪1%**  
> Do not treat this wave as exhaustive.  
> Focus trench (MANIFEST next-targets #1–3): **Boris Cherny primary-adjacent + Anthropic long-running harness + Claude Agent SDK + Codex Goals/Automations**

## Focus

Deep dive on **how elites run agents across sessions and organizational scale** — not listicles:

1. Anthropic engineering: *Effective harnesses for long-running agents* (primary)
2. Anthropic product blog: *A harness for every task* (dynamic workflows)
3. Claude Agent SDK official docs
4. Boris Cherny interviews / secondary primary-adjacent (WorkOS Acquired notes, Sequoia Ascent summaries, X adoption-levels map)
5. OpenAI Codex Goals + Automations (official cookbook + academy)
6. HN discussion threads on long-running harnesses / Agent SDK
7. Community (X, Reddit r/codex, YC library entry)

## Platforms / sources hit this wave (≥12)

| # | Platform | Role |
|---|---|---|
| 1 | anthropic.com/engineering | Long-running harness primary paper |
| 2 | claude.com/blog | Dynamic workflows / harness-per-task |
| 3 | code.claude.com/docs | Agent SDK overview (tools, hooks, subagents) |
| 4 | workos.com/blog | Acquired Unplugged Cherny takeaways |
| 5 | youtube.com (Sequoia / WorkOS) | Cherny primary video references |
| 6 | ycombinator.com/library | Inside Claude Code w/ Cherny entry |
| 7 | developers.openai.com/cookbook | Using Goals in Codex |
| 8 | openai.com/academy | Codex Automations |
| 9 | news.ycombinator.com | Long-running harness + Agent SDK threads |
| 10 | x.com | Adoption levels 0–4 / loop discourse (live) |
| 11 | reddit.com/r/codex | Goals as completion contracts |
| 12 | github.com/anthropics/claude-quickstarts | autonomous-coding quickstart (referenced) |
| 13 | epsilla.com (secondary) | Sequoia Ascent Cherny summary (use cautiously) |
| 14 | developers.openai.com/codex | Automations / long-running / worktrees nav |

## Concepts extracted (high signal)

### A. Anthropic long-running harness (Nov 2025 engineering post) — **elite core**

**Problem:** Agents work in **discrete sessions** with **no memory**. Compaction is not enough.

**Two failure modes without harness:**
1. **One-shot / too much at once** → context dies mid-implementation → next session guesses
2. **Early victory** → later agent sees partial progress and declares done

**Two-agent pattern (same harness, different first prompts):**
| Role | Job |
|---|---|
| **Initializer agent** | First session only: `init.sh`, `claude-progress.txt`, initial git commit, **feature_list JSON** with all features `passes: false` |
| **Coding agent** | Every later session: **one feature**, clean mergeable state, git commit + progress write |

**Disk artifacts that bridge sessions:**
- `claude-progress.txt` (what was done)
- `git` history (revert bad states)
- `feature_list.json` (JSON preferred over Markdown — less model thrash)
- `init.sh` (how to run + smoke test)

**Session boot ritual (elite):**
1. `pwd`
2. Read progress + features
3. `git log`
4. Run `init.sh` / smoke end-to-end as a **user** would
5. Only then pick next failing feature

**Testing rule:** Unit tests / `curl` alone insufficient. Prefer **browser automation as human user** before `passes: true`. Strong instruction: do not delete/edit tests to make green.

**Open questions Anthropic leaves:** single general agent vs specialized (test/QA/cleanup); generalize beyond web apps.

### B. Dynamic workflows (Jun 2026 Claude Code blog) — **harness writes harness**

Claude can **write its own multi-agent harness** (JS workflow) on the fly for tasks that break single-context defaults.

**Named failure modes in one context:**
| Mode | Meaning |
|---|---|
| **Agentic laziness** | Stops mid multi-part task; claims done |
| **Self-preferential bias** | Prefers its own findings when self-grading |
| **Goal drift** | Fidelity loss after compaction |

**Composable patterns (portable to any factory OS):**
- Classify-and-act
- Fan-out-and-synthesize
- **Adversarial verification** (maker ≠ checker structural)
- Generate-and-filter
- Tournament
- Loop-until-done
- **Quarantine** (agents that read untrusted content cannot take high-privilege actions)

**Host primitives to pair:** `/loop` (cadence) + `/goal` (hard completion) + token budgets + worktrees + model routing.

**When not:** most ordinary coding; multi-agent must **earn** coordination cost.

### C. Claude Agent SDK — **productizable harness**

Same tools/loop/context management as Claude Code, as a library (Python/TS). Built-ins: Read/Write/Edit/Bash/Monitor/Glob/Grep/Web*/AskUserQuestion + hooks (`PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`…) + subagents + MCP + sessions resume/fork + filesystem config (skills, CLAUDE.md).

**Elite split:** Client SDK = you implement tool loop; Agent SDK = harness owns tool loop.

### D. Boris Cherny (interview cluster — not full official transcript)

**Phase change:** stop prompting → **write loops** that prompt Claude (CI babysit, flaky tests, feedback clustering). Job = orchestrate.

**Org effects (WorkOS notes):** ramp days not weeks; high % of code agent-written; generalists ship across roles.

**Adoption ladder (X summaries of Cherny map — verify primary if published):**
| Level | Shape |
|---|---|
| 0 Gated | AI blocked |
| 1 Assisted | 1 human : 1 agent, heavy review |
| 2 Parallel | ~10 agents; self-check before human |
| 3 Supervised autonomy | ~100 background agents; human manages workflows |
| 4 AI-native | agents launch agents; human sets intent |

**Each level needs new guardrails:** E2E verification, auto code/security review, safe permissions, **isolated worktrees**, **cost controls**. Measure **engineering hours saved**, not tokens burned.

**Harness decay thesis (Sequoia summaries / Epsilla):** models may cannibalize rigid harness code over time. **Adaptoid stance: WATCH** — mission OS / evidence gates still needed while models remain jagged.

### E. Codex Goals + Automations (OpenAI official)

- **Goal** = persistent **completion contract**: what must be true, how success is checked, constraints. Not unbounded autonomy.
- **Automations** = scheduled/triggered runs (heartbeat) with triage/review surface.
- Aligns with maker≠checker if stop condition is **verified externally**.

### F. HN / community

- Long-running harness post resonates: progress files = state that survives `/clear`
- Agent SDK is “Claude Code as library”; OSS forks extract loops; auth/ToS friction for productizing OAuth
- Ash / open-agent-sdk class tools = “agent is a folder” (CLAUDE.md + skills + deploy)

## Elite candidates (for ELITE-10-PERCENT.md)

1. **Initializer / coding dual prompt** for multi-session work  
2. **Feature JSON with `passes` only toggled after E2E**  
3. **Progress file + git as shift-handoff**  
4. **Smoke boot before new work**  
5. **Agentic laziness / early victory as named FMs**  
6. **Self-preferential bias → force external verifier**  
7. **Dynamic workflow patterns** (adversarial, quarantine, tournament)  
8. **Adoption levels 0–4 + guardrails ladder**  
9. **Goals as completion contracts** (not vibes)  
10. **Measure eng-hours ROI, not token vanity**  
11. **Harness decay is a bet, not a product strategy**  

## Adaptoid delta (adopt / watch / refuse)

| Concept | Verdict | Notes |
|---|---|---|
| Initializer + progress + feature list | **Adopt (research→product later)** | Maps to intent-lock + plan/* + HANDOFF; consider `plan/feature-list.json` pattern in docs only this wave |
| Session boot ritual | **Adopt (playbook note later)** | Aligns wake.sh + SHIP stages |
| JSON feature passes | **Watch** | Strong for multi-day builds; don’t force on every T0 hackathon |
| Dynamic workflow full JS harness | **Watch** | Host-native; Adaptoid stays portable mission layer |
| Cherny “harness → 100 lines” | **Refuse as product strategy** | Keep gates; models still jagged |
| Adoption ladder 0–4 | **Adopt as mental model in elite/playbook** | Not a new kernel law |
| Codex Goals shape | **Adopt as language** | “acceptance contract” already in tasks; name it Goal-compatible |
| Multi-agent always | **Refuse default** | Earn coordination cost |
| Auto-mark done from unit tests | **Refuse** | E2E / preflight law |

**This wave: research corpus only — no Core product file edits.**

## Gaps opened (ocean grew)

- Full Boris primary transcript not scraped line-by-line (YouTube only referenced)
- No deep Managed Agents REST API pass
- Claude Code `/loop` `/goal` official slash-command pages not fully fetched
- DeepSeek / Kimi / CN discourse still untouched
- Enterprise multi-agent org design still thin
- Security prompt-injection papers not this wave

## Next wave should hit

1. **OpenClaw / Odysseus primary GitHub architecture audit** (local self-OS vs coding harness)  
2. **DeepSeek + Moonshot Kimi agent-loop product docs**  
3. **Claude Code official `/loop` `/goal` + migrations blog (Jul 16 2026)**  
4. **Terminal-Bench methodology vs product DoD**  

---

## Honesty footer (mandatory)

- Ocean still open. Coverage ≪1%.  
- We have not done the full agentic world; huge ecosystem remains.  
- Never claim complete, finished, or “mapped 100%”.  

**Ocean still open. Next wave should hit: OpenClaw/Odysseus primary architecture + DeepSeek/Kimi agent docs + Claude `/loop`/`/goal` official pages.**
