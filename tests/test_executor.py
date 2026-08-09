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
                        "input": None,
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
                        "input": None,
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
                        "input": {"path": "C:\\Users"},
                    },
                )(),
                type(
                    "Step",
                    (),
                    {
                        "plugin": "time",
                        "action": "current_time",
                        "input": {"timezone": "Jamaica"},
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
                        "input": {"timezone": "Jamaica"},
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
    assert runtime.received.input == {"timezone": "Jamaica"}


def test_executor_creates_execution_context():
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
                        "input": None,
                    },
                )()
            ]
        },
    )()

    executor.execute_plan(plan)

    assert executor.context is not None
    assert executor.context.status == "completed"


def test_executor_context_records_successful_execution():
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
                        "input": None,
                    },
                )()
            ]
        },
    )()

    executor.execute_plan(plan)

    assert len(executor.context.results) == 1
    assert len(executor.context.evaluations) == 1
    assert len(executor.context.decisions) == 1

    assert executor.context.decisions[0].action == "continue"


def test_executor_context_records_failure_and_stops():
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
                        "input": None,
                    },
                )()
            ]
        },
    )()

    executor.execute_plan(plan)

    assert executor.context.status == "stopped"
    assert len(executor.context.results) == 1
    assert len(executor.context.evaluations) == 1
    assert len(executor.context.decisions) == 1

    assert executor.context.evaluations[0].status == "failure"
    assert executor.context.decisions[0].action == "stop"


def test_executor_creates_execution_context():
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
                        "input": None,
                    },
                )()
            ]
        },
    )()

    executor.execute_plan(plan)

    assert executor.context is not None
    assert executor.context.status == "completed"


def test_executor_context_records_successful_execution():
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
                        "input": None,
                    },
                )()
            ]
        },
    )()

    results = executor.execute_plan(plan)

    assert len(results) == 1
    assert len(executor.context.results) == 1
    assert len(executor.context.evaluations) == 1
    assert len(executor.context.decisions) == 1
    assert executor.context.status == "completed"


def test_executor_context_records_failure_and_stops():
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
                        "input": None,
                    },
                )(),
                type(
                    "Step",
                    (),
                    {
                        "plugin": "filesystem",
                        "action": "list_pdfs",
                        "input": None,
                    },
                )(),
            ]
        },
    )()

    results = executor.execute_plan(plan)

    assert len(results) == 1
    assert executor.context.status == "stopped"
    assert len(executor.context.results) == 1
    assert len(executor.context.evaluations) == 1
    assert len(executor.context.decisions) == 1
