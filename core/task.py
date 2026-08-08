class Task:
    def __init__(
        self,
        intent="unknown",
        plugin=None,
        action=None,
        confidence=1.0,
        input=None,
    ):
        self.intent = intent
        self.plugin = plugin
        self.action = action
        self.confidence = confidence
        self.input = input

    def __repr__(self):
        return (
            f"Task("
            f"intent={self.intent}, "
            f"plugin={self.plugin}, "
            f"action={self.action}, "
            f"confidence={self.confidence}, "
            f"input={self.input}"
            f")"
        )
