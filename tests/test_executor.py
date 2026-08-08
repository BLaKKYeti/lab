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
