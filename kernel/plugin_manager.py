import importlib

from kernel.plugin_registry import PluginRegistry



class PluginManager:


    def __init__(self):

        self.registry = PluginRegistry()



    def register(self, plugin):

        self.registry.register(plugin)



    def load_builtin_plugins(self):

        filesystem = importlib.import_module(
            "plugins.filesystem"
        )


        plugin = filesystem.FilesystemPlugin()


        self.register(plugin)



    def get(self, name):

        return self.registry.get(name)



    def list_plugins(self):

        return self.registry.list_plugins()