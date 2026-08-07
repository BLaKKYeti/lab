from kernel.intent_registry import IntentRegistry


class IntentEngine:
    def __init__(self):

        self.registry = IntentRegistry()

        self.load_defaults()

    def load_defaults(self):

        # Filesystem intents
        self.registry.register(
            ["pdf", "pdfs", "document", "documents", "file", "files"],
            "filesystem",
            "list_pdfs",
        )

        # Time intents
        self.registry.register(
            ["time", "clock", "current time", "what time"], "time", "current_time"
        )

        # Date intents
        self.registry.register(
            ["date", "today", "current date", "what day"], "time", "current_date"
        )

    def resolve(self, command):

        return self.registry.find(command)

    def analyze(self, command):

        return self.resolve(command)
