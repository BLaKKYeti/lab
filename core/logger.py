import json
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


class Logger:
    LEVELS = ("debug", "info", "warning", "error")

    def __init__(self, level: str = "info", output: Optional[str] = None):
        if level not in self.LEVELS:
            raise ValueError(f"Unsupported log level: {level}")
        self.level = level
        self.output = output
        self.records: list[dict[str, Any]] = []

    def debug(self, message: str, **context: Any) -> None:
        self._log("debug", message, **context)

    def info(self, message: str, **context: Any) -> None:
        self._log("info", message, **context)

    def warning(self, message: str, **context: Any) -> None:
        self._log("warning", message, **context)

    def error(self, message: str, **context: Any) -> None:
        self._log("error", message, **context)

    def clear(self) -> None:
        self.records.clear()

    def _log(self, level: str, message: str, **context: Any) -> None:
        if self.LEVELS.index(level) < self.LEVELS.index(self.level):
            return

        record = {
            "level": level,
            "message": message,
            "context": context,
            "timestamp": self._timestamp(),
        }
        self.records.append(record)

        line = self._format(record)
        if self.output:
            self._write(line)
        else:
            print(line)

    def _timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    def _format(self, record: dict[str, Any]) -> str:
        line = f"[{record['timestamp']}] {record['level'].upper()} {record['message']}"
        if record["context"]:
            line += f" {json.dumps(record['context'], sort_keys=True, default=str)}"
        return line

    def _write(self, line: str) -> None:
        with Path(self.output).open("a", encoding="utf-8") as file:
            file.write(line + "\n")
