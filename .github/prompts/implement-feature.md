# Implement Feature

You are implementing a new feature for AXIS.

Before writing code:

1. Read:

   - DEVELOPMENT.md
   - .github/copilot-instructions.md
   - standards/AI_CONSTITUTION.md
   - standards/ARCHITECTURE_RULES.md
   - standards/CODING_STANDARDS.md
   - standards/PLUGIN_SPEC.md

2. Inspect the existing architecture.

Identify:

- existing implementation
- affected files
- dependencies
- possible conflicts
- architecture impact

Do not duplicate existing systems or create alternate execution paths.

---

## Plan

Before coding, explain:

- what will change
- why
- expected behavior
- affected components
- architecture impact

Do not change an architectural boundary without explicit approval.

---

## Implement

Requirements:

- preserve the current architecture
- preserve existing interfaces unless explicitly approved otherwise
- write modular code
- use type hints where appropriate
- keep functions focused
- reuse existing abstractions
- avoid unnecessary changes
- do not bypass Runtime for capability execution
- do not create duplicate execution systems

---

## Test

Run:

```powershell
python -m pytest