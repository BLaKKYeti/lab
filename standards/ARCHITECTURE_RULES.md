# AXIS — Architecture Rules

## Status

**Binding current-state architecture rules.**

These rules define ownership and boundaries for the architecture that exists today. Future systems may extend AXIS, but they must not be presented as implemented until their code and tests exist.

## Canonical Execution Flow

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

Memory is accessed through Runtime. Command Engine is implemented but is currently a supporting execution/task-conversion subsystem rather than a required stage in Agent.process().

## Ownership Rules

### Agent

Owns application-level coordination and the interactive loop.

Must not:

- implement plugin-specific behavior
- bypass Runtime for capability execution
- become a second execution engine

### Intent Engine

Owns intent resolution.

Must not:

- execute plugins
- own execution policy
- contain capability implementations

### Planner

Owns conversion of structured intent into an execution plan.

Must not:

- execute plugins
- directly perform side effects

### Executor

Owns traversal/execution of an `ExecutionPlan`.

Must:

- delegate capability execution to Runtime
- preserve structured execution results

Must not:

- implement plugin-specific behavior
- create an alternate path around Runtime

### Command Engine

Owns command/task conversion for execution plans.

Must not:

- directly execute plugins
- bypass Runtime
- become a duplicate of Executor

### Runtime

Owns the central execution boundary.

Must:

- coordinate plugin execution
- coordinate plugin management
- provide controlled access to persistent memory
- return structured results

Must not:

- contain plugin-specific business logic
- become a general-purpose application layer

### Plugin Manager

Owns plugin registration and resolution/coordination for Runtime.

Plugins must remain isolated from one another and from direct user interaction.

### Plugins

Own capability-specific behavior.

Plugins must be:

- independent
- replaceable
- self-contained

Plugins must not:

- call other plugins directly
- modify orchestration behavior
- create alternate execution paths

### Memory

Owns persistence and retrieval of AXIS state and history.

Memory implementation details may evolve, but callers must use its defined interfaces rather than duplicating storage logic.

## Change Management

Before changing an architectural boundary:

1. Inspect the current implementation.
2. Check tests and compatibility.
3. Identify all affected documentation.
4. Document the intended decision.
5. Implement the smallest coherent change.
6. Run affected tests.
7. Synchronize canonical documentation.

## Non-Negotiable Rules

- Do not bypass Runtime.
- Do not create duplicate execution systems.
- Do not put plugin-specific business logic into orchestration components.
- Do not silently change architectural ownership.
- Do not document future architecture as current implementation.
- Preserve backward compatibility unless an approved architecture change explicitly replaces it.
