import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Optional


class Memory:
    """Manage persisted AXIS memory data and provide helper methods."""

    def __init__(self) -> None:
        """Initialize memory storage and load persisted data."""
        self.memory_file: Path = Path("memory.json")
        self.data: Dict[str, Any] = {
            "profile": {},
            "preferences": {},
            "conversations": [],
            "events": [],
            "system": {},
        }
        self.load()

    def load(self) -> None:
        """Load memory from disk and apply migration if needed."""
        if self.memory_file.exists():
            with open(self.memory_file, "r") as file:
                self.data = json.load(file)
            self.migrate()
        else:
            self.save()

    def migrate(self) -> None:
        """Migrate legacy memory schemas to the current structure."""
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

    def save(self) -> None:
        """Persist the current memory state to disk."""
        with open(self.memory_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def _migrate_records(self, records: Any, record_type: str) -> None:
        """Ensure legacy records contain metadata and a consistent structure."""
        if isinstance(records, dict):
            items: List[Dict[str, Any]] = []
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
            for record in records:
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
        self,
        record_type: str,
        source: str = "memory",
        tags: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Build metadata for a memory record."""
        metadata: Dict[str, Any] = {
            "id": self._next_id(),
            "timestamp": self._timestamp(),
            "type": record_type,
            "source": source,
        }
        if tags:
            metadata["tags"] = tags
        return metadata

    def _timestamp(self) -> str:
        """Return a timestamp string for new records."""
        return "2026-08-06T00:00:00"

    def _next_id(self) -> str:
        """Return a deterministic next ID for migration and event records."""
        return f"{self._timestamp()}-{len(self.data.get('events', [])) + len(self.data.get('conversations', [])) + 1}"

    def remember(self, key: str, value: Any) -> None:
        """Store a value in the system memory namespace."""
        self.data["system"][key] = value
        self.save()

    def remember_event(self, plugin: str, action: Any, result: Any) -> None:
        """Record a runtime plugin event in memory."""
        event: Dict[str, Any] = {
            "plugin": plugin,
            "action": action,
            "result": result,
            "metadata": self._build_metadata("event", source="runtime", tags=["event"]),
        }
        self.data["events"].append(event)
        self.save()

    def remember_profile(self, key: str, value: Any) -> None:
        """Store a profile value in memory."""
        self.data["profile"][key] = value
        self.save()

    def remember_preference(self, key: str, value: Any) -> None:
        """Store a preference value in memory."""
        self.data["preferences"][key] = value
        self.save()

    def remember_conversation(self, user: str, response: str) -> None:
        """Append a conversation exchange to memory."""
        conversation: Dict[str, Any] = {
            "user": user,
            "response": response,
            "metadata": self._build_metadata(
                "conversation", source="runtime", tags=["conversation"]
            ),
        }
        self.data["conversations"].append(conversation)
        self.save()

    def recall(self, key: str) -> Any:
        """Recall a value from the system memory namespace."""
        return self.data["system"].get(key)

    def all(self) -> Dict[str, Any]:
        """Return a deep copy of the full memory payload."""
        return deepcopy(self.data)

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Search all memory records for a text query."""
        query_text = (query or "").strip().lower()
        if not query_text:
            return []

        matches: List[Dict[str, Any]] = []
        for record in self._iter_records():
            payload = self._record_search_text(record)
            if query_text in payload:
                matches.append(record)
        return matches

    def recent(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Return the most recent memory records up to the requested limit."""
        records = self._iter_records()
        if limit is None:
            return records
        return records[-limit:] if limit > 0 else []

    def get_profile(self) -> Dict[str, Any]:
        """Return the profile memory bucket."""
        return self.data.get("profile", {})

    def get_preferences(self) -> Dict[str, Any]:
        """Return the preferences memory bucket."""
        return self.data.get("preferences", {})

    def get_conversations(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Return the recent conversation records."""
        conversations = self.data.get("conversations", [])
        if limit is None:
            return conversations
        return conversations[-limit:] if limit > 0 else []

    def get_events(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Return the recent event records."""
        events = self.data.get("events", [])
        if limit is None:
            return events
        return events[-limit:] if limit > 0 else []

    def _iter_records(self) -> List[Dict[str, Any]]:
        """Yield all memory records across profile, preferences, conversations, and events."""
        records: List[Dict[str, Any]] = []
        for key, value in self.data.get("profile", {}).items():
            records.append(
                {
                    "type": "profile",
                    "key": key,
                    "value": value,
                    "metadata": self._build_metadata("profile", source="memory"),
                }
            )
        for key, value in self.data.get("preferences", {}).items():
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

    def _record_search_text(self, record: Dict[str, Any]) -> str:
        """Convert a record to searchable text."""
        parts: List[str] = []
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
