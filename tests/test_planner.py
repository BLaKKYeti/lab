from planner.planner import Planner


def test_pdf_search_plan():

    planner = Planner()

    intent = {"plugin": "filesystem", "action": "list_pdfs"}

    plan = planner.create_plan(intent)

    assert len(plan.steps) == 1

    assert plan.steps[0].plugin == "filesystem"

    assert plan.steps[0].action == "list_pdfs"


def test_multi_step_plan():
    planner = Planner()

    intent = {
        "steps": [
            {
                "plugin": "filesystem",
                "action": "list_pdfs",
            },
            {
                "plugin": "time",
                "action": "current_time",
            },
        ]
    }

    plan = planner.create_plan(intent)

    assert len(plan.steps) == 2

    assert plan.steps[0].plugin == "filesystem"
    assert plan.steps[0].action == "list_pdfs"

    assert plan.steps[1].plugin == "time"
    assert plan.steps[1].action == "current_time"
