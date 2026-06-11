# Adaptoid OS v4.0 — Phase 1 Design
## Foundation + Safety Core Merge

**Date:** 2026-06-11  
**Status:** Approved  
**Sources:** OS-Setup v3.0 + Adaptoid-OS v2.0 + ADAPTOID-DEVKIT-v3.3-TRUE-ETERNAL  

---

## Goal
Transform OS-Setup into Adaptoid OS v4.0 by merging the highest-leverage safety and architecture pieces from the Adaptoid materials, while keeping OS-Setup’s progressive-disclosure kernel, validators, and working executable engine intact.

## Principles
1. **Progressive disclosure stays.** Kernel remains small; new pieces load on trigger.
2. **Every new protocol gets a validator.** Nothing is documentation-only.
3. **No stubs.** Every merged component must be runnable or passable by dogfood.
4. **Backward compatible.** Existing `00-INVOCATION.md` and archetypes still work.

---

## Components (Phase 1)

### 1. Philosophy Layer
- Add `philosophy/` folder with three named pillars:
  - `philosophy/LLM-as-OS.md` (Karpathy mental model)
  - `philosophy/freedom-responsibility.md` (Netflix culture mapped to agents)
  - `philosophy/harness-engineering.md` (2026 consensus: harness > model)
- Add `philosophy/README.md` as navigation.
- Link from `kernel/PRINCIPLES.md` and `reference/mental-models.md`.

### 2. Typed Intent Capture
- Add `PROJECT-INTENT.md` template to `templates/root/` with JSON Schema (`schemas/ProjectIntent.schema.json`).
- Extend `adaptor/engine.py` to:
  - Read brief + context
  - Emit structured `PROJECT-INTENT.md` (YAML frontmatter + body)
  - Infer failure modes from intent and pre-select relevant FM validators
- Add `validators/check_intent.sh`:
  - Validates `PROJECT-INTENT.md` against schema
  - Checks that every declared failure mode has a matching validator

### 3. Route Sentinel (FM-16)
- Add `protocols/route-sentinel.md`:
  - Static DAG_TRANSITIONS map validation
  - Pre-execution wrong-route blocking
  - Retry limit + escalation rules
- Add `validators/route_sentinel.sh`:
  - Checks `adaptoid.config.yaml` for `dag_transitions` block
  - Validates every transition source/target exists
  - Flags self-loops, unknown nodes, missing retry policies
  - Emits `WRONG_ROUTE_BLOCKED` event on failure

### 4. VaultMMU (FM-17)
- Add `protocols/vault-mmu.md`:
  - SHA-256 state hashing at write
  - Hash-chain audit log
  - Tamper detection on read
- Add `validators/vault_mmu.sh`:
  - Computes SHA-256 of `orchestrator/memory/` files
  - Verifies chain integrity against last known hash
  - Flags tampered or missing files

### 5. OAP Security (FM-18)
- Add `protocols/oap-security.md`:
  - Pre-tool-call deterministic policy enforcement
  - Default policy packs: filesystem, network, code-execution, data-access
- Add `validators/oap_security.sh`:
  - Checks `policies/` directory for valid policy packs
  - Validates every tool call in events.jsonl against active policies
  - Flags missing policy packs for declared tools

### 6. Event Sourcing Extension
- Extend `validators/emit_event.sh` to:
  - Emit typed events: `INTENT_COMPILED`, `DAG_STARTED`, `NODE_EXECUTED`, `VERIFICATION_PASSED`, `VERIFICATION_FAILED`, `STATE_COMMITTED`, `WRONG_ROUTE_BLOCKED`
  - Append events with timestamp + hash + event_id
- Add `validators/audit_chain.sh`:
  - Verifies event log is append-only
  - Checks hash continuity
  - Reports gaps or tampering

### 7. Schema & Config
- Add `schemas/ProjectIntent.schema.json`
- Add `schemas/AdaptoidConfig.schema.json`
- Add `templates/root/adaptoid.config.yaml` (extends existing template with `dag_transitions`, `policies`, `vault`, `event_sourcing` blocks)

### 8. README & Branding
- Update `README.md` title to "Adaptoid OS v4.0 — Eternal Agentic Harness"
- Add v4.0 changelog entry
- Keep all existing OS-Setup content; append Adaptoid additions as "What’s new in v4.0"

---

## Verification Criteria
- `validators/dogfood.sh` PASS with zero warnings
- `validators/preflight.sh` PASS
- All new validators executable and passing on OS-Setup itself
- `adaptor/engine.py` still generates valid project structures

---

## Out of Scope (Phase 2+)
- Docker Compose harness
- Full 15 domain workflows
- GEPA / Hermes self-improvement loops
- Multi-channel gateway
- Obsidian vault integration
- Claw Bridge framework adapters
