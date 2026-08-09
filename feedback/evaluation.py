from dataclasses import dataclass
from typing import Any


@dataclass
class Evaluation:
    success: bool
    status: str
    message: str
    output: Any
