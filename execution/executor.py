from core.task import Task
from execution.result import ExecutionResult


class Executor:
    def __init__(self, runtime):
        self.runtime = runtime

    def execute_plan(self, plan):
        results = []

        for step in plan.steps:
            task = Task(
                intent="planned",
                plugin=step.plugin,
                action=step.action,
            )

            result = self.runtime.execute(task)

            results.append(
                ExecutionResult(
                    plugin=step.plugin,
                    action=step.action,
                    success=not (
                        isinstance(result, str)
                        and result.startswith("Plugin '")
                        and result.endswith("not found")
                    ),
                    output=result,
                )
            )

        return results
