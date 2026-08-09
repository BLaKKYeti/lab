from typing import Dict, Optional

from capabilities.capability import Capability


class CapabilityRegistry:
    def __init__(self):
        self.capabilities: Dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        self.capabilities[capability.name] = capability

    def get(self, name: str) -> Optional[Capability]:
        return self.capabilities.get(name)

    def has(self, name: str) -> bool:
        return name in self.capabilities

    def list_capabilities(self) -> list[Capability]:
        return list(self.capabilities.values())

    def clear(self) -> None:
        self.capabilities.clear()
