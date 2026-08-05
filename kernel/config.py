import yaml


class ConfigLoader:

    def __init__(self, path="config/config.yaml"):
        self.path = path

    def load(self):
        with open(self.path, "r") as file:
            return yaml.safe_load(file)