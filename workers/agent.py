from core.task import Task
from kernel.command_engine import CommandEngine
from kernel.intent_engine import IntentEngine


class Agent:
    def __init__(self, runtime):
        self.runtime = runtime
        self.intent_engine = IntentEngine()
        self.command_engine = CommandEngine(
            runtime=runtime, intent_engine=self.intent_engine
        )

    def process(self, user_input):
        if isinstance(user_input, Task):
            task = user_input
        elif isinstance(user_input, str):
            resolved_intent = self.intent_engine.resolve(user_input)
            task = self.command_engine.route(resolved_intent)
        else:
            return "I don't know how to perform that task yet"

        if getattr(task, "plugin", None) is None:
            return "I couldn't determine a suitable action."

        result = self.runtime.handle_task(task)
        return self.format_response(task, result)

    def run(self, user_input):
        return self.process(user_input)

    def format_response(self, task, result):
        return f"Result: {result}"
