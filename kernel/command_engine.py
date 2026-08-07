from core.task import Task
from kernel.intent_engine import IntentEngine


class CommandEngine:
    def __init__(self, runtime=None, intent_engine=None):

        self.runtime = runtime
        self.intent_engine = intent_engine or IntentEngine()

    def route(self, resolved_intent):

        if not resolved_intent:
            return Task(intent="unknown", plugin=None, action=None, confidence=0.0)

        plugin = resolved_intent.get("plugin")
        action = resolved_intent.get("action")
        confidence = resolved_intent.get("confidence", 0.0)

        if plugin and action:
            return Task(
                intent="resolved", plugin=plugin, action=action, confidence=confidence
            )

        return Task(intent="unknown", plugin=None, action=None, confidence=0.0)

    def interpret(self, command):

        resolved_intent = self.intent_engine.resolve(command)

        return self.route(resolved_intent)

    def execute_plan(self, plan):

        tasks = []

        for step in plan.steps:
            tasks.append(Task(intent="planned", plugin=step.plugin, action=step.action))

        return tasks
