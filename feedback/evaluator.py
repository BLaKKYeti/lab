from execution.result import ExecutionResult
from feedback.evaluation import Evaluation


class Evaluator:
    def evaluate(self, result: ExecutionResult) -> Evaluation:
        if not isinstance(result, ExecutionResult):
            return Evaluation(
                success=False,
                status="invalid",
                message="Invalid execution result.",
                output=result,
            )

        if not result.success:
            return Evaluation(
                success=False,
                status="failure",
                message=(f"{result.plugin}.{result.action} failed during execution."),
                output=result.output,
            )

        return Evaluation(
            success=True,
            status="success",
            message=(f"{result.plugin}.{result.action} completed successfully."),
            output=result.output,
        )
