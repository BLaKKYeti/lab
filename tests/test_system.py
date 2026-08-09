from agent.agent import Agent


def test_axis_executes_single_step_end_to_end():
    agent = Agent()
    agent.start()

    response = agent.process("what time is it")

    assert isinstance(response, str)
    assert response.startswith("The current time is ")

    time_value = response.removeprefix("The current time is ").removesuffix(".")

    assert len(time_value) == 8
    assert time_value.count(":") == 2


def test_axis_executes_multi_step_end_to_end():
    agent = Agent()
    agent.start()

    response = agent.process("find my pdf files and tell me the current time")

    assert isinstance(response, str)

    lines = response.splitlines()

    assert len(lines) == 2

    assert lines[0] == "I found no PDF files." or lines[0].startswith("I found ")

    assert lines[1].startswith("The current time is ")

    time_value = lines[1].removeprefix("The current time is ").removesuffix(".")

    assert len(time_value) == 8
    assert time_value.count(":") == 2
