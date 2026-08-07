class Step:
    def __init__(self, plugin, action):

        self.plugin = plugin
        self.action = action

    def __repr__(self):

        return f"Step(plugin={self.plugin}, action={self.action})"
