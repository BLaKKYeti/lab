from kernel.intent_registry import IntentRegistry



class IntentEngine:


    def __init__(self):

        self.registry = IntentRegistry()

        self.load_defaults()



    def load_defaults(self):

        self.registry.register(
            [
                "pdf",
                "pdfs",
                "document"
            ],
            "filesystem",
            "list_pdfs"
        )



    def analyze(self, command):

        return self.registry.find(command)