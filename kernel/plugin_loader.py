from kernel.plugin_manager import PluginManager


class PluginLoader:
    def __init__(self, manager=None):
        self.manager = manager or PluginManager()

    def discover(self):
        self.manager.discover_plugins()
        return list(self.manager.plugins.values())
