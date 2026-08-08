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
