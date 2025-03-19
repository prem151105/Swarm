# protocols/task_routing.py
from typing import List, Dict

class TaskRouter:
    def __init__(self, agent_roles: Dict[str, str]):
        """Initialize the task router with a mapping of agent names to roles."""
        self.agent_roles = agent_roles  # e.g., {"Researcher": "research", "Planner": "planning"}

    def assign_task(self, task: dict) -> str:
        """Assign a task to an agent based on the task type."""
        task_type = task.get("type")
        for agent, role in self.agent_roles.items():
            if role == task_type:
                return agent
        return "Coordinator"  # Default to Coordinator if no match

    def get_agents_by_role(self, role: str) -> List[str]:
        """Return a list of agents with a specific role."""
        return [agent for agent, agent_role in self.agent_roles.items() if agent_role == role]