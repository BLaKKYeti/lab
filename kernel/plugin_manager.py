from kernel.plugin_registry import PluginRegistry
from kernel.plugin_loader import PluginLoader



class PluginManager:


    def __init__(self):

        self.registry = PluginRegistry()

        self.loader = PluginLoader()



    def load_builtin_plugins(self):

        plugins = self.loader.discover()


        for plugin in plugins:

            self.register(plugin)



    def register(self, plugin):

        self.registry.register(plugin)



    def get(self, name):

        return self.registry.get(name)



    def list_plugins(self):

        return self.registry.list_plugins()