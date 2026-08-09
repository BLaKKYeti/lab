from capabilities.capability import Capability
from capabilities.registry import CapabilityRegistry


def test_capability_creates_name():
    capability = Capability(
        plugin="time",
        action="current_time",
    )

    assert capability.name == "time.current_time"


def test_capability_registry_registers_capability():
    registry = CapabilityRegistry()

    capability = Capability(
        plugin="time",
        action="current_time",
    )

    registry.register(capability)

    assert registry.has("time.current_time") is True


def test_capability_registry_gets_capability():
    registry = CapabilityRegistry()

    capability = Capability(
        plugin="time",
        action="current_time",
        description="Get the current system time.",
    )

    registry.register(capability)

    result = registry.get("time.current_time")

    assert result is capability
    assert result.description == "Get the current system time."


def test_capability_registry_lists_capabilities():
    registry = CapabilityRegistry()

    registry.register(
        Capability(
            plugin="time",
            action="current_time",
        )
    )

    registry.register(
        Capability(
            plugin="time",
            action="current_date",
        )
    )

    capabilities = registry.list_capabilities()

    assert len(capabilities) == 2
    assert capabilities[0].name == "time.current_time"
    assert capabilities[1].name == "time.current_date"


def test_capability_registry_returns_none_for_unknown_capability():
    registry = CapabilityRegistry()

    assert registry.get("unknown.action") is None


def test_capability_registry_can_clear():
    registry = CapabilityRegistry()

    registry.register(
        Capability(
            plugin="time",
            action="current_time",
        )
    )

    registry.clear()

    assert registry.list_capabilities() == []
