# Super-Prompt Protocol

> Meta-prompt system for composing, versioning, and testing system prompts.

## Purpose

Treat system prompts as versioned, tested artifacts rather than free-form text. The Super-Prompt protocol provides a framework for designing prompts that are clear, constrained, and evaluable.

## Core Rituals

1. **Prompt spec** — every system prompt has an explicit goal, constraints, output format, and failure modes.
2. **Versioning** — prompts are versioned alongside the code that consumes them.
3. **Prompt tests** — each prompt has a small eval set that checks for drift, leakage, and edge cases.
4. **Progressive disclosure** — compose large prompts from smaller, named blocks rather than one giant block.

## Artifacts

- `templates/orchestrator/prompts/` — prompt library.
- `tests/evals/prompts/` — prompt-specific evals.
- `docs/historical/prompts/` — archived prompt versions.
