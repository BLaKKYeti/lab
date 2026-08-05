class IntentRegistry:


    def __init__(self):

        self.intents = []



    def register(self, keywords, plugin, action):

        self.intents.append(
            {
                "keywords": keywords,
                "plugin": plugin,
                "action": action
            }
        )



    def find(self, command):

        command = command.lower()


        for intent in self.intents:

            for keyword in intent["keywords"]:

                if keyword in command:

                    return {
                        "plugin": intent["plugin"],
                        "action": intent["action"],
                        "confidence": 0.95
                    }


        return {
            "plugin": None,
            "action": None,
            "confidence": 0.0
        }