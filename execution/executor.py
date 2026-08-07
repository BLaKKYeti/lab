from execution.result import ExecutionResult


class Executor:
    def __init__(self, runtime):
        self.runtime = runtime

    def execute_plan(self, plan):

        results = []

        for step in plan.steps:
            result = self.runtime.execute(
                {"plugin": step.plugin, "action": step.action}
            )

            results.append(
                ExecutionResult(
                    plugin=step.plugin, action=step.action, success=True, output=result
                )
            )

        return results
