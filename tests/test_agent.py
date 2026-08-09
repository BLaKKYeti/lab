from agent.agent import Agent


def test_agent_process_executes_time_command():
    agent = Agent()

    agent.start()

    response = agent.process("what time is it")

    assert "The current time is " in response
    assert len(response) > 20
    assert response.endswith(".")


def test_agent_process_executes_multi_step_command():
    agent = Agent()

    agent.start()

    response = agent.process("find my pdf files and tell me the current time")

    assert "I found " in response
    assert "PDF" in response
    assert "The current time is " in response


def test_agent_stores_execution_context():
    agent = Agent()

    agent.start()

    response = agent.process("what time is it")

    assert "The current time is " in response

    assert agent.execution_context is not None
    assert agent.execution_context.status == "completed"


def test_agent_context_contains_execution_feedback():
    agent = Agent()

    agent.start()

    agent.process("what time is it")

    context = agent.execution_context

    assert len(context.results) == 1
    assert len(context.evaluations) == 1
    assert len(context.decisions) == 1

    assert context.results[0].plugin == "time"
    assert context.results[0].action == "current_time"

    assert context.evaluations[0].status == "success"
    assert context.decisions[0].action == "continue"
