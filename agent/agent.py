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

    def start(self):

        self.runtime.start()

    def process(self, user_input):

        intent = self.intent_engine.resolve(user_input)

        plan = self.planner.create_plan(intent)

        tasks = self.command_engine.execute_plan(plan)

        if not tasks:
            return "No plan created"

        return self.runtime.execute(tasks[0])

    def run(self):

        while True:
            user_input = input("\nUSER: ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("\nAXIS shutting down.")

                break

            result = self.process(user_input)

            self.runtime.memory.remember_conversation(user_input, result)

            print("\nAXIS:")
            print(result)

        print("\nMemory saved.")
