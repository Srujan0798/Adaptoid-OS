# Memory-Identity Protocol

> Persistent agent identity, session continuity, and memory-integrity rituals.

## Purpose

Ensure that an agentic workforce has a stable identity and durable memory across sessions, crashes, and compaction events, without bloating the active context window.

## Four-tier memory model

| Tier | Location | Scope | Example |
|---|---|---|---|
| **Working** | Active context + `orchestrator/memory/session/*.events.jsonl` | Current task only | Tool outputs, scratch reasoning, pending decisions |
| **Episodic** | `memory-bank/lessons/` + append-only `events.jsonl` | Wave / project | Post-mortems, anomaly stories, sprint retrospectives |
| **Semantic** | `memory-bank/facts/` + `docs/decisions/` | Project / ecosystem | ADRs, verified facts, stack rules, API contracts |
| **Identity** | `memory-bank/identity.md` | Cross-project agent persona | Role, voice, constraints, escalation rules |

## Rules

1. **One identity card.** `memory-bank/identity.md` is the single source of truth for role, voice, constraints, and escalation rules.
2. **Replace, never append, state.** `HANDOFF.md` is rewritten at session end; append-only is reserved for `events.jsonl`.
3. **Progressive disclosure.** Hot context stays in session; warm/cold facts are lazy-loaded from `memory-bank/`.
4. **Hash-chain verification.** Every durable write is covered by `validators/vault_mmu.sh` (FM-17).
5. **No scope creep from memory.** Recalling a lesson does not authorize acting on it unless it is in the current brief (FM-08).

## Required `PROJECT-INTENT.md` / `adaptoid.config.yaml` fields

```yaml
super_adaptoid:
  loaded:
    - memory-identity
  memory_identity:
    enabled: true
    identity_card: memory-bank/identity.md
    handoff_file: HANDOFF.md
    memory_bank: memory-bank/
    vault_dir: .vault
    hot_context_limit_tokens: 8000
```

## Failure modes addressed

- **FM-04 — Context Bloat:** progressive disclosure keeps hot context small; `context_budget.sh` enforces the kernel budget.
- **FM-06 — Config Revert:** identity and memory paths are declared in config and asserted by validators.
- **FM-08 — Scope Creep:** memory recall is read-only unless the current brief explicitly authorizes a change.
- **FM-18 — Unauthorized Tool Call:** OAP policies govern which tools may read/write each memory tier.

## Relationship to the Kernel

Depends on `kernel/TWO-TIER.md` (Brain/Hands/Session) and `kernel/ANTI-HALLUCINATION.md` (one source of truth per fact).

## Validator

```bash
[ -f memory-bank/identity.md ] || echo "Note: identity card not initialized"
bash validators/context_budget.sh
[ -f configs/default.yaml ] && [ -f configs/default.lock ] && bash validators/check_config.sh
bash validators/check_scope.sh
[ -d policies ] && bash validators/oap_security.sh
bash validators/dogfood.sh
```
