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

    def run(self, task):

        if isinstance(task, Task):
            return self.runtime.execute(task)

        if isinstance(task, str):
            resolved_intent = self.intent_engine.resolve(task)
            routed_task = self.command_engine.route(resolved_intent)
            return self.runtime.execute(routed_task)

        return "I don't know how to perform that task yet"
