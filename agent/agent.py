from execution.executor import Executor
from kernel.command_engine import CommandEngine
from kernel.intent_engine import IntentEngine
from kernel.runtime import Runtime
from planner.planner import Planner


class Agent:
    def __init__(self):

        self.runtime = Runtime()
        self.intent_engine = IntentEngine()
        self.planner = Planner()
        self.command_engine = CommandEngine()

        self.executor = Executor(self.runtime)

    def start(self):

        self.runtime.start()

    def process(self, user_input):

        intent = self.intent_engine.resolve(user_input)

        plan = self.planner.create_plan(intent)

        if not plan.steps:
            return "No plan created"

        results = self.executor.execute_plan(plan)

        return results

    def run(self):

        while True:
            user_input = input("\nUSER: ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("\nAXIS shutting down.")

                break

            result = self.process(user_input)

            memory_result = result

            if isinstance(result, list):
                memory_result = [
                    {
                        "plugin": item.plugin,
                        "action": item.action,
                        "success": item.success,
                        "output": item.output,
                    }
                    for item in result
                ]

            self.runtime.memory.remember_conversation(user_input, memory_result)

            print("\nAXIS:")

            if isinstance(result, list):
                for item in result:
                    print(item.output)

            else:
                print(result)

        print("\nMemory saved.")
