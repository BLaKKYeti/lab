from kernel.command_engine import CommandEngine
from kernel.intent_engine import IntentEngine
from kernel.runtime import Runtime

runtime = Runtime()

runtime.start()


print("\nCAPABILITIES:")
print(runtime.plugin_manager.get_capabilities())


intent_engine = IntentEngine()

command_engine = CommandEngine(runtime=runtime, intent_engine=intent_engine)


while True:
    user_input = input("\nUSER: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    resolved_intent = intent_engine.resolve(user_input)

    routed_task = command_engine.route(resolved_intent)

    result = runtime.execute(routed_task)

    runtime.memory.remember_conversation(user_input, result)

    print("\nJARVIS:")

    print(result)


print("\nMemory saved.")
