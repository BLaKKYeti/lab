from kernel.command_engine import CommandEngine
from kernel.intent_engine import IntentEngine
from kernel.runtime import Runtime
from planner.planner import Planner

runtime = Runtime()

runtime.start()


intent_engine = IntentEngine()

planner = Planner()

command_engine = CommandEngine(runtime=runtime, intent_engine=intent_engine)


while True:
    user_input = input("\nUSER: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    resolved_intent = intent_engine.resolve(user_input)

    execution_plan = planner.create_plan(resolved_intent)

    tasks = command_engine.execute_plan(execution_plan)

    if not tasks:
        result = "No plan created"

    else:
        result = runtime.execute(tasks[0])

    runtime.memory.remember_conversation(user_input, result)

    print("\nAXIS:")

    print(result)


print("\nMemory saved.")
