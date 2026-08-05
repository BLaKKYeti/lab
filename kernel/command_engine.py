from kernel.tasks import TASKS


class CommandEngine:

    def __init__(self, runtime):
        self.runtime = runtime


    def interpret(self, command):

        command = command.lower()


        for name, task in TASKS.items():

            keywords = name.split()

            if all(word in command for word in keywords):

                return self.runtime.execute(
                    task["plugin"],
                    task["action"]
                )


        return "I do not understand that command yet."