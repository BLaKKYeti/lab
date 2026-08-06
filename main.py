from kernel.command_engine import CommandEngine
from kernel.intent_engine import IntentEngine
from kernel.runtime import Runtime

runtime = Runtime()


runtime.start()


print("\nCAPABILITIES:")
print(runtime.plugin_manager.get_capabilities())


intent_engine = IntentEngine()
command_engine = CommandEngine(runtime=runtime, intent_engine=intent_engine)

resolved_intent = intent_engine.resolve("Find all PDFs on my computer")
routed_task = command_engine.route(resolved_intent)
result = runtime.execute(routed_task)


print("\nRESULT:")
print(result)


print("\nMEMORY:")
print(runtime.memory.all())
