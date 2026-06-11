# Claw Bridge — Framework Adapters

Claw Bridge lets Adaptoid OS import/export workflows, skills, and context to/from the major agentic frameworks without making the core dependent on any of them.

## Philosophy

- **Core is sovereign.** Adaptoid OS kernel, failure modes, validators, and orchestrator run with zero external frameworks.
- **Bridges are opt-in.** Use them only when you need a framework's runtime (e.g., LangGraph checkpoints) or want to migrate an existing workflow into Adaptoid OS.
- **Thin translators, not rewrites.** Each adapter maps concepts 1:1, then gets out of the way.

## Adapter contract

Every adapter exposes:

```python
adapter.import_plan(framework_artifact) -> dict   # F artifact -> Adaptoid plan YAML
adapter.export_plan(adaptoid_plan) -> any         # Adaptoid plan -> F-runnable
adapter.import_skill(skill_artifact) -> dict      # F skill/tool -> SKILL.md frontmatter
adapter.export_skill(skill_doc) -> any            # SKILL.md -> F skill/tool
```

## Available adapters

| Adapter | Framework | Best for |
|---|---|---|
| `langgraph_adapter.py` | LangGraph | durable/resumable graphs, checkpoints, human-in-the-loop |
| `crewai_adapter.py` | CrewAI | role-based crews, simple multi-agent tasks |
| `autogen_adapter.py` | AutoGen | conversational multi-agent, group chat, debate |

## Usage

```python
from claw_bridge.langgraph_adapter import LangGraphAdapter

plan = LangGraphAdapter().import_plan("./my_graph.py")
# plan is a dict matching templates/root/adaptoid.config.yaml structure
```

## When to bridge

- Need durable production graphs → **export to LangGraph**
- Need role debate for a hard decision → **import from AutoGen/CrewAI**
- Otherwise → stay in the independent core.

See `reference/ecosystem/compatibility-adapters.md` for the full architecture decision.
