# Deprecation Plan

This document tracks duplicate or temporary systems.

No component should be removed until its replacement is fully integrated and tested.

---

| Component | Status | Replacement | Action |
|-----------|--------|-------------|--------|
| plugin_registry | Review Required | Plugin Manager | Keep until migration complete |
| registry | Review Required | Capability Registry | Keep |
| resolver | Review Required | Planner | Keep |
| connector_loader | Active | None | Keep |
| filesystem connector | Review Required | Filesystem Plugin | Evaluate after Planner integration |
| filesystem plugin | Active | None | Keep |
| legacy execution paths | Temporary | Planner + Runtime | Remove after migration |

---

## Rules

- Never delete code without a replacement.
- Deprecate before removal.
- Remove only after tests pass.
- Update documentation after every removal.