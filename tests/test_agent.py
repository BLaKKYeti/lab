from agent.agent import Agent


def test_agent_process_executes_time_command():
    agent = Agent()

    agent.start()

    results = agent.process("what time is it")

    assert len(results) == 1

    result = results[0]

    assert result.plugin == "time"
    assert result.action == "current_time"
    assert result.success is True
    assert isinstance(result.output, str)
    assert len(result.output) == 8
    assert result.output.count(":") == 2


def test_agent_process_executes_multi_step_command():
    agent = Agent()

    agent.start()

    results = agent.process("find my pdf files and tell me the current time")

    assert len(results) == 2

    assert results[0].plugin == "filesystem"
    assert results[0].action == "list_pdfs"
    assert results[0].success is True

    assert results[1].plugin == "time"
    assert results[1].action == "current_time"
    assert results[1].success is True
