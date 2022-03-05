from abc import ABC, abstractmethod


class AbsEmployees(ABC):
    # abstract class which specifies the method need implementation

    @abstractmethod
    def get_employee_info(self, empids):
        pass
