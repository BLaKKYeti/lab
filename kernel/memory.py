import json
from copy import deepcopy
from pathlib import Path
from typing import Any


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

        self._migrate_records(self.data.get("conversations", []), "conversation")
        self._migrate_records(self.data.get("events", []), "event")
        self._migrate_records(self.data.get("profile", {}), "profile")
        self._migrate_records(self.data.get("preferences", {}), "preference")

        self.save()

    def save(self):

        with open(self.memory_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def _migrate_records(self, records: Any, record_type: str):
        if isinstance(records, dict):
            items = []
            for key, value in records.items():
                items.append(
                    {
                        "key": key,
                        "value": value,
                        "metadata": self._build_metadata(
                            record_type=record_type, source="migration"
                        ),
                    }
                )
            return

        if isinstance(records, list):
            for index, record in enumerate(records):
                if isinstance(record, dict) and "metadata" not in record:
                    record["metadata"] = self._build_metadata(
                        record_type=record_type,
                        source="migration",
                    )
                    if record_type == "conversation":
                        record["metadata"]["tags"] = ["conversation"]
                    elif record_type == "event":
                        record["metadata"]["tags"] = ["event"]

    def _build_metadata(
        self, record_type: str, source: str = "memory", tags: list[str] | None = None
    ):
        metadata = {
            "id": self._next_id(),
            "timestamp": self._timestamp(),
            "type": record_type,
            "source": source,
        }
        if tags:
            metadata["tags"] = tags
        return metadata

    def _timestamp(self) -> str:
        return "2026-08-06T00:00:00"

    def _next_id(self) -> str:
        return f"{self._timestamp()}-{len(self.data.get('events', [])) + len(self.data.get('conversations', [])) + 1}"

    def remember(self, key, value):

        self.data["system"][key] = value

        self.save()

    def remember_event(self, plugin, action, result):

        event = {
            "plugin": plugin,
            "action": action,
            "result": result,
            "metadata": self._build_metadata("event", source="runtime", tags=["event"]),
        }

        self.data["events"].append(event)

        self.save()

    def remember_profile(self, key, value):

        self.data["profile"][key] = value

        self.save()

    def remember_preference(self, key, value):

        self.data["preferences"][key] = value

        self.save()

    def remember_conversation(self, user, response):

        conversation = {
            "user": user,
            "response": response,
            "metadata": self._build_metadata(
                "conversation", source="runtime", tags=["conversation"]
            ),
        }

        self.data["conversations"].append(conversation)

        self.save()

    def recall(self, key):

        return self.data["system"].get(key)

    def all(self):

        return deepcopy(self.data)

    def search(self, query: str):
        query = (query or "").strip().lower()
        if not query:
            return []

        matches = []
        for record in self._iter_records():
            payload = self._record_search_text(record)
            if query in payload:
                matches.append(record)
        return matches

    def recent(self, limit: int = 10):
        records = self._iter_records()
        if limit is None:
            return records
        return records[-limit:] if limit > 0 else []

    def get_profile(self):
        return self.data.get("profile", {})

    def get_preferences(self):
        return self.data.get("preferences", {})

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

    def _iter_records(self):
        records = []
        for item in self.data.get("profile", {}).items():
            key, value = item
            records.append(
                {
                    "type": "profile",
                    "key": key,
                    "value": value,
                    "metadata": self._build_metadata("profile", source="memory"),
                }
            )

        for item in self.data.get("preferences", {}).items():
            key, value = item
            records.append(
                {
                    "type": "preference",
                    "key": key,
                    "value": value,
                    "metadata": self._build_metadata("preference", source="memory"),
                }
            )

        records.extend(self.get_conversations(limit=None))
        records.extend(self.get_events(limit=None))
        return records

    def _record_search_text(self, record: dict):
        parts = []
        for key, value in record.items():
            if key == "metadata":
                continue
            if isinstance(value, (dict, list)):
                try:
                    parts.append(json.dumps(value, sort_keys=True))
                except TypeError:
                    parts.append(str(value))
            else:
                parts.append(str(value))
        return " ".join(parts).lower()
