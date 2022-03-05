from abc import ABC, abstractmethod


class AbsFactory(ABC):

    @abstractmethod
    def create_auto(self):
        pass
