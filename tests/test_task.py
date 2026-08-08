from core.task import Task


def test_task_represents_executable_work():
    task = Task(
        intent="resolved",
        plugin="time",
        action="current_time",
        confidence=0.95,
    )

    assert task.intent == "resolved"
    assert task.plugin == "time"
    assert task.action == "current_time"
    assert task.confidence == 0.95


def test_task_can_represent_planned_work():
    task = Task(
        intent="planned",
        plugin="filesystem",
        action="list_pdfs",
    )

    assert task.plugin == "filesystem"
    assert task.action == "list_pdfs"


def test_task_can_carry_input():
    task = Task(
        intent="planned",
        plugin="filesystem",
        action="list_pdfs",
        input={"path": "C:\\Users"},
    )

    assert task.input == {"path": "C:\\Users"}
