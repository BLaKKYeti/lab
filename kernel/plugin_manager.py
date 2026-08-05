import importlib


class PluginManager:

    def __init__(self):
        self.plugins = {}

    def register(self, name, plugin):
        self.plugins[name] = plugin

    def load_builtin_plugins(self):

        filesystem = importlib.import_module(
            "plugins.filesystem"
        )

        plugin = filesystem.FilesystemPlugin()

        self.register(
            "filesystem",
            plugin
        )

    def list_plugins(self):
        return list(self.plugins.keys())