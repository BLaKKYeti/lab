class IntentEngine:


    def analyze(self, command):

        command = command.lower()


        if "pdf" in command:

            return {
                "plugin": "filesystem",
                "action": "list_pdfs",
                "confidence": 0.95
            }


        return {
            "plugin": None,
            "action": None,
            "confidence": 0.0
        }