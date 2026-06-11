#!/usr/bin/env python3
"""Smoke tests for Claw Bridge adapters."""
import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from claw_bridge import LangGraphAdapter, CrewAIAdapter, AutoGenAdapter


def test_langgraph_roundtrip():
    adapter = LangGraphAdapter()
    plan = adapter.import_plan({
        "nodes": [{"name": "research"}, {"name": "summarize"}],
        "edges": [("research", "summarize")],
    })
    assert "waves" in plan
    assert len(plan["waves"]) == 2
    exported = adapter.export_plan(plan)
    assert "StateGraph" in exported
    print("OK langgraph roundtrip")


def test_crewai_roundtrip():
    adapter = CrewAIAdapter()
    plan = adapter.import_plan({
        "agents": [{"name": "researcher", "role": "researcher", "goal": "find facts"}],
        "tasks": [{"name": "task1", "agent": "researcher", "description": "Research."}],
    })
    assert plan["framework"] == "crewai"
    exported = adapter.export_plan(plan)
    assert "Crew" in exported
    print("OK crewai roundtrip")


def test_autogen_roundtrip():
    adapter = AutoGenAdapter()
    plan = adapter.import_plan({
        "agents": [
            {"name": "assistant", "system_message": "You are a helpful assistant."},
            {"name": "critic", "system_message": "You are a rigorous critic."},
        ]
    })
    assert plan["framework"] == "autogen"
    exported = adapter.export_plan(plan)
    assert "GroupChat" in exported
    print("OK autogen roundtrip")


if __name__ == "__main__":
    test_langgraph_roundtrip()
    test_crewai_roundtrip()
    test_autogen_roundtrip()
    print("All claw-bridge tests passed.")
