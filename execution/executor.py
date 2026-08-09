from core.task import Task
from execution.context import ExecutionContext
from execution.result import ExecutionResult
from feedback.decision import DecisionEngine
from feedback.evaluator import Evaluator


class Executor:
    def __init__(self, runtime):
        self.runtime = runtime
        self.evaluator = Evaluator()
        self.decision_engine = DecisionEngine()
        self.context = None

    def execute_plan(self, plan):
        self.context = ExecutionContext()
        results = []

        for step in plan.steps:
            task = Task(
                intent="planned",
                plugin=step.plugin,
                action=step.action,
                input=step.input,
            )

            result = self.runtime.execute(task)

            execution_result = ExecutionResult(
                plugin=step.plugin,
                action=step.action,
                success=not (
                    isinstance(result, str)
                    and result.startswith("Plugin '")
                    and result.endswith("not found")
                ),
                output=result,
            )

            self.context.add_result(execution_result)
            results.append(execution_result)

            evaluation = self.evaluator.evaluate(execution_result)
            self.context.add_evaluation(evaluation)

            decision = self.decision_engine.decide(evaluation)
            self.context.add_decision(decision)

            if decision.action == "stop":
                self.context.stop()
                break

        else:
            self.context.complete()

        return results
