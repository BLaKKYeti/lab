from execution.executor import Executor
from kernel.command_engine import CommandEngine
from kernel.intent_engine import IntentEngine
from kernel.runtime import Runtime
from planner.planner import Planner
from response.builder import ResponseBuilder


class Agent:
    def __init__(self):
        self.runtime = Runtime()
        self.intent_engine = IntentEngine()
        self.planner = Planner()
        self.command_engine = CommandEngine()

        self.executor = Executor(self.runtime)
        self.response_builder = ResponseBuilder()

        self.execution_context = None

    def start(self):
        self.runtime.start()

    def process(self, user_input):
        intent = self.intent_engine.resolve(user_input)

        plan = self.planner.create_plan(intent)

        if not plan.steps:
            self.execution_context = None
            return "No plan created."

        results = self.executor.execute_plan(plan)

        self.execution_context = self.executor.context

        response = self.response_builder.build(results)

        return response

    def run(self):
        while True:
            user_input = input("\nUSER: ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("\nAXIS shutting down.")
                break

            response = self.process(user_input)

            self.runtime.memory.remember_conversation(
                user_input,
                response,
            )

            print("\nAXIS:")
            print(response)

        print("\nMemory saved.")
