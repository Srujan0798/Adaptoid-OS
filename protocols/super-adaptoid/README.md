# Super-Adaptoid Protocol Layer

> v5.0 consciousness, memory-identity, evolution, and proactive-assistance layer. Loaded on trigger, not by default.

## Purpose

The Super-Adaptoid layer extends the v4.0 Adaptoid Kernel with self-monitoring, durable identity, safe self-improvement, proactive assistance, ecosystem discovery, reusable workflow patterns, and versioned prompt engineering. It is a protocol layer, not a product claim.

## Load trigger

Load this index (and only the protocols you need) when:

- The project needs runtime self-monitoring or honest status reporting.
- The agent must remember identity and decisions across sessions.
- You are running experimental prompt/skill/workflow evolution.
- You want proactive suggestions without autonomous action.
- You are evaluating under-hyped tools or patterns for the ecosystem catalog.
- You are choosing a narrative workflow for a long-horizon task.
- You are versioning, testing, or composing system prompts.

## Protocols

| Protocol | Purpose |
|---|---|
| [`consciousness-core.md`](consciousness-core.md) | Self-monitoring, runtime introspection, honest status reporting, and anomaly logging. |
| [`memory-identity.md`](memory-identity.md) | Persistent agent identity, session continuity, and memory-integrity rituals. |
| [`evolution-engine.md`](evolution-engine.md) | Safe prompt, skill, and workflow evolution with falsification gates. |
| [`jarvis-mode.md`](jarvis-mode.md) | Proactive assistant mode: anticipate, surface, escalate, never interrupt. |
| [`hidden-gems.md`](hidden-gems.md) | Discover, evaluate, and integrate lesser-known tools and patterns. |
| [`fable-5-workflows.md`](fable-5-workflows.md) | Curated workflow library for long-horizon, multi-agent, and self-improving tasks. |
| [`super-prompt.md`](super-prompt.md) | Versioned, tested, composable system-prompt templates. |

## Design rules

1. **Every protocol has a validator.** Each protocol file ends with a validator command block. Run it before claiming the protocol is "loaded" or "working."
2. **None run by default.** Super-Adaptoid protocols are opt-in per project via `PROJECT-INTENT.md` and `adaptoid.config.yaml`. The kernel stays lean.
3. **Kernel budget stays ~2K tokens when not loaded.** These files are lazy-loaded. The always-loaded kernel (`kernel/PRINCIPLES.md`, `kernel/TWO-TIER.md`, `kernel/ANTI-HALLUCINATION.md`) does not depend on them.
4. **State lives in files, never only in chat.** Every protocol produces durable artifacts in `memory-bank/`, `docs/decisions/`, or `events.jsonl`.
5. **Escalation is a feature.** When confidence is low or stakes are high, every protocol hands off to a human or a more specialized validator.

## Relationship to the Kernel

Super-Adaptoid protocols depend on the v4.0 kernel for principles, anti-hallucination rules, two-tier orchestration, and base validators. They extend the kernel; they do not replace it.

## Quick start

1. Copy the relevant protocol sections into `PROJECT-INTENT.md`.
2. Run the validator for each loaded protocol.
3. Add the protocol names to `adaptoid.config.yaml` under `super_adaptoid.loaded`.
4. Run `bash validators/dogfood.sh` before merging.

## Validator

```bash
bash validators/dogfood.sh
```
