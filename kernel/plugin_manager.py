import importlib
import inspect


class PluginManager:


    def __init__(self):

        self.plugins = {}



    def register(self, name, plugin):

        self.plugins[name] = plugin



    def load_builtin_plugins(self):

        plugin_modules = [

            "plugins.filesystem.plugin",
            "plugins.time.plugin"

        ]


        for module_name in plugin_modules:

            module = importlib.import_module(
                module_name
            )


            for attribute in dir(module):

                obj = getattr(
                    module,
                    attribute
                )


                if (
                    isinstance(obj, type)
                    and not inspect.isabstract(obj)
                    and obj.__name__.endswith("Plugin")
                    and obj.__name__ != "Plugin"
                ):

                    plugin = obj()


                    self.register(
                        plugin.name(),
                        plugin
                    )



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

                "description":
                    plugin.description(),

                "actions":
                    plugin.actions()

            }


        return capabilities