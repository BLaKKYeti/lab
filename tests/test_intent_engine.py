from kernel.intent_engine import IntentEngine


def test_resolves_time_intent():
    engine = IntentEngine()

    intent = engine.resolve("what time is it")

    assert intent["plugin"] == "time"
    assert intent["action"] == "current_time"
    assert intent["confidence"] == 0.95


def test_resolves_date_intent():
    engine = IntentEngine()

    intent = engine.resolve("what is today's date")

    assert intent["plugin"] == "time"
    assert intent["action"] == "current_date"
    assert intent["confidence"] == 0.95


def test_resolves_pdf_intent():
    engine = IntentEngine()

    intent = engine.resolve("find my pdf files")

    assert intent["plugin"] == "filesystem"
    assert intent["action"] == "list_pdfs"
    assert intent["confidence"] == 0.95


def test_unknown_intent_is_explicit():
    engine = IntentEngine()

    intent = engine.resolve("tell me a joke")

    assert intent["plugin"] is None
    assert intent["action"] is None
    assert intent["confidence"] == 0.0


def test_resolves_multi_step_intent():
    engine = IntentEngine()

    intent = engine.resolve("find my pdf files and tell me the current time")

    assert "steps" in intent
    assert len(intent["steps"]) == 2

    assert intent["steps"][0]["plugin"] == "filesystem"
    assert intent["steps"][0]["action"] == "list_pdfs"

    assert intent["steps"][1]["plugin"] == "time"
    assert intent["steps"][1]["action"] == "current_time"


def test_resolves_multi_step_intent():
    engine = IntentEngine()

    intent = engine.resolve("find my pdf files and tell me the current time")

    assert "steps" in intent
    assert len(intent["steps"]) == 2

    assert intent["steps"][0]["plugin"] == "filesystem"
    assert intent["steps"][0]["action"] == "list_pdfs"

    assert intent["steps"][1]["plugin"] == "time"
    assert intent["steps"][1]["action"] == "current_time"
