class IntentAnalyzer:


    def analyze(self, command):

        command = command.lower()


        if "pdf" in command or "pdfs" in command:

            return {
                "intent": "search_files",
                "plugin": "filesystem",
                "action": "list_pdfs"
            }


        return {
            "intent": "unknown",
            "plugin": None,
            "action": None
        }