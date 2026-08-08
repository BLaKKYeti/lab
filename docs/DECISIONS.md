# AXIS Architecture Decision Records

This document records significant architectural decisions made during AXIS development.

ADRs document decisions and their historical context. They do not override the current implementation or the binding current-state architecture rules.

---

## ADR-001: Repository Structure

- **Status:** Accepted
- **Date:** 2026-08-04

### Context

AXIS requires a modular repository structure that supports separation of responsibilities, testing, documentation, and incremental development.

### Decision

AXIS uses a modular Python repository organized around its core subsystems, including:

- `agent/`
- `config/`
- `core/`
- `execution/`
- `kernel/`
- `planner/`
- `tests/`
- `docs/`
- `standards/`

### Consequences

- Responsibilities remain separated.
- Core components can evolve independently.
- Architectural boundaries must be maintained as the system grows.

---

## ADR-002: Python as the Primary Language

- **Status:** Accepted
- **Date:** 2026-08-04

### Context

AXIS requires rapid development, automation support, and access to the Python ecosystem for AI and systems development.

### Decision

Python is the primary implementation language for the AXIS core.

### Consequences

- Rapid development and iteration.
- Broad ecosystem support.
- External integrations can be introduced through defined interfaces as the project evolves.

---

## ADR-003: Modular Architecture

- **Status:** Accepted
- **Date:** 2026-08-04

### Context

AXIS needs clearly separated responsibilities so that planning, execution, memory, and capabilities do not become a single monolithic system.

### Decision

AXIS is organized into distinct components with explicit ownership boundaries.

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

Consequences
Components have clear responsibilities.
Execution ownership remains centralized.
Capabilities can be added without embedding capability-specific behavior into the Agent or Planner.
ADR-004: GitHub for Version Control
Status: Accepted
Date: 2026-08-04
Context

AXIS requires version control, development history, remote backup, and collaboration support.

Decision

Git and GitHub are used as the primary version-control and repository platform.

Consequences
Development history is preserved.
Branches and checkpoints provide recovery points.
Remote collaboration and review are available.
ADR-005: VS Code as Development Environment
Status: Accepted
Date: 2026-08-04
Context

AXIS requires a practical local development environment with strong Python and Git support.

Decision

Visual Studio Code is the recommended development environment.

Consequences
Consistent local development workflow.
Strong Python tooling.
Easy integration with AI development tools.

The architecture does not depend on a specific editor.

ADR-006: Multi-Provider AI Integration
Status: Proposed
Date: 2026-08-04
Context

AXIS is intended to work with multiple AI systems rather than permanently depend on a single provider.

Decision

AXIS should eventually support multiple AI providers through explicit integration boundaries.

Potential providers include local and external AI models.

Current Status

Provider integration and intelligent model routing are future capabilities unless implemented and verified in the current codebase.

Consequences

Core orchestration should avoid unnecessary provider-specific assumptions.

ADR-007: External Capability Integration
Status: Proposed
Date: 2026-08-04
Context

AXIS is intended to interact with external tools, applications, filesystems, and services.

Decision

External capabilities should be introduced through controlled capability/plugin boundaries rather than being embedded directly into core orchestration components.

Current Status

The plugin architecture is implemented.

Specific external integrations are future work unless their implementation and tests exist in the current repository.

Consequences
Capabilities remain isolated.
New integrations can be introduced incrementally.
Core orchestration remains independent from capability-specific implementation.
ADR-008: Memory-First Design
Status: Accepted
Date: 2026-08-04
Context

A persistent AI system requires continuity across interactions and runtime sessions.

Decision

Memory is a first-class AXIS subsystem responsible for persistence and retrieval of AXIS state and history.

Runtime provides the controlled access boundary for memory.

Current Status

The memory subsystem is implemented and includes persistence, retrieval, and recovery behavior.

Consequences
AXIS can retain information across runtime sessions.
Storage responsibilities remain centralized.
Other components must use defined memory interfaces rather than duplicating persistence logic.
ADR-009: Centralized Runtime Execution
Status: Accepted
Date: 2026-08-07
Context

Multiple execution paths would make capability behavior difficult to control and create architectural ambiguity.

Decision

Runtime is the central execution boundary for AXIS.

The Executor delegates capability execution to Runtime.

The Plugin Manager coordinates plugin registration and resolution for Runtime.

Plugins perform capability-specific operations but do not create alternate orchestration paths.

Consequences
Execution ownership is explicit.
Plugins cannot silently create independent execution systems.
Runtime remains the controlled boundary between orchestration and capabilities.
ADR-010: Planner and Executor Separation
Status: Accepted
Date: 2026-08-07
Context

Planning and execution have different responsibilities and should remain independently testable.

Decision

The Planner creates ExecutionPlan objects containing Step objects.

The Executor traverses and executes those plans.

The Planner does not directly execute plugins or perform execution side effects.

Consequences
Plans can be inspected independently of execution.
Planning remains separate from capability execution.
Execution behavior can be tested independently.
ADR-011: Command Engine as Supporting Subsystem
Status: Accepted
Date: 2026-08-07
Context

AXIS contains a Command Engine for converting structured plans into executable task representations.

Without a defined boundary, the Command Engine could become a duplicate execution system.

Decision

The Command Engine is a supporting command/task-conversion subsystem.

It is not a required stage in the current Agent.process() execution path.

The Command Engine must not:

execute plugins directly
bypass Runtime
replace the Executor
create an alternate execution path
Consequences

Command conversion can evolve independently while execution ownership remains centralized.

ADR-012: Plugin-Based Capability Architecture
Status: Accepted
Context

AXIS requires extensible capabilities without embedding every capability into the orchestration core.

Decision

Capabilities are exposed through plugins managed by the Plugin Manager.

Plugins are isolated from one another and from direct application orchestration.

Consequences
Capabilities are replaceable.
New capabilities can be added incrementally.
Plugin-specific behavior remains outside core orchestration components.
ADR-013: Current-State Documentation
Status: Accepted
Date: 2026-08-07
Context

AXIS is developed with multiple AI tools. Documentation drift can cause different development tools to operate from conflicting architectural assumptions.

Decision

Current-state documentation must describe what the repository actually implements.

Future architecture must be clearly separated from current implementation.

The canonical current-state architecture is defined by:

docs/ARCHITECTURE_MAP.md
standards/ARCHITECTURE_RULES.md

The high-level architecture is documented in:

docs/ARCHITECTURE.md
Consequences
AI tools have a consistent architectural reference.
Documentation cannot silently redefine implementation.
Architectural changes require corresponding documentation updates.
ADR-014: Tests as Architectural Verification
Status: Accepted
Date: 2026-08-07
Context

Architectural claims should be supported by verified behavior wherever practical.

Decision

Changes to core behavior must be verified through automated tests.

The current core test suite must pass before a development checkpoint is considered stable.

Consequences
Regressions are detected earlier.
Architectural changes can be validated against executable behavior.
Documentation can be compared against verified implementation.
Historical Architecture

Earlier AXIS/LAB AI OS documentation described concepts including:

Registry
Resolver
Workers
Event Bus
Connectors
distributed scheduling
multi-agent clusters
generalized interfaces and SDK layers

These concepts may remain relevant to the long-term vision or requirements, but they are not part of the current architecture unless implemented and verified.

Historical architecture must not be presented as current implementation.

ADR Governance

Before changing an architectural boundary:

Inspect the current implementation.
Inspect affected tests.
Identify affected documentation.
Record the intended architectural decision.
Implement the smallest coherent change.
Run affected tests.
Synchronize canonical documentation.
Review the Git diff.
Commit only after verification.

ADRs should be updated or superseded when an approved architectural decision changes.

ADRs do not replace the current implementation, automated tests, or binding architecture rules.