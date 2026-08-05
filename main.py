from kernel.runtime import Runtime
from kernel.command_engine import CommandEngine


os = Runtime()


os.start()


print("\nCAPABILITIES:")
print(
    os.plugin_manager.get_capabilities()
)


assistant = CommandEngine(os)


result = assistant.interpret(
    "Find all PDFs on my computer"
)


print("\nRESULT:")
print(result)


print("\nMEMORY:")
print(os.memory.all())