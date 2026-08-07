import json
import uuid
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


class Memory:
    """
    AXIS persistent memory system.

    Handles:
    - persistent storage
    - migration
    - conversations
    - events
    - profile
    - preferences
    - search
    - retrieval
    """

    def __init__(self) -> None:
        self.memory_file = Path("memory.json")

        self.data: Dict[str, Any] = {
            "profile": {},
            "preferences": {},
            "conversations": [],
            "events": [],
            "system": {},
        }

        self.load()

    def timestamp(self) -> str:
        return datetime.now().isoformat()

    def generate_id(self) -> str:
        return str(uuid.uuid4())

    def load(self) -> None:
        """
        Load memory safely.
        Repairs corrupted or outdated files.
        """

        if not self.memory_file.exists():
            self.save()
            return

        try:
            with open(self.memory_file, "r") as file:
                self.data = json.load(file)

        except json.JSONDecodeError:
            self.data = {
                "profile": {},
                "preferences": {},
                "conversations": [],
                "events": [],
                "system": {},
            }
            self.save()

        self.migrate()

    def save(self) -> None:
        """
        Save memory safely.
        """

        with open(self.memory_file, "w") as file:
            json.dump(self.data, file, indent=4, default=str)

    def migrate(self) -> None:
        """
        Upgrade old memory formats.
        """

        self.data.setdefault("profile", {})
        self.data.setdefault("preferences", {})
        self.data.setdefault("conversations", [])
        self.data.setdefault("events", [])
        self.data.setdefault("system", {})

        # Legacy history migration
        if "history" in self.data:
            for item in self.data["history"]:
                self.data["events"].append(
                    {
                        "id": self.generate_id(),
                        "plugin": item.get("plugin"),
                        "action": item.get("action"),
                        "result": item.get("result"),
                        "timestamp": self.timestamp(),
                    }
                )

            del self.data["history"]

        self.save()

    def remember(self, key: str, value: Any) -> None:

        self.data["system"][key] = value
        self.save()

    def remember_conversation(self, user: str, response: Any) -> None:

        self.data["conversations"].append(
            {
                "id": self.generate_id(),
                "user": user,
                "response": response,
                "timestamp": self.timestamp(),
            }
        )

        self.save()

    def remember_event(self, plugin: str, action: str, result: Any) -> None:

        self.data["events"].append(
            {
                "id": self.generate_id(),
                "plugin": plugin,
                "action": action,
                "result": result,
                "timestamp": self.timestamp(),
            }
        )

        self.save()

    def remember_profile(self, key: str, value: Any) -> None:

        self.data["profile"][key] = value
        self.save()

    def remember_preference(self, key: str, value: Any) -> None:

        self.data["preferences"][key] = value
        self.save()

    def get_profile(self) -> Dict[str, Any]:
        return deepcopy(self.data["profile"])

    def get_preferences(self) -> Dict[str, Any]:
        return deepcopy(self.data["preferences"])

    def get_conversations(self, limit: int = 10) -> List[Dict[str, Any]]:

        return self.data["conversations"][-limit:]

    def get_events(self, limit: int = 10) -> List[Dict[str, Any]]:

        return self.data["events"][-limit:]

    def all(self) -> Dict[str, Any]:
        return deepcopy(self.data)

    def search(self, query: str) -> List[Dict[str, Any]]:

        query = query.lower()

        results = []

        for key, value in self.data["profile"].items():
            if query in str(value).lower():
                results.append(
                    {
                        "type": "profile",
                        "key": key,
                        "value": value,
                        "metadata": {"id": f"profile_{key}"},
                    }
                )

        for key, value in self.data["preferences"].items():
            if query in str(value).lower():
                results.append(
                    {
                        "type": "preference",
                        "key": key,
                        "value": value,
                        "metadata": {"id": f"preference_{key}"},
                    }
                )

        for item in self.data["conversations"]:
            if query in str(item).lower():
                results.append(
                    {
                        "type": "conversation",
                        **item,
                        "metadata": {"id": item["id"]},
                    }
                )

        for item in self.data["events"]:
            if query in str(item).lower():
                results.append(
                    {
                        "type": "event",
                        **item,
                        "metadata": {"id": item["id"]},
                    }
                )

        return results

    def recent(self, limit: int = 10) -> List[Dict[str, Any]]:

        records = []

        for key, value in self.data["profile"].items():
            records.append(
                {
                    "type": "profile",
                    "key": key,
                    "value": value,
                    "metadata": {"id": f"profile_{key}"},
                }
            )

        for key, value in self.data["preferences"].items():
            records.append(
                {
                    "type": "preference",
                    "key": key,
                    "value": value,
                    "metadata": {"id": f"preference_{key}"},
                }
            )

        for item in self.data["conversations"]:
            records.append(
                {
                    "type": "conversation",
                    **item,
                    "metadata": {"id": item["id"]},
                }
            )

        for item in self.data["events"]:
            records.append(
                {
                    "type": "event",
                    **item,
                    "metadata": {"id": item["id"]},
                }
            )

        return records[-limit:]
