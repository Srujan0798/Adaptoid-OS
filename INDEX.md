# OS-Setup INDEX — Agent Navigation Table

> Agent: read this to know what exists and WHEN to load it. Do NOT load everything. Progressive disclosure is the point. Load the kernel always; load the rest only when the trigger fires.

## Always load (the kernel — ~2K tokens total)

| File | Load when | Contains |
|---|---|---|
| `kernel/PRINCIPLES.md` | every session start | the 12 non-negotiable laws |
| `kernel/TWO-TIER.md` | every session start | orchestrator vs workers, Brain/Hands/Session |
| `kernel/ANTI-HALLUCINATION.md` | every session start | the rules that stop drift/hallucination/false-status |

## Load on trigger

### Starting a project

| File | Load when (trigger) |
|---|---|
| `00-INVOCATION.md` | starting a brand-new project |
| `archetypes/<x>.md` | once, at project creation, to pick adaptation profile |
| `tiers/TIERS.md` | once, at project creation, to size the build |
| `adaptor/engine.py` | at project creation — RUN the executable Adaptoid (sovereign, no network needed) |
| `adaptor/ADAPTOR_ENGINE.md` | at project creation — understand the transform mechanism |
| `adaptor/OUTPUT_SPEC.md` | when emitting executable artifacts |
| `adaptor/EXAMPLE-given-brief-to-output.md` | to see a worked adaptation |
| `templates/root/adaptoid.config.yaml` | once, at project creation — the single source of truth for this project |
| `scripts/bootstrap.sh` | when creating a new project from template |

### Protocols

| File | Load when (trigger) |
|---|---|
| `protocols/wave-lifecycle.md` | starting any wave |
| `protocols/dispatch-protocol.md` | writing task files for workers |
| `protocols/review-protocol.md` | reviewing a worker report |
| `protocols/eval-driven-dev.md` | defining capabilities / evals |
| `protocols/blast-radius.md` | any action that touches remote/money/humans |
| `protocols/context-budget.md` | context feels full / before /clear |
| `protocols/runtime-context-check.md` | at EVERY major phase boundary (primary persistence) |
| `protocols/conductor-pattern.md` | high-velocity parallel specialized sessions |
| `protocols/route-sentinel.md` | before executing any DAG transition |
| `protocols/vault-mmu.md` | before reading/writing durable state |
| `protocols/oap-security.md` | before any tool call |
| `protocols/verification.md` | before claiming anything "done" |
| `protocols/self-improvement.md` | when setting up GEPA / Hermes loops |
| `protocols/adapt-loop.md` | when designing a request-handling workflow |
| `protocols/memory-tiers.md` | when building durable memory for long-running agents |
| `protocols/consolidation-cycle.md` | when adding background memory maintenance |
| `protocols/evolution-engine.md` | when adding experimental prompt/skill evolution |
| `protocols/event-sourcing.md` | designing session persistence / debugging a past run / proving what happened |
| `protocols/sandboxing.md` | before running untrusted or agent-generated code |
| `protocols/clarification-protocol.md` | when a brief is vague, garbled, or under-specified |
| `adaptor/INPUT-TAXONOMY.md` | at ANALYZE — classify request shape (15 input types × duration × complexity × risk) |

### Super-Adaptoid protocols (v5.0)

| File | Load when (trigger) |
|---|---|
| `protocols/super-adaptoid/README.md` | overview of the v5.0 consciousness + evolution layer |
| `protocols/super-adaptoid/consciousness-core.md` | implementing self-monitoring and honest status |
| `protocols/super-adaptoid/memory-identity.md` | building persistent agent identity |
| `protocols/super-adaptoid/evolution-engine.md` | running safe prompt/skill evolution |
| `protocols/super-adaptoid/proactive-assistant.md` | enabling proactive assistant mode |
| `protocols/super-adaptoid/hidden-gems.md` | evaluating and cataloging under-hyped tools |
| `protocols/super-adaptoid/fable-5-workflows.md` | choosing a Fable 5 workflow narrative |
| `protocols/super-adaptoid/super-prompt.md` | versioning and testing system prompts |

### Patterns & philosophy

| File | Load when (trigger) |
|---|---|
| `philosophy/README.md` | for the WHY (LLM-as-OS, freedom+guardrails) |
| `philosophy/LLM-as-OS.md` | designing architecture, choosing abstractions |
| `philosophy/freedom-responsibility.md` | setting autonomy boundaries, escalation rules |
| `philosophy/harness-engineering.md` | justifying time spent on validation, middleware, tooling |
| `patterns/README.md` | when choosing a design pattern for the current problem |
| `patterns/llm-as-os.md` | architecture decisions |
| `patterns/parallel-conductor.md` | high-velocity parallel sessions |
| `patterns/six-enforced-questions.md` | planning phase |
| `patterns/three-layer-planning-review.md` | review phase |
| `patterns/closed-learning-loop.md` | self-improving systems |
| `patterns/multi-channel-gateway.md` | multi-platform agents |
| `patterns/obsidian-second-brain.md` | knowledge work |
| `patterns/deep-research-three-stage.md` | research projects |
| `reference/mental-models.md` | for the WHY (LLM-as-OS, freedom+guardrails) |

### Workflows, examples, memory, slash commands

| File | Load when (trigger) |
|---|---|
| `workflows/*.yaml` | when composing a project's execution plan |
| `examples/hackathon/` | when learning from hackathon example |
| `examples/production/` | when learning from production SaaS example |
| `examples/research/` | when learning from research ML example |
| `examples/bug-fix/` | when learning from emergency bug fix example |
| `memory-bank/README.md` | when setting up durable memory |
| `memory-bank/FACT.template.md` | when recording a verified fact |
| `memory-bank/LESSON.template.md` | when capturing a post-mortem |
| `memory-bank/ADR.template.md` | when recording an architecture decision |
| `vault/README.md` | when setting up Obsidian second brain |
| `skills/README.md` | when selecting or authoring skills |
| `slash-commands/README.md` | when using named orchestrator commands |
| `setup/AGENTIC_OS_PROFILE.md` | when standing up a local harness |
| `setup/harness/docker-compose.yml` | when starting the optional local stack |

### Validators

| File | Load when (trigger) |
|---|---|
| `validators/memory_sync.sh` | monthly — rotate stale memory entries |
| `validators/emit_event.sh` | after every major action — append to durable session log |
| `validators/replay_session.sh` | after crash or compaction — reconstruct context |
| `validators/wake.sh` | at session start — rebuild orchestrator state from durable files |
| `validators/check_intent.sh` | after writing PROJECT-INTENT.md — validate schema |
| `validators/route_sentinel.sh` | after updating adaptoid.config.yaml — validate DAG |
| `validators/vault_mmu.sh` | after memory writes — verify hash chain |
| `validators/oap_security.sh` | after changing policies — verify coverage |
| `validators/audit_chain.sh` | before claiming session integrity — verify event log |
| `validators/dogfood.sh` | when modifying OS-Setup itself — verify the kit's integrity |

## Quick reference indexes

### Failure-mode quick-reference (load the file when symptom appears)

| FM | Symptom you'd see | One-line prevention |
|---|---|---|
| FM-01 | duplicate/contradictory rows in a state file | one writer, replace-not-append, `validate_state.sh` blocks dupes |
| FM-02 | old process running with wrong params | process registry + `check_processes.sh` before any new run |
| FM-03 | a doc links a file that doesn't exist | `check_references.sh` in pre-commit |
| FM-04 | agent forgets earlier decisions | progressive disclosure + HANDOFF.md + events.jsonl |
| FM-05 | same metric stated two different ways | single metrics source + `check_metrics.sh` |
| FM-06 | config silently reverted (epochs 60→30) | config is single source + runtime assertion |
| FM-07 | cheat-sheet / AI-prompt committed to repo | `publish_gate.sh` pre-commit scan |
| FM-08 | building features nobody asked for | SCOPE_GUARD + worker "NOT touch" lists |
| FM-09 | claimed done but it isn't / misframed | evidence-required, honest-status rule |
| FM-10 | test passes alone, fails in suite | flaky quarantine + shared-state isolation |
| FM-11 | errors swallowed by try/except fallback | no silent fallbacks rule |
| FM-12 | README shows old results | derived-docs regenerated, never hand-edited |
| FM-13 | two workers edit the same file | disjoint file ownership per task |
| FM-14 | new session has no idea where things are | HANDOFF.md + replay_session.sh |
| FM-15 | orchestrator hits token limit, loses state | CHECKPOINT.md before /compact + wake.sh |
| FM-16 | hallucinated DAG transitions / wrong route | static DAG_TRANSITIONS + `route_sentinel.sh` |
| FM-17 | tampered state / undetected drift | SHA-256 hash chain + `vault_mmu.sh` |
| FM-18 | unauthorized tool call / destructive action | OAP policy packs + `oap_security.sh` |

### Fable 5 quick-reference

| Fable | Trigger | Go-to protocol / workflow |
|---|---|---|
| Fable 1 — Deep Research | open-ended question | `patterns/deep-research-three-stage.md` |
| Fable 2 — Build & Ship | typed intent available | `workflows/planner-coder-reviewer.yaml` |
| Fable 3 — Critical Review | report/code exists | `protocols/review-protocol.md` |
| Fable 4 — Launch & Grow | public release | `docs/launch/` playbook suite |
| Fable 5 — Evolve | post-ship or anomaly | `protocols/super-adaptoid/evolution-engine.md` |

### Hidden gems quick-reference

| Area | Starting point |
|---|---|
| Coding agents & ADKs | `reference/ecosystem/coding-agents.md` |
| Memory & context | `reference/ecosystem/memory-context.md` |
| Lesser-known tools | `reference/ecosystem/hidden-gems.md` |
| Stack selection | `reference/ecosystem/SELECTION.md` |

## Reference

Use these files for deep dives, monthly maintenance, and ecosystem research — not for every session.

| File | Load when |
|---|---|
| `reference/ecosystem/compatibility-adapters.md` | when bridging to LangGraph/CrewAI/AutoGen |
| `reference/ecosystem/STALE_CHECK.sh` | monthly — flag stale ecosystem catalog entries |
| `reference/HOW-TO-PULL.md` | once, at setup, to learn how to use the ecosystem library |
| `reference/ecosystem/INDEX.md` | at setup, to see the tool/skill/SDK catalog |
| `reference/ecosystem/SELECTION.md` | at setup, to map archetype → recommended stack |
| `reference/ecosystem/<topic>.md` | pull the 2–4 that match the project (coding-agents, sdks-adks, memory-context, optimizations, etc.) |
| `reference/ecosystem/tools-compendium.md` | when choosing your tool stack |
| `reference/ecosystem/skills-registry.md` | when selecting or authoring skills |
| `reference/ecosystem/hidden-gems.md` | when evaluating lesser-known tools and patterns |
| `reference/ecosystem/ecosystem-analysis.md` | when positioning against the broader agentic landscape |
| `reference/workflows/startup-mvp.md` | startup MVP playbook |
| `reference/workflows/data-science.md` | data science / ML playbook |
| `reference/workflows/hackathon-48h.md` | 48-hour hackathon playbook |
| `reference/workflows/web-development.md` | full-stack web dev playbook |
| `reference/workflows/security-audit.md` | security audit playbook |
| `reference/workflows/mobile-development.md` | mobile app playbook |
| `reference/workflows/bioinformatics.md` | bioinformatics pipeline playbook |
| `reference/workflows/content-creation.md` | content creation playbook |
| `reference/workflows/devops-sre.md` | DevOps / SRE playbook |
| `reference/workflows/game-development.md` | game development playbook |
| `reference/workflows/blockchain-web3.md` | blockchain / Web3 playbook |
| `reference/workflows/finance-trading.md` | finance / trading playbook |
| `reference/workflows/education-tutoring.md` | education / tutoring playbook |
| `reference/workflows/consulting.md` | consulting playbook |
| `reference/workflows/iot-robotics.md` | IoT / robotics playbook |
| `reference/ADAPTOID-ENGINE.md` | detailed engine specification |
| `reference/MASTER-SETUP.md` | stack wiring guide |
| `reference/VERIFICATION-PROTOCOLS.md` | verification taxonomy |
| `reference/MEMORY-INDEX.md` | memory protocol specification |
| `reference/research-bibliography.md` | evidence base bibliography |
| `reference/research-landscape-map.md` | ecosystem landscape map |
| `reference/research-headroom-analysis.md` | harness headroom analysis |
| `reference/OS_SETUP_v1.3_full.md` | when you need an exact template body |
| `ROADMAP.md` | future direction |
| `SECURITY.md` | security policy |
| `Makefile` | common commands |
| `tests/run_tests.sh` | validator test suite |
| `templates/**` | when generating a specific file |
| `validators/*.sh` | run via preflight before every merge/ship |

## Generation order (when creating a project)

1. `kernel/*` (load)
2. `archetypes/<detected>.md` + `tiers/TIERS.md` (decide profile + tier)
2b. `reference/HOW-TO-PULL.md` → `reference/ecosystem/SELECTION.md` → pull the 2–4 catalog files that match; choose the stack; write `docs/decisions/0002-stack-selection.md` (ADR)
3. **Run `adaptor/engine.py --brief "..." --output <dir>`** — generates structure, config, validators, ADR (or do it manually via steps 4-10)
4. `templates/root/*` → CLAUDE.md, KIMI.md, HANDOFF.md, HIERARCHY.md, README.md, `adaptoid.config.yaml`
5. `templates/plan/*` → PRD, ARCHITECTURE, EXECUTION
6. `templates/specify/*` → constitution + wave-1 spec/plan/tasks/contracts
7. `templates/orchestrator/*` → ROLE, core, commands, skills, agents, hooks, memory/session/
8. `templates/work/*` → TASK/REPORT/WORKER templates + wave-1 task files
9. `templates/evals/*` → eval tasks + graders
10. `templates/docs/*` + `templates/ci/*`
11. copy `validators/*` into the project's `orchestrator/scripts/`
12. run `validators/preflight.sh` → must pass before first dispatch
13. run `validators/dogfood.sh` from OS-Setup root to verify the kit itself
