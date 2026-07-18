# Adaptoid OS Changelog

## v5.4.0 — Jul 2026 — Honest core + distribution (W5 research-driven)
- **Honesty pass (P1s closed):** conductor shell mode rejects missing/no-op acceptances (`true`/`echo`/`exit 0` = FAIL, no stub fallback); portable SHA-256 on macOS (`emit_event.sh`, `vault_mmu.sh`); stale v5.1/Pro/OS_SETUP refs killed (`.cursorrules`, `config/claude-code/CLAUDE.md`, Makefile fallback)
- **Hooks now real:** `core/hosts/pre-tool-use.sh` (FM-18 blast-radius guard: force-push main, `rm -rf /`, curl|sh) + emitted `.claude/settings.json` registering SessionStart/PreToolUse — emitted hooks previously never fired
- **FM-21 eval theater** (benchmark-green ≠ reviewer-accepted; real-PR gap 35–50% vs 74–78% bench); SHIP-SYSTEM row 23 context budget; playbook §3b spec-driven-dev interop (Spec Kit/Kiro/OpenSpec → PROJECT-INTENT is the spec)
- **60-second install:** `pyproject.toml` + `adaptoid_cli` bootstrap (`uvx --from git+… adaptoid` / `pip install`; `adaptoid home|update|conductor` passthrough); README leads with one-liner
- **Claude Code plugin:** `.claude-plugin/plugin.json` + self-marketplace; `skills/` generated from engine's ADAPTOID_SKILLS via `make plugin-skills` (single truth)
- **Ocean W5:** distribution economics wave (`era-ocean/waves/…w5-distribution-economics.md`) — traction law (install moment × channel × proof), ClawHub/CVE security bill, MCP trust stats; ELITE + MANIFEST updated
- **Launch:** `docs/launch/DISTRIBUTION.md` — gated channel checklist (PyPI → demo repo → skill directories → awesome lists → posts); "anti-false-done harness" positioning

## v5.3.0 — Jul 2026 — Era adapt (multi-agent audit + live 2026)
- **Research-driven:** AGENTS.md standard, agentskills.io, worktrees, soft vs hard enforcement, MCP sandbox reality
- Engine always **Core** (no hollow pro); version from `VERSION`; clean UTC timestamps; stack filled from archetype tables
- Emit portable skills: `.agents/skills/*` + `.claude/skills/*` (intent-lock, verify, blast-radius, handoff, worktree-parallel)
- SHIP-SYSTEM rows 19–22; HOST-CAPABILITIES host×matrix; playbook §3b mid-2026 reality
- Archetype **agent-product**; FM-19 cost runaway; FM-20 MCP/tool trust
- Host-neutral `kernel/TWO-TIER.md`; wake.sh paths for generated projects
- Cursor `.mdc` requires SHIP-SYSTEM + intent-lock + Agent mode
- Docs: `ADAPTATION.md`, Lite brand unify, FLOW honesty (kit libs not full-copied)
- Multi-agent corner audit findings in ADAPTATION leftovers

## v5.2.1 — Jul 2026 — Final product close
- FLOW/USE/PRODUCT/README/core/README/install aligned: Lite=`ADAPTOID-LITE.md`, Core=folder
- Entry docs slimmed; legacy OS_SETUP / short LITE paths are stubs or attic only
- Lite invocation + templates README no longer point at OS_SETUP as product
- AUDIT closed as final; tests require ADAPTOID-LITE + Core ship docs
- Ready to use (`make ship-check`)

## v5.2.0 — Jul 2026 — Kill OS_SETUP_v1.3 name confusion
- **Lite = only `ADAPTOID-LITE.md`** (repo root + Desktop)
- `reference/OS_SETUP_v1.3_full.md` is a **stub redirect**, not a second product
- Docs/USE say one name only

## v5.1.9 — Jul 2026 — Lite = one file ADAPTOID-LITE.md
- **THE Lite product** is repo root **`ADAPTOID-LITE.md`** (ultimate standalone, one file)
- Merged Desktop OS_SETUP v2.0 + SHIP SYSTEM + host playbook
- Synced Desktop `ADAPTOID-LITE.md` / `OS_SETUP.md` (same content)
- Docs simplified: no multi-name confusion

## v5.1.8 — Jul 2026 — Lite Ultimate standalone v3.0
- Rebuilt **Lite** single file from Desktop `OS_SETUP.md` v2.0 + SHIP SYSTEM + host playbook
- Canonical: `reference/OS_SETUP_v1.3_full.md` · alias `reference/ADAPTOID-LITE.md`
- Synced Desktop: `~/Desktop/OS_SETUP.md` + `~/Desktop/ADAPTOID-LITE.md`
- Fully standalone: multi-host, intent-lock, SDLC×toolkit, FMs §13, archetypes §14, adaptor §15

## v5.1.7 — Jul 2026 — Host operating playbook (Grok-style proceed)
- **`core/HOST-OPERATING-PLAYBOOK.md`** — extract Grok Build efficiency: intent lock A/B/C, plan→approve→implement, one outcome/turn, verify-before-done, subagent policy, AGENTS.md once, session hygiene
- Cold-start + SHIP-SYSTEM + USE magic prompt require this behavior
- Engine writes `plan/intent-lock.md`; conductor adds `00-intent-lock` stage
- Lite OS_SETUP canonical override updated

## v5.1.6 — Jul 2026 — Deep audit fixes
- **`AUDIT.md`** — competitor-style full-flow audit
- **`--sdlc` default on** (`--no-sdlc` to skip)
- Lite **canonical override** block in `OS_SETUP_v1.3_full.md` (wins over legacy mid-file)
- MANIFEST aligned (Lite file / Core folder); engine honesty on SELECTION.md
- install/00-INVOCATION → USE.md; drop tracked last_results noise

## v5.1.5 — Jul 2026 — Lite naming fixed
- **Lite** = only `reference/OS_SETUP_v1.3_full.md` (original standalone)
- **Core** = entire Adaptoid-OS folder/repo
- Removed misleading root `LITE.md` (archived)
- USE / START_HERE / README / dogfood aligned — no third “Pro product” naming confusion

## v5.1.4 — Jul 2026 — SHIP SYSTEM: SDLC × full host toolkit
- **`core/SHIP-SYSTEM.md`** — GFG 7-stage SDLC fused with Grok Build capabilities (plan mode, subagents, skills, hooks, MCP, memory, git, CI, review, sandbox, …)
- Cold-start + conductor tasks require **host tools per stage** (not optional tips)
- Engine copies SHIP-SYSTEM into every project; `--sdlc` emits 7 stage tasks

## v5.1.3 — Jul 2026 — Use path complete (Lite/Core/Pro)
- **`USE.md`** — hand brief + Lite/Core/Pro to any model; magic prompt
- **`LITE.md`** — short paste-only kit (deep Lite remains OS_SETUP full)
- **`engine --sdlc`** — auto `init-wave --sdlc` after generate
- PRODUCT planned-vs-done aligned to user promise

## v5.1.2 — Jul 2026 — Final spine cleanup
- **`FLOW.md`** — every live file on one product spine
- Orphans archived → `docs/historical/attic-v5.1.2-orphans/` (claw_bridge, skills, extra protocols/validators, unused workflows, adaptor prose)
- Live protocols = 5 (sdlc + blast-radius + verification + oap + route-sentinel)
- Dogfood fails if disconnected top-level modules return

## v5.1.1 — Jul 2026 — SDLC loop + host capabilities
- **`protocols/sdlc-loop.md`** — Agile SDLC gates (plan→maintain); anti-waste rules
- **`workflows/core/sdlc-agile.yaml`** — machine-readable stages
- **`core/HOST-CAPABILITIES.md`** — Grok Build / Claude / Cursor features mapped to harness (use host, don’t reinvent)
- **`conductor init-wave --sdlc`** — PLAN/DESIGN/BUILD/TEST/SHIP task briefs
- Engine copies SDLC docs into generated projects; cold-start + START_HERE updated

## v5.1.0 — Jul 2026 — Lean Core product
- **Archived** launch kits, research dumps, super-adaptoid theater, extra examples, multi-channel/vault stubs → `docs/historical/attic-v5.1-lean/`
- Dogfood/tests skip optional Pro protocols when archived
- Slim README + INDEX; hot path = `START_HERE` → engine → project only
- **`VERSION`**, **`PRODUCT.md`**, kit **`HANDOFF.md`**, full CI gate
- Host adapters + conductor + generated project README
- CONTRIBUTING / SECURITY / `.cursorrules` aligned to v5.1

## v5.1 — Jun 2026 — Core product finish (shippable)
Focus: **portable harness + host adapters + thin runtime + proof gates**. Finish projects, not more protocol theater.

### Added
- **`core/` package** — Core vs Pro vs Lite ladder (`README.md`, `MANIFEST.yaml`, templates, host templates).
- **`adaptor/host_emit.py`** — emit `AGENTS.md`, `CLAUDE.md`, Cursor `.mdc`, Codex/Grok cold-starts from one template.
- **Engine flags** — `--host`, `--core-only`, `--archetype`, `--tier`; copies intent schema into projects.
- **`conductor/conductor.py`** — status, wake, init-wave, check-disjoint (FM-13), dispatch (stub|shell), rewrite-handoff.
- **`benchmarks/run_bench.sh`** — engine / preflight / conductor / dogfood timing + correctness.
- **`calibration/`** — 50 harness cases (`generate_cases.py` → `cases.json`) + smoke runner.
- **`scripts/ship_check.sh`** + `make ship-check` — release gate.
- **`examples/core-finish/`** — documented dogfood path with evidence commands.
- **Tests** for host emit, conductor, calibration count.

### Changed
- Install / Makefile / 00-INVOCATION / Lite OS_SETUP / healthcheck updated for v5.1 Core hosts.
- Bootstrap wraps engine with `--host` / `--core-only` / `--brief`.
- `route_sentinel.sh` integer + DAG node parsing fixed.
- Multi-channel / enterprise stay demand-gated.

### Philosophy
Model = weapon. Host + MCP + skills = field. Adaptoid Core adapts the field so any weapon can finish the project.

## v5.0 — Jun 2026 — Public Product Layer + Super-Adaptoid Protocols
The v5.0 release transforms Adaptoid OS into a professional open-source project with a clear category claim, launch playbook, and self-monitoring protocol layer.

### Added
- **`docs/launch/` — Public Product Layer.** POSITIONING.md, GROWTH-PLAYBOOK.md, LAUNCH-CHECKLIST.md, BRAND-GUIDELINES.md, CONTENT-CALENDAR.md.
- **`protocols/super-adaptoid/` — Super-Adaptoid Protocol Layer.** README, consciousness-core, memory-identity, evolution-engine, proactive-assistant, hidden-gems, fable-5-workflows, super-prompt.
- **README v5.0 rewrite.** Professional open-source positioning, 3-layer architecture diagram, expanded comparison matrix, Super-Adaptoid section.
- **INDEX v5.0 restructure.** "Always load / Load on trigger / Reference" sections, Super-Adaptoid navigation, Fable 5 and hidden-gems quick-reference indexes.
- **Historical backups.** README.md and INDEX.md archived to `docs/historical/` before rewrite.
- **`protocols/event-sourcing.md` — event log as single source of truth.** Every state mutation is an immutable hash-chained event; HANDOFF/EXECUTION are projections. Replay, time-travel debugging, snapshots, retention. Grounded in existing `emit_event.sh`/`audit_chain.sh`/`replay_session.sh` machinery (FM-14/15/17).
- **`protocols/sandboxing.md` — isolation levels + credential proxy.** Four isolation tiers (V8 isolate → namespaces → gVisor → microVM) with selection rules, the four non-negotiable guarantees (filesystem, network deny-by-default, secrets-never-enter-sandbox, resource caps), and a hardening checklist. Incident-grounded.
- **`protocols/clarification-protocol.md` — ambiguity handling (FM-08/FM-16 upstream).** Ambiguity scoring table, 4-step protocol (deconstruct → ≤4 questions → analytical frame → confirm), 3-iteration cap, anti-patterns. Feeds typed PROJECT-INTENT.
- **`adaptor/INPUT-TAXONOMY.md` — 15 canonical input types.** Request-shape classification (PROJECT/PROBLEM/RESEARCH/…/AUDIT) orthogonal to archetypes, plus duration/complexity/risk axes and the risk×complexity verification scaling matrix with dynamic in-run scaling triggers.
- **7 Super-Adaptoid validators.** `check_consciousness`, `check_memory_identity`, `check_evolution`, `check_proactive_assistant`, `check_hidden_gems`, `check_fable5`, `check_super_prompt` — each protocol's invariants (config fields, FM coverage, catalog counts, template variables, kernel refs) are executable checks, wired into `dogfood.sh` and `tests/run_tests.sh`.
- **`reference/workflows/fable-5-index.md`.** Maps the 10 Fable 5 workflow patterns to concrete OS-Setup assets and validators, with selection heuristics keyed to the input taxonomy.
- **`examples/super-adaptoid/`.** Worked T2 example: typed intent with the full `super_adaptoid:` config block, session walkthrough, trust gate before proactive mode, falsification criteria.

### Changed
- **`validators/emit_event.sh` now hash-CHAINS events.** Each event embeds `prev_hash` (genesis = 64 zeros), making `audit_chain.sh` continuity checks real tamper evidence instead of best-effort. Verified by test.
- **`protocols/verification.md` adds gate ordering + cost cascade.** Route gate → policy gate → schema gate → state gate → cheap-model self-check → cross-check → grounding; fail-closed ternary outcomes; max_retries=3 then human escalation.
- **`adaptor/ADAPTOR_ENGINE.md` ANALYZE step** now detects input type (INPUT-TAXONOMY) and routes ambiguous briefs to the clarification protocol.
- README centered hero and badges updated to v5.0.
- Comparison matrix adds Super-Adaptoid rows: self-monitoring/consciousness, proactive assistant mode, self-improving evolution.
- Architecture section now shows Layer 1 (Kernel), Layer 2 (Public Product), Layer 3 (Super-Adaptoid).

### Philosophy
v4.0 proved the kernel: safety, typed intent, deterministic validation. v5.0 adds the public product layer and the consciousness/evolution protocols that let the harness monitor and improve itself without hype.

## v4.0 — Jun 2026 — Safety Core + Typed Intent + Philosophy
Merged the Adaptoid safety core into OS-Setup.

### Added
- **`philosophy/` — Three Pillars.** LLM-as-OS, Freedom & Responsibility, Harness Engineering. Optional reading for architectural decisions.
- **`PROJECT-INTENT.md` + JSON Schema.** Typed intent capture with stakeholders, success criteria, failure modes, falsification. Validated by `validators/check_intent.sh`.
- **`protocols/route-sentinel.md` + `validators/route_sentinel.sh` (FM-16).** Pre-execution wrong-route blocking via static DAG_TRANSITIONS map.
- **`protocols/vault-mmu.md` + `validators/vault_mmu.sh` (FM-17).** SHA-256 state hashing + hash-chain audit log for tamper detection.
- **`protocols/oap-security.md` + `validators/oap_security.sh` (FM-18).** Deterministic fail-closed policy enforcement before any tool call.
- **`validators/audit_chain.sh`.** Verifies events.jsonl append-only integrity and hash continuity.
- **`validators/check_intent.sh`.** Schema-validates PROJECT-INTENT.md YAML frontmatter.
- **`templates/root/policies/default.yaml`.** Default OAP policy packs for filesystem, network, execution, data.
- **`schemas/ProjectIntent.schema.json`.** Machine-readable intent schema.
- **`schemas/AdaptoidConfig.schema.json`.** Machine-readable config schema.

### Changed
- `validators/emit_event.sh` now appends SHA-256 hash per event for audit-chain verification.
- `validators/preflight.sh` now runs `route_sentinel`, `oap_security`, `check_intent`, and `audit_chain` when their triggers are present.
- `INDEX.md` updated with new philosophy, protocol, and validator entries.
- README updated to "Adaptoid OS v4.0 — A Harness-First Agentic AI Operating System".

### Philosophy
v3.x focused on preventing failures and self-healing. v4.0 adds explicit verification: typed intent, deterministic routing, state integrity, and policy enforcement. The harness remains the primary optimization target.

## v3.0 — Jun 2026 — Executable Adaptoid + Self-Healing + FM-15
The Adaptoid is now executable, not just documented. Validators detect problems and many can auto-fix them. The kit validates itself.

### Added
- **`adaptor/engine.py` — executable Adaptor Engine.** Ingest→Analyze→Pull→Compose→Record→Verify. Detects archetype from brief, picks tier, consults SELECTION.md, generates project structure, copies validators, writes `adaptoid.config.yaml`, runs preflight. Runs locally with no network, no daemon, no git required.
- **`templates/root/adaptoid.config.yaml` — single source of truth per project.** Archetype, tier, stack, compliance, MCP servers, active wave, orchestrator config. Validators check it against reality (FM-05: one fact, one home).
- **Validator `--fix` and `--dry-run` modes.** Most validators support auto-healing; destructive fixes require `--dry-run` review first.
- **`validators/emit_event.sh` — durable session log (Brain/Hands/Session).** Append-only JSONL per wave-task. `replay_session.sh` reconstructs context. `wake.sh` rebuilds orchestrator state from kernel + HANDOFF + EXECUTION + events.
- **`validators/dogfood.sh` — OS-Setup validates itself.** Checks: archetype uniqueness, FM sequentiality, INDEX.md link resolution, CHANGELOG date uniqueness, every FM has a validator, no embarrassing artifacts in the kit itself, engine smoke test.
- **`failure-modes/FM-15-context-compaction.md` — token limit crash.** Prevention: checkpoint protocol (`CHECKPOINT.md` before `/compact`), compaction ritual, reload from events.jsonl.
- **`reference/ecosystem/STALE_CHECK.sh` — freshness enforcement.** Flags ecosystem catalog files older than N days (default 90). Every catalog file gets `last-verified:` frontmatter.

### Changed
- `validators/preflight.sh` now runs `check_processes.sh` automatically if `src/` exists.
- All validators made executable (`chmod +x`).

### Philosophy
v2.x focused on preventing failures. v3.0 adds self-healing and self-validation: detect problems, fix what is safe to fix automatically, and verify the kit's own integrity.

## v2.2 — May 2026 — Adaptor Engine + Conductor + Runtime-Checks + Mental Models
Folded the highest-signal concepts from a parallel "Adaptoid DevKit" research track into the core, generically (no project-specific names).

### Added
- **`adaptor/` — the explicit Adaptor Engine.** 6-step transform (Ingest→Analyze→Pull→Compose→Record→Verify), executable-first `OUTPUT_SPEC.md` (workflow YAML, tool/skill manifests, routing rules, validator wiring, self-heal fields), and a worked `EXAMPLE-given-brief-to-output.md`. Three architecture decisions locked: hybrid independent-core+adapters · executable-first output · runtime-checks as primary persistence.
- **`protocols/runtime-context-check.md`** — primary persistence: validate/refresh context before every phase (detect staleness/contradiction/missing/stale-process/config-drift); git hooks + daemons optional, never required (sovereign/air-gapped-safe).
- **`protocols/conductor-pattern.md`** — ⚡ verified from garrytan/gstack: 10–15 parallel specialized sessions behind mandatory matched review gates (design/eng/devex/security/QA); the high-velocity pattern mapped onto the two-tier model.
- **`reference/mental-models.md`** — Karpathy's LLM-as-OS (kernel/RAM/FS/syscalls/processes/permissions → our implementation) + Netflix freedom-and-responsibility (autonomy inside guardrails + observability + learn-from-failure).
- **`reference/ecosystem/compatibility-adapters.md`** — hybrid stance + framework catalog (LangGraph, CrewAI, AutoGen, MetaGPT, LlamaIndex Workflows, ⚡ADK, Semantic Kernel, Agno, OWL/CAMEL, DeerFlow/MagiC, DSPy) with an adapter contract (import/export/skill-bridge/memory-bridge). Items not freshly fetched are marked "verify before relying."
- **`workflows/` — parameterized flow library** (planner-coder-reviewer, hackathon-sprint, self-healing-verify + catalog of conductor/long-horizon/graph-synthesis/multi-agent-debate/cost-routing/production-deploy). YAML the Adaptor composes into a project plan.
- **`setup/AGENTIC_OS_PROFILE.md`** — local-first harness template (Ollama, vector/graph store, sandbox with no-network containment, observability, 24/7 daemon), honestly labeled as a template to verify.
- **Graphify + code-knowledge-graph layer** added to `knowledge-systems.md` (graph memory for large codebases).
- ⚡ research this turn: gstack (23 skills, conductor), Google ADK 2.0 (context-as-source-code), Anthropic cookbook.

### Honesty
External tools are tagged `⚡` (freshly fetched) vs `(corpus)`/`(reported; verify)`. The DevKit instructs re-fetch-before-rely for anything stale (FM-12 applied to the library itself).

## v2.1 — May 2026 — DevKit Library (pull-on-demand ecosystem)
Turned OS-Setup into a Universal Agentic DevKit by adding a curated, pull-on-demand
reference library so a generated project starts from the collective frontier.

### Added
- **`reference/ecosystem/` (12 catalog files)** — the agentic-AI ecosystem from the last 6 months + leading practitioners:
  - `coding-agents.md`, `sdks-adks.md` (incl. ⚡Google ADK 2.0 "context-as-source-code"), `protocols-standards.md`, `skills-catalog.md` (1000+ skills + sources), `memory-context.md` (⚡headroom 60–95% token cut, ⚡codegraph, ⚡agentmemory, Letta), `optimizations.md`, `knowledge-systems.md` (Obsidian, NotebookLM, ⚡markitdown, RAG), `orchestration-multiagent.md`, `personal-agents.md` (OpenClaw, Hermes), `people.md` (Karpathy, Boris, Willison, Anthropic, Pocock, YC), `INDEX.md`, `SELECTION.md`.
- **`reference/HOW-TO-PULL.md`** — the "books, not memorized" mechanism: read catalog → pull 2–4 matching → choose smallest stack → ADR → close books. Keeps the library huge without bloating context (FM-04-safe).
- **`SELECTION.md` decision engine** — archetype → recommended concrete stack.
- Fresh research burst this turn (⚡): Google ADK 2.0, Anthropic cookbook, and trending repos (headroom, codegraph, agentmemory, oh-my-pi, hermes-desktop, markitdown, knowledge-work-plugins, Understand-Anything).
- Wired the library into `INDEX.md` generation order (step 2b), `00-INVOCATION.md` (step 3b), and README.

### Why
The single biggest "beat everyone" lever isn't a secret model — it's disciplined use of the ecosystem's best tools, auto-selected per problem. The library lets the orchestrator inherit the frontier (compression, indexing, memory, the right SDK) instead of reinventing, while progressive disclosure keeps it from bloating context.

## v2.0 — May 2026 — Folder System + Failure-Prevention + Archetypes
Rebuilt the single-file `OS_SETUP.md` into a modular FOLDER, because the single file
itself caused the "agent forgets everything" bloat it was meant to prevent (FM-04).

### Added
- **Progressive-disclosure folder.** Small always-loaded `kernel/`; everything else pulled on trigger. `INDEX.md` is the agent's navigation table.
- **`failure-modes/` library (14 FMs).** Every entry is a REAL failure observed across rfq2boq / swa-erp / DRO-FairML, with symptom · root cause · prevention · executable validator. Several caught LIVE during the build:
  - FM-01 state drift — live duplicate wave rows + headers + active-wave mismatch in swa-erp
  - FM-02 stale process — live 157-min run with wrong `k_inner=5` in DRO-FairML
  - FM-07 embarrassing artifacts — live `MEETING_CHEAT_SHEET.md` resurfaced in DRO-FairML
- **`archetypes/` adaptation engine (11).** hackathon, internship, job-take-home, research-ml, nlp-pipeline, internal-tool, saas-product, startup-mvp, cli-tool, data-pipeline, + `_TEMPLATE`. The setup now ADAPTS to project type, not one-size.
- **`validators/` (10 executable scripts).** Proven to catch the live failures. `preflight.sh` runs them all; wired into pre-commit + CI + review.
- **`protocols/` (7).** wave-lifecycle, dispatch, review, eval-driven-dev, blast-radius, context-budget, verification.
- **`kernel/` (3).** PRINCIPLES (12 laws), TWO-TIER (Brain/Hands/Session), ANTI-HALLUCINATION (rules mapped to real failures).
- **`tiers/TIERS.md`** — T0–T4 sizing.
- **`00-INVOCATION.md`** — paste-and-go prompt with archetype auto-detection + interview fallback.
- Preserved v1.3 single-file at `reference/OS_SETUP_v1.3_full.md` (all templates live there).

### Carried from v1.3 (still in reference/)
Brain/Hands/Session triad · eval-driven dev (pass@k/pass^k) · skills/commands unification · blast-radius governance · auto mode · durable session log · Swiss-Cheese verification · all v1.0–v1.2 lessons (tiers, HALL_OF_SHAME, BACKLOG, operational docs, audits, compliance, multi-Dockerfile, workflows, etc.)

### Philosophy shift
v1.x = "here's a great structure." v2.0 = "here's a structure that ADAPTS to your project AND actively prevents the specific ways agentic runs fail, with executable proof." The failure-modes library is the heart: the system now learns from scars, not just best practices.

## v1.3 / v1.2 / v1.1 / v1.0
See `reference/OS_SETUP_v1.3_full.md` § "Changelog" for the full single-file history.
