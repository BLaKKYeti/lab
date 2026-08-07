class ExecutionPlan:
    def __init__(self):

        self.steps = []

    def add_step(self, step):

        self.steps.append(step)

    def __repr__(self):

        return f"ExecutionPlan(steps={self.steps})"
