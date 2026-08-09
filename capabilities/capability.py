from dataclasses import dataclass


@dataclass
class Capability:
    plugin: str
    action: str
    description: str = ""

    @property
    def name(self) -> str:
        return f"{self.plugin}.{self.action}"
