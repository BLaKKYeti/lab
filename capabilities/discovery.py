from capabilities.capability import Capability
from capabilities.registry import CapabilityRegistry
from kernel.plugin_manager import PluginManager


class CapabilityDiscovery:
    """Discovers capabilities exposed by registered AXIS plugins."""

    def __init__(self, plugin_manager: PluginManager):
        self.plugin_manager = plugin_manager

    def discover(self) -> CapabilityRegistry:
        registry = CapabilityRegistry()

        for plugin_name, details in self.plugin_manager.get_capabilities().items():
            description = details.get("description", "")
            actions = details.get("actions", [])

            for action in actions:
                capability = Capability(
                    plugin=plugin_name,
                    action=action,
                    description=description,
                )

                registry.register(capability)

        return registry
