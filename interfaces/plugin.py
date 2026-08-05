from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Base interface for every LAB AI OS plugin.
    """

    @abstractmethod
    def name(self) -> str:
        """Return the unique plugin name."""
        pass

    @abstractmethod
    def initialize(self, config: dict):
        """Initialize the plugin."""
        pass

    @abstractmethod
    def execute(self, task):
        """Execute a task."""
        pass

    @abstractmethod
    def shutdown(self):
        """Clean up before shutdown."""
        pass