from planner.planner import Planner


def test_pdf_search_plan():

    planner = Planner()

    intent = {"plugin": "filesystem", "action": "list_pdfs"}

    plan = planner.create_plan(intent)

    assert len(plan.steps) == 1

    assert plan.steps[0].plugin == "filesystem"

    assert plan.steps[0].action == "list_pdfs"
