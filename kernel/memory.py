import json
from pathlib import Path


class Memory:

    def __init__(self):

        self.memory_file = Path("memory.json")

        self.data = {}

        self.load()


    def load(self):

        if self.memory_file.exists():

            with open(self.memory_file, "r") as file:

                self.data = json.load(file)

        else:

            self.data = {}



    def save(self):

        with open(self.memory_file, "w") as file:

            json.dump(
                self.data,
                file,
                indent=4
            )



    def remember(self, key, value):

        self.data[key] = value

        self.save()



    def recall(self, key):

        return self.data.get(key)



    def all(self):

        return self.data