"""Claw Bridge adapter for LangGraph.

Maps:
- LangGraph StateGraph nodes/edges  -> Adaptoid waves/tasks
- LangGraph checkpoints             -> memory-bank/events + route sentinel
- LangGraph conditional edges       -> dag_transitions in adaptoid.config.yaml
"""
import ast
from pathlib import Path
from typing import Any, Dict

from .base import FrameworkAdapter


class LangGraphAdapter(FrameworkAdapter):
    """Import/export between LangGraph StateGraph and Adaptoid OS plans."""

    name = "langgraph"

    def import_plan(self, artifact: Any) -> Dict:
        """Read a LangGraph source file and produce an Adaptoid plan dict."""
        if isinstance(artifact, dict):
            graph = artifact
        else:
            path = Path(artifact)
            source = path.read_text()
            graph = self._extract_graph(source)

        waves = []
        for node in graph.get("nodes", []):
            waves.append({
                "id": f"wave-{node['name']}",
                "name": node.get("name", "unnamed"),
                "tasks": [{"id": node["name"], "prompt": node.get("doc", "")}],
                "gate": {"type": "auto"},
            })

        return {
            "archetype": "langgraph-import",
            "tier": "T2",
            "framework": "langgraph",
            "dag_transitions": self._build_transitions(graph.get("edges", [])),
            "waves": waves,
            "memory": {"checkpoint": True, "events": "memory-bank/events/events.jsonl"},
        }

    def export_plan(self, plan: Dict) -> str:
        """Emit a minimal LangGraph StateGraph Python script."""
        lines = [
            "from langgraph.graph import StateGraph, END",
            "from typing import TypedDict",
            "",
            "class State(TypedDict):",
            "    pass",
            "",
            "builder = StateGraph(State)",
        ]
        for wave in plan.get("waves", []):
            for task in wave.get("tasks", []):
                tid = task["id"]
                lines += [
                    "",
                    f"def node_{tid}(state):",
                    f'    """{task.get("prompt", "")}"""',
                    "    return state",
                    f"builder.add_node(\"{tid}\", node_{tid})",
                ]
        edges = plan.get("dag_transitions", {})
        for src, cfg in edges.items():
            for dst in cfg.get("allowed_next", []):
                lines.append(f"builder.add_edge(\"{src}\", \"{dst}\")")
        lines += ["graph = builder.compile()", ""]
        return "\n".join(lines)

    def import_skill(self, artifact: Any) -> Dict:
        """Map a LangGraph tool declaration to SKILL.md frontmatter."""
        if isinstance(artifact, str):
            return {"name": Path(artifact).stem, "source": "langgraph"}
        return {"name": artifact.get("name", "unknown"), "source": "langgraph"}

    def export_skill(self, skill_doc: Dict) -> str:
        """Emit a LangGraph @tool decorator stub."""
        name = skill_doc.get("name", "tool")
        desc = skill_doc.get("description", "")
        return f"""from langchain_core.tools import tool

@tool
def {name}(query: str) -> str:
    \"\"\"{desc}\"\"\"
    return "result"
"""

    @staticmethod
    def _extract_graph(source: str) -> Dict:
        tree = ast.parse(source)
        nodes, edges = [], []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
                if func == "add_node":
                    nodes.append({"name": _str_arg(node.args[0]), "doc": ""})
                elif func == "add_edge":
                    edges.append((_str_arg(node.args[0]), _str_arg(node.args[1])))
        return {"nodes": nodes, "edges": edges}

    @staticmethod
    def _build_transitions(edges):
        transitions = {}
        for src, dst in edges:
            transitions.setdefault(src, {"allowed_next": []})
            transitions[src]["allowed_next"].append(dst)
        return transitions


def _str_arg(node):
    return node.value if isinstance(node, ast.Constant) else getattr(node, "id", "unknown")
