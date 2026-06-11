# Jarvis Mode Protocol

> Proactive assistant mode: anticipate, surface, escalate, never interrupt.

## Purpose

Give Adaptoid OS a proactive-but-restrained assistant mode that surfaces the right information at the right time, asks permission before acting, and escalates when confidence is low.

## Core Rituals

1. **Anticipate** — predict the next likely task from context and recent history.
2. **Surface** — show relevant memory, docs, or failure-mode warnings before they are asked for.
3. **Ask, don't act** — proactive mode never executes tools without explicit approval (blast-radius rule applies).
4. **Escalate** — when confidence is low or stakes are high, hand off to a human or a more specialized agent.

## Boundaries

- No autonomous remote/money/human actions.
- All proactive suggestions are logged to `events.jsonl`.
- User can disable with `adaptoid.config.yaml` setting `jarvis_mode: false`.
