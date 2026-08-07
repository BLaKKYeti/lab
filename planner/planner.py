from planner.execution_plan import ExecutionPlan
from planner.interfaces import PlannerInterface
from planner.step import Step


class Planner(PlannerInterface):
    def create_plan(self, intent):

        plan = ExecutionPlan()

        if not intent:
            return plan

        plugin = intent.get("plugin")
        action = intent.get("action")

        if plugin and action:
            plan.add_step(Step(plugin=plugin, action=action))

        return plan
