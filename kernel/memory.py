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

            self.migrate()

        else:
            self.save()

    def migrate(self):

        if "profile" not in self.data:
            self.data["profile"] = {}

        if "preferences" not in self.data:
            self.data["preferences"] = {}

        if "conversations" not in self.data:
            self.data["conversations"] = []

        if "events" not in self.data:
            if "history" in self.data:
                self.data["events"] = self.data.pop("history")
            else:
                self.data["events"] = []

        if "system" not in self.data:
            self.data["system"] = {}

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

    def remember_conversation(self, user, response):

        conversation = {"user": user, "response": response}

        self.data["conversations"].append(conversation)

        self.save()

    def recall(self, key):

        return self.data["system"].get(key)

    def all(self):

        return self.data

    def get_conversations(self, limit: int = 10):

        conversations = self.data.get("conversations", [])
        if limit is None:
            return conversations

        return conversations[-limit:] if limit > 0 else []

    def get_events(self, limit: int = 10):

        events = self.data.get("events", [])
        if limit is None:
            return events

        return events[-limit:] if limit > 0 else []
