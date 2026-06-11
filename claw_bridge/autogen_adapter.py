"""Claw Bridge adapter for AutoGen.

Maps:
- AutoGen ConversableAgent     -> Adaptoid worker with system message
- AutoGen GroupChat            -> review/debate wave
- AutoGen register_function    -> skill binding
"""
from pathlib import Path
from typing import Any, Dict

from .base import FrameworkAdapter


class AutoGenAdapter(FrameworkAdapter):
    """Import/export between AutoGen agents/chats and Adaptoid OS plans."""

    name = "autogen"

    def import_plan(self, artifact: Any) -> Dict:
        if isinstance(artifact, dict):
            chat = artifact
        else:
            chat = {"agents": [{"name": "assistant"}, {"name": "critic"}], "messages": []}

        waves = [{
            "id": "wave-debate",
            "name": "Multi-agent debate",
            "mode": "groupchat",
            "tasks": [{"id": a["name"], "role": a.get("system_message", "")} for a in chat.get("agents", [])],
            "gate": {"type": "human", "reason": "resolve debate"},
        }]

        return {
            "archetype": "autogen-import",
            "tier": "T2",
            "framework": "autogen",
            "waves": waves,
        }

    def export_plan(self, plan: Dict) -> str:
        """Emit a minimal AutoGen group chat script."""
        lines = [
            "from autogen import ConversableAgent, GroupChat, GroupChatManager",
            "",
        ]
        for wave in plan.get("waves", []):
            for task in wave.get("tasks", []):
                name = task["id"]
                sys_msg = task.get("role", f"You are {name}.")
                lines += [
                    f"{name} = ConversableAgent(",
                    f'    name="{name}",',
                    f'    system_message="{sys_msg}",',
                    '    llm_config={"config_list": [{"model": "gpt-4o", "api_key": "<YOUR_KEY>"}]},',
                    ")",
                    "",
                ]
        agent_names = [t["id"] for w in plan.get("waves", []) for t in w.get("tasks", [])]
        lines += [
            "group_chat = GroupChat(",
            f"    agents=[{', '.join(agent_names)}],",
            '    messages=[],',
            '    max_round=5,',
            ")",
            "manager = GroupChatManager(groupchat=group_chat)",
            f"{agent_names[0]}.initiate_chat(manager, message=\"Start the discussion.\")",
        ]
        return "\n".join(lines)

    def import_skill(self, artifact: Any) -> Dict:
        if isinstance(artifact, str):
            return {"name": Path(artifact).stem, "source": "autogen"}
        return {"name": artifact.get("name", "unknown"), "source": "autogen"}

    def export_skill(self, skill_doc: Dict) -> str:
        name = skill_doc.get("name", "tool")
        desc = skill_doc.get("description", "")
        return f"""def {name}(query: str) -> str:
    \"\"\"{desc}\"\"\"
    return "result"

# Bind with: assistant.register_for_llm(name="{name}", description="{desc}")({name})
"""
