# LAB AI OS Development Guide

## Mission

LAB AI OS is a modular operating system framework designed to understand tasks, plan actions, and execute capabilities through plugins.

The goal is not just adding features.

The goal is building a maintainable intelligence platform.

---

# Before Making Changes

Always check:

1. What layer does this belong to?

Architecture:

Application
↓
Intelligence
↓
Kernel
↓
Plugins
↓
Infrastructure

Never place logic in the wrong layer.

---

# Required Workflow

## Step 1 - Design

Before coding:

Define:

- Problem
- Expected behavior
- Files affected
- Architecture impact

---

## Step 2 - Implementation

Follow:

- AI Constitution
- Architecture Rules
- Coding Standards
- Plugin Specification

---

## Step 3 - Testing

Run:

```powershell
ruff check .
pytest

Verify:

- Existing functionality works
- New functionality works
- No architecture rules were violated

---

## Step 4 - Review

Ask:

- Does this duplicate existing functionality?
- Does this create hidden dependencies?
- Does this break plugin compatibility?
- Does this belong in another layer?

---

## AI Responsibilities

### ChatGPT

Architecture authority.

Used for:

- Planning
- System design
- Debugging strategy

---

### GitHub Copilot

Implementation assistant.

Used for:

- Writing code
- Refactoring
- Boilerplate

Must follow:

`.github/copilot-instructions.md`

---

### Claude

Review assistant.

Used for:

- Large reviews
- Documentation
- Alternative analysis

---

# Git Rules

Never work directly on main.

Branches:
main
develop
lab-005-memory-layer
lab-006-time
feature/*


Every commit should explain:

- What changed
- Why it changed

---

# Definition of Complete

A feature is complete when:

✓ Designed

✓ Implemented

✓ Tested

✓ Documented

✓ Reviewed

✓ Committed

---

# Core Principle

Speed comes from automation.

Stability comes from discipline.

LAB AI OS must grow without losing its architecture.