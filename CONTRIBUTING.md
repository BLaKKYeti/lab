# Contributing to LAB AI OS

Thank you for your interest in contributing to LAB AI OS. This document outlines the contribution workflow, coding and documentation standards, and expected behaviors to keep collaboration productive and respectful.

---

## How to fork

1. Fork the repository on GitHub.
2. Clone your fork:

```bash
git clone git@github.com:<your-username>/lab.git
cd lab
```

3. Create a remote to track upstream:

```bash
git remote add upstream https://github.com/BLaKKYeti/lab.git
git fetch upstream
```

---

## Branch naming

Use descriptive, kebab-case branch names with a short prefix:

- feat/<short-description> or feat/<ticket>-<short-description>
- fix/<short-description>
- docs/<short-description>
- chore/<short-description>

Examples:

```
feat/add-memory-backend
fix/worker-timeout
docs/update-architecture
```

---

## Commit message format

Follow Conventional Commits (recommended):

```
<type>(<scope>): <short summary>

<body>

<footer>
```

Types include: feat, fix, docs, chore, refactor, test, perf.

Example:

```
feat(memory): add sqlite memory backend

Implements a pluggable memory adapter and adds unit tests.
```

---

## Pull Requests

- Open a pull request from your fork/branch to the project `main` or an agreed-upon integration branch.
- Fill the PR template with a description, motivation, and test plan.
- Link related issues and ADRs when applicable.
- Keep PRs focused and small where possible.

---

## Code Reviews

- Reviewers should evaluate correctness, design, tests, and documentation.
- Request changes for missing tests, unclear logic, or API-contract regressions.
- Approve when changes meet quality standards and tests pass.

---

## Issue Templates

Use the GitHub issue templates to report bugs, request features, or propose ADRs. Include reproduction steps, environment, and expected vs actual behavior for bugs.

---

## Coding Standards

- Prefer clear, idiomatic Python for core components. Use type hints and docstrings.
- Keep functions small and focused; single-responsibility for modules.
- Follow PEP 8 style guidelines for Python. Use linters (flake8, pylint) configured in CI.
- Write tests that assert behavior rather than implementation details.

---

## Documentation Standards

- Document high-level design in `docs/` and API-level details in module READMEs.
- Use Markdown with clear headings, examples, and expected outputs.
- Update docs concurrently with feature patches.

---

## Testing Requirements

- Unit tests for logic-heavy components.
- Integration tests for cross-component behavior; include small end-to-end scenarios.
- Add tests for bug fixes to prevent regressions.

---

## Expected contributor behavior

- Be respectful and professional in discussions and reviews.
- Open issues for significant design changes and discuss before implementation.
- Avoid committing secrets or proprietary data.
- When in doubt, ask maintainers or open an issue to discuss design choices.

---

Thank you for contributing — your work helps LAB AI OS become a robust, open platform for autonomous agents.