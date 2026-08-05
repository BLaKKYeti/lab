from kernel.plugin_manager import PluginManager
from kernel.memory import Memory



class Runtime:


    def __init__(self):

        self.plugin_manager = PluginManager()

        self.memory = Memory()



    def start(self):

        self.plugin_manager.load_builtin_plugins()

        print("LAB AI OS online")

        print(
            "Plugins:",
            self.plugin_manager.list_plugins()
        )



    def execute(self, plugin_name, action):

        plugin = self.plugin_manager.get(plugin_name)


        if plugin is None:

            return f"Plugin '{plugin_name}' not found"



        try:

            result = plugin.execute(action)


            self.memory.remember(
                "last_plugin",
                plugin_name
            )


            self.memory.remember(
                "last_action",
                action
            )


            self.memory.remember(
                "last_result",
                result
            )


            return result



        except ValueError as e:

            return str(e)