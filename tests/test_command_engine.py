def test_command_engine_import():
    from kernel.command_engine import CommandEngine

    assert CommandEngine is not None


def test_command_engine_builds_task_from_intent():
    from kernel.command_engine import CommandEngine
    from kernel.intent_engine import IntentEngine

    engine = CommandEngine(runtime=None, intent_engine=IntentEngine())
    task = engine.interpret("Find all PDFs on my computer")

    assert task.plugin == "filesystem"
    assert task.action == "list_pdfs"
    assert task.confidence >= 0.95
