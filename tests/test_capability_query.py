from capabilities.capability import Capability
from capabilities.query import CapabilityQuery
from capabilities.registry import CapabilityRegistry


def test_capability_query_describes_registered_capabilities():
    registry = CapabilityRegistry()

    registry.register(
        Capability(
            plugin="time",
            action="current_time",
            description="Get the current system time.",
        )
    )

    query = CapabilityQuery(registry)

    result = query.describe()

    assert "time.current_time" in result
    assert "Get the current system time." in result


def test_capability_query_describes_multiple_capabilities():
    registry = CapabilityRegistry()

    registry.register(
        Capability(
            plugin="time",
            action="current_time",
            description="Get the current system time.",
        )
    )

    registry.register(
        Capability(
            plugin="filesystem",
            action="list_pdfs",
            description="Filesystem management plugin",
        )
    )

    query = CapabilityQuery(registry)

    result = query.describe()

    assert "time.current_time" in result
    assert "filesystem.list_pdfs" in result


def test_capability_query_handles_empty_registry():
    registry = CapabilityRegistry()

    query = CapabilityQuery(registry)

    result = query.describe()

    assert result == "AXIS currently has no discovered capabilities."
