from kernel.planner import Planner


def test_planner_creation():
    planner = Planner()
    assert planner is not None


def test_plan_returns_a_list():
    planner = Planner()
    plan = planner.plan("what time is it")

    assert isinstance(plan, list)


def test_single_step_plan_is_created_correctly():
    planner = Planner()
    plan = planner.plan("what time is it")

    assert plan == [{"step": 1, "description": "what time is it"}]
