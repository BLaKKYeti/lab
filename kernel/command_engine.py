class CommandEngine:


    def __init__(self, runtime):

        self.runtime = runtime



    def interpret(self, command):

        command = command.lower()



        capabilities = (
            self.runtime
            .plugin_manager
            .get_capabilities()
        )



        for plugin, data in capabilities.items():

            for action in data["actions"]:


                keywords = action.replace(
                    "_",
                    " "
                )


                if keywords in command:

                    return self.runtime.execute(
                        plugin,
                        action
                    )



        return "No matching capability found."