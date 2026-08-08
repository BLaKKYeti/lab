# AXIS Deprecation Plan

## Status

**Current-state maintenance document.**

This document tracks legacy, duplicate, temporary, or superseded components in the AXIS repository.

Deprecation status must reflect the actual implementation. A component must not be marked for removal merely because a future architecture is planned.

---

## Current Deprecation Candidates

| Component | Status | Current Relationship | Action |
|---|---|---|---|
| `plugin_registry` | Review Required | Possible legacy/duplicate plugin registration path | Inspect implementation before removal |
| `registry` | Review Required | May represent an older capability/service registry design | Inspect implementation before removal |
| `resolver` | Review Required | Legacy component requiring architectural reconciliation | Do not replace with Planner |
| `connector_loader` | Active / Review Required | Existing connector-loading functionality | Preserve until replacement is verified |
| filesystem connector | Review Required | Existing connector capability | Compare with filesystem plugin implementation |
| filesystem plugin | Active | Current plugin-based capability | Preserve |
| legacy execution paths | Temporary | May overlap with Runtime/Executor behavior | Remove only after migration is verified |

---

## Deprecation Rules

1. Never delete code without identifying its replacement.
2. Inspect implementation and tests before marking a component for removal.
3. Deprecate before removal when compatibility requires it.
4. Remove only after the replacement is implemented and tested.
5. Preserve backward compatibility unless an approved architectural change explicitly replaces an interface.
6. Update affected documentation after every removal or migration.
7. Do not treat planned architecture as an implemented replacement.
8. Do not introduce duplicate execution paths during migration.

---

## Architectural Boundary

The current execution architecture is:

```text
User
  ↓
Agent
  ↓
Intent Engine
  ↓
Planner
  ↓
Executor
  ↓
Runtime
  ↓
Plugin Manager
  ↓
Plugin
  ↓
Result / Response

Memory is accessed through Runtime.

Command Engine exists as a supporting execution/task-conversion subsystem and is not currently a required stage in Agent.process().

Review Procedure

Before removing or replacing a component:

Inspect its implementation.
Inspect all imports and callers.
Inspect related tests.
Determine whether another subsystem already provides the same capability.
Identify compatibility requirements.
Update the architecture documentation if ownership changes.
Implement the smallest coherent migration.
Run the affected test suite.
Remove the deprecated component only after verification.