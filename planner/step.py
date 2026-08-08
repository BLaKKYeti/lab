class Step:
    def __init__(self, plugin, action, input=None):
        self.plugin = plugin
        self.action = action
        self.input = input

    def __repr__(self):
        return f"Step(plugin={self.plugin}, action={self.action}, input={self.input})"
