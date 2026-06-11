"""Base interface for all Claw Bridge framework adapters."""
from abc import ABC, abstractmethod
from typing import Any, Dict


class FrameworkAdapter(ABC):
    """Every framework bridge must implement this four-method contract."""

    name: str = "abstract"

    @abstractmethod
    def import_plan(self, artifact: Any) -> Dict:
        """Translate a framework-specific workflow/graph/crew into an Adaptoid plan."""

    @abstractmethod
    def export_plan(self, plan: Dict) -> Any:
        """Translate an Adaptoid plan into a framework-runnable artifact."""

    @abstractmethod
    def import_skill(self, artifact: Any) -> Dict:
        """Translate a framework-specific tool/skill into SKILL.md frontmatter."""

    @abstractmethod
    def export_skill(self, skill_doc: Dict) -> Any:
        """Translate SKILL.md frontmatter into a framework-specific tool/skill."""

    def supports(self, operation: str) -> bool:
        """Return True if this adapter implements the requested operation."""
        return hasattr(self, operation) and callable(getattr(self, operation))
