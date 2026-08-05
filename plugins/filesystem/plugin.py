from pathlib import Path

from interfaces.plugin import Plugin



class FilesystemPlugin(Plugin):


    def __init__(self):

        self.config = {}



    def name(self) -> str:

        return "filesystem"



    def description(self) -> str:

        return "Manages local computer files"



    def actions(self) -> list:

        return [
            "list_pdfs"
        ]



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