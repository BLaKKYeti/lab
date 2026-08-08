# AXIS — Project Context

## Status

AXIS is an active software project. This document describes the current project state and mission.

## Vision

AXIS is a personal AI operating system designed to understand requests, plan actions, execute capabilities through modular plugins, persist useful memory, and grow without sacrificing architectural integrity.

The current implementation is a Python foundation for that larger vision. Future capabilities must be introduced as explicit, tested architecture changes rather than assumed to already exist.

## Current Mission

Build a reliable AI orchestration foundation that can:

- Understand user intent.
- Turn intent into structured plans.
- Execute plans through a controlled Runtime boundary.
- Expose capabilities through independent plugins.
- Persist and retrieve useful memory.
- Support AI-assisted development without losing architectural continuity.

## Canonical Current Architecture

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

Memory is a persistent subsystem accessed through Runtime. Command Engine exists and is tested, but is not currently part of Agent.process()'s primary execution path.

The authoritative current-state architecture is `docs/ARCHITECTURE_MAP.md`.

## Current Implementation Status

Implemented and tested foundations include:

- Agent layer
- Intent Engine
- Planner and execution-plan structures
- Command Engine
- Executor
- Runtime
- Plugin Manager
- Plugin architecture
- Persistent memory layer
- Memory recovery behavior
- Logger foundation
- Configuration foundation
- Pytest testing foundation
- AI development instructions and standards

The exact implementation state is determined by the code and tests, not by older roadmap language.

## Current Development Priorities

1. Keep documentation and AI instructions synchronized with the implementation.
2. Strengthen architecture boundaries and contracts.
3. Expand execution capabilities through plugins.
4. Integrate model providers and local model support through explicit adapters.
5. Build toward richer orchestration, memory use, voice control, and autonomous workflows only after their architecture is defined and tested.

## AI Development Workflow

AI coding agents are implementation tools, not the final authority on architecture.

Before making changes:

1. Read the canonical project and architecture documents.
2. Inspect the relevant implementation and tests.
3. Identify the owning component.
4. Explain architecture impact.
5. Make the smallest coherent change.

After making changes:

- run the relevant tests
- report files changed
- report architecture impact
- report test results
- keep documentation synchronized when behavior changes

## Engineering Principles

Prefer:

- simplicity
- modularity
- explicit ownership
- testability
- maintainability
- backward compatibility
- small, reviewable changes

Avoid:

- duplicate systems
- hidden dependencies
- bypassing Runtime
- business logic in orchestration layers
- describing future systems as current functionality
- unnecessary rewrites

## Definition of Success

AXIS should evolve into a capable personal AI operating system while remaining understandable, testable, auditable, and extensible. Every implementation change should strengthen that foundation rather than merely increase the amount of code.