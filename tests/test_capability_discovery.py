from capabilities.discovery import CapabilityDiscovery
from kernel.plugin_manager import PluginManager


def test_capability_discovery_finds_builtin_plugins():
    manager = PluginManager()
    manager.load_builtin_plugins()

    discovery = CapabilityDiscovery(manager)
    registry = discovery.discover()

    capabilities = registry.list_capabilities()
    names = [capability.name for capability in capabilities]

    assert "time.current_time" in names
    assert "time.current_date" in names
    assert "filesystem.list_pdfs" in names


def test_capability_discovery_links_capability_to_plugin():
    manager = PluginManager()
    manager.load_builtin_plugins()

    discovery = CapabilityDiscovery(manager)
    registry = discovery.discover()

    capability = registry.get("time.current_time")

    assert capability is not None
    assert capability.plugin == "time"
    assert capability.action == "current_time"


def test_capability_discovery_preserves_plugin_description():
    manager = PluginManager()
    manager.load_builtin_plugins()

    discovery = CapabilityDiscovery(manager)
    registry = discovery.discover()

    capability = registry.get("time.current_time")

    assert capability is not None
    assert capability.description == ("System time and date management plugin")
