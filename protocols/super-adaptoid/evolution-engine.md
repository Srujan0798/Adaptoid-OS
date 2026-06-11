# Evolution Engine Protocol

> Experimental prompt, skill, and workflow evolution with falsification gates.

## Purpose

Make the harness self-improving by proposing, testing, and selectively adopting better prompts, skills, validators, and workflows — while preventing runaway mutation and hype.

## Core Rituals

1. **Variant generation** — produce a small, bounded set of candidate changes with a falsifiable hypothesis.
2. **Eval before merge** — every candidate must pass the existing eval suite plus a new regression test.
3. **Canary rollout** — adopt the winner in one archetype or workflow before promoting it globally.
4. **Rollback ready** — archive superseded variants to `docs/historical/` or `attic/`, never delete.

## Relationship to Existing Work

This protocol is the v5.0 continuation of `protocols/self-improvement.md` and `protocols/evolution-engine.md` in the kernel layer.

## Artifacts

- `memory-bank/decisions/` ADR for each adopted evolution.
- `tests/` regression tests for each variant.
- `docs/historical/` archive for rejected or superseded candidates.
