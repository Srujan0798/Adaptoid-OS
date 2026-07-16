# Adaptor Output Spec — Executable-First Artifacts

> What the Adaptor Engine emits. Machine-consumable first; human guidance second. These formats are what agents/runners directly consume.

## 1. Workflow spec (`workflows/<project>.plan.yaml`)
The execution plan as data — DAG of phases, gates, parallelism, verification.
```yaml
project: <name>
archetype: <archetype>
tier: T<n>
stack: [<chosen tools from SELECTION>]
waves:
  - id: wave-1
    goal: <one line>
    parallelism: 5            # max concurrent worker tasks
    tasks:
      - id: 01-<name>
        writes: [src/a.py, tests/test_a.py]    # disjoint across siblings (FM-13)
        forbid: [migrations/, src/b.py]
        skills: [tdd, code-review]             # worker-side
        acceptance: "pytest tests/test_a.py"   # executable
        blast_radius: r1                        # blast-radius.md
        budget: {minutes: 90, tokens: 50000}
    gates:
      pre_dispatch: [check_dispatch_disjoint.sh]
      pre_merge:    [preflight.sh]
      pre_ship:     [preflight.sh, eval pass^k>=0.95]
    verification: [unit, integration, acceptance, verifier-subagent]
    self_heal:
      on_acceptance_fail: revise_brief
      on_flaky: quarantine_and_fix    # FM-10
```

## 2. Tool/skill manifest (`mcp.json` + `skills.manifest.json`)
```json
// mcp.json — declared MCP servers (the project's tools/hands)
{ "mcpServers": { "filesystem": {...}, "git": {...}, "tavily": {...} } }
```
```json
// skills.manifest.json — worker skills + versions (reproducibility)
{ "skills": { "tdd": "^1.2", "pdf-processing": "^1.5" } }
```

## 3. Routing rules (`adaptor/routing.yaml`)
Which model/agent handles which work (cost-aware cascade).
```yaml
routing:
  plan:        {tier: orchestrator, model: opus-class}
  implement:   {tier: worker, model: balanced}
  review:      {tier: orchestrator, sub_agent: verifier, model: opus-class}
  explore:     {tier: sub_agent, model: cheap}     # read-heavy → cheaper
  bulk_format: {tier: worker, model: cheap, auto_mode: true}  # r0/r1 only
cost_budget: {per_wave_usd: 5, alert_at: 0.8}
```

## 4. Validator wiring (`.pre-commit-config.yaml` + `.github/workflows/`)
The failure-mode validators bound to hooks + CI (generated from failure-modes/).

## 5. Kernel + briefs
`CLAUDE.md`/`KIMI.md` (kernel laws embedded, project-tuned, SHORT) and `work/wave-1/*.md` self-contained task briefs.

## 6. The ADR (human layer)
`docs/decisions/0002-stack-selection.md` — chosen stack + one-line why each + rejected alternatives + the headroom rationale. This is the "why" a human or future agent reads.

## Format priority
YAML/JSON for anything an agent executes. Markdown only for the ADR and the kernel. A number or status that an agent acts on lives in a spec file, never in prose (FM-05/FM-12).

## Self-healing fields (per workflow spec)
Every wave declares `self_heal` rules so the runner recovers without a human:
`on_acceptance_fail → revise_brief` · `on_flaky → quarantine_and_fix` · `on_stale_process → kill_and_restart` (FM-02) · `on_drift → regenerate_from_source` (FM-01/FM-12) · `on_context_full → handoff_and_clear` (FM-04).
