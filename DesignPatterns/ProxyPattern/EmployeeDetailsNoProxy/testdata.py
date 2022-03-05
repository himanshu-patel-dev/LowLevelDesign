from employee import Employee
from access_control import AccessControl

EMPLOYEES = {
    1: Employee(1, 'A', '1 Jan 1990', 10000),
    2: Employee(2, 'B', '2 Jan 1990', 20000),
    3: Employee(3, 'C', '3 Jan 1990', 30000),
    4: Employee(4, 'D', '4 Jan 1990', 40000),
    101: Employee(101, 'Manager', '5 Jan 1990', 50000),
}

ACCESSCONTROL = {
    101: AccessControl(101, True)
}
