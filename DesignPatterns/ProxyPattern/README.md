# Proxy Pattern

**Classification**: Structural
It acts on a real subject and keeps a reference to the subject. Proxy exposes a identical interface as original subject thus make client almost unaware of that he is using a proxy as same time controlling access to a real subject.

It stands as an interface in between client code and the actual code a client want to access. It’s recommended when you want to add some additional behaviors to an object of some existing class without changing the client code. The meaning of word **Proxy** is ___in place of___ or ___on behalf of___ that directly explains the Proxy Method. Proxy pattern controls and manage access to the object they are protecting.

- **Virtual Proxy**: A virtual proxy is a placeholder for "expensive to create" objects. The real object is only created (on demand) when a client first requests/accesses the object.
- **Protective Proxy**: A protective proxy controls access to a sensitive master object. The "surrogate" object checks that the caller has the access permissions required prior to forwarding the request.
- **Remote Proxy**: It is particularly used when the service object is located on a remote server. In such cases, the proxy passes the client request over the network handling all the details while actual resource is behind some firewall.
- **Smart proxy**: A smart proxy interposes additional actions when an object is accessed. Typical uses include:
  - Counting the number of references to the real object so that it can be freed automatically when there are no more references (aka smart pointer),
  - Loading a persistent object into memory when it's first referenced,
  - Checking that the real object is locked before it is accessed to ensure that no other object can change it.

DBMS use all of them.

## Without using Proxy

Employee Class: Resource for which we need proxy

```python
class Employee:
    def __init__(self, empid, name, birthdate, salary):
        self.empid = empid
        self.name = name
        self.birthdate = birthdate
        self.salary = salary
```

Access Control Class before retriving Employee data

```python
class AccessControl:
    def __init__(self, empid, can_see_personal):
        self.empid = empid
        self.can_see_personal = can_see_personal
```

After creating some testdata (substitute of DB) we can write a logic to let only autorized person access the sensitive info.

```python
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
```

## Proxy Pattern Structure: Protection Proxy

- **Abstract Subject**: Subject class is a abstract class which defines the interfaces client is expected to use while interacting with it.
- **Concrete Subject**: Concrete class which implement the abstract method and properties declared in abstract subject.
- **Proxy**: It containt reference to original concrete class so as to preoduce the actual object for valid request. And also contains same interface as declared in abstract subject so as to provide same interface for client while using proxy. Client request is received by client and client do not know about any proxy and directly make requrest as if it is making request directly with Subject.

1. Make an abstract representation of subject/class we want to implement so that concrete class as well as proxy pattern are on same page while implementing abs method.

```python
from abc import ABC, abstractmethod

class AbsEmployees(ABC):
    # abstract class which specifies the method need implementation
    @abstractmethod
    def get_employee_info(self, empids):
        pass
```

2. Make classes to hold data in specific format.

```python
class Employee:
    def __init__(self, empid, name, birthdate, salary):
        self.empid = empid
        self.name = name
        self.birthdate = birthdate
        self.salary = salary


class AccessControl:
    # keep record of which emp id is given
    # privilages to see personal data
    def __init__(self, empid, can_see_personal):
        self.empid = empid
        self.can_see_personal = can_see_personal
```

3. Class to access given users privilages from the testdata we madeup.

```python
from testdata import ACCESSCONTROLS

class AccessControls:
    @staticmethod
    def get_access_control(reqid):
        '''
            reqid: a integer representing empid as key
            in ACCESSCONTROLS dictionary
        '''
        # returns access right of request requid employee
        if reqid in ACCESSCONTROLS:
            return ACCESSCONTROLS[reqid].can_see_personal
        return False
```

4. Implement the concrete class for subject and all abstract methods.

```python
from abstract_employees import AbsEmployees
from testdata import EMPLOYEES

class Employees(AbsEmployees):
    def get_employee_info(self, empids):
        # return employee instance if present in EMPLOYEES dict
        return (EMPLOYEES[empid] for empid in empids if empid in EMPLOYEES)
```

5. Now go and implement the proxy and note we need to implement the same abstract method which concrete subject class was supposed to implement.

```python
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
```

6. A factory to create a proxy instance easily without actually interacting with proxy class.

```python
from concrete_employees import Employees
from proxy import Proxy


def get_employees_collection(reqid):
    return Proxy(Employees(), reqid)
```

7. Now create a main method and use proxy and its factory.

```python
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
print_employee_details([1, 2, 3, 4], 3
```

## Consequences

- Introduces a level of indirection when accessing the actual object.
- Use proxy pattern when you want to add control over some object.
