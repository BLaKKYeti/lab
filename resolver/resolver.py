class Resolver:

    def __init__(self, registry):
        self.registry = registry

    def resolve(self, connector_name, task):
        connector = self.registry.get(connector_name)

        if not connector:
            return "Connector not found"

        return connector.execute(task)