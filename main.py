from kernel.runtime import Runtime
from kernel.command_engine import CommandEngine


os = Runtime()


os.start()


assistant = CommandEngine(os)


result = assistant.interpret(
    "Find all PDFs on my computer"
)


print("RESULT:")
print(result)


print("\nMEMORY:")
print(os.memory.all())