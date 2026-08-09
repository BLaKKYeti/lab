from execution.context import ExecutionContext


def test_execution_context_starts_pending():
    context = ExecutionContext()

    assert context.status == "pending"
    assert context.results == []
    assert context.evaluations == []
    assert context.decisions == []


def test_execution_context_records_result():
    context = ExecutionContext()

    result = "12:34"

    context.add_result(result)

    assert context.results == ["12:34"]


def test_execution_context_records_evaluation():
    context = ExecutionContext()

    evaluation = "success"

    context.add_evaluation(evaluation)

    assert context.evaluations == ["success"]


def test_execution_context_records_decision():
    context = ExecutionContext()

    decision = "continue"

    context.add_decision(decision)

    assert context.decisions == ["continue"]


def test_execution_context_can_complete():
    context = ExecutionContext()

    context.complete()

    assert context.status == "completed"


def test_execution_context_can_stop():
    context = ExecutionContext()

    context.stop()

    assert context.status == "stopped"
