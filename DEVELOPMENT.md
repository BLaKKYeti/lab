# AXIS Development Guide

## Mission

AXIS is a modular personal AI operating system designed to understand requests, plan actions, and execute capabilities through plugins.

The current repository is a tested Python foundation. Development should strengthen the existing architecture rather than assume future systems already exist.

## Canonical Architecture

The current execution path is:

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

Memory is accessed through Runtime. Command Engine exists and is tested, but currently serves as a supporting plan-to-task conversion subsystem rather than a required stage in `Agent.process()`.

For authoritative current-state details, use `docs/ARCHITECTURE_MAP.md` and `standards/ARCHITECTURE_RULES.md`.

## Before Making Changes

Always:

1. Inspect the relevant implementation and tests.
2. Identify the owning architectural layer.
3. Check the canonical project and architecture documents.
4. Define expected behavior and affected files.
5. Identify architecture impact before editing.

Do not place logic in the wrong layer.

## Required Workflow

### Step 1 - Design

Define:

- Problem
- Expected behavior
- Files affected
- Architecture impact
- Compatibility considerations

### Step 2 - Implementation

Follow:

- `standards/AI_CONSTITUTION.md`
- `standards/ARCHITECTURE_RULES.md`
- `standards/CODING_STANDARDS.md`
- `standards/PLUGIN_SPEC.md`

Prefer the smallest coherent change and reuse existing systems.

### Step 3 - Testing

Run:

```powershell
python -m pytest
```

If configured, also run:

```powershell
ruff check .
ruff format .
```

Verify existing and new functionality and confirm no architecture rules were violated.

### Step 4 - Review

Ask:

- Does this duplicate existing functionality?
- Does this create hidden dependencies?
- Does this bypass Runtime?
- Does this break plugin isolation?
- Does this change architectural ownership?
- Does documentation need synchronization?

### Step 5 - Commit

Keep commits focused. Explain what changed and why.

## AI Responsibilities

AI assistants are implementation and review tools, not silent architecture authorities. Architectural conflicts should be surfaced before changing boundaries.

## Git Rules

Do not work directly on protected release branches. Use focused feature or lab branches appropriate to the current development phase.

## Definition of Complete

A feature is complete when it is:

✓ Designed

✓ Implemented

✓ Tested

✓ Documented when required

✓ Reviewed

✓ Committed

## Core Principle

Speed comes from automation. Stability comes from discipline. AXIS must grow without losing its architecture.