# Show HN — Adaptoid OS v4.0

## Title
Show HN: Adaptoid OS — a failure-mode-first harness for agentic AI

## Link
https://github.com/Srujan0798/Adaptoid-OS

## Body
Most agentic projects fail in a small set of predictable ways: state drift, wrong tool calls, unverified "done" claims, and embarrassing artifacts.

Frameworks give you primitives. I wanted a harness that treats those failure modes as first-class citizens.

Adaptoid OS is that attempt:
- 18 documented failure modes (FM-01 → FM-18), each with a bash validator
- typed PROJECT-INTENT.md with JSON Schema
- memory bank + event sourcing
- workflow files that enforce valid wave transitions
- optional adapters for LangGraph / CrewAI / AutoGen

The core has zero framework dependencies. The adapters are opt-in.

It is rough and opinionated. Feedback from anyone shipping agentic systems would be great.

## Posting tips
- Post between 8–10 AM PT on a weekday
- Stay in the thread for the first hour
- Don't ask friends to upvote
