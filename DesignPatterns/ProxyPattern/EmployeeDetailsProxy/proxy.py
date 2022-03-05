from abstract_employees import AbsEmployees
from access_controls import AccessControls
from employee import Employee


class Proxy(AbsEmployees):
    # as per proxy principle it inherits from abstract class as it
    # need implement the exact same methods required by concrete class

    # at the same time it also need instance of concrete class of subject
    # so that it can return requested object

    def __init__(self, employees, reqid):
        '''
            reqid: id of employee requesting info
            employees: instance of concrete employee class
        '''
        self._employees = employees
        self._reqid = reqid

    def get_employee_info(self, empids):
        '''
            empids: list of integers where integers are employee id's
        '''
        reqid = self._reqid

        # get the dict which contain key-value pairs of emp
        # who are given privilages to see private data
        access_rights = AccessControls.get_access_control(reqid)

        # get all employees instances whose empid is given in empids list
        # get_employee_info is the same abs method which proxy over rides
        for e in self._employees.get_employee_info(empids):

            # either emp is requsting his own info or is a privilaged user
            if e.empid == reqid or access_rights:

                # Show everything
                yield Employee(
                    e.empid,
                    e.name,
                    ('%.2f' % e.salary),
                    e.birthdate
                )

            else:  # Hide birthdate and salary details
                yield Employee(e.empid, e.name, '*****', '*****')
