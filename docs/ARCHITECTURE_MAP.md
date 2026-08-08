# AXIS Core Architecture Map

## Status

**Canonical current-state architecture.**

This document describes what AXIS implements today. It is the source of truth for the current execution path. Future architecture belongs in `docs/ARCHITECTURE.md` and must not be described as implemented until the code supports it.

## Canonical Execution Pipeline

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

### Memory

Memory is a persistent subsystem owned and exposed through Runtime. The Agent also records conversation results through Runtime after execution.

### Command Engine

Command Engine is an implemented subsystem for converting structured plans into executable task representations. It is not currently part of the Agent's primary `process()` execution path.

## Current Component Responsibilities

### Agent
- Application-level coordinator and user-facing loop.
- Resolves intent, creates plans, and delegates plan execution.
- Starts and owns the Runtime instance.
- Does not implement plugin functionality.

### Intent Engine
- Converts user input into structured intent.
- Does not execute capabilities.

### Planner
- Converts an intent into an `ExecutionPlan` containing `Step` objects.
- Does not execute plugins.

### Executor
- Executes an `ExecutionPlan` against Runtime.
- Delegates actual capability execution to Runtime.

### Command Engine
- Converts execution-plan steps into executable task representations.
- Coordinates command/task preparation.
- Must not bypass Runtime for plugin execution.

### Runtime
- Central execution boundary.
- Owns memory access and plugin-manager coordination.
- Executes validated plugin operations and returns structured results.

### Plugin Manager
- Registers, resolves, and coordinates plugins for Runtime.
- Keeps plugin implementations isolated from the core orchestration flow.

### Plugins
- Expose isolated capabilities.
- Perform capability-specific operations.
- Do not own system orchestration.

### Memory
- Persists conversations, events, profiles, preferences, and related project knowledge.
- Supports retrieval, search, recent records, and recovery behavior.
- Is accessed through the Runtime boundary in the current architecture.

## Architectural Rules

- Runtime owns execution.
- Planner owns plan creation.
- Executor owns plan traversal.
- Memory owns persistence.
- Plugins expose capabilities.
- Agent coordinates the application flow.
- Do not create duplicate execution paths.
- Do not describe planned/future subsystems as implemented.
- Preserve backward compatibility unless an approved architecture change explicitly replaces an interface.
