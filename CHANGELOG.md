# Adaptoid OS Changelog

## v4.0 — Jun 2026 — Eternal Agentic Harness (Safety Core + Typed Intent + Philosophy)
Merged the highest-leverage Adaptoid safety core into OS-Setup to create the eternal harness.

### Added
- **`philosophy/` — The Three Pillars.** LLM-as-OS (Karpathy), Freedom & Responsibility (Netflix), Harness Engineering (2026 consensus). Codifies the worldview behind every decision.
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
- README rebranded to "Adaptoid OS v4.0 — Eternal Agentic Harness".

### Philosophy
v3.x = "the kit prevents failures and heals itself." v4.0 = "the kit prevents failures, heals itself, and verifies relentlessly through cryptographic integrity and deterministic policy enforcement." The harness is the primary optimization target.

## v3.0 — Jun 2026 — The Ultimate OS-Setup (Executable Adaptoid + Self-Healing + FM-15)
The recommendations from the deep forensic analysis are now implemented. The Adaptoid is no longer a document — it executes. Validators don't just detect, they fix. The OS validates itself.

### Added
- **`adaptor/engine.py` — executable Adaptor Engine.** Ingest→Analyze→Pull→Compose→Record→Verify. Detects archetype from brief, picks tier, consults SELECTION.md, generates project structure, copies validators, writes `adaptoid.config.yaml`, runs preflight. Sovereign: needs no network, no daemon, no git.
- **`templates/root/adaptoid.config.yaml` — single source of truth per project.** Archetype, tier, stack, compliance, MCP servers, active wave, orchestrator config. Validators check it against reality (FM-05: one fact, one home).
- **Validator `--fix` and `--dry-run` modes.** All 10 validators support auto-healing:
  - `validate_state.sh --fix` — removes duplicate rows/headers, reconciles active wave
  - `check_processes.sh --fix` — kills stale processes with param drift
  - `check_config.sh --fix` — rewrites config to match lock
  - `publish_gate.sh --fix` — moves embarrassing artifacts to `attic/`, untracks `.env`
  - `check_references.sh --fix` — marks broken links
  - `check_metrics.sh --fix` — adds auto-generated headers
  - `check_silent_failures.sh --fix` — replaces bare `except:` with `except Exception as e:`
  - `context_budget.sh --fix` — suggests what to move out of kernel
  - `preflight.sh` passes `--fix`/`--dry-run` through to all sub-validators
- **`validators/emit_event.sh` — durable session log (Brain/Hands/Session).** Append-only JSONL per wave-task. `replay_session.sh` reconstructs context. `wake.sh` rebuilds full orchestrator state from kernel + HANDOFF + EXECUTION + events.
- **`validators/dogfood.sh` — OS-Setup validates itself.** Checks: archetype uniqueness, FM sequentiality, INDEX.md link resolution, CHANGELOG date uniqueness, every FM has a validator, no embarrassing artifacts in the kit itself, engine smoke test.
- **`failure-modes/FM-15-context-compaction.md` — token limit crash.** Observed live: Claude died 3x from context limits in the DRO-FairML session. Prevention: checkpoint protocol (`CHECKPOINT.md` before `/compact`), compaction ritual, reload from events.jsonl.
- **`reference/ecosystem/STALE_CHECK.sh` — freshness enforcement.** Flags ecosystem catalog files older than N days (default 90). Every catalog file gets `last-verified:` frontmatter.

### Changed
- `validators/preflight.sh` now runs `check_processes.sh` automatically if `src/` exists.
- All validators made executable (`chmod +x`).

### Philosophy
v2.x = "the kit prevents failures." v3.0 = "the kit prevents failures, heals itself when they happen, and validates its own integrity." The Adaptoid is now a true agentic OS — not a guide, but a running system.

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
