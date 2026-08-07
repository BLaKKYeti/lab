import importlib
import inspect
import pkgutil
from typing import Any, Dict, List, Optional

from interfaces.plugin import Plugin


class PluginManager:
    """Discover, register, and expose plugin capabilities."""

    def __init__(self) -> None:
        """Initialize plugin manager storage."""
        self.plugins: Dict[str, Plugin] = {}
        self.capabilities: Dict[str, Dict[str, Any]] = {}

    def register(self, plugin: Plugin) -> None:
        """Register a plugin and record its capabilities."""
        name = plugin.name()
        self.plugins[name] = plugin
        self.capabilities[name] = {
            "description": plugin.description(),
            "actions": plugin.actions(),
        }

    def discover_plugins(self) -> None:
        """Discover and register plugins from the plugins package."""
        package = importlib.import_module("plugins")
        for _, module_name, _is_pkg in pkgutil.iter_modules(package.__path__):
            if module_name.startswith("__"):
                continue
            try:
                module = importlib.import_module(f"plugins.{module_name}.plugin")
                for _, obj in inspect.getmembers(module):
                    if (
                        inspect.isclass(obj)
                        and issubclass(obj, Plugin)
                        and obj is not Plugin
                    ):
                        plugin = obj()
                        self.register(plugin)
            except Exception as e:
                print("Plugin load error:", module_name, e)

    def load_builtin_plugins(self) -> None:
        """Discover plugins provided by the current package."""
        self.discover_plugins()

    def list_plugins(self) -> List[str]:
        """List the registered plugin names."""
        return list(self.plugins.keys())

    def get(self, name: str) -> Optional[Plugin]:
        """Return a registered plugin instance by name."""
        return self.plugins.get(name)

    def get_capabilities(self) -> Dict[str, Dict[str, Any]]:
        """Return the capabilities dictionary for registered plugins."""
        return self.capabilities
