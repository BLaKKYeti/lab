class Registry:

    def __init__(self):
        self.connectors = {}

    def register(self, connector):
        self.connectors[connector.name()] = connector

    def get(self, name):
        return self.connectors.get(name)

    def list_connectors(self):
        return list(self.connectors.keys())