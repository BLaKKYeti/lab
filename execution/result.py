from dataclasses import dataclass
from typing import Any


@dataclass
class ExecutionResult:
    plugin: str
    action: str
    success: bool
    output: Any
