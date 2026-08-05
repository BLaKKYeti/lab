class Task:

    def __init__(
        self,
        intent,
        plugin,
        action,
        confidence=1.0
    ):
        self.intent = intent
        self.plugin = plugin
        self.action = action
        self.confidence = confidence

    def __repr__(self):
        return (
            f"Task("
            f"intent={self.intent}, "
            f"plugin={self.plugin}, "
            f"action={self.action}, "
            f"confidence={self.confidence}"
            f")"
        )