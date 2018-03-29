import logging
import threading

"""

Male and Female users of the bathroom.


"""

class User(object):
    
    def __init__(self, cv, sex, line_full_event):
        self.cv = cv
        self.sex = sex
        self.line_full_event = line_full_event

    def enter_bathroom(self, bathroom):
        with self.cv:
            bathroom.enter(self.sex, self.cv)

    def leave_bathroom(self, bathroom):
        bathroom.leave(self.sex, self.cv)


class Male(User):
    
    def __init__(self, cv, sex, line_full_event):
        super(Male, self).__init__(cv, sex, line_full_event)

    def go(self, bathroom):
        logging.debug("Male queueing up")
        self.line_full_event.wait()
        super(Male, self).enter_bathroom(bathroom)
        super(Male, self).leave_bathroom(bathroom)
        
class Female(User):
    def __init__(self, cv, sex, line_full_event):
        super(Female, self).__init__(cv, sex, line_full_event)

    def go(self, bathroom):
        logging.debug("Female queueing up")
        self.line_full_event.wait()
        super(Female, self).enter_bathroom(bathroom)
        super(Female, self).leave_bathroom(bathroom)

