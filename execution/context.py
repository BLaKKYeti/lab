from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionContext:
    """Tracks the state of a single AXIS execution."""

    results: list[Any] = field(default_factory=list)
    evaluations: list[Any] = field(default_factory=list)
    decisions: list[Any] = field(default_factory=list)
    status: str = "pending"

    def add_result(self, result: Any) -> None:
        self.results.append(result)

    def add_evaluation(self, evaluation: Any) -> None:
        self.evaluations.append(evaluation)

    def add_decision(self, decision: Any) -> None:
        self.decisions.append(decision)

    def complete(self) -> None:
        self.status = "completed"

    def stop(self) -> None:
        self.status = "stopped"
