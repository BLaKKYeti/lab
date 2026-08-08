# AXIS Plugin Specification

## Status

**Binding plugin contract for the current AXIS architecture.**

## Purpose

Define the standard contract and responsibilities for AXIS plugins.

Plugins provide isolated capabilities to the AXIS Runtime through the Plugin Manager.

---

## Plugin Requirements

Every plugin must provide:

- Identity
- Capabilities
- Execution
- Health status

Plugins must remain isolated from orchestration logic and from direct plugin-to-plugin communication.

---

## Required Interface

Example:

```python
class Plugin:

    NAME = "plugin_name"
    VERSION = "1.0"

    def capabilities(self):
        pass

    def execute(self, task):
        pass

    def health(self):
        pass