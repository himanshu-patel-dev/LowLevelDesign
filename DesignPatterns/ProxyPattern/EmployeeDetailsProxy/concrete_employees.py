from abstract_employees import AbsEmployees
from testdata import EMPLOYEES


class Employees(AbsEmployees):
    def get_employee_info(self, empids):
        # return employee instance if present in EMPLOYEES dict
        return (EMPLOYEES[empid] for empid in empids if empid in EMPLOYEES)
