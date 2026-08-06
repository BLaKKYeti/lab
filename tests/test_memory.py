import json

from kernel import memory


def test_memory_import():
    assert memory is not None


def test_conversation_memory_storage(tmp_path):
    memory_file = tmp_path / "memory.json"
    memory_file.write_text(
        json.dumps(
            {
                "profile": {},
                "preferences": {},
                "conversations": [],
                "events": [],
                "system": {},
            }
        )
    )

    instance = memory.Memory()
    instance.memory_file = memory_file
    instance.data = {
        "profile": {},
        "preferences": {},
        "conversations": [],
        "events": [],
        "system": {},
    }
    instance.load()

    instance.remember_conversation("what time is it", "23:35:05")

    stored = json.loads(memory_file.read_text())
    assert stored["conversations"][-1]["user"] == "what time is it"
    assert stored["conversations"][-1]["response"] == "23:35:05"


def test_legacy_memory_file_migrates_to_new_structure(tmp_path):
    memory_file = tmp_path / "memory.json"
    memory_file.write_text(
        json.dumps(
            {
                "system": {},
                "history": [
                    {"plugin": "time", "action": "current_time", "result": "23:35:05"}
                ],
            }
        )
    )

    instance = memory.Memory()
    instance.memory_file = memory_file
    instance.load()

    stored = instance.all()

    assert stored["events"][-1]["plugin"] == "time"
    assert stored["conversations"] == []
    assert stored["preferences"] == {}


def test_conversations_can_be_retrieved_with_limit(tmp_path):
    memory_file = tmp_path / "memory.json"
    memory_file.write_text(
        json.dumps(
            {
                "profile": {},
                "preferences": {},
                "conversations": [],
                "events": [],
                "system": {},
            }
        )
    )

    instance = memory.Memory()
    instance.memory_file = memory_file
    instance.data = {
        "profile": {},
        "preferences": {},
        "conversations": [],
        "events": [],
        "system": {},
    }
    instance.load()

    instance.remember_conversation("first", "one")
    instance.remember_conversation("second", "two")
    instance.remember_conversation("third", "three")

    recent = instance.get_conversations(limit=2)

    assert len(recent) == 2
    assert recent[0]["user"] == "second"
    assert recent[1]["user"] == "third"


def test_events_can_be_retrieved_with_limit(tmp_path):
    memory_file = tmp_path / "memory.json"
    memory_file.write_text(
        json.dumps(
            {
                "profile": {},
                "preferences": {},
                "conversations": [],
                "events": [],
                "system": {},
            }
        )
    )

    instance = memory.Memory()
    instance.memory_file = memory_file
    instance.data = {
        "profile": {},
        "preferences": {},
        "conversations": [],
        "events": [],
        "system": {},
    }
    instance.load()

    instance.remember_event("time", "current_time", "10:00")
    instance.remember_event("time", "current_date", "2026-08-05")
    instance.remember_event("filesystem", "list_files", ["a.txt"])

    recent_events = instance.get_events(limit=2)

    assert len(recent_events) == 2
    assert recent_events[0]["action"] == "current_date"
    assert recent_events[1]["action"] == "list_files"
