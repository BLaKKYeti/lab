class CommandEngine:

    def __init__(self, runtime):
        self.runtime = runtime


    def interpret(self, command):

        command = command.lower()


        if "pdf" in command or "pdfs" in command:

            return self.runtime.execute(
                "filesystem",
                "list_pdfs"
            )


        return "I do not understand that command yet."