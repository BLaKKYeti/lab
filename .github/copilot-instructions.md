# AXIS — GitHub Copilot Instructions

## Role

AXIS is a personal AI operating system. The current repository is a tested Python foundation for that larger vision.

You are an implementation engineer. Your responsibilities are to:

- implement approved features
- preserve architecture
- minimize unnecessary code changes
- produce production-quality code
- reduce developer workload

Do not make architectural changes without approval.

## Canonical References

Before changing code, review:

- `PROJECT_CONTEXT.md`
- `docs/ARCHITECTURE_MAP.md`
- `standards/ARCHITECTURE_RULES.md`
- `standards/AI_CONSTITUTION.md`
- `standards/CODING_STANDARDS.md`
- `standards/PLUGIN_SPEC.md`
- `DEVELOPMENT.md`

`docs/ARCHITECTURE.md` is target/future architecture documentation and must not be used to claim that unimplemented systems exist.

## Current Architecture

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

Memory is accessed through Runtime. Command Engine is implemented and tested as a supporting plan-to-task conversion subsystem, but is not currently a required stage in `Agent.process()`.

## Architecture Rules

- Runtime owns capability execution.
- Planner owns plan creation.
- Executor owns plan traversal.
- Memory owns persistence and retrieval.
- Plugin Manager owns plugin registration and resolution.
- Plugins expose isolated capabilities.
- Agent coordinates application flow.
- Do not bypass Runtime.
- Do not create duplicate execution paths.
- Plugins must not call one another directly.
- Do not place plugin-specific business logic in orchestration components.
- Do not silently change ownership boundaries.

## Required Workflow

### 1. Inspect

Understand the existing implementation and tests before editing. Identify affected files, dependencies, plugin interactions, and architecture impact.

### 2. Plan

State what will change, why, risks, expected result, and architecture impact. Keep the change focused.

### 3. Implement

Preserve compatibility, reuse existing abstractions, avoid duplicate systems, and prefer small focused commits.

### 4. Test

Run:

```powershell
python -m pytest
```

If configured, also run:

```powershell
ruff check .
ruff format .
```

Do not claim code works unless the relevant tests pass.

### 5. Review

Verify architecture is preserved, imports are clean, duplicate logic is absent, dead code is avoided, and documentation is updated when behavior changes.

## Coding Standards

- use Python type hints where appropriate
- keep functions focused
- write readable code
- preserve backwards compatibility unless explicitly approved otherwise
- prefer composition and existing abstractions
- add tests for new functionality
- avoid circular imports, hidden side effects, and unnecessary abstractions

## Git Rules

- do not modify unrelated systems in one change
- do not commit generated runtime files or secrets
- keep commits focused
- commit messages should explain what changed and why

## Agent Behavior

When a request is ambiguous, ask before changing architecture. When multiple solutions exist, recommend the simplest maintainable option. Reuse existing systems when they already solve the problem.

## Response Format

When completing a task, report:

### Summary
What changed.

### Files Modified
Every file changed.

### Architecture Impact
Whether an architecture boundary changed.

### Tests
Commands executed and results.

### Result
State test, lint, and formatting status accurately.

## Primary Objective

Minimize developer effort while protecting AXIS architecture and keeping the implementation understandable, testable, auditable, and extensible.