from agent.agent import Agent


def test_axis_executes_single_step_end_to_end():
    agent = Agent()
    agent.start()

    results = agent.process("what time is it")

    assert isinstance(results, list)
    assert len(results) == 1

    result = results[0]

    assert result.plugin == "time"
    assert result.action == "current_time"
    assert result.success is True
    assert isinstance(result.output, str)
    assert len(result.output) == 8
    assert result.output.count(":") == 2


def test_axis_executes_multi_step_end_to_end():
    agent = Agent()
    agent.start()

    results = agent.process("find my pdf files and tell me the current time")

    assert isinstance(results, list)
    assert len(results) == 2

    assert results[0].plugin == "filesystem"
    assert results[0].action == "list_pdfs"
    assert results[0].success is True

    assert results[1].plugin == "time"
    assert results[1].action == "current_time"
    assert results[1].success is True
