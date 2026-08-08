# AXIS — AI Constitution

## Mission

Build a modular personal AI operating system capable of understanding requests, planning actions, and executing capabilities through independent systems and plugins while remaining reliable, auditable, and extensible.

The current repository is a tested Python foundation. Future capabilities must not be described as implemented until code and tests support them.

## Core Principles

1. Never sacrifice architecture for speed.
2. Every feature must be modular.
3. Every module must have one clear responsibility.
4. Runtime controls capability execution.
5. Plugins remain independent.
6. Plugins communicate through approved system layers.
7. Preserve backward compatibility unless an approved change replaces an interface.
8. Avoid duplicated functionality.
9. Prefer composition over unnecessary inheritance.
10. Keep subsystems replaceable where practical.
11. Keep documentation synchronized with implementation.

## Canonical Current Execution Flow

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

Memory is accessed through Runtime. Command Engine is implemented and tested as a supporting plan-to-task conversion subsystem, but is not currently part of the primary `Agent.process()` path.

## Boundary Rules

- Runtime owns capability execution.
- Planner owns plan creation.
- Executor owns plan traversal.
- Memory owns persistence and retrieval.
- Plugin Manager owns plugin registration and resolution.
- Plugins expose isolated capabilities.
- Agent owns application-level coordination.
- Never bypass Runtime.
- Never allow direct plugin-to-plugin communication.
- Never create a duplicate execution path.
- Never put plugin-specific business logic into orchestration components.
- Never document future architecture as current implementation.

## Engineering Standards

Always:

- use Python type hints where appropriate
- keep functions focused
- document public behavior where useful
- use clear naming
- write testable code
- keep modules loosely coupled
- prefer readable, maintainable solutions

Avoid:

- global state without a clear reason
- circular imports
- hardcoded plugin names
- duplicate systems
- hidden dependencies
- breaking existing interfaces without approval

## AI Agent Responsibilities

### Architecture Authority

The human owner approves architectural direction. AI assistants may analyze, propose, implement approved changes, and identify conflicts, but must not silently change architectural boundaries.

### Implementation Assistants

AI coding tools should:

- inspect before editing
- follow the canonical references
- make the smallest coherent change
- add or update tests
- report architecture impact
- report test results accurately

### Review Assistants

Review-oriented AI tools should identify architectural, security, compatibility, maintainability, and documentation risks without treating proposed future systems as current implementation.

## Definition of Done

A feature is complete when it is:

✓ Implemented

✓ Tested

✓ Documented when behavior or architecture requires it

✓ Compatible or explicitly approved as breaking

✓ Reviewed

✓ Committed

## Decision Priority

1. Architecture
2. Reliability
3. Maintainability
4. Security
5. Performance
6. Convenience