# Memory-Identity Protocol

> Persistent agent identity, session continuity, and memory-integrity rituals.

## Purpose

Ensure that an agentic workforce has a stable identity and durable memory across sessions, crashes, and compaction events, without bloating the active context window.

## Core Rituals

1. **Identity card** — a single source-of-truth file describing the agent's role, constraints, and escalation rules.
2. **Session handoff** — `HANDOFF.md` is replaced, not appended, at the end of every session.
3. **Memory tiers** — hot context in session, warm facts in `memory-bank/facts/`, cold lessons in `memory-bank/lessons/`.
4. **Hash-chain verification** — `VaultMMU` validates memory writes so tampered or drifted state is detected on load.

## Relationship to Kernel

Depends on `kernel/TWO-TIER.md` (Brain/Hands/Session) and `protocols/vault-mmu.md` for integrity.
