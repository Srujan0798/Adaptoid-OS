"""Claw Bridge — framework adapters for Adaptoid OS."""
from .base import FrameworkAdapter
from .langgraph_adapter import LangGraphAdapter
from .crewai_adapter import CrewAIAdapter
from .autogen_adapter import AutoGenAdapter

__all__ = ["FrameworkAdapter", "LangGraphAdapter", "CrewAIAdapter", "AutoGenAdapter"]
