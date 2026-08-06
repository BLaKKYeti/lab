from abc import ABC, abstractmethod


class Plugin(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def actions(self) -> list:
        pass

    @abstractmethod
    def initialize(self, config: dict):
        pass

    @abstractmethod
    def execute(self, task):
        pass

    @abstractmethod
    def shutdown(self):
        pass
