from connectors.claude import ClaudeConnector
from connectors.filesystem import FileSystemConnector


class ConnectorLoader:
    def __init__(self, registry, config):
        self.registry = registry
        self.config = config

    def load(self):

        connectors = self.config.get("connectors", {})

        if connectors.get("filesystem", {}).get("enabled"):
            self.registry.register(FileSystemConnector())

        if self.config.get("claude", {}).get("enabled"):
            self.registry.register(ClaudeConnector())
