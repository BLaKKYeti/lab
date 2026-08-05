import importlib
import pkgutil
import inspect

from interfaces.plugin import Plugin


class PluginManager:

    def __init__(self):

        self.plugins = {}
        self.capabilities = {}


    def register(self, plugin):

        name = plugin.name()

        self.plugins[name] = plugin

        self.capabilities[name] = {
            "description": plugin.description(),
            "actions": plugin.actions()
        }


    def discover_plugins(self):

        package = importlib.import_module(
            "plugins"
        )


        for _, module_name, is_pkg in pkgutil.iter_modules(
            package.__path__
        ):

            if module_name.startswith("__"):
                continue


            try:

                module = importlib.import_module(
                    f"plugins.{module_name}.plugin"
                )


                for _, obj in inspect.getmembers(module):

                    if (
                        inspect.isclass(obj)
                        and issubclass(obj, Plugin)
                        and obj is not Plugin
                    ):

                        plugin = obj()

                        self.register(plugin)


            except Exception as e:

                print(
                    "Plugin load error:",
                    module_name,
                    e
                )


    def load_builtin_plugins(self):

        self.discover_plugins()


    def list_plugins(self):

        return list(
            self.plugins.keys()
        )


    def get(self, name):

        return self.plugins.get(name)


    def get_capabilities(self):

        return self.capabilities