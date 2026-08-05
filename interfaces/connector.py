from abc import ABC, abstractmethod


class Connector(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def execute(self, task):
        pass