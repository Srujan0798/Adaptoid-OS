# ERA-OCEAN Partial A — YC Agent / Coding-Agent Startups (W25→S26)

**Wave:** `wave-20260718-0841-A`  
**Agent:** A (YC market / founder narrative / Demo Day themes)  
**Status:** INCOMPLETE (web + YC directory + press + RFS; **not** full directory scrape of ~700 companies; **not** Bookface/investor decks; S26 mid-batch)  
**Written:** 2026-07-18  
**Scope:** YC **W25, Spring/X25, S25, W26, Spring/P26, S26-RFS** agent & coding-agent startups — founder narratives, Demo Day themes, harness/mission-OS patterns for Adaptoid.

**Batch naming (YC calendar, 2025–26):**

| Label | Season | Agent density (reported) | Demo Day |
|-------|--------|--------------------------|----------|
| **W25** | Winter 2025 | High AI (~133/160 ML/AI); agents + agent *support* tools | ~Mar 2025 |
| **X25 / Spring 25** | First Spring batch | **~46–50%** labeled AI agents (67/144 PitchBook; CB Insights “70+ agentic”) | ~Jun 2025 |
| **S25** | Summer 2025 | Agents + infra/tools; voice + monetize AI economy | ~Sep 9–15 2025 |
| **W26** | Winter 2026 | AI-native **service** + agent **devtools** dominant; ~199 cos | Mar 24 2026 |
| **P26 / Spring 26** | Spring 2026 | Coding-agent fleets, agent security, digital twins | Jun 16 2026 |
| **S26** | Summer 2026 | **In batch now** (Demo Day **2026-09-10**); RFS is primary signal | Sep 10 2026 |

*Note:* User asked W25/W26/S25/S26. Spring (X25/P26) is included because it is the **peak agent-share** and **coding-agent fleet** signal; omitting it would falsify the arc.

---

## 0. Honesty / coverage gaps

| Gap | Why it matters |
|-----|----------------|
| No full YC directory export for all batches | Hundreds of vertical “AI agents for X” not enumerated; this is a **pattern** map + **high-signal** cos |
| S26 incomplete (pre–Demo Day as of 2026-07-18) | Company list fluid; use **RFS + Launch YC**, not final cohort claims |
| Secondary databases (Extruct, Stealth Spy, BI paywalls) | One-liners may lag rebrand; verify against ycombinator.com when shipping product claims |
| Founder narratives mostly Launch YC + press, not deep founder interviews | Voice is filtered through Demo Day storytelling |
| No private traction sheets / Bookface | ARR claims (Pocket $27M, Eloquent $500K/4wks, etc.) are **self/press-reported** |
| Spring 25 BI “10 most exciting” full list partially paywalled | Names recovered via secondary + YC pages; some BI-only blurbs thin |
| “Coding agent” vs “vertical agent” continuum | Many “agents” are workflow automation with LLM; coding-specific subset called out explicitly |
| Star/ARR/valuation numbers move weekly | Treat as order-of-magnitude |

**What is solid:** Official YC company pages + Launch posts (Browser Use, Dedalus, Airweave), TechCrunch Demo Day lists (W25, S25, P26), YC RFS Summer 2026, Extruct W26 taxonomy, PitchBook/CB Insights agent-share stats for Spring 25.

**Coverage honesty (era-ocean contract):** This is **≪1%** of the agentic-startup ocean (not even 1% of YC alone across 20 years). It is a **high-signal slice** of 2025–26 YC agent/coding-agent surface.

---

## 1. Arc in one screen (what changed batch-to-batch)

```
W25   →  "Year of agents" begins: browser control, human teleop, vibe coding as skill
X25   →  Agents as DEFAULT product form (~half the batch); context retrieval; Cursor-for-X
S25   →  Agent INFRA (MCP/deploy), production bug-fix agents, eval/debug layers
W26   →  SaaSpocalypse thesis: do the WORK (AI-native service) + agent harness stack
P26   →  Fleet management of coding agents; agent security; digital twins for agent test
S26   →  Partner RFS: Company Brain, AI OS for companies, software-for-agents, agent silicon
```

**Elite one-liner:** Models commoditized the “agent demo.” YC money piled into **substrate** (browser/terminal/MCP/hosting), **control plane** (HITL, guardrails, observability), **company memory**, and **outcome-selling** (do the job, not ship the copilot).

---

## 2. Macro Demo Day themes (cross-batch)

### 2.1 Themes that kept winning airtime

| Theme | Manifestation | Why investors care |
|-------|---------------|--------------------|
| **Agent substrate** | Browser Use, Meteor, Terminal Use, Dedalus, Kernel (browser infra) | Whoever owns the execution environment owns the agent |
| **HITL / teleoperation** | Abundant (W25) — Waymo-style remote takeover for failed agents | Autonomy is partial; **graceful human takeover** = deployable |
| **Vibe coding / AI-written codebases** | Jared Friedman: ~¼ of W25 had **~95% AI-generated** code; Nextbyte hires “vibe coders” | Hiring, eval, and review loops must change |
| **Cursor for X** | Den (knowledge), Stilta (patents), Scalar Field (trading), Embedder (firmware) | Same UX: agent **inside** the work surface, not a chat tab |
| **MCP as USB-C for tools** | Dedalus MCP gateway; Airweave MCP search; RFS “Software for Agents” | Tool surface standardizing; hosts compete on reliability |
| **Context / company brain** | Airweave; Epicenter; RFS “Company Brain” + “AI OS for companies” | Domain knowledge, not model IQ, is the automation bottleneck |
| **Do the work (AI-native service)** | Healthcare denial/appeals, insurance, legal, CPG back-office (esp. W26) | Services TAM ≫ SaaS TAM (Gustaf Alströmer RFS) |
| **Agent reliability stack** | Fulcrum, ZeroEval, Sentrial, ashr, Canary, Salus, Silmaril | Shipping agents without eval/obs = liability |
| **Coding agent fleets** | Superset (100+ CLI agents), Omnara (command center), Keystone/Sazabi (prod fix) | Multi-agent is default; need **workspaces + isolation + review** |
| **Agent economy rails** | Maven/Sponge/Orthogonal (payments); Sitefire (market *to* agents); Autumn (Stripe for AI pricing) | Agents as buyers/users need identity, money, discovery |
| **Security for agents** | Silmaril (prompt injection immunity), Antigen (offensive), Salus (guardrails) | Prompt injection = new perimeter |

### 2.2 Founder narrative patterns (language that repeats)

- **“We built the tool we wished existed”** — Dedalus (Cathy Di / Windsor Nguyen): tired of Docker/YAML spaghetti for agents → 5-line SDK + hosted MCP.
- **“How hard could X be?”** then OSS viral loop — Browser Use (Magnus Müller / Gregor Zunic): LLM↔browser interface → 25k→50k+ stars → Cloud + API after Operator launch.
- **“MCP servers alone aren’t enough”** — Airweave: need **semantic search over workspace apps**, not just tool calls.
- **Waymo metaphor for agents** — Abundant: remote human takeover when the agent is stuck.
- **Staff engineer agents** — Keystone / Sazabi / Sonarly: find bugs in **production**, propose fixes, reduce breakages.
- **Solo / young technical founders** — W26: 22 solo founders (11%); AI-agent founders younger (Extruct: ~4.8y median experience); Keystone founder Pablo Hansen ~20 at Demo Day; GetASAP Asia founder started at 14.
- **Princeton / ETH / Amazon feeder** — Dedalus (Princeton CS dropouts-adjacent narratives), Browser Use (ETH Data Science), Amazon #1 feeder in W26 overall.
- **“Let us build the wings so your agents can fly 🪽”** — Dedalus brand line (substrate, not model).
- **“Make Something Agents Want”** — Aaron Epstein RFS (S26): rebuild software for agent-first interfaces (API/MCP/CLI + docs agents can consume).

---

## 3. Batch dossiers

### 3.1 W25 — Winter 2025 (~160 cos; Demo Day ~Mar 2025)

**Batch character:** AI-heavy (investor notes: ~133/160 ML/AI). TechCrunch angle: not only agents, but **tools that make other agents work**.

| Company | One-liner | Founder / narrative | Harness relevance |
|---------|-----------|---------------------|-------------------|
| **[Browser Use](https://www.ycombinator.com/companies/browser-use)** | OSS web-agent layer; LLM controls browser | Magnus Müller (ETH DS, scraping/bots), Gregor Zunic (ETH DS/Physics). Launch: OSS alt to Operator; Cloud $30/mo after Operator FOMO. Viral when Manus used it; $17M seed (Felicis et al., Mar 2025). Stars claimed 40k–50k+ in 3 months (later secondary: higher). | **Browser as tool surface**; stealth/proxy/session persistence; OSS → hosted dual path |
| **[Abundant](https://www.abundant.ai/)** | API for **agent teleoperation** | Pitch: catch agent failure → human operator takes over (Waymo teleop analog) | **HITL control plane**; mission OS needs pause/hand-off/resume |
| **Nextbyte** | Hire best **vibe coders** | Interview model tests AI-leveraged coding skill | Eval of **humans who pilot agents**, not only agents |
| **Rebolt** | Restaurant ops agents | Inventory/supplier grunt work; BK parent pricing talks (press) | Vertical agents = harness + domain SOP |
| (Batch meme) | ~25% of batch **95% AI-written** codebases | Jared Friedman (YC MP) public comment | Product SDLC must assume AI-majority code + **proof gates** |

**W25 Demo Day theme (TechCrunch):** “Enhance other companies’ AI agents” > pure “we are an agent.”

**Sources:**  
- https://techcrunch.com/2025/03/13/10-startups-to-watch-from-y-combinators-w25-demo-day/  
- https://www.ycombinator.com/companies/browser-use  
- https://techcrunch.com/2025/03/12/browser-use-one-of-the-tools-powering-manus-is-also-going-viral/  
- https://techcrunch.com/2025/03/23/browser-use-the-tool-making-it-easier-for-ai-agents-to-navigate-websites-raises-17m/  
- https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/

---

### 3.2 X25 / Spring 2025 (~144–160 cos; first Spring batch)

**Batch character:** Peak **agent-as-product** share. PitchBook: **67/144 (46%)** “AI agents.” CB Insights: **70+** agentic companies across ~18 categories. YC itself: “2025 is shaping up to be the year of AI agents.”

| Company | One-liner | Founder / narrative | Harness relevance |
|---------|-----------|---------------------|-------------------|
| **[Airweave](https://www.ycombinator.com/companies/airweave)** | OSS **context retrieval** for agents across apps | Lennert Jansen (AI research Amazon/IBM), Rauf Akdemir (data platform). Partner: Aaron Epstein. Launch: “Let Agents Search Any App”; MCP + REST; GDrive/Slack/GitHub… $6M seed (Jul 2025). | **Company/workspace memory for agents**; missing layer between MCP tool I/O and semantic recall |
| **[Den](https://getden.io)** | “Cursor for knowledge workers”; multiplayer agents | Justin Lee, Linus Talacko. Vision: “trillions of AI agents into the mainstream workforce.” Agent marketplace evolution. | Agent UX outside IDE; **shared agent workflows** |
| **[Sim Studio](https://www.simstudio.ai/)** | Visual multi-agent workflow builder | Emir Karabeg, Waleed Latif. 4k+ GH stars; waitlist hosted | Orchestration canvas; debug transparency |
| **[Vybe](https://www.vybe.build/)** | Vibe-code internal apps | Repeat YC founders Quang Hoang, Fabien Devos. “Lovable for internal tools” narrative. | Non-eng + agents + SSO/integrations |
| **Eloquent AI** | Autonomous ops for financial services | Tugce Bulut, Aldo Lipani. Press: **$500K ARR in 4 weeks**. “Doing, not just talking.” | Regulated **closed-loop agents** |
| **[Aegis](https://www.ycombinator.com/companies/aegis)** | Healthcare denial appeals agents | Krishang Todi, Aarav Bajaj, Dhanya Shah; partner Aaron Epstein | Vertical outcome agents (revenue recovery) |
| **LLM Data Company** | Agent QA / RL-eval | Khazi / Bains / Besgen; Perplexity/Rewind mentioned as users | **Eval as product** for agents |
| **Auctor** | SaaS implementation agents (SOWs, plans) | Used by SEs at AWS/SAP/ServiceNow (press) | Agents that compress **implementation** labor |
| **Scalar Field** | Agentic trading desk / terminal | Real-time alerts, backtests | Domain agent + tool loop |
| **Approval AI, Atlog, Beluga…** | BI “10 most exciting agent startups” set | Various vertical agents | Pattern: **vertical SOP + agent loop** |

**Spring 25 themes:**

1. Vertical agents in regulated industries (health, fin, legal)  
2. “Cursor for X” product pattern  
3. Context retrieval / knowledge substrate  
4. Agent **builders** (Sim Studio) + agent **evals** (LLM Data Co)

**Sources:**  
- https://pitchbook.com/news/articles/y-combinator-is-going-all-in-on-ai-agents-making-up-nearly-50-of-latest-batch  
- https://www.cbinsights.com/research/y-combinator-spring25-agentic-ai/  
- https://www.businessinsider.com/y-combinator-yc-demo-day-spring-ai-agent-startups-2025-6  
- https://www.ycombinator.com/companies/airweave  
- https://codeconductor.ai/blog/yc-spring-top-startups/  
- https://www.forbes.com/sites/dariashunina/2025/06/09/the-most-promising-startups-from-the-first-ever-yc-spring-batch/

---

### 3.3 S25 — Summer 2025 (~160–167 cos; Demo Day ~Sep 2025)

**Batch character:** Evolution from “AI-powered” to **agents + infrastructure to build agents**. TechCrunch: voice AI flurry; monetize AI economy; investor demand concentrated.

| Company | One-liner | Founder / narrative | Harness relevance |
|---------|-----------|---------------------|-------------------|
| **[Dedalus Labs](https://www.ycombinator.com/companies/dedalus-labs)** | “Vercel for AI agents” → **compute substrate**; MCP gateway + Agents SDK | Cathy Di (ex-Voyage/Salesforce), Windsor Nguyen (ex-DeepMind/Sentient). Partner: Jared Friedman. Launch: any LLM ↔ any MCP, 5 lines; hosted MCP in 3 clicks; long-running stateful agents <250ms cold narrative. Princeton CS high-standards story. | **Host layer** for long-running agents; multi-model; MCP as first-class |
| **Keystone** | AI engineer that **fixes production bugs** | Pablo Hansen (~20, AI master’s). Clients e.g. Lovable; turned down 7-figure acq (press). Later: bug triage / first-pass fix platform. | Coding agent as **ops loop**, not greenfield codegen |
| **Autumn** | Stripe for AI startups (complex usage pricing) | Used by hundreds of AI apps / ~40 YC cos (press) | Economic control plane for agent products |
| **Fulcrum** | Agent debugging & visibility | Stealth Spy early list | Observability = ship criterion |
| **TraceRoot** | Agents that test & fix apps | Stealth Spy | Auto-repair loop |
| **Meteor** | Agent-native browsers | Stealth Spy | Browser substrate contender post-Browser Use |
| **ZeroEval** | Human feedback quality scores for agents | Stealth Spy | Eval + RLHF-ish productization |
| **Kernel** | Fast browser infra for AI web agents | Hosted YC Agents Hackathon w/ Dedalus | Browser at infra scale |
| **stagewise** | Open-source agentic IDE | Extruct one-liner | Coding-agent surface |
| **Omnara** | Command center for coding agents | Extruct one-liner | Multi-agent control plane |
| **Embedder** | “Cursor for embedded” / firmware loops | DEV writeup | Hardware-in-loop agent harness |

**YC Agents Hackathon (Aug 2025, YC office):** Tracks — Tools for Agents (MCP), Developer & Code Agents. Hosts: Dedalus, Kernel. Guests: OpenAI, Anthropic, Vercel, Convex, Vapi. Signal: **MCP + code agents** as official YC culture center of gravity mid-S25.

**Sources:**  
- https://techcrunch.com/2025/09/15/the-9-most-sought-after-startups-from-yc-demo-day/  
- https://www.ycombinator.com/companies/dedalus-labs  
- https://stealthstartupspy.substack.com/p/stealth-startup-spy-270-y-combinator  
- https://luma.com/pz27h0xy (Agents Hackathon)  
- https://av.vc/blog/decoding-ycs-s25-demo-day-trends-takeaways (digital twin QA agents: Bluejay, Propolis, Janus)

---

### 3.4 W26 — Winter 2026 (~196–199 cos; Demo Day Mar 24 2026)

**Batch character:** Extruct: “something materially changed.” Dual software modes — **AI-native service (56, 28%)** vs **AI-enhanced software (45, 22%)** + **developer infrastructure (34, 17%)**. Hardware resurgence (20). Rebel Fund: **35%** of W26 score “top 20%” historically (strongest measured). AI agent founders younger (~4.8y median experience).

#### Agent infrastructure (defining sub-cluster)

| Company | Claimed role | Harness map |
|---------|--------------|-------------|
| **Terminal Use** | “Vercel for **background** agents” | Long-running terminal agents as deploy unit |
| **Salus** | Guardrails / validate agent actions | Policy gate before tool exec |
| **Tensol** | Multi-agent orchestration | Swarm control plane |
| **Glue** | Interface design canvas for agents | Agent UX / HMI |
| **Carrot Labs** | Continuous learning for agents | Online improvement loop |
| **Cascade** | Distill proprietary intelligence for safe autonomy | Safe distillation / policy |

#### Coding / dev-environment agents

| Company | Claimed role | Harness map |
|---------|--------------|-------------|
| **EmDash** | OSS **agentic development environment** | Local/OSS coding harness |
| **Syntropy** | Agentic coding for complex tasks | Long-horizon coding |
| **Fission AI (OpenSpec)** | **Plan mode** for complex features | Spec/plan gate before code (Adaptoid-adjacent) |
| **Sparkles** | Make everyone on the team an engineer | Non-eng → ship |
| **21st Labs** | AI programming tools | Tooling layer |
| **Haladir** | Formal methods in codegen RL | Correctness-aware generation |
| **Compresr** | Context compression (Claude Code integration signal) | Context budget / harness efficiency |

#### Monitoring / reliability for agents & software

| Company | Claimed role | Harness map |
|---------|--------------|-------------|
| **Sonarly** | Self-healing software | Auto-remediation |
| **Sentrial** | “Datadog for agent reliability” | Agent observability product category |
| **ashr** | Multi-modal testing for agents | Agent QA |
| **Canary** | AI QA engineer that understands codebase | Codebase-aware test agent |

#### Agent economy / vertical services (selected)

- **Maven / Sponge / Orthogonal** — payments rails for voice/API/agent economy  
- **Sitefire** — market products **to** agents (ChatGPT, OpenClaw discovery)  
- **Beacon Health, Eos AI, ClaimGlide…** — healthcare AI employees / OS  
- **Stilta** — “Cursor for patent attorneys”  
- **Hex Security** — agentic offensive security  

**W26 founder narrative (meta):** SaaSpocalypse is real → fund **deep tech + services replacement + agent harness**, not chatbot wrappers. Solo founders highest in **devtools** (22% solo rate in that category per Extruct).

**Sources:**  
- https://www.extruct.ai/research/ycw26/  
- https://jaredheyman.medium.com/on-the-freakishly-strong-yc-w26-batch-056ccb666076  
- https://www.thevccorner.com/p/yc-w26-batch-complete-company-database  
- https://www.ycombinator.com/companies (directory filters)  
- https://www.neweconomies.co/p/yc-w26-batch  

---

### 3.5 P26 / Spring 2026 (Demo Day Jun 16 2026) — coding-agent fleet era

TechCrunch VC poll standouts **directly about coding/agent harnesses:**

| Company | What VCs said | Harness relevance |
|---------|---------------|-------------------|
| **[Superset](https://superset.sh/)** | Run **100+ coding agents** simultaneously; any CLI agent (Claude/Cursor); isolated workspaces; open in VS Code/Cursor | **Fleet OS for coding agents** — isolation, scale, IDE bridge |
| **[Arga Labs](https://www.argalabs.com/)** | Instant **digital twins** of company software so agents can test before prod | Sandbox/twin = safe agent execution environment |
| **[Lightsprint](https://lightsprint.ai/)** | Non-engineers ship features; PM describes → agent builds → eng review/merge | Human roles in agent SDLC (PM generate, eng gate) |
| **[Sazabi](https://www.sazabi.com/)** | Find/fix production software problems; Slack + log analysis + one-click fix PR | Production coding agent + chat ops |
| **[Silmaril](https://www.silmaril.dev/)** | Agent security: probe prompt-injection threats; retrain firewall | Security control plane for agent surfaces |
| **[Tasklet](https://tasklet.ai/)** | Always-on task agent across Slack/Outlook/Drive APIs; writes own code | Horizontal agent OS; continuous session |

Also defense/physical (9 Mothers, etc.) — out of coding scope but shows batch multipolarity.

**Sources:**  
- https://techcrunch.com/2026/06/18/the-11-standout-startups-from-ycs-demo-day-according-to-vcs/  
- https://www.ycombinator.com/blog/2026-demo-days  

---

### 3.6 S26 — Summer 2026 (**mid-batch**; Demo Day **Sep 10 2026**)

**Status:** As of 2026-07-18, S26 is **running**; full agent roster incomplete. Primary signal = **[YC Requests for Startups — Summer 2026](https://www.ycombinator.com/rfs)** + Launch YC stream + directory drip.

#### Partner RFS items most relevant to mission OS / harness

| RFS (partner) | Thesis | Adaptoid resonance |
|---------------|--------|-------------------|
| **Company Brain** (Tom Blomfield) | Models good enough; bottleneck = **domain knowledge** scattered in heads/Slack/tickets. Need executable **skills file** of how the company works — not chat-over-docs. | `AGENTS.md` / skills / memory / policy as **company OS** |
| **The AI Operating System for Companies** (Diana Hu) | Make company **queryable** (meetings, tickets, GH, Notion) → closed loop that flags wrong work, generates **agent-executable specs**. Not another dashboard. | Mission loop + evidence + self-improving org |
| **Software for Agents** (Aaron Epstein) | Next trillion users = agents. Rebuild software for **API/MCP/CLI** + docs agents can discover/use without humans. “Make Something Agents Want.” | Host-agnostic tool interfaces; MCP-first products |
| **Inference Chips for Agent Workflows** (Diana Hu) | Agent loop ≠ single-shot inference: tool calls, branch, backtrack, long KV. GPU util 30–40% on agent workloads. Need silicon + **compiler** for agent graphs. | Long-horizon harness economics |
| **AI-Native Service Companies** (Gustaf Alströmer) | Don’t sell copilot SaaS — **sell the completed service** (insurance, accounting, compliance, healthcare admin). | Outcome metrics as acceptance tests |
| **Dynamic Software Interfaces** (Ankit Gupta) | Coding agents let users be their own FDEs; ship **primitives** users heavily modify. | User-extensible surfaces; agent-as-customizer |
| **SaaS Challengers** (Jared Friedman) | AI collapses software production cost → attack legacy SaaS (even ERP/chip design tools). | Generative rebuild of workflows |
| **AI Personalized Medicine** (Ankit Gupta) | Explicitly: use **agent harness like Claude Code** on personal health data. | Coding harness generalized to personal data missions |
| **Hardware Supply Chain** | Mentions **Hlabs (W26)**, **Prototyping.io (P26)** as early pieces. | Physical iteration loops |

**S26 Demo Day logistics:** https://www.ycombinator.com/demoday — invite-only ~1,500 investors; preview via directory + Launch YC.

**Launch YC (live stream, examples around research date):** Pluto (voice agent discovery), Whitespace (AI OS for wholesale), Scalar Field (agentic trading — may be multi-batch visibility), Conifer (local least-cost routing for tokens) — treat as **live pulse**, not complete S26 set.

---

## 4. Coding-agent cluster (cross-batch shortlist)

| Need | Example YC cos | Batch |
|------|----------------|-------|
| Browser tool | Browser Use, Meteor, Kernel | W25–S25 |
| Terminal / background agents | Terminal Use | W26 |
| Deploy / host agents | Dedalus Labs | S25 |
| Plan-before-code | Fission AI (OpenSpec) | W26 |
| Agentic IDE / OSS env | EmDash, stagewise, Embedder | S25–W26 |
| Multi-agent coding fleet | Superset, Omnara | S25–P26 |
| Production fix / on-call | Keystone, Sazabi, Sonarly, TraceRoot | S25–P26 |
| Context for agents | Airweave, Compresr | X25–W26 |
| Agent eval / debug | ZeroEval, Fulcrum, ashr, Canary, LLM Data Co | X25–W26 |
| Guardrails / security | Salus, Silmaril, Antigen | W26–P26 |
| Digital twin sandbox | Arga Labs | P26 |
| HITL takeover | Abundant | W25 |
| Non-eng ship path | Lightsprint, Vybe, Sparkles | X25–P26 |

---

## 5. Elite concepts → Adaptoid / mission-OS mapping

*Ranked for harness/evidence/multi-host compound value — not for fundraising hype.*

### E1. Substrate > model (W25→S25→W26)

Browser / terminal / MCP host / long-running compute are the scarce layers. Dedalus + Browser Use + Terminal Use are different skins of the same insight: **the agent is only as good as its durable execution environment.**

**Adopt for Adaptoid:** Treat host adapters (Claude Code, Cursor, Codex, local CLI, gateway) as first-class **substrates**, not plugins. Measure cold start, session persistence, tool reliability — not model brand.

### E2. HITL teleop is a product feature, not a failure mode (W25 Abundant)

Deployed agents need **detect stuck → human takeover → resume** with audit trail.

**Adopt:** Explicit pause / escalate / pair modes in the mission loop; never “autonomous-only” default for high blast-radius tools.

### E3. Company Brain / executable skills (S26 RFS + Airweave)

Automation dies on **tacit process knowledge**. Searchable app data (Airweave) is necessary but not sufficient; Blomfield’s RFS wants **skills files** of how refunds/incidents/pricing exceptions work.

**Adopt:** Strengthen `AGENTS.md` / skills / SOUL / TOOLS as **versioned, testable company procedures**; continuous sync from tickets/Slack is product surface, not docs theater.

### E4. Plan mode as a company (Fission OpenSpec) + SDLC gates

W26 funds “plan mode for complex features” as a **startup**. Adaptoid already treats loops as SDLC gates — market validates that **plan → verify → act** is missing in raw coding agents.

**Adopt:** Keep plan gates; make plans **agent-executable specs** (Diana Hu AI OS RFS).

### E5. Fleet isolation (Superset P26)

100+ coding agents need **isolated workspaces**, no merge conflicts, IDE visibility.

**Adopt:** Multi-agent = multi-workspace + resource quotas + review queue; never shared dirty tree by default.

### E6. Observability category: “Datadog for agents” (Sentrial et al.)

If agents are employees, they need metrics, traces, failure taxonomies, regression alerts.

**Adopt:** Every mission run emits structured evidence (already principle); productize dashboards for tool error rates, loop depth, human escalations.

### E7. Production is the arena (Keystone, Sazabi)

Greenfield codegen is saturated; money chases **prod logs → repro → fix PR**.

**Adopt:** Mission types for on-call: attach logs/Sentry, sandbox repro, patch, proof, PR — not only feature builds.

### E8. AI-native service economics (W26 + Gustaf RFS)

Sell outcomes (appeals won, claims filed, patents drafted), not seats.

**Adopt:** Acceptance criteria as **business outcomes** where possible; harness proves work done with artifacts.

### E9. Software for agents (Epstein RFS)

Rebuild interfaces as MCP/CLI/API with agent-readable docs.

**Adopt:** Expose Adaptoid itself as agent-consumable (CLI + structured status + MCP); dogfood “Make Something Agents Want.”

### E10. Vibe-coding majority codebases need stronger proof (W25 Friedman)

When 95% of code is AI-written, **evidence or it didn’t happen** becomes table stakes, not culture.

**Adopt:** Double down on ship-check / preflight / layered verification; never trust “agent said done.”

### E11. Agent security perimeter (Silmaril, Salus)

Prompt injection and tool abuse are default threats once agents read email/web.

**Adopt:** Tool allowlists, sandbox non-main, injection tests in eval suite (aligns with existing anti-hallucination + policy files).

### E12. Context compression is infrastructure (Compresr W26)

Long missions hit context walls; compression middleware becomes a startup category.

**Adopt:** Session compaction + memory hierarchy (working / episodic / company) as core harness, not optional.

---

## 6. Competitive landscape map (for positioning Adaptoid)

```
                    VERTICAL OUTCOME AGENTS
                    (Aegis, Eloquent, Beacon…)
                              ▲
                              │ sell the work
                              │
     CONTEXT / BRAIN ─────────┼───────── FLEET / IDE
     (Airweave, Company Brain)│         (Superset, EmDash, Omnara)
                              │
                    HARNESS / MISSION OS  ←── Adaptoid target
                    (plan, evidence, multi-host,
                     skills, gates, policies)
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
         BROWSER           TERMINAL         MCP HOST
         (Browser Use)     (Terminal Use)   (Dedalus)
              │               │               │
              └───────────────┴───────────────┘
                              │
                         MODEL APIs
                    (commoditized weapon)
```

**Differentiation note:** Most YC cos pick **one layer** (browser OR eval OR vertical healthcare). Adaptoid’s bet is the **portable mission rules + SDLC gates** spanning hosts — aligned with RFS “AI OS / Company Brain” more than with “another coding agent.”

---

## 7. What to watch next (S26 → F26)

1. **S26 Demo Day 2026-09-10** — count Company-Brain / AI-OS / agent-security / coding-fleet pitches.  
2. Whether **MCP gateway** consolidates (Dedalus-class) or fragments.  
3. **OpenClaw / Sitefire** style “agents as users” discovery (already in W26 marketing copy).  
4. Coding fleets (Superset) vs single-agent IDE (Cursor/Claude Code) — orchestration layer winners.  
5. Formal methods + RL codegen (Haladir) for correctness under vibe-coding flood.  
6. Partner RFS follow-through: who actually ships **executable company skills**, not RAG chat.

---

## 8. Source index (URLs)

### YC primary
- https://www.ycombinator.com/companies  
- https://www.ycombinator.com/launches  
- https://www.ycombinator.com/rfs  
- https://www.ycombinator.com/demoday  
- https://www.ycombinator.com/blog/2026-demo-days  
- https://www.ycombinator.com/companies/browser-use  
- https://www.ycombinator.com/companies/dedalus-labs  
- https://www.ycombinator.com/companies/airweave  
- https://www.ycombinator.com/companies/industry/Artificial%20Intelligence  

### Demo Day / press
- https://techcrunch.com/2025/03/13/10-startups-to-watch-from-y-combinators-w25-demo-day/  
- https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/  
- https://techcrunch.com/2025/03/12/browser-use-one-of-the-tools-powering-manus-is-also-going-viral/  
- https://techcrunch.com/2025/03/23/browser-use-the-tool-making-it-easier-for-ai-agents-to-navigate-websites-raises-17m/  
- https://techcrunch.com/2025/09/15/the-9-most-sought-after-startups-from-yc-demo-day/  
- https://techcrunch.com/2026/06/18/the-11-standout-startups-from-ycs-demo-day-according-to-vcs/  
- https://pitchbook.com/news/articles/y-combinator-is-going-all-in-on-ai-agents-making-up-nearly-50-of-latest-batch  
- https://www.cbinsights.com/research/y-combinator-spring25-agentic-ai/  
- https://www.businessinsider.com/y-combinator-yc-demo-day-spring-ai-agent-startups-2025-6  
- https://www.forbes.com/sites/dariashunina/2025/06/09/the-most-promising-startups-from-the-first-ever-yc-spring-batch/  

### Batch databases / analysis
- https://www.extruct.ai/research/ycw26/  
- https://www.extruct.ai/data-room/ycombinator-companies-w25/  
- https://www.extruct.ai/data-room/ycombinator-companies-s25/  
- https://www.extruct.ai/data-room/ycombinator-companies-x25/  
- https://www.extruct.ai/data-room/ycombinator-companies-w26/  
- https://stealthstartupspy.substack.com/p/stealth-startup-spy-270-y-combinator  
- https://jaredheyman.medium.com/on-the-freakishly-strong-yc-w26-batch-056ccb666076  
- https://www.thevccorner.com/p/yc-w26-batch-complete-company-database  
- https://www.neweconomies.co/p/yc-w26-batch  
- https://codeconductor.ai/blog/yc-spring-top-startups/  
- https://av.vc/blog/decoding-ycs-s25-demo-day-trends-takeaways  
- https://dev.to/stephenstilwell/yc-s25-coolest-software-focused-startups-developer-forward-review-54n9  

### Culture / events
- https://luma.com/pz27h0xy (YC Agents Hackathon S25)  
- https://x.com/ycombinator/status/1920147533264978173 (YC “year of AI agents”)  

---

## 9. Distill for elite/ELITE-10-PERCENT.md (candidates only — not auto-merged)

1. **Execution substrate is the product** (browser/terminal/MCP host).  
2. **HITL teleop + policy gates** as deploy requirements.  
3. **Company Brain = executable skills**, not RAG chat.  
4. **Plan mode / agent-executable specs** as funded category.  
5. **Fleet isolation** for multi-coding-agent default.  
6. **Agent observability** as Datadog-class category.  
7. **Production fix loop** > greenfield codegen.  
8. **Outcome-sold services** as AI-native business model.  
9. **Software-for-agents** (MCP/CLI-first).  
10. **Proof layers under vibe-coded majority codebases**.

---

## 10. Done criteria for *this* partial

| Criterion | Status |
|-----------|--------|
| W25 agent/coding signal | Done (Browser Use, Abundant, vibe-code meme) |
| X25/S25 agent density + infra | Done (stats + Dedalus/Airweave/Keystone…) |
| W26 harness taxonomy | Done (Extruct clusters) |
| P26 coding fleets | Done (Superset et al.) |
| S26 full company list | **Incomplete by design** (mid-batch; RFS done) |
| Every YC agent startup named | **Impossible / not attempted** (≪1%) |
| Bookface/deck verification | Not done |
| Local product trials | Not done |

**Next wave options:** (1) scrape YC directory filters for batch=Winter+Summer 2025/26 + keyword agent/coding; (2) deep-dive Dedalus + Superset + OpenSpec only; (3) post–S26 Demo Day refresh 2026-09-11.

---

*End partial wave-20260718-0841-A. Honesty: ocean ≫ wave. Incomplete ≪1% of agentic ecosystem; strong on public YC agent/coding arc 2025–mid-2026.*
