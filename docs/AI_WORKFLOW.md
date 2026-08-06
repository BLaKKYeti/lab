# LAB AI OS - AI Development Workflow

## Purpose

Define how AI agents collaborate during LAB AI OS development.

The goal is controlled acceleration:
- AI assists development
- Human approves decisions
- Git records history

---

# Agent Responsibilities

## ChatGPT - Chief Architect

Responsibilities:

- System architecture
- Feature planning
- Design decisions
- Debugging strategy
- Long-term roadmap

Rules:

- Do not blindly rewrite working files
- Prefer small controlled changes
- Explain tradeoffs before major decisions

---

## GitHub Copilot - Implementation Engineer

Responsibilities:

- Write code
- Refactor existing modules
- Create boilerplate
- Fix implementation issues

Rules:

- Follow AI Constitution
- Preserve plugin compatibility
- Do not redesign architecture
- Do not bypass Runtime

---

## Claude - Review Engineer

Responsibilities:

- Review large changes
- Analyze documentation
- Find architectural problems
- Suggest improvements

Rules:

- Review before approval
- Do not directly change architecture
- Do not override existing decisions

---
## Cursor - Repository Implementation Engineer

Responsibilities:

- code navigation
- implementation
- testing
- refactoring

Rules:
- follow architecture
- do not redesign systems
- defer architecture conflicts

## Human Owner

Responsibilities:

- Final approval
- Testing
- Product direction
- Merge decisions

---

# Development Cycle

Every feature follows:

## 1. Design

Question:

"What problem are we solving?"

Output:

- Architecture decision
- Required files
- Expected behavior

---

## 2. Implementation

Copilot writes code.

Requirements:

- Type hints
- Documentation
- Tests
- Modular design

---

## 3. Review

Claude or ChatGPT reviews:

- Architecture
- Security
- Compatibility
- Maintainability

---

## 4. Testing

Run:

- pytest
- Ruff
- Manual verification

---

## 5. Commit

Commit must explain:

- What changed
- Why it changed

---

# Golden Rule

AI creates speed.

Architecture creates survival.

Every change must improve the system, not just add features.