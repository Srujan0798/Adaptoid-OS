# Pattern: Multi-Channel Gateway

## Source
OpenClaw / Peter Steinberger (2026).

## Context
Agents are trapped in a single IDE or chat. Users want to interact via Slack, Telegram, email, etc.

## Pattern
Single gateway process owns every channel, routes to N isolated agents, maintains per-channel context.

## Recipe
1. Define channel bindings in `multi-channel/bindings.yaml`.
2. Each channel gets an isolated agent with its own memory context.
3. Gateway enforces OAP policy packs before forwarding any request.
4. Audit trail captures cross-channel activity.

## Anti-patterns
- One agent handling all channels without isolation.
- No audit trail for cross-channel requests.
