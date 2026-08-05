import importlib


class PluginManager:

    def __init__(self):
        self.plugins = {}


    def register(self, plugin):

        self.plugins[
            plugin.name()
        ] = plugin



    def load_builtin_plugins(self):

        filesystem = importlib.import_module(
            "plugins.filesystem.plugin"
        )

        plugin = filesystem.FilesystemPlugin()

        self.register(plugin)



    def get(self, name):

        return self.plugins.get(name)



    def list_plugins(self):

        return list(
            self.plugins.keys()
        )



    def get_capabilities(self):

        capabilities = {}

        for name, plugin in self.plugins.items():

            capabilities[name] = {
                "description": plugin.description(),
                "actions": plugin.actions()
            }


        return capabilities