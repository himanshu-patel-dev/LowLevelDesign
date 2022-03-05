from abc import ABC, abstractmethod


class AbstractAuto(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
