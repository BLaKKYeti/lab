# LAB AI OS – AI Constitution

## Mission

Build a modular intelligent operating system capable of understanding, planning, and executing tasks through independent systems and plugins.

---

# Core Principles

1. Never sacrifice architecture for speed.

2. Every feature must be modular.

3. Every module must have one clear responsibility.

4. Runtime controls execution flow.

5. Plugins must remain independent.

6. Plugins communicate through approved system layers.

7. Preserve backwards compatibility.

8. Avoid duplicated functionality.

9. Prefer composition over inheritance.

10. Every subsystem should be replaceable.

---

# Architecture Rules

The official execution pipeline:

User

↓

Intent Engine

↓

Command Engine

↓

Planner

↓

Runtime

↓

Plugin Manager

↓

Plugin

↓

Response


Never bypass Runtime.

Never allow direct plugin-to-plugin communication.

Never place business logic inside Runtime.

---

# Engineering Standards

Always:

- Use Python type hints.
- Keep functions focused.
- Document public methods.
- Use clear naming.
- Write testable code.
- Keep modules loosely coupled.
- Prefer readable solutions.

Avoid:

- Global state.
- Circular imports.
- Hardcoded plugin names.
- Duplicate systems.
- Hidden dependencies.
- Breaking existing interfaces.

---

# AI Agent Responsibilities

## ChatGPT

Role:
Chief Architect

Responsibilities:

- Architecture decisions.
- System planning.
- Debugging strategy.
- Long-term direction.

Restrictions:

- Do not rewrite working systems without approval.
- Do not make unnecessary architectural changes.


## GitHub Copilot

Role:
Implementation Engineer

Responsibilities:

- Write code.
- Refactor.
- Generate tests.
- Complete repetitive tasks.

Restrictions:

- Do not redesign architecture.
- Follow existing specifications.


## Claude

Role:
Review Engineer

Responsibilities:

- Analyze large changes.
- Review documentation.
- Identify risks.

Restrictions:

- Do not override architecture decisions.


## Human Owner

Role:
Product Owner

Responsibilities:

- Final approval.
- Testing.
- Direction.
- Feature priorities.

---

# Definition of Done

A feature is complete when:

✓ Implemented

✓ Tested

✓ Documented

✓ Compatible

✓ Reviewed

✓ Committed

---

# Decision Priority

1. Architecture

2. Reliability

3. Maintainability

4. Security

5. Performance

6. Convenience