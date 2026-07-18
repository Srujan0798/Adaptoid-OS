# Archetype — agent-product

> The product **is** an agent, tool-using system, MCP server, or multi-agent app — not a classic CRUD SaaS with a chat box bolted on.

## Signals
agent, multi-agent, tool-use, MCP server, coding agent, agentic, function calling, subagent, autonomous agent

## Default tier
T2 (production-minded). Hackathon demos of agents → force T0/T1.

## Emphasize
- Intent lock + eval/acceptance for agent behavior (not only unit tests)
- Blast-radius + OAP for tools (FM-18, FM-20)
- Cost/token ceiling (FM-19)
- HANDOFF + evidence; single orchestrator default
- Progressive disclosure (skills over mega-prompts)
- Sandbox / permissions for tool execution

## Skip by default
- Full CrewAI/LangGraph "framework as OS" unless the brief requires it
- Multi-agent crews for greenfield scaffolding
- Vector memory theater when file HANDOFF + skills suffice

## Stack hints
- Language: Python (or brief)
- Tools: host-native tools + minimal MCP allowlist
- Skills: intent-lock, verify-before-done, blast-radius-check, handoff-rewrite
- Evals: golden tasks under `evals/` when tier ≥ T1

## Failure modes
FM-09 false status · FM-13 parallel collisions · FM-18 unauthorized tool · FM-19 cost runaway · FM-20 MCP/tool trust

## Definition of done
- Agent path completes a golden task with evidence
- Tool policy allowlist present; high blast-radius actions gated
- Preflight green; HANDOFF rewritable for cold start
