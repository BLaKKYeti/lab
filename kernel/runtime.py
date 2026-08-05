from registry.registry import Registry
from resolver.resolver import Resolver
from connectors.filesystem import FileSystemConnector


class Runtime:

    def __init__(self):
        self.registry = Registry()
        self.resolver = Resolver(self.registry)

    def start(self):
        filesystem = FileSystemConnector()

        self.registry.register(filesystem)

        print("LAB AI OS online")
        print("Connectors:", self.registry.list_connectors())

    def execute(self, connector, task):
        return self.resolver.resolve(connector, task)