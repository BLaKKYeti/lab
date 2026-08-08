from core.task import Task
from execution.executor import Executor


class FakeRuntime:
    def __init__(self, result):
        self.result = result

    def execute(self, task):
        return self.result


def test_executor_reports_success_for_successful_runtime_result():
    runtime = FakeRuntime("12:34")
    executor = Executor(runtime)

    plan = type(
        "Plan",
        (),
        {
            "steps": [
                type(
                    "Step",
                    (),
                    {
                        "plugin": "time",
                        "action": "current_time",
                    },
                )()
            ]
        },
    )()

    results = executor.execute_plan(plan)

    assert len(results) == 1
    assert results[0].plugin == "time"
    assert results[0].action == "current_time"
    assert results[0].success is True
    assert results[0].output == "12:34"


def test_executor_reports_failure_for_runtime_error():
    runtime = FakeRuntime("Plugin 'time' not found")
    executor = Executor(runtime)

    plan = type(
        "Plan",
        (),
        {
            "steps": [
                type(
                    "Step",
                    (),
                    {
                        "plugin": "time",
                        "action": "current_time",
                    },
                )()
            ]
        },
    )()

    results = executor.execute_plan(plan)

    assert len(results) == 1
    assert results[0].success is False
    assert results[0].output == "Plugin 'time' not found"


def test_executor_executes_multiple_steps_in_order():
    runtime = FakeRuntime("success")
    executor = Executor(runtime)

    plan = type(
        "Plan",
        (),
        {
            "steps": [
                type(
                    "Step",
                    (),
                    {
                        "plugin": "filesystem",
                        "action": "list_pdfs",
                    },
                )(),
                type(
                    "Step",
                    (),
                    {
                        "plugin": "time",
                        "action": "current_time",
                    },
                )(),
            ]
        },
    )()

    results = executor.execute_plan(plan)

    assert len(results) == 2

    assert results[0].plugin == "filesystem"
    assert results[0].action == "list_pdfs"
    assert results[0].success is True

    assert results[1].plugin == "time"
    assert results[1].action == "current_time"
    assert results[1].success is True


def test_executor_passes_task_to_runtime():
    class InspectingRuntime:
        def __init__(self):
            self.received = None

        def execute(self, task):
            self.received = task
            return "12:34"

    runtime = InspectingRuntime()
    executor = Executor(runtime)

    plan = type(
        "Plan",
        (),
        {
            "steps": [
                type(
                    "Step",
                    (),
                    {
                        "plugin": "time",
                        "action": "current_time",
                    },
                )()
            ]
        },
    )()

    results = executor.execute_plan(plan)

    assert len(results) == 1
    assert isinstance(runtime.received, Task)
    assert runtime.received.plugin == "time"
    assert runtime.received.action == "current_time"
