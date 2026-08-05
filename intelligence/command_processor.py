from core.task import Task


class CommandProcessor:

    def __init__(self):
        pass

    def interpret(self, command: str):

        command = command.lower()

        if "pdf" in command and "find" in command:

            return Task(
                intent="search_documents",
                plugin="filesystem",
                action="list_pdfs",
                confidence=0.95
            )

        return Task(
            intent="unknown",
            plugin=None,
            action=None,
            confidence=0.0
        )