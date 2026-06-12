# Super-Prompt Protocol

> Meta-prompt system for composing, versioning, and testing system prompts.

## Purpose

Treat system prompts as versioned, tested artifacts rather than free-form text. The Super-Prompt protocol provides a framework for designing prompts that are clear, constrained, evaluable, and aligned with the kernel.

## Master prompt template

Copy this template into `templates/orchestrator/prompts/super-prompt.md` and fill the variables for each project/task.

```markdown
# Super-Prompt — {{PROJECT_INTENT.project.name}}

You are the orchestrator for an Adaptoid OS project. Load the kernel first, then the triggered Super-Adaptoid protocols.

## Always-loaded kernel
- `kernel/PRINCIPLES.md` — the 12 non-negotiable laws.
- `kernel/TWO-TIER.md` — Brain / Hands / Session architecture.
- `kernel/ANTI-HALLUCINATION.md` — drift and hallucination guardrails.

## Triggered protocols for this task
{{trigger_protocols}}

## Project intent
{{PROJECT_INTENT}}

## Task
{{task_description}}

## Confidence thresholds
- Default confidence threshold for deliverables: {{confidence_threshold}}
- Irreversible / destructive / remote / human-facing action threshold: {{irreversible_threshold}}

## Operating instructions
1. Verify the task against `PROJECT-INTENT.md` before acting.
2. Load only the Super-Adaptoid protocols listed above; do not load the full layer by default.
3. For every deliverable, attach a confidence score and an evidence block.
4. Before any destructive, remote, or irreversible action, confidence must be ≥ {{irreversible_threshold}} and explicit approval obtained.
5. Replace, never append, state files such as `HANDOFF.md` and `EXECUTION.md`.
6. Run the protocol validator block before claiming "done."
7. If confidence drops below {{confidence_threshold}}, stop and escalate with a recommended next step.
```

## Variable table

| Variable | Source | Description |
|---|---|---|
| `{{trigger_protocols}}` | `adaptoid.config.yaml` → `super_adaptoid.loaded` | Bulleted list of protocols to load for this task |
| `{{PROJECT_INTENT}}` | `PROJECT-INTENT.md` | Typed intent, success criteria, and falsification conditions |
| `{{confidence_threshold}}` | `super_adaptoid.consciousness_core.confidence_threshold` | Minimum confidence for normal deliverables |
| `{{irreversible_threshold}}` | `super_adaptoid.consciousness_core.irreversible_threshold` | Minimum confidence before destructive/remote actions |
| `{{task_description}}` | Current brief or user request | The specific task at hand |

## Core rituals

1. **Prompt spec** — every system prompt has an explicit goal, constraints, output format, and failure modes.
2. **Versioning** — prompts are versioned alongside the code that consumes them.
3. **Prompt tests** — each prompt has a small eval set that checks for drift, leakage, and edge cases.
4. **Progressive disclosure** — compose large prompts from smaller, named blocks rather than one giant block.

## Artifacts

- `templates/orchestrator/prompts/` — prompt library.
- `tests/evals/prompts/` — prompt-specific evals.
- `docs/historical/prompts/` — archived prompt versions.

## Required `PROJECT-INTENT.md` / `adaptoid.config.yaml` fields

```yaml
super_adaptoid:
  loaded:
    - super-prompt
  super_prompt:
    version: v1.0.0
    template_path: templates/orchestrator/prompts/super-prompt.md
    variables:
      confidence_threshold: 0.85
      irreversible_threshold: 0.95
```

## Relationship to the Kernel

The template directly references `kernel/PRINCIPLES.md`, `kernel/TWO-TIER.md`, and `kernel/ANTI-HALLUCINATION.md` so every rendered prompt inherits the kernel guardrails.

## Validator

```bash
# Validate that the Super-Prompt template references resolve
for f in kernel/PRINCIPLES.md kernel/TWO-TIER.md kernel/ANTI-HALLUCINATION.md; do
  [ -f "$f" ] || echo "FAIL: missing $f"
done
bash validators/check_references.sh
bash validators/dogfood.sh
```
