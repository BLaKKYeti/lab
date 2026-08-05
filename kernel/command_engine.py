from kernel.intent_engine import IntentEngine



class CommandEngine:


    def __init__(self, runtime):

        self.runtime = runtime
        self.intent_engine = IntentEngine()



    def interpret(self, command):

        intent = self.intent_engine.analyze(command)


        if intent is None:

            return "I do not understand that command yet."


        return self.runtime.execute(
            intent["plugin"],
            intent["action"]
        )