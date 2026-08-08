AXIS - AI Development Workflow
Status

Binding development workflow for AI-assisted AXIS development.

This document defines how AI tools participate in AXIS development without overriding the project's canonical architecture, tests, or human ownership.

AI tools accelerate implementation and analysis. They do not independently redefine AXIS architecture.

Development Principles

AXIS development follows these principles:

Architecture is explicit.
Current implementation is verified against code and tests.
Documentation must reflect the verified implementation.
AI-generated changes must be reviewed.
Changes should be small and coherent.
Existing interfaces should be preserved unless an architectural change is intentional and approved.
Tests are part of the implementation contract.
Git history provides the record of accepted changes.
Future capabilities must not be represented as implemented capabilities.
Authority
Human Project Owner

The human project owner has final authority over:

Product direction
Architectural changes
Feature priorities
Acceptance of implementation work
Merge and release decisions

AI tools provide analysis, implementation, review, and recommendations.

They do not have independent authority to redefine the project.

AI Responsibilities

Different AI tools may be used for different tasks.

Tool assignments are operational preferences, not architectural rules.

Architecture and Planning

AI may assist with:

architecture analysis
repository archaeology
feature decomposition
implementation planning
dependency analysis
documentation analysis
identifying architectural conflicts

Architectural recommendations must be checked against:

Current code
Existing tests
docs/ARCHITECTURE_MAP.md
standards/ARCHITECTURE_RULES.md
Accepted architectural decisions
Implementation

AI coding tools may assist with:

writing new code
modifying existing code
refactoring
adding tests
fixing implementation defects
updating documentation

Implementation tools must not silently redesign architectural boundaries.

Review

AI tools may review:

correctness
architecture
compatibility
security
maintainability
tests
documentation consistency

Review findings must be treated as recommendations until verified against the repository.

Canonical Architecture Authority

AI tools must use the following hierarchy when reasoning about the current architecture:

Verified source code and tests
docs/ARCHITECTURE_MAP.md
standards/ARCHITECTURE_RULES.md
Accepted architectural decisions in docs/DECISIONS.md
Other project documentation
Future vision and proposals

When documents disagree, the conflict must be investigated rather than resolved by guessing.

Future architecture must never be treated as current implementation merely because it appears in an older document.

Required Development Cycle

Every meaningful implementation change should follow this cycle.

1. Inspect

Before changing code:

inspect the relevant implementation
inspect related tests
inspect relevant documentation
identify existing interfaces
identify architectural boundaries

Do not begin by rewriting files based only on assumptions.

2. Plan

Define:

the problem being solved
the affected component
the expected behavior
the files that should change
the tests required
any architectural implications

If the change crosses an architectural boundary, stop and explicitly review that boundary before implementation.

3. Implement

Make the smallest coherent implementation that satisfies the requirement.

Prefer:

existing interfaces
existing abstractions
incremental changes
backward-compatible behavior

Avoid:

duplicate execution systems
unnecessary rewrites
speculative infrastructure
undocumented architectural changes
4. Test

Run the relevant tests after implementation.

The baseline project test command is:

python -m pytest -q --basetemp="$env:TEMP\axis-pytest-temp"

A change is not considered verified until the relevant tests pass.

Additional checks such as Ruff or manual verification should be performed when applicable.

5. Review

Review the resulting changes for:

correctness
architecture
compatibility
security
maintainability
unnecessary complexity
documentation accuracy
6. Synchronize Documentation

If implementation changes affect architecture, responsibilities, interfaces, or behavior:

update the relevant canonical documentation
remove stale claims
ensure AI-facing instructions remain consistent
ensure future architecture is clearly separated from current implementation
7. Inspect the Diff

Before committing:

git diff
git status

Confirm that:

only intended files changed
no generated artifacts were accidentally included
no runtime data was committed
no unrelated refactoring occurred
documentation matches the implementation
8. Commit

Commit only after implementation, testing, review, and documentation synchronization are complete.

Commit messages should clearly describe the accepted change.

Architectural Safety Rules

AI-assisted development must preserve the following current-state boundaries:

Runtime owns execution.
Planner owns plan creation.
Executor owns plan traversal.
Memory owns persistence.
Agent owns application-level coordination.
Intent Engine owns intent resolution.
Command Engine owns command/task conversion.
Plugin Manager owns plugin registration and resolution.
Plugins own capability-specific behavior.

AI tools must not:

bypass Runtime for capability execution
create duplicate execution engines
put plugin-specific behavior into orchestration components
silently change component ownership
represent planned systems as implemented
remove compatibility without an intentional architectural decision

The binding architectural rules are defined in:

standards/ARCHITECTURE_RULES.md

Documentation Rules

Documentation is part of the system's engineering state.

When changing documentation:

Determine whether the document describes current state, architecture, standards, decisions, requirements, or future vision.
Compare its claims against the implementation.
Remove stale implementation claims.
Preserve valid future goals as explicitly future.
Keep terminology consistent with the canonical architecture.
Do not create duplicate sources of truth unnecessarily.

The goal is a repository where an AI agent can inspect the documentation and arrive at the same architectural understanding as a human developer inspecting the code.

Git Discipline

AI tools should never assume that a clean-looking change is safe to commit.

Before committing:

git status
git diff

After committing:

git status
git log --oneline --decorate -5

Branches, commits, tags, and working-tree state must be treated as part of the project's development record.

Recovery and Continuity

AXIS development may involve work performed across different AI tools or development sessions.

To preserve continuity:

important architectural decisions must be documented
implementation state must be recoverable from Git
tests must establish known-good checkpoints
documentation must distinguish current state from future intent
AI tools must inspect the repository before assuming historical context

No AI tool should assume that a previous implementation or architectural claim is correct without verification.

Golden Rule

AI creates development speed.

Architecture creates system stability.

Tests create confidence.

Git creates history.

Documentation preserves continuity.

Every change should make AXIS more understandable, more reliable, or more capable without sacrificing the boundaries that make future development possible.