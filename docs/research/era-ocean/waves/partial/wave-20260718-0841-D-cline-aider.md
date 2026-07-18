# ERA-OCEAN Partial D — Cline + Aider

**Wave:** `wave-20260718-0841-D`  
**Agent:** D (open coding harnesses — Plan/Act, rules, MCP, git)  
**Status:** INCOMPLETE (web + docs primary; no local install, no deep monorepo source audit, no head-to-head eval run)  
**Written:** 2026-07-18  
**Scope:** Cline (`cline.bot`, `github.com/cline/cline`) and Aider (`aider.chat`) — Plan/Act (and ask/architect), AGENTS.md / rules / conventions, MCP, git shape, harness vs Claude Code, elite portable concepts for Adaptoid.  
**Files touched:** **This file only.**

---

## 0. Honesty / coverage gaps

| Gap | Why it matters |
|-----|----------------|
| No local `npm i -g cline` / `aider-install` / Kanban run | Latency, approval UX, checkpoint storage cost, true YOLO risk unmeasured |
| Cline monorepo ~6.5k commits; packages (`sdk/`, `apps/cli/`, hub-spoke) only sampled via docs + README | Exact tool schemas, permission matrix, eval harness in `evals/` not audited |
| JetBrains client not open-sourced (README) | Parity claims with VS Code are product narrative |
| Aider native MCP: **not first-class** in core CLI (open issues + community wrappers; re-verify) | Do not claim Aider = full MCP host without code proof |
| Star / install / “singularity %” marketing stats lag or self-report | Soft signals only |
| Claude Code comparison is public product shape, not Anthropic internal harness docs | Not a reverse-engineer of Claude Code |
| Secondary “vs Claude Code” roundups (MorphLLM, Codepick, Reddit) mixed in lightly | Prefer primary docs; treat score tables as soft |

**What is solid:** official READMEs, docs.cline.bot (Plan/Act, Rules, Skills, MCP, Checkpoints, Auto Approve, Hub-Spoke, Memory Bank), aider.chat (modes, conventions, git, repomap, tips), GitHub product surfaces, prior wave `wave-20260718-w1-hosts-models-standards` notes.

---

## Mission question

What **elite, portable harness patterns** do Cline and Aider encode (Plan before Act, git as transaction log, rules/skills loading, approval ladders, multi-surface agent core) — and what should Adaptoid **steal as contracts** vs leave to host fields (Claude Code / Cline / Aider / Codex / Grok Build)?

---

## Executive thesis (for Adaptoid)

1. **Cline is a full multi-surface coding agent product** (IDE + CLI + TUI + SDK + Kanban + connectors + hub-spoke daemon). Closest open analogue to Claude Code’s *product shape*, with stronger historical emphasis on **explicit Plan/Act** and **per-tool approval**, now expanded into YOLO, teams, schedules, and messaging.

2. **Aider is a terminal-native pair-programmer with git as the transaction log.** Smaller “agent product” surface (few subagents/MCP/schedules) but **elite** on: repo map context, edit formats, auto-commit / undo, ask→code workflow, architect/editor dual-model split, conventions via read-only files.

3. **Plan/Act is not marketing — it is a permission + context discipline.** Cline hard-separates modes (Plan cannot write/run). Aider soft-separates via `/ask` vs `/code` (and dual-model architect). Claude Code also has plan mode (markdown plan artifact + tool permission interplay) — same elite idea, different packaging.

4. **Rules stack is converging on AGENTS.md as cross-host standard**, while hosts keep proprietary skins (`.clinerules`, `CONVENTIONS.md`, `CLAUDE.md`). Cline explicitly multi-loads: `.clinerules/`, Cursor/Windsurf rules, `AGENTS.md` + `~/.agents/AGENTS.md`. Aider: any markdown via `--read` / `read:` in `.aider.conf.yml` (community asks to *recommend* `AGENTS.md`).

5. **Git policy diverges and both are portable lessons.**  
   - **Aider:** every AI edit → descriptive commit (Conventional Commits default); dirty-file pre-commit; `/undo`; attribute “(aider)”.  
   - **Cline:** **shadow git checkpoints** separate from user history + optional Kanban auto-commit/PR; user owns real git.  
   Adaptoid: **evidence commits** + **replace-state HANDOFF** already map; do not force one host’s git policy into Core.

6. **MCP is first-class in Cline, second-class/workaround in Aider.** Portable rule: mission OS must treat MCP as **high blast-radius** (FM-20) regardless of host polish.

7. **Do not reimplement Cline or Aider inside Adaptoid Core.** Steal patterns: dual-mode gates, progressive skill loading, shadow checkpoint semantics, repo-map-class context, conventions as always-on read context, multi-host AGENTS.md.

---

## 1. Positioning map

| Dimension | **Cline** | **Aider** | **Claude Code** (public shape, for contrast) |
|-----------|-----------|-----------|-----------------------------------------------|
| **One-liner** | Open coding agent: IDE/CLI/SDK/Kanban | AI pair programming in the terminal | Anthropic coding agent CLI/IDE/SDK |
| **Primary surface** | VS Code/Cursor/Windsurf/JB + CLI/TUI | Terminal (any editor); watch-mode comments | Terminal-first + IDE + Agent SDK |
| **License** | Apache-2.0 (Cline Bot Inc.) | Open source (Aider-AI/aider; Apache-class — confirm LICENSE on clone) | Proprietary product; Agent SDK published |
| **Model posture** | Multi-provider + Cline credits / ClinePass / BYOK / local | Multi-provider BYOK / local; edit-format aware | Anthropic-centric + subscription paths |
| **Plan/Act** | First-class Plan vs Act (Plan: no file/cmd mutations) | `/ask` vs `/code`; `/architect` dual-model | Plan mode + plan markdown; YOLO/autonomy levels |
| **Rules** | `.clinerules/`, AGENTS.md, Cursor/Windsurf rules, skills | `CONVENTIONS.md` / any `--read`; conf `read:` | `CLAUDE.md`, skills, hooks, settings |
| **MCP** | Native client (stdio + streamable HTTP/SSE); `autoApprove` per tool | **No strong native host** (issues; wrappers; AiderDesk fork-class) | Native MCP + skills ecosystem |
| **Git** | Checkpoints = shadow repo; user git clean; Kanban worktrees | Auto-commit every edit; undo via git | Git-aware; user-controlled commits typical |
| **Multi-agent** | Teams, subagents, Kanban parallel worktrees | Weak / single-session focused | Subagents, Agent teams (product evolution) |
| **Embed** | `@cline/sdk`, hub-spoke, ClineCore | CLI-first; community MCP wrappers of Aider | Claude Agent SDK ≈ Code-as-library |
| **Repo (primary)** | https://github.com/cline/cline | https://github.com/Aider-AI/aider | Anthropic product docs |
| **Docs** | https://docs.cline.bot | https://aider.chat/docs/ | https://code.claude.com/docs |
| **Site** | https://cline.bot | https://aider.chat | https://claude.com/product/claude-code |

**Species difference:** Cline competes as a **Claude Code–class agent OS surface**. Aider competes as a **minimal, git-correct edit loop** — closer to “best-in-class patch engine + chat” than full agent product.

---

## 2. Cline — harness shape

### 2.1 Surfaces (one engine, many clients)

From README + docs overview (2026-07-18 scrape):

| Surface | Role |
|---------|------|
| **VS Code extension** | Marketplace (`saoudrizwan.claude-dev` historical id); diffs, approvals, browser, tools |
| **JetBrains plugin** | Same experience; client not OSS |
| **CLI** | `npm i -g cline` — interactive + **headless** / JSON / CI |
| **TUI** | Terminal UI workflow |
| **Kanban** | `npx kanban` / `npm i -g kanban` — parallel cards, **git worktrees**, auto-commit/PR (research preview) |
| **SDK** | `@cline/sdk` — Agent, tools, plugins, teams, schedule, connectors |
| **Connectors** | Slack, Telegram, Discord, WhatsApp, Linear, etc. |
| **Enterprise** | SSO, remote config, MCP allowlists, OTEL, YOLO governance |

**Hub-spoke architecture (SDK/docs):**

- **Hub** — singleton local daemon; sessions, approvals, schedules, capability brokerage; does **not** run the agent loop.
- **Spoke** — worker runs `@cline/core` agent loop; process isolation.
- **Client** — CLI/IDE/custom; WebSocket attach; can disconnect without killing session.
- Modes: `auto` | `hub` | `remote` | `local`.
- Session store: `~/.cline/data/sessions/` (SQLite index + JSON snapshots).
- Default hub listen: `127.0.0.1:25463` (docs).

**Elite portable idea:** separate **coordination daemon** from **execution workers** from **UI clients** — sessions survive IDE close; multi-client attach; capability brokerage (IDE opens diffs, CLI owns shell).

### 2.2 Plan & Act (core dual-mode)

Official behavior ([Plan & Act](https://docs.cline.bot/core-workflows/plan-and-act)):

| Mode | Can do | Cannot do |
|------|--------|-----------|
| **Plan** | Read codebase, search, discuss strategy, clarify, review | Modify files, execute commands |
| **Act** | Full tool loop: edit, bash, browser, MCP (per approval) | — |

- Conversation history **carries over** on mode switch.
- Optional **separate models** for Plan vs Act (e.g. Opus plan / Sonnet act; cheap plan / fast act).
- **`/deep-planning`** for large multi-file work: systematic explore → affected files → detailed plan → clarifying questions.
- Task sizing guidance: small → Act only; medium → Plan→Act; large → deep-planning + todo list + checkpoints.

CLI flags (docs): `-p/--plan` start in Plan; `--auto-approve` for global tool auto-approval in headless paths.

**Vs Claude Code plan mode (public secondary + community):** Claude Code plan often materializes as a **markdown plan artifact** under a plans folder; permission/YOLO interaction has evolved (e.g. plan mode historically fought full-auto). Cline’s Plan mode is a **hard capability gate** (no writes), not only a prompt style.

**Adaptoid map:** Plan mode ≈ **read-only SDLC stage** + clarifying questions; Act ≈ **implementation gate with evidence**. Mission OS should keep Plan as *policy*, not only as model “thinking.”

### 2.3 Rules, AGENTS.md, Skills, Memory Bank

**Rules** ([cline-rules](https://docs.cline.bot/customization/cline-rules)):

| Type | Location |
|------|----------|
| Cline Rules | `.clinerules/` (workspace) |
| Cursor / Windsurf | `.cursorrules`, `.windsurfrules` (auto-detected) |
| **AGENTS.md** | `AGENTS.md`, `~/.agents/AGENTS.md` ([agents.md](https://agents.md/) standard) |
| Global Cline | OS-specific `Documents/Cline/Rules` (macOS/Linux docs; also `~/.cline/rules` in config tree) |

- Workspace rules override global on conflict.
- **Conditional rules** via YAML frontmatter `paths:` globs — only inject when context files match (open tabs, edited files, mentioned paths). **Fail-open** on bad YAML (rule still activates).
- Toggle per-rule on/off without deleting.
- `/newrule` slash command.

**Skills** ([skills](https://docs.cline.bot/customization/skills)):

- Progressive loading: metadata always (~100 tokens) → full `SKILL.md` on trigger → bundled docs/scripts on demand.
- Trigger: model `use_skill` match on description, or slash command (`/aws-deploy`).
- Layout: `.cline/skills/`, also `.clinerules/skills/`, `.claude/skills/`; global `~/.cline/skills/`.
- Unlike rules (always-on), skills **don’t burn context until needed**.

**Memory Bank** ([memory-bank](https://docs.cline.bot/best-practices/memory-bank)):

- Methodology (not proprietary binary memory): `memory-bank/` markdown hierarchy:

  | File | Role |
  |------|------|
  | `projectbrief.md` | Goals / scope |
  | `productContext.md` | Why / UX |
  | `activeContext.md` | Current focus (hottest) |
  | `systemPatterns.md` | Architecture |
  | `techContext.md` | Stack |
  | `progress.md` | Status / known issues |

- Driven by rules instructions: “I must read ALL memory bank files at start of EVERY task.”
- Commands: initialize / update memory bank; “follow your custom instructions.”
- Explicitly **cross-tool portable** — works with any agent that reads docs.

**Adaptoid map:** Memory Bank ≈ structured disk memory / HANDOFF + PROJECT-INTENT patterns; conditional rules ≈ path-scoped pack instructions; skills ≈ progressive AgentSkills.

### 2.4 MCP, tools, approval, YOLO

**MCP** ([mcp-overview](https://docs.cline.bot/mcp/mcp-overview)):

- Config: CLI `~/.cline/mcp.json`; IDE settings JSON / Remote Servers UI.
- Transports: **STDIO** local; remote **streamable HTTP** (recommended) or legacy SSE.
- Per-server `autoApprove: []` tool list; enable/disable without delete.
- `cline mcp` wizard; enterprise MCP allowlists.

**Built-in tools (product claims):** read/write/search, bash (long-running watch), browser, ask_question, MCP tools alongside builtins; lint/compiler feedback loop; Jupyter cell awareness.

**Auto Approve / YOLO** ([auto-approve](https://docs.cline.bot/features/auto-approve)):

| Ladder | Behavior |
|--------|----------|
| Per-category toggles | Read project / read all; edit project / edit all; safe cmds / all cmds; browser; MCP |
| Safe vs requires_approval commands | Model-flagged `requires_approval` (not a fixed allowlist — soft) |
| **YOLO** | Auto-approve *everything* including Plan→Act transitions |

Default recommendation in docs: auto-read only; use **Checkpoints** if enabling edits.

### 2.5 Checkpoints (shadow git) vs user git

([checkpoints](https://docs.cline.bot/core-workflows/checkpoints)):

- After each tool use, snapshot to a **shadow Git repository** — **user `.git` history stays clean**.
- Includes untracked files.
- Restore options: Files only | Task only | Files & Task.
- Enables practical auto-approve: move fast, roll back.
- Cost: large repos may slow / bloat — toggle off.

**Kanban git:** parallel agents get **isolated worktrees**; review diffs; Commit / Open PR; trash cleans worktrees.

**Contrast Aider:** Aider *is* your commit history. Cline *preserves* your commit history while offering discrete restore points.

### 2.6 Multi-agent, schedule, headless

- **Agent Teams:** coordinator breaks work; specialists with own tools/context; CLI `--team-name`.
- **Subagents:** parallel research without filling main context.
- **Schedule:** cron via CLI (`cline schedule create ...`).
- **Headless:** pipe `git diff` into review; `--json` for automation; GitHub Actions samples (issue RCA, PR review).

### 2.7 Config tree (sampled)

Docs describe `~/.cline/` holding global rules, hooks, skills, agents, plugins, mcp, data/sessions, locks for hub. Workspace: `.clinerules/`, `.cline/`, `.clineignore`.

---

## 3. Aider — harness shape

### 3.1 What it is

- Terminal AI pair programmer: edits **local source files** in a **git repo**, multi-file, multi-language.
- Model-agnostic BYOK (Claude, GPT, DeepSeek, Gemini, Ollama, OpenAI-compatible, …).
- Scale signals (marketing homepage, soft): high star count, millions of installs, large weekly token volume, “singularity” % of aider written by aider — treat as community maturity, not proof.
- Product philosophy: **pair with human**; bite-sized steps; human selects files; git for safety.

### 3.2 Chat modes (Plan/Act analogue)

([modes](https://aider.chat/docs/usage/modes.html)):

| Mode | Behavior |
|------|----------|
| **code** (default) | Make file edits |
| **ask** | Discuss only — **no edits** |
| **architect** | Main model proposes plan; **editor model** emits edit format (two LLM calls) |
| **help** | Docs about aider itself |

- Sticky: `/chat-mode <mode>` or launch `--architect` / `--chat-mode`.
- One-shot: `/ask`, `/code`, `/architect` on a single message.
- **Elite workflow:** bounce ask ↔ code; when plan is agreed, terse “go ahead” in code mode.
- Architect/editor: pairs strong reasoners (historically o1-class) with edit-capable models; can use same model twice for two-pass quality.
- Edit formats: diff / whole / editor-diff / editor-whole / etc. (model-dependent; elite detail of Aider).

**Vs Cline Plan/Act:** same *think then do* discipline; Aider’s ask is **soft** (user-enforced via mode); Cline’s Plan is **hard tool deny**. Architect ≈ Cline dual-model Plan/Act + structured edit emission.

### 3.3 Repo map (elite context engineering)

([repomap](https://aider.chat/docs/repomap.html)):

- Concise map of **whole git repo**: important classes/functions, signatures, key definition lines.
- Graph ranking on file dependency graph → **most relevant** symbols under `--map-tokens` budget (default ~1k, expands when chat empty).
- LLM uses map to (a) answer from signatures alone, (b) request the right files into chat.
- Human tips: **don’t dump entire repo into chat** — add files that need edits; map covers the rest.

**Adaptoid map:** host-side context engineering; portable concept is “ranked structural index + token budget,” not Aider’s tree-sitter graph specifically.

### 3.4 Git as transaction log (elite)

([git](https://aider.chat/docs/git.html)):

| Behavior | Detail |
|----------|--------|
| Auto-commit | Each AI edit set → descriptive commit |
| Dirty files | Pre-commit existing human edits first (separate AI vs human) |
| Commit messages | Weak model summarizes diffs; **Conventional Commits** default; `--commit-prompt` |
| Attribution | “(aider)” on author/committer; optional Co-authored-by / message prefixes |
| Commands | `/undo`, `/diff`, `/commit`, `/git` |
| Escape hatches | `--no-auto-commits`, `--no-dirty-commits`, `--no-git` |
| Hooks | Default **skips** pre-commit (`--no-verify`); `--git-commit-verify` to run hooks |

**Elite portable idea:** AI changes must be **atomically reversible** with **clear authorship**. Adaptoid “evidence or it didn’t happen” aligns more with *verified outcomes* than auto-commit spam — but undoability is non-negotiable.

### 3.5 Conventions / AGENTS.md

([conventions](https://aider.chat/docs/usage/conventions.html)):

- Put guidelines in markdown (commonly `CONVENTIONS.md`).
- Load **read-only**: `/read CONVENTIONS.md` or `aider --read ...` or `.aider.conf.yml`:

```yaml
read: CONVENTIONS.md
# or
read: [CONVENTIONS.md, AGENTS.md]
```

- Community: [Aider-AI/conventions](https://github.com/Aider-AI/conventions); GitHub issue #4363 suggests documenting **AGENTS.md** as the standard name for cross-tool rules.
- Prior Adaptoid wave note: configure `read: AGENTS.md` in `.aider.conf.yml`.

**Not** the same as Cline’s always-injected multi-source rules panel — Aider relies on user/conf to keep conventions in context (and prompt cache when possible).

### 3.6 Lint, test, watch, voice

- Auto lint/test after edits; `/test` shares failures back into chat.
- **Watch mode:** AI comments in editor files → aider applies; strips AI comments after.
- Images/URLs in chat; voice-to-code; browser UI mode.
- Tips: bite-sized steps; `/clear` when stuck; switch models; pair with human for next step.

### 3.7 MCP / multi-agent / orchestration

- **Core Aider is not a full MCP host** as of primary docs scraped 2026-07-18 (no MCP chapter parallel to Cline).
- Ecosystem: open issues requesting MCP; community CLI bridges; forks/products (e.g. AiderDesk) add agent mode + MCP; reverse pattern: wrap Aider *as* MCP server for other hosts.
- Multi-agent teams / schedules / messaging: **out of Aider’s center of gravity**.

---

## 4. Head-to-head: harness patterns

| Pattern | Cline | Aider | Claude Code (public) | Portable elite rule |
|---------|-------|-------|----------------------|---------------------|
| **Plan before write** | Hard Plan mode | `/ask` then `/code` | Plan mode + plan file | Separate *strategy session* from *mutation session* |
| **Dual models** | Plan model ≠ Act model | Architect + editor | Model + optional subagents | Route reasoning cost vs edit cost |
| **Rules injection** | Multi-format + conditional | Read-only conventions file | CLAUDE.md + skills | Prefer **AGENTS.md** as shared; host skins optional |
| **Skills progressive** | SKILL.md + use_skill | Weak / ad-hoc | Skills ecosystem | Metadata always; body on demand |
| **Tool approval** | Per category + YOLO | Human watches terminal; no MCP ladder | Configurable autonomy | Ladder + blast-radius classes |
| **Undo** | Shadow checkpoints | Git commit + `/undo` | User git + product undo surfaces | Always have restore cheaper than re-prompt |
| **Repo context** | Agent tools + search + rules | **Repo map** + selected files | Agent search + CLAUDE.md | Structural index + deliberate file selection |
| **Multi-agent** | Teams, subagents, Kanban worktrees | Single chat loop | Subagents / teams | Isolate FS (worktrees) when parallel |
| **Persistence** | Hub sessions + Memory Bank files | Chat + git history + conventions | Sessions + CLAUDE.md / memory features | Disk memory > chat alone |
| **MCP** | Native | Ecosystem / missing native | Native | Policy allowlist + autoApprove empty by default |
| **CI/headless** | Strong CLI JSON | Scriptable CLI messages | Strong | Same mission rules in CI as interactive |
| **Openness** | OSS harness + paid model paths | OSS | Closed product, open SDK | Adaptoid stays model/host-agnostic |

---

## 5. Elite portable concepts (steal list)

### From Cline

1. **Hard Plan/Act capability split** — plan cannot mutate; not just a system prompt vibe.
2. **Deep-planning command** for multi-session / multi-file work with explicit affected-file inventory.
3. **Shadow checkpoints** orthogonal to user git — experiment without polluting history.
4. **Conditional rules (path globs)** — inject only relevant policy; fail-open vs silent drop (know the tradeoff).
5. **Progressive skills** (AgentSkills-shaped SKILL.md) vs always-on rules.
6. **Approval ladder** ending in YOLO with explicit danger copy — enterprise can disable YOLO.
7. **Hub-spoke session survival** — daemon ownership of long jobs; multi-client attach.
8. **Kanban + worktrees** — parallel agents without shared dirty tree collisions.
9. **Memory Bank as portable markdown memory** — methodology that outlives any host.
10. **AGENTS.md first-class** alongside proprietary `.clinerules`.
11. **MCP autoApprove default empty** — trust on install is a security story.
12. **Headless JSON + GH Actions samples** — same agent in CI.

### From Aider

1. **Git as AI transaction log** — every edit reversible; dirty human work separated.
2. **Conventional commit messages from weak model** — cheap summarizer, not hero model.
3. **Repo map under token budget** — graph-ranked structural context.
4. **Human file selection discipline** — don’t flood context; map fills the rest.
5. **Ask→code bounce with terse “go ahead”** — plan agreement before edits.
6. **Architect/editor dual-pass** — reasoner ≠ editor; two-request quality.
7. **Edit-format specialization** — model-specific patch languages (diff-fenced etc.).
8. **Conventions as read-only always-context** — simple AGENTS.md / CONVENTIONS.md.
9. **Lint/test feedback loop** after each edit set.
10. **Attribution of AI commits** — `(aider)` / Co-authored-by for audit trails.
11. **Bite-sized SDLC steps** as product culture (tips), not optional soft skill.
12. **Watch-mode AI comments** — editor-native task handoff without leaving IDE.

### Shared / ecosystem

- **Model-agnostic host** wins long-term over single-provider lock-in for Adaptoid’s “weapon swap.”
- **Evidence > chat** — commits, checkpoints, memory-bank files, plans written to markdown.
- **Cross-host AGENTS.md** is the emerging cold-start contract (Adaptoid already uses this).

---

## 6. Adaptoid implications (non-doctrine; wave partial)

| Decision | Guidance |
|----------|----------|
| **Kit maintenance host** | Any of Claude Code / Cline / Aider / Grok Build / Codex — Adaptoid supplies mission rules, not a fourth CLI |
| **AGENTS.md** | Keep as **portable cold-start**; allow host skins (`.clinerules`, `CLAUDE.md`) as generated projections if needed |
| **Plan gate** | Encode as SDLC stage: explore/read → plan artifact → human or auto gate → act with evidence |
| **Git policy** | Prefer **user-owned history** + optional AI attribution; Aider auto-commit is great for pair sessions, noisy for multi-agent product; Cline shadow checkpoints map better to “experiment freely” |
| **MCP** | Host implements; Adaptoid policy (`policies/default.yaml`) gates blast radius — do not auto-approve by default |
| **Memory** | Memory Bank shape complements HANDOFF replace-state; don’t duplicate both as append-only logs |
| **Parallel agents** | Prefer worktree isolation (Kanban/Claude patterns) over shared dirty tree |
| **Do not** | Rebuild hub-spoke, Kanban, or Aider edit-format engine inside Core |

---

## 7. Incomplete next probes (not done this partial)

1. Clone `cline/cline` — measure tool list, permission model in code, evals/ harness.
2. Run Plan→Act on a real multi-file task; capture checkpoint storage size.
3. Confirm Aider LICENSE + whether any 2026 release added native MCP (re-open issues #2525, #4506).
4. Side-by-side Claude Code plan-mode permissions vs Cline Plan hard gate (same repo, same task).
5. Kanban worktree lifecycle vs Adaptoid multi-agent corner audit.
6. Cline enterprise YOLO/MCP allowlist vs Adaptoid FM-20.
7. Aider repomap quality on monorepo vs Cline tool search (latency/token).
8. Register durable source IDs in `docs/research/era-ocean/sources/INDEX.md` for this wave’s primary URLs (if wave runner requires).

---

## 8. Sources

### Cline (primary)

| ID (local) | Source |
|------------|--------|
| C-GH | https://github.com/cline/cline — README: Plan/Act, rules/skills, MCP, teams, schedule, connectors, headless, Apache-2.0, product matrix |
| C-SITE | https://cline.bot |
| C-DOCS | https://docs.cline.bot — overview, llms.txt index |
| C-PLAN | https://docs.cline.bot/core-workflows/plan-and-act |
| C-RULES | https://docs.cline.bot/customization/cline-rules — AGENTS.md, conditional paths |
| C-SKILL | https://docs.cline.bot/customization/skills |
| C-MCP | https://docs.cline.bot/mcp/mcp-overview |
| C-CKPT | https://docs.cline.bot/core-workflows/checkpoints |
| C-AUTO | https://docs.cline.bot/features/auto-approve |
| C-HUB | https://docs.cline.bot/sdk/architecture/hub-spoke |
| C-MEM | https://docs.cline.bot/best-practices/memory-bank |
| C-CLI | https://docs.cline.bot/usage/cli-overview |
| C-KAN | https://docs.cline.bot/usage/kanban · https://github.com/cline/kanban |
| C-TOOLS | https://docs.cline.bot/tools-reference/all-cline-tools |

### Aider (primary)

| ID (local) | Source |
|------------|--------|
| A-SITE | https://aider.chat/ |
| A-DOCS | https://aider.chat/docs/ |
| A-MODE | https://aider.chat/docs/usage/modes.html — code/ask/architect |
| A-CONV | https://aider.chat/docs/usage/conventions.html |
| A-GIT | https://aider.chat/docs/git.html |
| A-MAP | https://aider.chat/docs/repomap.html |
| A-TIPS | https://aider.chat/docs/usage/tips.html |
| A-CONF | https://aider.chat/docs/config/aider_conf.html |
| A-GH | https://github.com/Aider-AI/aider |
| A-AGENTS-ISSUE | https://github.com/Aider-AI/aider/issues/4363 — recommend AGENTS.md |
| A-MCP-ISSUE | https://github.com/Aider-AI/aider/issues/2525 · #4506 — MCP requests |

### Claude Code / comparison (context only)

| ID (local) | Source |
|------------|--------|
| CC-DOCS | https://code.claude.com/docs/en/overview |
| CC-PLAN-SEC | https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/ — plan markdown + YOLO interplay |
| VS-MORPH | https://www.morphllm.com/comparisons/cline-vs-claude-code — secondary table (Plan/Act, approval) |
| VS-CODEPICK | https://codepick.dev/en/compare/claude-code-vs-cline/ — secondary |

### Internal prior wave

| ID | Source |
|----|--------|
| W1-HOSTS | `docs/research/era-ocean/waves/wave-20260718-w1-hosts-models-standards.md` §§1.6–1.7 Cline/Aider |
| S-047..051 | `docs/research/era-ocean/sources/INDEX.md` — earlier Cline/Aider source rows |
| ELITE | `docs/research/era-ocean/elite/ELITE-10-PERCENT.md` — host list includes Cline/Aider |

---

## 9. Status stamp

**Partial D complete as research scrape + synthesis.**  
**Not** product doctrine. **Not** ship-check evidence. **Not** a substitute for local install verification.

**Next consumer:** wave merger / elite extraction / HOST-CAPABILITIES updates — only after dual-sourcing any claim that becomes kit policy.
