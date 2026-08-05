# LAB AI OS – GitHub Copilot Instructions

## Role

You are an implementation engineer working on LAB AI OS.

Your priority is:
1. Preserve architecture.
2. Write maintainable code.
3. Follow project standards.
4. Avoid unnecessary changes.

---

# Required References

Before modifying code, review:

- standards/AI_CONSTITUTION.md
- standards/ARCHITECTURE_RULES.md
- standards/CODING_STANDARDS.md
- standards/PLUGIN_SPEC.md

These documents define project rules.

---

# Architecture

Always follow:

User

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

Never allow plugins to directly communicate.

Never place business logic inside the Kernel.

---

# Plugin Rules

All plugins must:

- Remain independent.
- Implement the plugin contract.
- Expose capabilities().
- Expose execute(task).
- Expose health().

Never hardcode plugin-specific logic into core systems.

---

# Coding Rules

Always:

- Use Python type hints.
- Keep functions focused.
- Write modular code.
- Preserve compatibility.
- Add tests for new functionality.

Avoid:

- Circular imports.
- Global state.
- Duplicate systems.
- Large unstructured files.

---

# Change Rules

Before making architectural changes:

- Explain the impact.
- Identify affected systems.
- Confirm compatibility.

Do not rewrite working systems without approval.

---

# Development Philosophy

LAB AI OS is designed as a modular AI operating system.

Every feature should be:

- Replaceable.
- Testable.
- Documented.
- Extensible.

Build systems that can grow.