class PluginRegistry:


    def __init__(self):

        self.plugins = {}



    def register(self, plugin):

        self.plugins[plugin.name()] = plugin



    def get(self, name):

        return self.plugins.get(name)



    def list_plugins(self):

        return list(self.plugins.keys())



    def describe(self):

        return {
            name: {
                "description": plugin.description(),
                "actions": plugin.actions()
            }
            for name, plugin in self.plugins.items()
        }