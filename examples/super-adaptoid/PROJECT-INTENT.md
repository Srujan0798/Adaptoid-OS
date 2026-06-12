---
schema_version: "1.0"
project_type: "infrastructure"
archetype: "internal-tool"
tier: "T2"
stakeholders:
  - role: "solo-developer"
    needs: "a long-running research+build assistant that survives sessions and improves weekly"
success_criteria:
  - "assistant recalls prior decisions across sessions without re-explaining (FM-04/FM-14)"
  - "every 'done' claim carries an evidence block (FM-09)"
  - "one adopted improvement per week with a passing eval (Learning Loop)"
failure_modes:
  - "hallucination"
  - "context_forgetting"
  - "false_status"
  - "scope_creep"
non_negotiables:
  - "no destructive/remote action without explicit approval"
  - "proactive suggestions never execute tools unilaterally"
preferences:
  tech_stack: "python + markdown memory-bank"
  worker_tool: "any (Claude Code / Kimi Code / Fable)"
verification_level: "standard"
super_adaptoid:
  loaded:
    - consciousness-core
    - memory-identity
    - evolution-engine
    - fable-5-workflows
  consciousness_core:
    enabled: true
    confidence_threshold: 0.85
    irreversible_threshold: 0.95
    cost_usd_limit: 10.0
    latency_ms_limit: 30000
    anomaly_log: orchestrator/memory/anomalies.jsonl
    checkpoint_file: orchestrator/memory/CHECKPOINT.md
  memory_identity:
    enabled: true
    identity_card: memory-bank/identity.md
    handoff_file: HANDOFF.md
    memory_bank: memory-bank/
    vault_dir: .vault
    hot_context_limit_tokens: 8000
  evolution_engine:
    enabled: true
    gepa:
      max_variants: 3
      eval_threshold: 0.90
      canary_archetype: internal-tool
    hermes:
      max_cycles: 5
      escalation_after_failures: 3
      monitor_interval_hours: 168
    archive_dir: docs/historical/evolution/
  fable_5_workflows:
    enabled: true
    default_workflow: research-synthesis
    registry: workflows/fable-5/
    require_evidence: true
    require_disjoint_writes: true
  proactive_assistant:
    enabled: false   # opt in only after two clean waves
---

# Project Intent

## Problem Statement
A solo developer runs multi-week research+build projects through agent sessions. Context evaporates between sessions, status claims drift from reality, and lessons learned are never reused. This project stands up a persistent assistant on Adaptoid OS with the v5.0 protocol layer enabled: self-monitoring, durable 4-tier memory, and a weekly improvement loop.

## Scope
### IN
- Memory-bank with identity card, facts, lessons; HANDOFF rewritten every session
- Confidence-tagged deliverables with evidence blocks
- Weekly Hermes loop: observe anomalies → propose one improvement → eval → adopt or archive

### OUT
- Autonomous tool execution (proactive mode stays off until trust is earned)
- Any remote/money/human-facing action without approval

### LATER
- Enable `proactive_assistant` after two consecutive clean waves (no FM-08/FM-09 hits)
- Multi-channel gateway (`patterns/multi-channel-gateway.md`)

## Falsification
- A session starts and the assistant cannot state the active wave, last decision, and open anomalies from durable files alone → memory-identity failed.
- Any "done" claim without runnable evidence survives review → consciousness-core failed.
- Three weekly loops pass without a single adopted-or-archived improvement → evolution-engine is theater.
