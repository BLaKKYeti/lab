from pathlib import Path

from interfaces.plugin import Plugin


class FilesystemPlugin(Plugin):

    def __init__(self):
        self.config = {}

        self.metadata = {
            "name": "filesystem",
            "version": "1.0",
            "description": "Filesystem management plugin",
            "capabilities": [
                "list_pdfs"
            ]
        }


    def name(self) -> str:
        return self.metadata["name"]


    def description(self) -> str:
        return self.metadata["description"]


    def actions(self) -> list:
        return self.metadata["capabilities"]


    def initialize(self, config: dict):
        self.config = config


    def execute(self, task):

        if task == "list_pdfs":

            documents = Path.home() / "Documents"

            if not documents.exists():
                return []

            return [
                str(file)
                for file in documents.rglob("*.pdf")
            ]


        raise ValueError(
            f"Unsupported filesystem task: {task}"
        )


    def shutdown(self):
        pass