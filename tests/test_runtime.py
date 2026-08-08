from core.task import Task
from kernel.runtime import Runtime


def test_runtime_import():
    assert Runtime is not None


def test_runtime_passes_task_input_to_plugin():
    runtime = Runtime()

    class FakePlugin:
        def __init__(self):
            self.received_action = None
            self.received_input = None

        def execute(self, action, input=None):
            self.received_action = action
            self.received_input = input
            return "success"

    fake_plugin = FakePlugin()

    runtime.plugin_manager.get = lambda name: fake_plugin

    task = Task(
        intent="planned",
        plugin="filesystem",
        action="list_pdfs",
        input={"path": "C:\\Users"},
    )

    result = runtime.execute(task)

    assert result == "success"
    assert fake_plugin.received_action == "list_pdfs"
    assert fake_plugin.received_input == {"path": "C:\\Users"}