from registry.registry import Registry
from resolver.resolver import Resolver
from connectors.filesystem import FileSystemConnector
from kernel.config import ConfigLoader


class Runtime:

    def __init__(self):
        self.config = ConfigLoader().load()
        self.registry = Registry()
        self.resolver = Resolver(self.registry)

    def start(self):

        if self.config["connectors"]["filesystem"]["enabled"]:
            filesystem = FileSystemConnector()
            self.registry.register(filesystem)

        print(self.config["system"]["name"], "online")
        print("Version:", self.config["system"]["version"])
        print("Connectors:", self.registry.list_connectors())

    def execute(self, connector, task):
        return self.resolver.resolve(connector, task)