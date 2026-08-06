from kernel.command_engine import CommandEngine
from kernel.intent_engine import IntentEngine


class CommandProcessor:
    def __init__(self):
        self.intent_engine = IntentEngine()
        self.command_engine = CommandEngine(
            runtime=None, intent_engine=self.intent_engine
        )

    def interpret(self, command: str):
        return self.command_engine.interpret(command)
