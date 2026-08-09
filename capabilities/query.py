from capabilities.registry import CapabilityRegistry


class CapabilityQuery:
    """Provides human-readable information about AXIS capabilities."""

    def __init__(self, registry: CapabilityRegistry) -> None:
        self.registry = registry

    def describe(self) -> str:
        capabilities = self.registry.list_capabilities()

        if not capabilities:
            return "AXIS currently has no discovered capabilities."

        lines = ["I can currently help with:", ""]

        for capability in capabilities:
            if capability.name == "time.current_time":
                friendly_name = "Telling you the current time"
            elif capability.name == "time.current_date":
                friendly_name = "Telling you today's date"
            elif capability.name == "filesystem.list_pdfs":
                friendly_name = "Finding PDF files on your computer"
            else:
                friendly_name = capability.name.replace(".", " → ")

            lines.append(f"• {friendly_name}")
            lines.append(f"  Capability: {capability.name}")

            if capability.description:
                lines.append(f"  Description: {capability.description}")

            lines.append("")

        return "\n".join(lines).rstrip()
