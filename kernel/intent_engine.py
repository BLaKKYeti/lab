from kernel.intent_registry import IntentRegistry


class IntentEngine:
    def __init__(self):
        self.registry = IntentRegistry()
        self.load_defaults()

    def load_defaults(self):
        # Capability query intents
        self.registry.register(
            [
                "what can you do",
                "what can axis do",
                "what are your capabilities",
                "what can you help me with",
                "show me what you can do",
                "show capabilities",
            ],
            "capabilities",
            "describe",
        )

        # Filesystem intents
        self.registry.register(
            ["pdf", "pdfs", "document", "documents", "file", "files"],
            "filesystem",
            "list_pdfs",
        )

        # Time intents
        self.registry.register(
            ["time", "clock", "current time", "what time"],
            "time",
            "current_time",
        )

        # Date intents
        self.registry.register(
            ["date", "today", "current date", "what day"],
            "time",
            "current_date",
        )

    def resolve(self, command):
        command = command.lower()

        matched_steps = []

        for intent in self.registry.intents:
            for keyword in intent["keywords"]:
                if keyword in command:
                    step = {
                        "plugin": intent["plugin"],
                        "action": intent["action"],
                    }

                    if step not in matched_steps:
                        matched_steps.append(step)

                    break

        if len(matched_steps) > 1:
            return {
                "steps": matched_steps,
                "confidence": 0.95,
            }

        if len(matched_steps) == 1:
            return {
                "plugin": matched_steps[0]["plugin"],
                "action": matched_steps[0]["action"],
                "confidence": 0.95,
            }

        return {
            "plugin": None,
            "action": None,
            "confidence": 0.0,
        }

    def analyze(self, command):
        return self.resolve(command)
