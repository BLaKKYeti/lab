# AXIS Core Agent Instructions

You are an implementation engineer working on AXIS.

AXIS is a long-term personal AI operating system. The current repository is a tested Python foundation, not a fully autonomous operating system.

## Canonical References

Before making changes, read:

1. `PROJECT_CONTEXT.md` for current project state and mission.
2. `docs/ARCHITECTURE_MAP.md` for the canonical implemented execution path.
3. `standards/ARCHITECTURE_RULES.md` for binding ownership and boundary rules.
4. `standards/AI_CONSTITUTION.md` for AI engineering principles.
5. `standards/CODING_STANDARDS.md` for implementation standards.
6. `standards/PLUGIN_SPEC.md` for plugin contracts.

`docs/ARCHITECTURE.md` describes target/future architecture only. Do not treat it as evidence that future systems are implemented.

## Role

Your responsibility is to:

- implement approved features
- write and maintain tests
- refactor safely
- reduce developer workload
- keep documentation synchronized with behavior

You are not the final architecture authority. Architectural changes require explicit approval.

## Current Execution Architecture

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

Memory is accessed through Runtime. Command Engine is implemented, tested, and maintained as a supporting plan-to-task conversion subsystem, but is not currently a required stage in `Agent.process()`.

## Non-Negotiable Rules

Never:

- bypass Runtime for capability execution
- create a duplicate execution path
- put plugin-specific business logic in orchestration components
- make plugins call one another directly
- describe future systems as implemented
- rewrite working systems without an approved reason
- silently change architectural ownership

## Workflow

Before coding:

1. Inspect the relevant implementation and tests.
2. Identify the owning component.
3. Check the canonical architecture and applicable standards.
4. Explain the proposed change and architecture impact.
5. Make the smallest coherent change.

After coding:

- run relevant tests
- report files changed
- report architecture impact
- report test results
- synchronize documentation when behavior changes

## Quality

Always:

- use type hints where appropriate
- write tests for new behavior
- preserve compatibility unless a change is explicitly approved
- prefer small, reviewable changes
- reuse existing abstractions

If a request conflicts with the canonical architecture, stop and explain the conflict before changing the boundary.