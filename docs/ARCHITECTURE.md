# AXIS Architecture

## Status

**Canonical high-level architecture for the current AXIS implementation.**

This document describes the architecture that AXIS implements today. It distinguishes current implementation from future capabilities so that development tools and contributors do not mistake planned systems for existing ones.

For the detailed current execution path, see `docs/ARCHITECTURE_MAP.md`.

---

## 1. System Overview

AXIS is an AI orchestration platform designed to coordinate user intent, planning, execution, runtime capabilities, persistent memory, and extensible plugins.

The current implementation is centered around a controlled execution pipeline:

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
```

The architecture is intentionally modular. Each subsystem has a defined responsibility and execution boundaries are preserved between components.

---

## 2. Current Architecture

### Agent

The Agent is the application-level coordinator.

Responsibilities:

* Accept user input.
* Resolve user intent.
* Create execution plans.
* Delegate execution to the Executor.
* Own and coordinate the Runtime instance.
* Record relevant execution results through Runtime.
* Produce the final application response.

The Agent must not implement plugin-specific capabilities or create an alternate execution path around Runtime.

---

### Intent Engine

The Intent Engine converts user input into structured intent.

Responsibilities:

* Interpret incoming user requests.
* Produce structured intent information for the Planner.
* Separate intent resolution from execution.

The Intent Engine does not execute plugins or perform capability-specific side effects.

---

### Planner

The Planner converts structured intent into an `ExecutionPlan`.

Responsibilities:

* Determine the steps required to satisfy an intent.
* Construct `Step` objects.
* Produce a structured execution plan for the Executor.

The Planner does not execute plugins or perform execution-side effects.

---

### Executor

The Executor traverses and executes an `ExecutionPlan`.

Responsibilities:

* Process plan steps in the defined execution order.
* Delegate capability execution to Runtime.
* Preserve structured execution results.

The Executor is responsible for plan traversal, but Runtime remains the central execution boundary.

The Executor must not contain plugin-specific implementations.

---

### Runtime

Runtime is the central execution boundary of AXIS.

Responsibilities:

* Coordinate execution of capabilities.
* Coordinate the Plugin Manager.
* Provide controlled access to persistent Memory.
* Execute validated plugin operations.
* Return structured execution results.
* Provide the boundary between orchestration and capability execution.

Runtime must not become a general-purpose application layer or contain plugin-specific business logic.

---

### Plugin Manager

The Plugin Manager manages the available plugins used by Runtime.

Responsibilities:

* Register plugins.
* Resolve plugins.
* Coordinate plugin access for Runtime.
* Keep plugin implementations isolated from the core orchestration flow.

The Plugin Manager does not replace Runtime as the execution boundary.

---

### Plugins

Plugins expose isolated capabilities to AXIS.

Responsibilities:

* Implement capability-specific behavior.
* Receive execution requests through the Runtime/Plugin Manager path.
* Return capability-specific results.

Plugins must remain isolated from the application's orchestration logic.

Plugins must not:

* Create alternate execution paths.
* Directly control the Agent.
* Bypass Runtime.
* Depend directly on other plugins for orchestration.

---

### Memory

Memory is a persistent subsystem of AXIS.

Responsibilities include:

* Persisting conversations and records.
* Retrieving stored information.
* Searching relevant records.
* Maintaining persistent project and agent context.
* Supporting recovery behavior.
* Preserving structured state across runtime sessions.

Memory is accessed through the Runtime boundary in the current architecture.

Memory owns persistence logic and callers should use its defined interfaces rather than duplicating storage behavior.

---

### Command Engine

The Command Engine is an implemented supporting subsystem.

It converts structured execution-plan steps into executable task representations.

The Command Engine is **not currently a required stage in the primary `Agent.process()` execution path**.

It must not become a second execution engine or bypass Runtime.

Its role may expand in a future architectural change, but such a change must be explicitly designed, implemented, tested, and documented before being treated as current architecture.

---

### Logger

The Logger provides application-level logging infrastructure.

Responsibilities:

* Record operational events.
* Support debugging and observability.
* Provide structured logging facilities to core components.

Runtime log files are operational data and are not part of the source architecture.

---

## 3. Architectural Boundaries

AXIS maintains the following ownership boundaries:

| Component      | Primary Responsibility                    |
| -------------- | ----------------------------------------- |
| Agent          | Application coordination                  |
| Intent Engine  | Intent resolution                         |
| Planner        | Plan creation                             |
| Executor       | Plan traversal and execution coordination |
| Runtime        | Central execution boundary                |
| Plugin Manager | Plugin registration and resolution        |
| Plugins        | Capability-specific behavior              |
| Memory         | Persistence and retrieval                 |
| Command Engine | Task/command conversion                   |
| Logger         | Operational logging                       |

The following rules are mandatory:

1. Runtime owns capability execution.
2. Planner owns plan creation.
3. Executor owns plan traversal.
4. Memory owns persistence.
5. Plugins expose capabilities.
6. Agent owns application-level coordination.
7. Components must not create duplicate execution systems.
8. Plugin-specific behavior must remain outside orchestration components.
9. Future architecture must not be described as implemented.
10. Existing interfaces must remain backward compatible unless an approved architecture change explicitly replaces them.

---

## 4. Execution Lifecycle

A normal AXIS request currently follows this conceptual lifecycle:

1. The user provides a request.
2. The Agent receives the request.
3. The Intent Engine resolves the request into structured intent.
4. The Planner converts the intent into an `ExecutionPlan`.
5. The Executor traverses the plan.
6. Runtime coordinates execution of required capabilities.
7. Runtime uses the Plugin Manager to resolve appropriate plugins.
8. Plugins perform their isolated capability-specific operations.
9. Results return through Runtime and the Executor.
10. The Agent records relevant results through Runtime and produces the response.

Memory may participate in the lifecycle through Runtime when persistent context or historical information is required.

---

## 5. Current Repository Architecture

The current implementation is organized around the following primary components:

```text
agent/
    Agent coordination

kernel/
    Intent Engine
    Runtime
    Memory
    Plugin Manager
    Command Engine

planner/
    ExecutionPlan
    Step
    Planner interfaces
    Planner implementation

execution/
    Executor
    ExecutionResult

core/
    Logging infrastructure

tests/
    Automated verification
```

The exact repository structure may evolve, but architectural ownership must remain consistent with the boundaries defined in this document and `docs/ARCHITECTURE_MAP.md`.

---

## 6. Current Capabilities

The current AXIS implementation includes:

* Agent coordination.
* Intent resolution.
* Execution planning.
* Execution-plan traversal.
* Runtime execution boundaries.
* Plugin management.
* Plugin architecture.
* Persistent memory.
* Memory recovery behavior.
* Runtime persistence.
* Command/task conversion infrastructure.
* Logging infrastructure.
* Automated tests.

The current implementation should be treated as the authoritative source for capability availability.

---

## 7. Future Architecture

AXIS is intended to grow beyond its current implementation.

Potential future capabilities may include:

* Local and remote LLM provider integration.
* Ollama integration.
* Intelligent model selection between local and external models.
* Voice interaction.
* Desktop and operating-system automation.
* Expanded tool and connector capabilities.
* More advanced memory and retrieval systems.
* Multi-agent coordination.
* Sandboxed capability execution.
* Advanced observability and auditing.
* Distributed execution.

These capabilities are **future architecture unless their implementation exists in the repository and has been verified by tests or explicit integration validation**.

Future concepts must never be presented as current implementation.

---

## 8. Architectural Change Policy

Before changing an architectural boundary:

1. Inspect the current implementation.
2. Inspect affected tests.
3. Identify affected documentation and AI instructions.
4. Define the intended architectural decision.
5. Implement the smallest coherent change.
6. Add or update tests.
7. Run the affected test suite.
8. Synchronize canonical documentation.
9. Review the resulting diff.
10. Commit only after the implementation and documentation agree.

Architecture changes must not be introduced indirectly through refactoring or feature work.

---

## 9. Canonical Documentation

The documentation hierarchy is:

### Current-state architecture

`docs/ARCHITECTURE_MAP.md`

Defines the detailed execution path and current component responsibilities.

### High-level architecture

`docs/ARCHITECTURE.md`

Defines the overall architecture and boundaries described in this document.

### Binding architecture rules

`standards/ARCHITECTURE_RULES.md`

Defines mandatory architectural ownership and development constraints.

### Architecture decisions

`docs/DECISIONS.md`

Records historical and approved architectural decisions.

### AI development instructions

`AGENTS.md`, `.github/prompts/`, and `docs/AI_WORKFLOW.md`

Define how AI development tools must operate within the canonical architecture.

These documents must remain consistent with the implementation. When documentation conflicts with verified code and tests, the conflict must be resolved before further architectural development.

---

## 10. Source of Truth

The hierarchy of truth is:

```text
Verified implementation + tests
            ↓
docs/ARCHITECTURE_MAP.md
            ↓
standards/ARCHITECTURE_RULES.md
            ↓
docs/ARCHITECTURE.md
            ↓
AI instructions and project documentation
```

Documentation exists to describe the system, not to override it.

AXIS development must preserve this relationship.
