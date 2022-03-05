class AccessControl:
    # keep record of which emp id is given
    # privilages to see personal data
    def __init__(self, empid, can_see_personal):
        self.empid = empid
        self.can_see_personal = can_see_personal
