import json
from pathlib import Path


class Memory:
    def __init__(self):

        self.memory_file = Path("memory.json")

        self.data = {
            "profile": {},
            "preferences": {},
            "conversations": [],
            "events": [],
            "system": {},
        }

        self.load()

    def load(self):

        if self.memory_file.exists():
            with open(self.memory_file, "r") as file:
                self.data = json.load(file)

        else:
            self.save()

    def save(self):

        with open(self.memory_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def remember(self, key, value):

        self.data["system"][key] = value

        self.save()

    def remember_event(self, plugin, action, result):

        event = {"plugin": plugin, "action": action, "result": result}

        self.data["events"].append(event)

        self.save()

    def remember_preference(self, key, value):

        self.data["preferences"][key] = value

        self.save()

    def remember_conversation(self, role, content):

        conversation = {"role": role, "content": content}

        self.data["conversations"].append(conversation)

        self.save()

    def recall(self, key):

        return self.data["system"].get(key)

    def all(self):

        return self.data
