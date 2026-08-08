# AXIS

**AXIS** is an AI orchestration platform designed to coordinate intent, planning, execution, memory, and extensible capabilities.

AXIS is being developed incrementally. The repository contains a working core architecture while larger capabilities such as advanced model orchestration, voice control, and operating-system automation remain future development.

> **Important:** The current implementation is defined by the code and tests in this repository. Future capabilities must not be treated as implemented until they exist and are verified.

---

## Current Status

The current AXIS core includes:

* Agent coordination
* Intent resolution
* Execution planning
* Execution-plan traversal
* Central Runtime execution boundary
* Plugin management
* Plugin architecture
* Persistent memory
* Memory recovery
* Runtime persistence
* Command/task conversion infrastructure
* Logging infrastructure
* Automated tests

The current verified test suite should be run before and after architectural changes.

---

## Architecture

AXIS currently follows this execution path:

```text
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
```

### Component responsibilities

| Component      | Responsibility                                           |
| -------------- | -------------------------------------------------------- |
| Agent          | Application-level coordination                           |
| Intent Engine  | Converts user input into structured intent               |
| Planner        | Creates execution plans                                  |
| Executor       | Traverses execution plans                                |
| Runtime        | Central execution boundary                               |
| Plugin Manager | Registers and resolves plugins                           |
| Plugins        | Provide isolated capabilities                            |
| Memory         | Persistent state and retrieval                           |
| Command Engine | Converts plan steps into executable task representations |
| Logger         | Operational logging                                      |

Runtime is the central boundary for capability execution.

Plugins must not bypass Runtime or create alternate orchestration paths.

For the detailed current-state architecture, see `docs/ARCHITECTURE_MAP.md`.

For binding architectural rules, see `standards/ARCHITECTURE_RULES.md`.

---

## Repository Structure

The current repository is organized around the implemented architecture:

```text
AXIS/
├── agent/
│   └── Agent coordination
│
├── kernel/
│   ├── command_engine.py
│   ├── intent_engine.py
│   ├── memory.py
│   ├── plugin_manager.py
│   └── runtime.py
│
├── planner/
│   ├── execution_plan.py
│   ├── interfaces.py
│   ├── planner.py
│   └── step.py
│
├── execution/
│   ├── executor.py
│   └── result.py
│
├── core/
│   └── logger.py
│
├── config/
│   └── settings.py
│
├── tests/
│
├── docs/
├── standards/
├── AGENTS.md
├── main.py
├── requirements.txt
└── README.md
```

The repository structure may evolve as AXIS develops, but architectural ownership must remain explicit.

---

## Memory

Memory is a first-class AXIS subsystem.

The current memory layer supports persistent storage and retrieval of AXIS state and project context, including recovery behavior for corrupted persistence data.

Memory is accessed through Runtime in the current architecture.

Runtime persistence and memory behavior are covered by automated tests.

---

## Plugins

AXIS uses a plugin architecture to isolate capability-specific functionality from the orchestration core.

Plugins are managed through the Plugin Manager and executed through Runtime.

This architecture allows new capabilities to be added without turning the Agent, Planner, or Runtime into collections of unrelated capability-specific implementations.

---

## Command Engine

The Command Engine is currently implemented as a supporting task/command conversion subsystem.

It is **not currently a required stage in the primary `Agent.process()` execution path**.

It must not be treated as a replacement for the Executor or Runtime.

Its architectural role may expand in future development, but such a change requires explicit implementation, testing, and documentation.

---

## Development

AXIS is currently developed in Python.

Create and activate the project virtual environment before installing dependencies.

Example PowerShell workflow:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the test suite:

```powershell
python -m pytest -q
```

For isolated pytest temporary files:

```powershell
python -m pytest -q --basetemp="$env:TEMP\axis-pytest-temp"
```

---

## Development Workflow

AXIS follows a controlled development process:

```text
Architecture / Design
        ↓
Implementation
        ↓
Testing
        ↓
Review
        ↓
Documentation synchronization
        ↓
Commit
```

Changes should be small and intentional.

Before changing an architectural boundary:

1. Inspect the existing implementation.
2. Inspect relevant tests.
3. Identify affected documentation.
4. Define the intended change.
5. Implement the smallest coherent change.
6. Add or update tests.
7. Run the test suite.
8. Synchronize canonical documentation.
9. Review the Git diff.
10. Commit the change.

---

## AI-Assisted Development

AXIS uses AI development tools as engineering assistants.

AI tools may assist with:

* Architecture analysis
* Implementation
* Debugging
* Refactoring
* Testing
* Documentation
* Code review

AI tools must follow the canonical AXIS architecture.

They must not:

* Invent nonexistent subsystems.
* Treat future architecture as implemented.
* Bypass Runtime.
* Create duplicate execution systems.
* Change architectural ownership without an explicit decision.
* Rewrite working systems unnecessarily.
* Ignore existing tests or compatibility constraints.

The human project owner retains final authority over architectural and product decisions.

See:

* `AGENTS.md`
* `docs/AI_WORKFLOW.md`
* `.github/prompts/`
* `standards/ARCHITECTURE_RULES.md`

---

## Documentation

Important documentation:

| Document                          | Purpose                                        |
| --------------------------------- | ---------------------------------------------- |
| `docs/ARCHITECTURE_MAP.md`        | Canonical current-state execution architecture |
| `docs/ARCHITECTURE.md`            | High-level architecture                        |
| `standards/ARCHITECTURE_RULES.md` | Binding architecture rules                     |
| `docs/DECISIONS.md`               | Architecture decisions                         |
| `docs/AI_WORKFLOW.md`             | AI development workflow                        |
| `docs/REQUIREMENTS.md`            | Project requirements                           |
| `docs/VISION.md`                  | Long-term project vision                       |
| `AGENTS.md`                       | AI engineering instructions                    |

These documents must remain consistent with the verified implementation.

---

## Future Vision

AXIS is intended to grow into a broader AI operating and orchestration platform.

Potential future capabilities include:

* Local LLM integration through Ollama
* Multiple LLM provider integration
* Intelligent model selection
* Voice-controlled interaction
* Desktop and operating-system automation
* Expanded tool and connector support
* Advanced memory and retrieval
* Multi-agent coordination
* Sandboxed capability execution
* Advanced observability
* Workflow automation
* Greater autonomy

These are **future capabilities**, not claims about the current implementation.

Development will proceed incrementally, with each major capability becoming part of the canonical architecture only after it has been implemented and verified.

---

## Contributing

Keep changes focused and consistent with the architecture.

Before submitting a change:

```powershell
python -m pytest -q
```

Review:

```powershell
git diff
git status
```

Do not commit generated runtime data, credentials, virtual environments, or other files excluded by `.gitignore`.

---

## Project Principle

> **AI creates speed. Architecture creates survival.**

AXIS should become more capable without becoming less understandable.

Every feature should strengthen the system rather than merely increase its feature count.
