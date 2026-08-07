# AXIS Core Architecture Map

## Canonical Execution Pipeline

User
↓
Agent
↓
Intent Engine
↓
Planner
↓
Command Engine
↓
Runtime
↓
Plugins
↓
Memory
↓
Response

---

## Responsibilities

### Agent
- Receives user requests.
- Coordinates the pipeline.
- Does not execute commands.

### Intent Engine
- Determines user intent.
- Produces structured intents.
- Does not create execution logic.

### Planner
- Converts intents into execution plans.
- Selects required capabilities.
- Never executes plugins directly.

### Command Engine
- Executes the Planner's execution plan.
- Coordinates Runtime calls.

### Runtime
- Owns execution.
- Manages plugin lifecycle.
- Executes validated tasks.

### Plugins
- Expose capabilities.
- Perform isolated operations.
- Never communicate directly with users.

### Memory
- Stores long-term knowledge.
- Stores execution history.
- Stores preferences and project knowledge.
- Supplies context to planning.

---

## Architectural Rules

- Runtime owns execution.
- Planner owns planning.
- Memory owns persistence.
- Plugins expose capabilities only.
- Agent coordinates the system.
- Components communicate through defined interfaces.
- Avoid duplicate execution paths.
- Preserve backward compatibility whenever possible.