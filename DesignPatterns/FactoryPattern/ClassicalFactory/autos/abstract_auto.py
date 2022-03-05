from abc import ABC, abstractmethod


class AbstractAuto(ABC):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
