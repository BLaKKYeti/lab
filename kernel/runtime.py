from registry.registry import Registry
from resolver.resolver import Resolver
from kernel.config import ConfigLoader
from kernel.connector_loader import ConnectorLoader


class Runtime:

    def __init__(self):
        self.config = ConfigLoader().load()
        self.registry = Registry()
        self.resolver = Resolver(self.registry)

    def start(self):

        loader = ConnectorLoader(
            self.registry,
            self.config
        )

        loader.load()

        print(self.config["system"]["name"], "online")
        print("Version:", self.config["system"]["version"])
        print("Connectors:", self.registry.list_connectors())

    def execute(self, connector, task):
        return self.resolver.resolve(connector, task)