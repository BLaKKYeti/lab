from datetime import datetime

from interfaces.plugin import Plugin


class TimePlugin(Plugin):
    def __init__(self):
        self.config = {}

    def name(self) -> str:
        return "time"

    def description(self) -> str:
        return "System time and date management plugin"

    def actions(self) -> list:
        return [
            "current_time",
            "current_date",
        ]

    def initialize(self, config: dict):
        self.config = config

    def execute(self, task, input=None):
        if task == "current_time":
            return datetime.now().strftime("%H:%M:%S")

        if task == "current_date":
            return datetime.now().strftime("%Y-%m-%d")

        raise ValueError(f"Unsupported time task: {task}")

    def shutdown(self):
        pass
