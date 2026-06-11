# Product Hunt Launch Kit — Adaptoid OS v4.0

## Product Name
Adaptoid OS

## Tagline
A failure-mode-first harness for agentic AI projects.

## Description
I kept shipping LLM demos that broke in production. State drift. Wrong tool calls. Tasks marked "done" with no proof. So I wrote down every failure mode and built a harness around them.

Adaptoid OS v4.0 gives you:
- 18 documented failure modes with dedicated validators
- typed project intent (PROJECT-INTENT.md + JSON Schema)
- memory bank + event sourcing
- wave-transition enforcement
- one-command project scaffolding
- optional bridges to LangGraph, CrewAI, and AutoGen

The core is framework-agnostic. Use the adapters only when you need them.

## Topics / Categories
- Developer Tools
- Open Source
- Artificial Intelligence
- Software Engineering

## Maker Comment
I made this because my own agentic projects kept failing in predictable ways and existing frameworks did not give me a way to catch those failures early. It is opinionated, imperfect, and open source. Feedback from people actually shipping this stuff would mean a lot.

## Screenshots needed
1. `screenshots/hero.png` — README hero section
2. `screenshots/engine-demo.png` — terminal running `adaptor/engine.py`
3. `screenshots/fm-table.png` — failure modes table
4. `screenshots/workflows.png` — workflow YAML example
5. `screenshots/validators.png` — `bash validators/dogfood.sh` passing

## First comment reply strategy
- Thank hunters
- Ask: "what failure mode hits you most often?"
- Point to `failure-modes/`

## Launch timing
- Preferred: Tuesday 00:01 PT
- Alternative: Monday 00:01 PT
- Stay active first 4 hours

## Link
https://github.com/Srujan0798/Adaptoid-OS
