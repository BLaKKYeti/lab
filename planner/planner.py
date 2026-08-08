from planner.execution_plan import ExecutionPlan
from planner.interfaces import PlannerInterface
from planner.step import Step


class Planner(PlannerInterface):
    def create_plan(self, intent):
        plan = ExecutionPlan()

        if not intent:
            return plan

        steps = intent.get("steps")

        if steps:
            for step in steps:
                plugin = step.get("plugin")
                action = step.get("action")
                input_data = step.get("input")

                if plugin and action:
                    plan.add_step(
                        Step(
                            plugin=plugin,
                            action=action,
                            input=input_data,
                        )
                    )

            return plan

        plugin = intent.get("plugin")
        action = intent.get("action")
        input_data = intent.get("input")

        if plugin and action:
            plan.add_step(
                Step(
                    plugin=plugin,
                    action=action,
                    input=input_data,
                )
            )

        return plan
