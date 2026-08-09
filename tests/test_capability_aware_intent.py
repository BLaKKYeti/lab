from capabilities.discovery import CapabilityDiscovery
from kernel.intent_engine import IntentEngine
from kernel.plugin_manager import PluginManager


def test_intent_engine_accepts_capability_registry():
    manager = PluginManager()
    manager.load_builtin_plugins()

    discovery = CapabilityDiscovery(manager)
    registry = discovery.discover()

    engine = IntentEngine(registry)

    assert engine.capability_registry is registry


def test_intent_engine_resolves_discovered_time_capability():
    manager = PluginManager()
    manager.load_builtin_plugins()

    discovery = CapabilityDiscovery(manager)
    registry = discovery.discover()

    engine = IntentEngine(registry)

    intent = engine.resolve("what time is it")

    assert intent["plugin"] == "time"
    assert intent["action"] == "current_time"


def test_intent_engine_resolves_discovered_filesystem_capability():
    manager = PluginManager()
    manager.load_builtin_plugins()

    discovery = CapabilityDiscovery(manager)
    registry = discovery.discover()

    engine = IntentEngine(registry)

    intent = engine.resolve("find my pdf files")

    assert intent["plugin"] == "filesystem"
    assert intent["action"] == "list_pdfs"
