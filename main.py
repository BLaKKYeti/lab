from kernel.runtime import Runtime
from intelligence.command_processor import CommandProcessor


os = Runtime()

os.start()


brain = CommandProcessor()


command = "find my pdf files"


task = brain.interpret(command)


print("\nTASK GENERATED:")
print(task)


if task.plugin is not None:

    result = os.execute(
        task.plugin,
        task.action
    )

    print("\nLAB RESPONSE:")
    print(result)

else:

    print("\nLAB RESPONSE:")
    print("I do not understand that command yet.")