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
