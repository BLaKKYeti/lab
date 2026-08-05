import os

from interfaces.connector import Connector


class ClaudeConnector(Connector):
    """
    Claude connector.

    This class is responsible for communicating with the Claude service.
    For now it only validates configuration and returns placeholder
    responses until API integration is added.
    """

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")

    def name(self):
        return "claude"

    def execute(self, task):

        if not self.api_key:
            return {
                "status": "error",
                "message": "ANTHROPIC_API_KEY not configured."
            }

        return {
            "status": "ok",
            "connector": "claude",
            "task": task,
            "message": "Claude connector initialized successfully."
        }