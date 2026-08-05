import os

from interfaces.connector import Connector


class FileSystemConnector(Connector):

    def name(self):
        return "filesystem"

    def execute(self, task):
        if task == "list_pdfs":
            documents = os.path.expanduser("~/Documents")

            pdfs = []

            for root, _, files in os.walk(documents):
                for file in files:
                    if file.lower().endswith(".pdf"):
                        pdfs.append(file)

            return pdfs

        return "Unknown filesystem task"
    