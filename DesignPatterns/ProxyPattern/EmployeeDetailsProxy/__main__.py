from factory import get_employees_collection

DETAILS = 'Employee Id: %d, Name: %s, Birthdate: %s, Salary: %s'


def print_employee_details(empids, reqid):
    employees = get_employees_collection(reqid)
    for e in employees.get_employee_info(empids):
        print(DETAILS % (e.empid,
                         e.name,
                         e.birthdate,
                         e.salary)
              )


print("Requestor authorized to see everything:")
print_employee_details([1, 2], 101)

print("Requestor is an ordinary employee.")
print_employee_details([1, 2, 3, 4], 3)
