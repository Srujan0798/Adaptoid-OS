---
last-verified: 2026-06-12
confidence: corpus
---

# Fable 5 Workflow Index

> Pull when choosing a workflow for a long-horizon, multi-agent, or self-improving task. This index maps the 10 Fable 5 workflow patterns (defined in `protocols/super-adaptoid/fable-5-workflows.md`) to the concrete OS-Setup assets each one loads. The patterns came from practitioner testing of frontier orchestrators; they are orchestrator-agnostic — they run on Fable 5, Kimi Code, Claude Code, or any harness that reads this kit.

## Workflow → assets map

| # | Workflow | Load these assets | Validators in the loop |
|---|---|---|---|
| 1 | Research Synthesis | `patterns/deep-research-three-stage.md`, `protocols/clarification-protocol.md` | `check_references.sh`, `check_status_claims.sh` |
| 2 | Code Generation with Tests | `workflows/planner-coder-reviewer.yaml`, `protocols/eval-driven-dev.md` | `check_tests.sh`, `preflight.sh` |
| 3 | Review & Refactor Loop | `patterns/three-layer-planning-review.md`, `protocols/review-protocol.md` | `check_metrics.sh`, `check_tests.sh` |
| 4 | Bug Hunt & Patch | `workflows/self-healing-verify.yaml`, `failure-modes/FM-11-silent-failures.md` | `check_silent_failures.sh`, `check_tests.sh` |
| 5 | Documentation Sprint | `failure-modes/FM-12-stale-derived-docs.md`, `failure-modes/FM-03-broken-references.md` | `check_references.sh`, `publish_gate.sh` |
| 6 | Migration Assistant | `adaptor/INPUT-TAXONOMY.md` (MIGRATE), `protocols/blast-radius.md` | `validate_state.sh`, `check_config.sh` |
| 7 | Release Orchestrator | `protocols/wave-lifecycle.md`, `templates/ci/ci.yml` | `publish_gate.sh`, `preflight.sh` |
| 8 | Dependency Auditor | `reference/ecosystem/STALE_CHECK.sh`, `skills/domain/security-audit.md` | `check_config.sh` |
| 9 | On-call Responder | `protocols/event-sourcing.md`, `failure-modes/README.md` | `replay_session.sh`, `audit_chain.sh` |
| 10 | Learning Loop | `protocols/super-adaptoid/evolution-engine.md`, `memory-bank/LESSON.template.md` | `check_processes.sh`, `dogfood.sh` |

## Selection heuristics

- Start from the **input type** (`adaptor/INPUT-TAXONOMY.md`): DEBUG → Bug Hunt; MIGRATE → Migration Assistant; RESEARCH → Research Synthesis; OPTIMIZE → Review & Refactor or Learning Loop.
- If the task spans multiple workflows, sequence them as waves (`protocols/wave-lifecycle.md`) — never interleave two workflows in one wave (FM-13).
- Every workflow starts from a typed `PROJECT-INTENT.md` and ends with an evidence-backed verification pass (FM-09).

## Origin and honesty

The pattern names trace to a practitioner post testing Fable 5 ("the 10 workflows that matter"); the versions here are re-grounded onto OS-Setup primitives and validators. Treat the table as corpus knowledge: re-verify orchestrator-specific behaviors against the live tool before relying on them (FM-12).
