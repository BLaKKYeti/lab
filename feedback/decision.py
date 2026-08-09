from dataclasses import dataclass
from typing import Optional

from execution.context import ExecutionContext
from feedback.evaluation import Evaluation


@dataclass
class Decision:
    action: str
    reason: str


class DecisionEngine:
    def decide(
        self,
        evaluation: Evaluation,
        context: Optional[ExecutionContext] = None,
    ) -> Decision:

        if evaluation.status == "invalid":
            return Decision(
                action="stop",
                reason="The execution result was invalid.",
            )

        if evaluation.status == "failure":
            return Decision(
                action="stop",
                reason=evaluation.message,
            )

        return Decision(
            action="continue",
            reason=evaluation.message,
        )
