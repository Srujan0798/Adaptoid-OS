# Consciousness Core Protocol

> Self-monitoring, runtime introspection, and honest status reporting.

## Purpose

Give the agent a lightweight, always-on capability to observe its own state, detect when it is uncertain, and report status honestly rather than confabulating confidence.

## Core Rituals

1. **Status honesty** — every "done" claim must cite evidence; "uncertain" is a valid status.
2. **Confidence tagging** — attach a confidence level (certain / likely / uncertain / blocked) to every deliverable.
3. **Anomaly self-reporting** — when the agent notices drift, contradiction, or missing context, it records it before proceeding.
4. **Reflection checkpoint** — at major phase boundaries, answer: what do I know, what do I assume, what could invalidate this?

## Anti-Hallucination Tie-In

This protocol extends `kernel/ANTI-HALLUCINATION.md` by making self-correction an explicit, reviewable step rather than an implicit hope.

## Artifacts

- `memory-bank/lessons/` entries for every detected anomaly.
- `validators/check_silent_failures.sh` or equivalent for runtime self-check.
