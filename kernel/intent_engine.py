from capabilities.registry import CapabilityRegistry
from kernel.intent_registry import IntentRegistry


class IntentEngine:
    def __init__(self, capability_registry=None):
        self.registry = IntentRegistry()
        self.capability_registry = (
            capability_registry
            if capability_registry is not None
            else CapabilityRegistry()
        )
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
            [
                "pdf",
                "pdfs",
                "document",
                "documents",
                "file",
                "files",
            ],
            "filesystem",
            "list_pdfs",
        )

        # Time intents
        self.registry.register(
            [
                "time",
                "clock",
                "current time",
                "what time",
            ],
            "time",
            "current_time",
        )

        # Date intents
        self.registry.register(
            [
                "date",
                "today",
                "current date",
                "what day",
            ],
            "time",
            "current_date",
        )

    def _resolve_from_capabilities(self, command):
        """
        Resolve capabilities that can be identified from the user's command.

        Returns all discovered capability matches rather than stopping at
        the first match.
        """
        command = command.lower()

        matches = []

        for capability in self.capability_registry.list_capabilities():
            name = capability.name.lower()
            action = capability.action.lower()
            description = capability.description.lower()

            match_position = None

            # Match complete capability name.
            position = command.find(name)

            if position >= 0:
                match_position = position

            # Match action words.
            action_words = action.replace("_", " ").split()

            if action_words and all(word in command for word in action_words):
                positions = [
                    command.find(word)
                    for word in action_words
                    if command.find(word) >= 0
                ]

                if positions:
                    action_position = min(positions)

                    if match_position is None or action_position < match_position:
                        match_position = action_position

            # Match meaningful description words.
            description_words = [
                word.strip(".,!?")
                for word in description.split()
                if len(word.strip(".,!?")) > 3
            ]

            if description_words:
                matching_words = [word for word in description_words if word in command]

                if len(matching_words) >= min(2, len(description_words)):
                    positions = [
                        command.find(word)
                        for word in matching_words
                        if command.find(word) >= 0
                    ]

                    if positions:
                        description_position = min(positions)

                        if (
                            match_position is None
                            or description_position < match_position
                        ):
                            match_position = description_position

            if match_position is not None:
                matches.append((match_position, capability))

        return matches

    def _resolve_from_registered_intents(self, command):
        """
        Resolve commands using the registered intent aliases.
        """
        command = command.lower()

        matches = []

        for intent in self.registry.intents:
            for keyword in intent["keywords"]:
                position = command.find(keyword)

                if position >= 0:
                    matches.append(
                        (
                            position,
                            {
                                "plugin": intent["plugin"],
                                "action": intent["action"],
                            },
                        )
                    )
                    break

        return matches

    def resolve(self, command):
        command = command.lower()

        all_matches = []

        # Gather discovered capability matches.
        capability_matches = self._resolve_from_capabilities(command)

        for position, capability in capability_matches:
            all_matches.append(
                (
                    position,
                    {
                        "plugin": capability.plugin,
                        "action": capability.action,
                    },
                )
            )

        # Gather registered intent matches.
        intent_matches = self._resolve_from_registered_intents(command)

        for position, step in intent_matches:
            all_matches.append((position, step))

        # Remove duplicate plugin/action matches while preserving the earliest
        # position in the user's command.
        unique_matches = {}

        for position, step in all_matches:
            key = (step["plugin"], step["action"])

            if key not in unique_matches:
                unique_matches[key] = (position, step)
            else:
                existing_position, _ = unique_matches[key]

                if position < existing_position:
                    unique_matches[key] = (position, step)

        # Order matches according to where they appeared in the user's command.
        ordered_matches = sorted(
            unique_matches.values(),
            key=lambda item: item[0],
        )

        if len(ordered_matches) > 1:
            return {
                "steps": [step for _, step in ordered_matches],
                "confidence": 0.95,
            }

        if len(ordered_matches) == 1:
            step = ordered_matches[0][1]

            return {
                "plugin": step["plugin"],
                "action": step["action"],
                "confidence": 0.95,
            }

        return {
            "plugin": None,
            "action": None,
            "confidence": 0.0,
        }

    def analyze(self, command):
        return self.resolve(command)
