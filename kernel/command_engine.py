from kernel.intent import IntentAnalyzer


class CommandEngine:


    def __init__(self, runtime):

        self.runtime = runtime
        self.intent = IntentAnalyzer()



    def interpret(self, command):

        task = self.intent.analyze(command)


        if task["plugin"] is None:

            return "I do not understand that command yet."


        return self.runtime.execute(
            task["plugin"],
            task["action"]
        )