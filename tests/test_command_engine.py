from kernel.command_engine import CommandEngine
from planner.execution_plan import ExecutionPlan
from planner.step import Step


def test_command_engine_converts_plan_to_tasks():

    engine = CommandEngine()

    plan = ExecutionPlan()

    plan.add_step(Step(plugin="time", action="current_time"))

    tasks = engine.execute_plan(plan)

    assert len(tasks) == 1
    assert tasks[0].plugin == "time"
    assert tasks[0].action == "current_time"


def test_command_engine_preserves_step_input():

    engine = CommandEngine()

    plan = ExecutionPlan()

    plan.add_step(
        Step(
            plugin="filesystem",
            action="list_pdfs",
            input={"path": "C:\\Users"},
        )
    )

    tasks = engine.execute_plan(plan)

    assert len(tasks) == 1
    assert tasks[0].plugin == "filesystem"
    assert tasks[0].action == "list_pdfs"
    assert tasks[0].input == {"path": "C:\\Users"}
