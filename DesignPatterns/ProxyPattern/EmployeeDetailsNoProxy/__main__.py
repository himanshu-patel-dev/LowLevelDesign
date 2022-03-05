from testdata import EMPLOYEES, ACCESSCONTROL


def get_employee_info(empids, reqid):
    for empid in empids:
        if empid not in EMPLOYEES:
            continue
        employee = EMPLOYEES[empid]
        details = 'Employee Id: %d, Name: %s'
        details = details % (employee.empid, employee.name)

        if reqid in ACCESSCONTROL:
            if ACCESSCONTROL[reqid].can_see_personal:
                details += (', BirthDate: %s, Salary: %.2f' %
                            (employee.birthdate, employee.salary))
        print(details)


get_employee_info([3, 4], 3)  # requestor may not see personal data

get_employee_info([1, 2], 101)  # requestor *may* see personal data
