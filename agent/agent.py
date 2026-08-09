from capabilities.discovery import CapabilityDiscovery
from capabilities.query import CapabilityQuery
from execution.executor import Executor
from kernel.command_engine import CommandEngine
from kernel.intent_engine import IntentEngine
from kernel.runtime import Runtime
from planner.planner import Planner
from response.builder import ResponseBuilder


class Agent:
    def __init__(self):
        self.runtime = Runtime()

        self.planner = Planner()

        self.executor = Executor(self.runtime)

        self.response_builder = ResponseBuilder()

        self.execution_context = None

        self.capability_query = None

        self.intent_engine = IntentEngine()

        self.command_engine = CommandEngine(
            runtime=self.runtime,
            intent_engine=self.intent_engine,
        )

    def start(self):
        self.runtime.start()

        discovery = CapabilityDiscovery(self.runtime.plugin_manager)

        registry = discovery.discover()

        self.capability_query = CapabilityQuery(registry)

        self.intent_engine.capability_registry = registry

    def process(self, user_input):
        intent = self.intent_engine.resolve(user_input)

        if (
            intent.get("plugin") == "capabilities"
            and intent.get("action") == "describe"
        ):
            self.execution_context = None

            if self.capability_query is None:
                return "Capability discovery has not been initialized."

            return self.capability_query.describe()

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
