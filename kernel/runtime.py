from kernel.plugin_manager import PluginManager


class Runtime:

    def __init__(self):
        self.plugin_manager = PluginManager()

    def start(self):

        self.plugin_manager.load_builtin_plugins()

        print("LAB AI OS online")
        print(
            "Plugins:",
            self.plugin_manager.list_plugins()
        )

    def execute(self, plugin_name, action):

        plugin = self.plugin_manager.plugins.get(plugin_name)

        if plugin is None:
            return f"Plugin '{plugin_name}' not found"

        try:
            return plugin.execute(action)

        except ValueError as e:
            return str(e)