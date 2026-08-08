from typing import Any, Dict, Optional, Union

from core.task import Task
from interfaces.plugin import Plugin
from kernel.memory import Memory
from kernel.plugin_manager import PluginManager


class Runtime:
    """Runtime orchestrator responsible for plugin execution and memory persistence."""

    def __init__(self) -> None:
        """Initialize runtime components."""
        self.plugin_manager = PluginManager()
        self.memory = Memory()

    def start(self) -> None:
        """Start the runtime and discover available plugins."""
        self.plugin_manager.discover_plugins()

        print("AXIS online")
        print("Plugins:", self.plugin_manager.list_plugins())
        print("\nCAPABILITIES:")
        print(self.plugin_manager.get_capabilities())

    def handle_task(self, task: Union[Task, Dict[str, Any], str]) -> Any:
        """Execute a task through the runtime."""
        return self.execute(task)

    def execute(self, task: Union[Task, Dict[str, Any], str]) -> Any:
        """Execute a plugin task and persist execution metadata."""

        if isinstance(task, Task):
            plugin_name = task.plugin
            action = task.action
            task_input = task.input

        elif isinstance(task, dict):
            plugin_name = task.get("plugin")
            action = task.get("action")
            task_input = task.get("input")

        else:
            plugin_name = task
            action = None
            task_input = None

        if plugin_name is None:
            return "No plugin selected"

        plugin: Optional[Plugin] = self.plugin_manager.get(plugin_name)

        if plugin is None:
            return f"Plugin '{plugin_name}' not found"

        try:
            result = plugin.execute(action, task_input)

            self.memory.remember("last_plugin", plugin_name)
            self.memory.remember("last_action", action)
            self.memory.remember("last_result", result)
            self.memory.remember_event(
                plugin_name,
                action,
                result,
            )

            return result

        except ValueError as e:
            return str(e)
