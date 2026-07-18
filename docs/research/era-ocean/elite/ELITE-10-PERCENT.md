# Elite 10% concepts (DRAFT — living)

> **Honesty:** This is **not** the full agentic world. It is a working distillation of  
> “concepts the top ~10% of practitioners use that drive ~100% of their leverage.”  
> Coverage of the ocean: **≪ 1%**. Every wave can rewrite this file.  
> Last synthesis: **2026-07-18** Wave-1 + **W2 Cherny/long-run harness**. Still ≪1%.

## The stack the elite actually climb

```
Software 1.0  code you write
Software 2.0  weights you train
Software 3.0  context + tools + loops you program   ← Karpathy
        │
        ▼
Prompt engineering     (baseline)
Context engineering    (right information in window)
Harness engineering    (environment one agent runs in)
Loop engineering       (system that prompts agents on a timer / goal)
Factory / mission OS   (gates, evidence, multi-host, ship)  ← Adaptoid target
```

---

## Concept dictionary (elite language)

| Term | Definition (working) | Why it matters |
|---|---|---|
| **Harness** | Scaffold around a model: tools, memory, rules, permissions, lifecycle, subagents | Model is commodity; harness = reliability |
| **Loop** | Recurring plan→act→verify→state-write; system prompts agents, not human every turn | Boris Cherny / Steinberger / Osmani 2026 |
| **LLM-as-OS** | Model as kernel; tools = syscalls; files = FS; context = RAM | Karpathy metaphor for product shape |
| **Software 3.0** | Program via context window, tools, examples, memory | Unit of work = macro actions |
| **Agentic engineering** | Professional discipline: specs, review, evals, security, taste while agents code | Raises ceiling; vibe coding raises floor |
| **Verifiability** | What has automatic success signal trains and ships fastest | Coding wins because tests/run/diff |
| **Jagged intelligence** | Spikes on trained+verifiable domains; fails oddly elsewhere | Don’t assume smooth IQ |
| **Maker ≠ checker** | Separate writer from verifier (second agent/model grades done) | `/goal` pattern; no self-grading |
| **Disk memory** | HANDOFF / progress / AGENTS on disk; model forgets between sessions | Long-running agents require FS state |
| **Fewer tools** | Vercel: remove ~80% tools → higher success, fewer tokens | Tool bloat = decision tax |
| **Worktrees** | Parallel isolation for multi-agent | FM-13 at filesystem level |
| **Skills** | Portable SKILL.md procedures (agentskills.io) | Progressive disclosure vs mega-prompt |
| **Soft vs hard** | Rules text vs hooks/sandbox/validators | Soft alone = theater |
| **Comprehension debt** | Code ships faster than human understanding | Engineer must stay in loop |
| **Intent debt** | Cold session fills holes with confident guesses | Skills + INTENT lock close holes |

---

## The five loop primitives (Osmani / host convergence)

| Primitive | Job | Host examples | Adaptoid today |
|---|---|---|---|
| **Automations** | Heartbeat: discover/triage on schedule | Codex Automations, Claude `/loop` cron | Partial (conductor; not scheduled) |
| **Worktrees** | Parallel without collision | Claude/Codex/Grok | Documented; not auto-created |
| **Skills** | Codify project knowledge | agentskills both sides | **Emitted** `.agents/skills` (v5.3) |
| **Connectors** | Real tools (MCP) | MCP everywhere | OAP allowlist; keep sparse |
| **Sub-agents** | Ideate vs verify | Claude/Codex subagents | Playbook: sparse use |
| **State** | What’s done/next | HANDOFF, progress files, Linear | **HANDOFF rewrite** core law |

---

## Karpathy (Sequoia Ascent 2026) — elite takeaways

1. **Dec 2025 agentic inflection** — macro actions trusted more; profession → orchestrator  
2. **Software 3.0** — context is the program  
3. **Some apps should disappear** into direct model transforms (MenuGen lesson)  
4. **Automate what you can verify** — tests, diffs, evals = rails  
5. **Vibe coding vs agentic engineering** — floor vs ceiling  
6. **Agent-native infrastructure** — CLIs, MCP, schemas, headless, audit  
7. **You can outsource thinking, not understanding**  

Primary: https://karpathy.bearblog.dev/sequoia-ascent-2026/

---

## Loop engineering (Cherny / Osmani / Steinberger)

- Job of elite engineer: **write loops**, not one-shot prompts  
- Loop without **verifier** = high-confidence bug machine  
- **Token costs** explode unattended — budget is part of loop design  
- Same five primitives now ship **inside** Claude Code and Codex — stop arguing tool tribe, design portable loops  

Primary: https://addyosmani.com/blog/loop-engineering/

---

## Harness moat (industry consensus 2026)

- Multi-day coherence > single-shot SWE-bench  
- Initializer agents + progress files (e.g. progress.txt + git) bridge sessions  
- Manus rewrote harness 5×; LangChain re-architected research agents 4× — **iteration on harness is the work**  
- Meta-harness research: agents optimizing harness via filesystem experience  

---

## Vercel lesson

**Fewer tools, better agent.** Removing ~80% tools → 100% success vs 80%, 37% fewer tokens.  
→ Adaptoid default: **smallest MCP stack**, CLI over tool zoo.

Primary: https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools

---

## Odysseus / community “self OS” (note carefully)

- **Odysseus** (public discourse 2026): self-hosted AI workspace (often linked to PewDiePie / local-first) — agents, memory, MCP, skills; OpenCode roots mentioned on HN.  
- Treat as **local agent OS / workspace** pattern, not yet a coding-harness gold standard.  
- Related: OpenClaw, Hermes-class names appear in social — verify before adopting brand claims.  
- Elite signal: **local-first + skills + memory + MCP**, not celebrity product.

---

## What elite refuse

| Hype | Why refuse |
|---|---|
| Framework-as-OS (CrewAI default) | Hosts already own the agent loop |
| Infinite multi-agent crews greenfield | Token tax + coordination theater |
| Self-grading “done” | False status FM-09 |
| Fat always-on system prompts | Context rot; skills win |
| Marketplace free-install MCP | Supply chain / FM-20 |
| Claiming ocean mapped | Infinite surface; models move |

---

## Adaptoid delta (from this draft only — NOT done)

| Elite concept | In Adaptoid now? | Next (research → product later) |
|---|---|---|
| Disk state / HANDOFF | Yes | Keep sacred |
| Verify-before-done | Yes (law + skill) | Harder SDLC acceptances |
| Skills portable | Yes v5.3 emit | Expand pack carefully |
| Worktrees | Documented | Conductor flag |
| Maker ≠ checker | Partial (playbook) | Explicit verify subagent skill |
| Automations / `/goal` | Weak | Protocol for host `/goal` + scheduled wake |
| Fewer tools | SELECTION smallest | Engine enforce MCP max N |
| Software 3.0 copy-paste install | Lite paste | Keep Lite as Software 3.0 program |
| Loop engineering as product OS | SHIP-SYSTEM stages | Name “loop” in SHIP; automation heartbeat |
| Comprehension debt | Not explicit | Playbook warning row |
| Agent-native surfaces | Host emit | GEMINI.md etc. demand-gated |

---

## Categories still almost untouched (ocean)

Models (DeepSeek, Kimi training agent patterns) · full official doc diffs weekly · enterprise multi-agent · security papers · every YC W26 agent startup · non-English communities · hardware/local inference harnesses · eval science · legal/compliance agent loops · robotics/embodied · …

## Wave-1 additions (2026-07-18 parallel scrapers)

### From harness/loop research
- **Outer loop vs inner loop** (Ronacher *Coming Loop*): outer keeps work alive after model would stop  
- **Ralph loop**: often fresh context + disk state + mechanical done  
- **Factory model** (Osmani): build the system that builds software; verification bottleneck  
- **Failure → harness ratchet**: every bug becomes AGENTS.md / hook / test  

### From community pulse
- Early stopping = harness bug; re-inject TODOs  
- Long AGENTS.md walls (~80–150 lines) silently ignored — **thin always-on**  
- Auto-generated AGENTS often **hurts** (must be human-curated)  
- Stronger models + incomplete context can **increase** cost (hunt/retry)  
- YC signal: coding-agent sessions as hiring/product input  

### From hosts/standards
- Hosts converge: plan · act · hooks · skills · subagents · headless · MCP  
- MCP **2026 RC**: stateless core, extensions — track breaking changes  
- Antigravity / host brand churn — never hardcode unstable host IDs  
- Claude Agent SDK / OpenAI Agents SDK = productizable same loops  

### From stack/tools/eval
- Encode **capability shapes** not vendor brands (edge vs VM long-loop)  
- Postgres-first memory; vector optional  
- OTEL-shaped observability default  
- Public bench % ≠ product definition of done — **golden tasks** win  
- MCP deny-by-default (aligns FM-20)  

### Named community harnesses to watch (not adopt wholesale)
Claude Code · Codex · OpenCode · Cursor · Cline · Aider · Agentsmith · Citadel · OpenRig · mini-SWE-agent · Odysseus (local workspace) · OpenClaw · Ash (agent=folder) · open-agent-sdk forks  

## Wave-2 additions (2026-07-18 daily loop) — Cherny + long-running harness

### Initializer / coding dual-session harness (Anthropic Eng primary)
| Artifact | Role |
|---|---|
| `init.sh` | How to run + smoke |
| `claude-progress.txt` (or HANDOFF) | Shift handoff text |
| `feature_list.json` + `passes` | Only flip after E2E; do not delete tests |
| `git` commits | Clean mergeable state between sessions |

**Boot ritual every session:** pwd → progress → features → git log → smoke as user → one feature only.

**Named failure modes (add to elite FM language):**
- **One-shot mid-context death**
- **Early victory** (declares done after partial progress)
- **Agentic laziness** (stops multi-part early)
- **Self-preferential bias** (self-grades own work)
- **Goal drift** (after compaction)

### Dynamic workflows (Claude Code Jun 2026)
Host can **write a custom harness per task**. Patterns: fan-out, **adversarial verification**, tournament, loop-until-done, **quarantine** (untrusted readers ≠ privileged actors). Pair **`/loop` + `/goal` + budgets + worktrees**.

### Goals (Codex official)
**Goal = completion contract** (what true, how checked, constraints) — not unbounded autonomy. Automations = scheduled heartbeat.

### Org ladder (Cherny discourse)
0 Gated → 1 Assisted → 2 Parallel (~10) → 3 Supervised autonomy (~100) → 4 AI-native (agents spawn agents).  
**Each step needs new guardrails** (verify, review, permissions, worktrees, cost). Measure **eng-hours saved**, not tokens.

### Harness decay thesis
Some claim product harness shrinks toward ~100 LOC as models improve. **Elite for Adaptoid: WATCH — do not delete mission gates** while intelligence remains jagged.

### Adaptoid delta update (research only)
| Concept | Status |
|---|---|
| Progress + clean commits between sessions | Aligns HANDOFF/git — keep |
| Feature JSON `passes` after E2E | **Watch** for multi-day Core templates |
| Session smoke before BUILD | **Adopt candidate** for playbook |
| Dynamic host workflows | **Watch** (host-native) |
| Harness disappearance | **Refuse** as product strategy |
| Goals language | **Adopt** as acceptance-contract synonym |

---

## Wave-3 additions (2026-07-18 · 20m multi-agent · 6 subagents)

### Species split (don’t confuse products)
- **Channel daemon** (OpenClaw) · **Workspace cockpit** (Odysseus) · **Repo coding harness** (OpenCode / Claude Code)  
- Adaptoid orchestrates mission; does not reimplement all three UIs.

### Client-owned tool loops (DeepSeek / Kimi)
- Re-inject `reasoning_content` on tool turns or multi-step breaks  
- **Dynamic tool loading** (Kimi K3): search tools → inject schemas mid-loop = progressive tool disclosure  
- Route heavy model for main / flash for subagents  

### Framework / runtime / harness layers
- LangGraph = runtime · DeepAgents = harness batteries · Agent SDKs = host loop as library  
- Adaptoid stays **mission OS** above; steal disk memory, maker≠checker, hard hooks  

### Loop + Goal (official Claude / Codex)
- **Goal** = measurable end + how checked + constraints (completion contract)  
- **Loop** = time-cadence proactive work  
- Migrations: rulebook → mechanical queue on disk → adversarial review → smoke  

### Community / evals / security
- Discover → Isolate (worktree) → Verify (external) → Persist → Schedule  
- Leaderboards ≠ ship DoD; steal end-state pytest methodology only  
- MCP quarantine: no token passthrough, deny-by-default, schema pin  

### Continuous process
- Research loop now **every 20 minutes** with **≥5 live subagents**  
- Coverage still ≪1%; improve every fire  

---

## Wave-4 additions (2026-07-18 · 20m · 6 subagents)

### YC market (what founders fund)
Substrate & teleop · Company Brain/skills · plan gates · fleet isolation · agent observability · prod-fix · MCP-first + agent security · proof under vibe code.  
→ Mission OS stays the wedge; not “another chat agent.”

### OpenClaw security imports
- Pairing = **admission**; capability approval separate  
- sessionKey ≠ auth  
- Skills/plugins = TCB; install-as-privilege  
- Sandbox-off default is **anti-pattern** for Adaptoid  
- External-content quarantine (PI chains)

### Standards delta
- AGENTS.md AAIF plain MD, nested nearest-wins, thin  
- Skills progressive disclosure + validate  
- **MCP 2026-07-28 RC:** stateless core, biggest break since launch — dual-stack readiness

### Hosts: Cline / Aider / Grok / Antigravity
- Plan/Act hard gate (Cline)  
- Repo map + lint-test loop + dirty git hygiene (Aider)  
- Grok: worktrees + ACP + Claude-compat skills  
- Antigravity: plugin monorepo unit; host emit **watch**

### Community delta
- Delete-tests-to-green  
- verified=1 binary gate desire  
- Orphan swarm if parent dies without killing children  
- Outer deterministic harness naming war (loop/flow/exoskeleton)

---

## Wave-5 additions (2026-07-18 · distribution economics)

### The traction law (verified against 2026 winners)
**Content ≠ traction. Install moment × existing channel × shareable proof = traction.**
- OpenClaw ~382k ⭐ (channels users already use) · Superpowers ~243k ⭐ (Claude Code plugin) · BMAD ~49k ⭐ (`npx` one-liner + retellable personas) · Spec Kit (GitHub brand + 30 integrations).  
- Aggregator lists (~141k ⭐) are indexes, not products — word count is not a moat.  
- **BMAD asymmetry lesson:** its content is heavier than Adaptoid's; its install is lighter. Fix the install, not the content.

### Distribution's security bill
ClawHub: 800+ malicious skills; OpenClaw: 9 CVEs / 4 days (one 9.9). Marketplace distribution = FM-20 at ecosystem scale. Deny-by-default survives the distro push or the push is refused.

### Eval theater now has numbers (→ FM-21)
SWE-bench V saturating at 74–78% (93.9% top claim with ~19.8% semantically wrong) · Terminal-Bench 52–58% · **real human PR acceptance 35–50%**. Benchmark-green ≠ reviewer-accepted = the "false done" thesis, industry-confirmed.

### Adaptoid delta update (research → product)
| Concept | Status |
|---|---|
| `uvx`/pip one-liner install | **Adopt** (v5.4 target) |
| Claude Code plugin + skills.sh listing | **Adopt** (v5.4 target) |
| Awesome-list presence | **Adopt** after gates honestly green |
| Public demo repo with evidence trail | **Adopt** — the proof artifact |
| BMAD-style named personas | **Watch** — retellability vs lean two-tier |
| Skills marketplace as product | **Refuse** — hot-path law + ClawHub lesson |

---

**Ocean still open. This file is a draft sponge, not a finish line.**  
**Next 20m wave:** CN harness discourse · PydanticAI · Cherny transcript · MCP RC re-verify.
