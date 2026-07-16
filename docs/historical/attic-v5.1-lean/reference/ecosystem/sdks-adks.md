# Ecosystem — SDKs & ADKs (when you BUILD an agent, not just code in one)

> Use these only if the project IS an agent product/runtime. If you're just building software with an agent's help, you don't need these — the coding agent is enough.

| Framework | Model | Strengths | Pick when | Source |
|---|---|---|---|---|
| **Claude Agent SDK** | Anthropic | Skills, sub-agents (Opus+Haiku), hooks, the same engine as Claude Code | building on Claude, want Claude Code's primitives in your app | platform.claude.com (corpus) |
| **OpenAI Agents SDK** | 100+ via LiteLLM | handoffs, guardrails, sessions, tracing; Sandbox Agents for long containerized tasks | OpenAI-stack, need guardrails+tracing | github.com/openai/openai-agents-python (corpus) |
| **Google ADK 2.0** | Gemini/Claude/Gemma/Ollama | ⚡ **context-as-source-code** (auto filter/summarize/lazy-load/token-track); graph workflows; multi-lang (Py/TS/Go/Java/Kotlin); one-command GCP deploy; A2A built-in; agents CLI scaffolds | enterprise, multi-language, GCP, context-discipline matters | adk.dev ⚡ |
| **LangGraph** | any | stateful, durable, graph nodes/edges; used by Klarna/Uber/JPMorgan | long-running stateful agents needing persistence | langchain (corpus) |
| **DSPy** | any | program agents as signatures+modules+optimizers; auto-tunes prompts (MIPROv2) | systems where you optimize, not hand-prompt | dspy.ai (corpus) |
| **Pydantic AI** | 20+ | type-safe, dependency injection, durable execution, "FastAPI feeling" | Python, type-safety, structured outputs | pydantic.dev/docs/ai (corpus) |
| **CrewAI / AutoGen** | any | role-based multi-agent crews / conversational multi-agent | quick multi-agent prototypes | (corpus) |

## Notable 2026 shift: ADK's "context as source code"
ADK 2.0's headline is treating context like code — automatic filtering, summarization of old turns, lazy-loading artifacts, token tracking — rather than concatenating until the window fills. This is the same principle as OS-Setup's progressive disclosure + FM-04 discipline, now baked into a framework. Worth studying even if you don't use ADK.

## Decision rule
- Building software → you DON'T need these; use a coding agent (see `coding-agents.md`).
- Building an agent that ships to users → pick by model allegiance + needs:
  - Claude → Claude Agent SDK
  - OpenAI → OpenAI Agents SDK
  - Google/enterprise/multi-lang → Google ADK
  - Stateful/durable/graph → LangGraph
  - Optimize-don't-prompt → DSPy
  - Type-safe Python → Pydantic AI
- Record the choice as an ADR with the why.

`verified: 2026-05 (ADK ⚡ this burst; rest corpus)`
