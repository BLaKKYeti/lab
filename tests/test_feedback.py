from execution.result import ExecutionResult
from feedback.decision import DecisionEngine
from feedback.evaluator import Evaluator


def test_evaluator_recognizes_success():
    evaluator = Evaluator()

    result = ExecutionResult(
        plugin="time",
        action="current_time",
        success=True,
        output="12:34:56",
    )

    evaluation = evaluator.evaluate(result)

    assert evaluation.success is True
    assert evaluation.status == "success"
    assert evaluation.output == "12:34:56"


def test_evaluator_recognizes_failure():
    evaluator = Evaluator()

    result = ExecutionResult(
        plugin="time",
        action="current_time",
        success=False,
        output="Plugin 'time' not found",
    )

    evaluation = evaluator.evaluate(result)

    assert evaluation.success is False
    assert evaluation.status == "failure"
    assert evaluation.output == "Plugin 'time' not found"


def test_decision_engine_continues_after_success():
    evaluator = Evaluator()
    decision_engine = DecisionEngine()

    result = ExecutionResult(
        plugin="time",
        action="current_time",
        success=True,
        output="12:34:56",
    )

    evaluation = evaluator.evaluate(result)
    decision = decision_engine.decide(evaluation)

    assert decision.action == "continue"


def test_decision_engine_stops_after_failure():
    evaluator = Evaluator()
    decision_engine = DecisionEngine()

    result = ExecutionResult(
        plugin="time",
        action="current_time",
        success=False,
        output="Plugin 'time' not found",
    )

    evaluation = evaluator.evaluate(result)
    decision = decision_engine.decide(evaluation)

    assert decision.action == "stop"


def test_decision_engine_accepts_execution_context():
    from execution.context import ExecutionContext

    evaluator = Evaluator()
    decision_engine = DecisionEngine()
    context = ExecutionContext()

    result = ExecutionResult(
        plugin="time",
        action="current_time",
        success=True,
        output="12:34:56",
    )

    evaluation = evaluator.evaluate(result)

    decision = decision_engine.decide(
        evaluation,
        context,
    )

    assert decision.action == "continue"
