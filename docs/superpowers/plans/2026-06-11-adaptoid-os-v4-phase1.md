# Adaptoid OS v4.0 Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Merge the Adaptoid safety core (Route Sentinel, VaultMMU, OAP Security, Event Sourcing, Typed Intent, Philosophy) into OS-Setup while keeping dogfood and preflight green.

**Architecture:** Keep OS-Setup’s progressive-disclosure kernel. Add new protocols under `protocols/`, validators under `validators/`, philosophy under `philosophy/`, schemas under `schemas/`, and extend `adaptor/engine.py` to emit `PROJECT-INTENT.md`. Every new protocol gets a runnable validator.

**Tech Stack:** Bash (validators), Python 3 (engine.py), Markdown (docs), JSON Schema (schemas).

---

## File Map

| File | Responsibility |
|---|---|
| `philosophy/README.md` | Navigation for philosophy layer |
| `philosophy/LLM-as-OS.md` | Karpathy mental model |
| `philosophy/freedom-responsibility.md` | Netflix culture → agents |
| `philosophy/harness-engineering.md` | Harness-first consensus |
| `templates/root/PROJECT-INTENT.md` | Typed intent template for generated projects |
| `schemas/ProjectIntent.schema.json` | JSON Schema for intent validation |
| `validators/check_intent.sh` | Validates PROJECT-INTENT.md against schema |
| `protocols/route-sentinel.md` | Route Sentinel protocol documentation |
| `validators/route_sentinel.sh` | Validates DAG transitions and route correctness |
| `protocols/vault-mmu.md` | VaultMMU protocol documentation |
| `validators/vault_mmu.sh` | Computes/verifies SHA-256 hash chain |
| `protocols/oap-security.md` | OAP Security protocol documentation |
| `validators/oap_security.sh` | Validates policy packs and tool coverage |
| `validators/audit_chain.sh` | Verifies event log append-only + hash continuity |
| `templates/root/adaptoid.config.yaml` | Extended project config with new blocks |
| `README.md` | Updated to v4.0 branding |
| `CHANGELOG.md` | v4.0 entry added |
| `INDEX.md` | Updated with new files |

---

## Task 1: Philosophy Layer

**Files:**
- Create: `philosophy/README.md`
- Create: `philosophy/LLM-as-OS.md`
- Create: `philosophy/freedom-responsibility.md`
- Create: `philosophy/harness-engineering.md`
- Modify: `INDEX.md` (add philosophy entries)

- [ ] **Step 1: Create `philosophy/README.md`**

```markdown
# Philosophy — The Three Pillars of Adaptoid OS

Load these when you need the **why** behind a decision. They never contradict `kernel/PRINCIPLES.md`; they deepen it.

| Pillar | File | When to load |
|---|---|---|
| LLM-as-OS | `philosophy/LLM-as-OS.md` | Designing architecture, choosing abstractions |
| Freedom & Responsibility | `philosophy/freedom-responsibility.md` | Setting autonomy boundaries, escalation rules |
| Harness Engineering | `philosophy/harness-engineering.md` | Justifying time spent on validation, middleware, tooling |
```

- [ ] **Step 2: Create `philosophy/LLM-as-OS.md`**

```markdown
# Pillar I — LLM-as-OS

Andrej Karpathy: LLMs are the new operating systems.

| OS Primitive | Traditional | Agentic Equivalent |
|---|---|---|
| CPU | Silicon | LLM inference |
| RAM | DRAM | Context window |
| I/O devices | Keyboard/mouse/display | Tools (Read, Write, Bash, MCP...) |
| Kernel | Linux | Adaptoid harness (verification, memory, routing) |
| Filesystem | ext4 | Living-folder Markdown + hash chain |
| Scheduler | cron/systemd | Conductor / parallel dispatcher |
| Permissions | chmod/ACL | OAP Policy Packs + Route Sentinel |

**Implication:** The harness ( Adaptoid ) is the binding constraint. Optimizing it yields gains comparable to model upgrades.
```

- [ ] **Step 3: Create `philosophy/freedom-responsibility.md`**

```markdown
# Pillar II — Freedom & Responsibility

Netflix culture applied to agentic AI:

- **High autonomy** — Agents have broad authority to act.
- **Strong guardrails** — Every action passes runtime validation before persistence.
- **Deep observability** — Immutable audit trail, cost attribution, trace IDs.
- **Resilient recovery** — Automatic rollback on verification failure; escalation after retry exhaustion.

**The Keeper Test for skills:** Would you fight to keep this skill in the system? If not, archive it.
```

- [ ] **Step 4: Create `philosophy/harness-engineering.md`**

```markdown
# Pillar III — Harness Engineering

By mid-2026, the evidence is clear: **harness upgrades match or exceed model upgrades.**

| Study | Harness Change | Gain |
|---|---|---|
| Stanford/MIT Meta-Harness | System prompts + middleware | +4.7pp on IMO math |
| LangChain DeepAgents | Middleware + routing | +26% TerminalBench 2.0 |
| OpenAI Codex team | "Harness engineering" coined | Formal discipline |

**Adaptoid's stance:** The harness is the primary optimization target. Models are swappable; a robust harness compounds forever.
```

- [ ] **Step 5: Update `INDEX.md`**

Add to the "Load on trigger" table:
```
| `philosophy/README.md` | when you need the WHY behind a decision |
| `philosophy/LLM-as-OS.md` | designing architecture, choosing abstractions |
| `philosophy/freedom-responsibility.md` | setting autonomy boundaries, escalation rules |
| `philosophy/harness-engineering.md` | justifying time spent on validation, middleware, tooling |
```

---

## Task 2: Typed Intent Capture

**Files:**
- Create: `templates/root/PROJECT-INTENT.md`
- Create: `schemas/ProjectIntent.schema.json`
- Modify: `adaptor/engine.py`
- Create: `validators/check_intent.sh`

- [ ] **Step 1: Create `templates/root/PROJECT-INTENT.md`**

```markdown
---
schema_version: "1.0"
project_type: "web_app"
archetype: "saas-product"
tier: "T2"
stakeholders:
  - role: "user"
    needs: "..."
success_criteria:
  - "..."
failure_modes:
  - "hallucination"
  - "wrong_route"
non_negotiables:
  - "..."
preferences:
  tech_stack: "..."
  worker_tool: "OpenCode CLI"
verification_level: "standard"
---

# Project Intent

## Problem Statement
<!-- What are we building and why? -->

## Scope
### IN
<!-- Must deliver -->

### OUT
<!-- Explicitly excluded -->

### LATER
<!-- Backlog for future waves -->

## Falsification
<!-- What would prove this project failed? -->
```

- [ ] **Step 2: Create `schemas/ProjectIntent.schema.json`**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ProjectIntent",
  "type": "object",
  "required": ["schema_version", "project_type", "archetype", "tier", "success_criteria", "failure_modes"],
  "properties": {
    "schema_version": { "type": "string", "enum": ["1.0"] },
    "project_type": { "type": "string", "enum": ["web_app", "data_analysis", "api_design", "ml_pipeline", "infrastructure", "research", "content_creation"] },
    "archetype": { "type": "string" },
    "tier": { "type": "string", "enum": ["T0", "T1", "T2", "T3", "T4"] },
    "stakeholders": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "role": { "type": "string" },
          "needs": { "type": "string" }
        },
        "required": ["role", "needs"]
      }
    },
    "success_criteria": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
    "failure_modes": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
    "non_negotiables": { "type": "array", "items": { "type": "string" } },
    "preferences": { "type": "object" },
    "verification_level": { "type": "string", "enum": ["minimal", "standard", "maximum"] }
  }
}
```

- [ ] **Step 3: Extend `adaptor/engine.py`**

Add a function `emit_project_intent(brief, archetype, tier, output_dir)` that writes `PROJECT-INTENT.md` with inferred fields filled from the brief. Use existing archetype detection logic.

- [ ] **Step 4: Create `validators/check_intent.sh`**

```bash
#!/usr/bin/env bash
# Validates PROJECT-INTENT.md YAML frontmatter against JSON Schema.
set -uo pipefail
ROOT="${1:-.}"
INTENT="$ROOT/PROJECT-INTENT.md"
SCHEMA="$ROOT/../schemas/ProjectIntent.schema.json"
[ -f "$SCHEMA" ] || SCHEMA="$ROOT/schemas/ProjectIntent.schema.json"

if [ ! -f "$INTENT" ]; then
  echo "OK check-intent: no PROJECT-INTENT.md found (optional for small projects)"
  exit 0
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "WARN check-intent: python3 not available; skipping schema validation"
  exit 0
fi

python3 -c "
import json, sys, yaml
from pathlib import Path
intent_file = Path('$INTENT')
schema_file = Path('$SCHEMA')
if not schema_file.exists():
    print('WARN check-intent: schema not found')
    sys.exit(0)
try:
    import jsonschema
except ImportError:
    print('WARN check-intent: jsonschema not installed; install with pip install jsonschema')
    sys.exit(0)

lines = intent_file.read_text().splitlines()
if lines[0].strip() != '---':
    print('FAIL check-intent: PROJECT-INTENT.md missing YAML frontmatter')
    sys.exit(1)
end = lines.index('---', 1)
front = yaml.safe_load('\n'.join(lines[1:end]))
schema = json.loads(schema_file.read_text())
jsonschema.validate(front, schema)
print('OK check-intent: PROJECT-INTENT.md valid')
except Exception as e:
    print(f'FAIL check-intent: {e}')
    sys.exit(1)
" || exit 1
```

---

## Task 3: Route Sentinel

**Files:**
- Create: `protocols/route-sentinel.md`
- Create: `validators/route_sentinel.sh`

- [ ] **Step 1: Create `protocols/route-sentinel.md`**

(Documentation of static DAG_TRANSITIONS map, pre-execution route checking, retry limits, escalation.)

- [ ] **Step 2: Create `validators/route_sentinel.sh`**

Validates `adaptoid.config.yaml` contains a `dag_transitions` block with valid source/target nodes, no self-loops, and retry policies.

---

## Task 4: VaultMMU

**Files:**
- Create: `protocols/vault-mmu.md`
- Create: `validators/vault_mmu.sh`

- [ ] **Step 1: Create `protocols/vault-mmu.md`**

(Documentation of SHA-256 hashing, hash chain, tamper detection.)

- [ ] **Step 2: Create `validators/vault_mmu.sh`**

Computes SHA-256 of `orchestrator/memory/` files, verifies chain against stored hashes in `.vault/hashes.json`.

---

## Task 5: OAP Security

**Files:**
- Create: `protocols/oap-security.md`
- Create: `validators/oap_security.sh`
- Create: `templates/root/policies/default.yaml`

- [ ] **Step 1: Create `protocols/oap-security.md`**

(Documentation of deterministic policy enforcement, default packs.)

- [ ] **Step 2: Create `validators/oap_security.sh`**

Checks `policies/` directory exists, validates YAML syntax, checks every active tool has a matching policy.

- [ ] **Step 3: Create `templates/root/policies/default.yaml`**

```yaml
policies:
  filesystem:
    - pattern: "Read"
      decision: allow
    - pattern: "Write"
      decision: ask
    - pattern: "Bash(rm -rf*)"
      decision: deny
  network:
    - pattern: "Bash(curl*|wget*)"
      decision: ask
```

---

## Task 6: Event Sourcing Extension

**Files:**
- Modify: `validators/emit_event.sh`
- Create: `validators/audit_chain.sh`

- [ ] **Step 1: Extend `validators/emit_event.sh`**

Add typed event prefixes and hash field.

- [ ] **Step 2: Create `validators/audit_chain.sh`**

Verifies events.jsonl is append-only, hashes are continuous, no gaps.

---

## Task 7: Config & README Updates

**Files:**
- Create: `templates/root/adaptoid.config.yaml`
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Modify: `INDEX.md`

- [ ] **Step 1: Create extended `templates/root/adaptoid.config.yaml`**

Add `dag_transitions`, `policies`, `vault`, `event_sourcing` blocks.

- [ ] **Step 2: Update `README.md`**

Change title to "Adaptoid OS v4.0 — Eternal Agentic Harness". Add "What’s new in v4.0" section.

- [ ] **Step 3: Update `CHANGELOG.md`**

Add v4.0 entry.

---

## Task 8: Final Validation

- [ ] **Step 1: Run `bash validators/dogfood.sh`**
- [ ] **Step 2: Run `bash validators/preflight.sh`**
- [ ] **Step 3: Fix any failures**

---

## Spec Coverage Checklist

| Design Doc Section | Task |
|---|---|
| Philosophy Layer | Task 1 |
| Typed Intent Capture | Task 2 |
| Route Sentinel | Task 3 |
| VaultMMU | Task 4 |
| OAP Security | Task 5 |
| Event Sourcing | Task 6 |
| Config & README | Task 7 |
| Verification | Task 8 |
