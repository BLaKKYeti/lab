import importlib
import pkgutil


class PluginLoader:


    def discover(self):

        plugins = []


        package = importlib.import_module(
            "plugins"
        )


        for _, module_name, _ in pkgutil.iter_modules(
            package.__path__
        ):

            module = importlib.import_module(
                f"plugins.{module_name}"
            )


            for attribute in dir(module):

                obj = getattr(
                    module,
                    attribute
                )


                if (
                    isinstance(obj, type)
                    and obj.__name__.endswith("Plugin")
                ):

                    plugins.append(
                        obj()
                    )


        return plugins