from core.task import Task
from kernel.memory import Memory
from kernel.plugin_manager import PluginManager


class Runtime:
    def __init__(self):

        self.plugin_manager = PluginManager()

        self.memory = Memory()

    def start(self):

        self.plugin_manager.discover_plugins()

        print("LAB AI OS online")

        print("Plugins:", self.plugin_manager.list_plugins())

        print("\nCAPABILITIES:")

        print(self.plugin_manager.get_capabilities())

    def handle_task(self, task):
        return self.execute(task)

    def execute(self, task):

        if isinstance(task, Task):
            plugin_name = task.plugin
            action = task.action
        elif isinstance(task, dict):
            plugin_name = task.get("plugin")
            action = task.get("action")
        else:
            plugin_name = task
            action = None

        if plugin_name is None:
            return "No plugin selected"

        plugin = self.plugin_manager.get(plugin_name)

        if plugin is None:
            return f"Plugin '{plugin_name}' not found"

        try:
            result = plugin.execute(action)

            self.memory.remember("last_plugin", plugin_name)

            self.memory.remember("last_action", action)

            self.memory.remember("last_result", result)

            self.memory.remember_event(plugin_name, action, result)

            return result

        except ValueError as e:
            return str(e)
