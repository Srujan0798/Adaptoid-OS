# Pattern: LLM-as-OS

## Source
Andrej Karpathy (Sept 2023), refined by 2026 harness engineering consensus.

## Context
When designing agent architecture, teams treat the LLM as an application layer. This causes harness neglect.

## Pattern
Treat the LLM as the **CPU**, the context window as **RAM**, tools as **I/O devices**, and the Adaptoid harness as the **kernel**.

## Recipe
1. Design the harness first (verification, memory, routing, observability).
2. Slot the LLM in as a swappable compute unit.
3. Optimize the harness before requesting a bigger model.

## Anti-patterns
- "We need GPT-5" before exhausting harness improvements.
- Hard-coding model-specific prompts without abstraction layers.

## Headroom
Stanford/MIT Meta-Harness: +4.7pp on IMO math through harness changes alone.
