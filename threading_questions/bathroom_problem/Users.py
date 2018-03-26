import threading
import logging

class User:
    
    def __init__(self, same_sex_cv, opp_sex_cv):
        self.same_sex_cv = same_sex_cv
        self.opp_sex_cv = opp_sex_cv

    def enter_bathroom(self, bathroom, debug_message):
        with bathroom.lock:
            self.same_sex_cv.notify_all()
            bathroom.count = bathroom.count + 1
            logging.debug(debug_message +  " count: %d", bathroom.count)

    def leave_bathroom(self, bathroom, debug_message):
        with bathroom.lock:
            bathroom.count = bathroom.count - 1
            logging.debug(debug_message + " count: %d", bathroom.count)
            self.opp_sex_cv.notify_all()


class Male(User):
    
    def __init__(self, same_sex_cv, opp_sex_cv):
        super(Male, self).__init__(same_sex_cv, opp_sex_cv)

    def enter_bathroom(self, bathroom, debug_message="Man entering bathroom"):
        super(Male,self).enter_bathroom(bathroom, debug_message)

    def leave_bathroom(self, bathroom, debug_message="Man leaving bathroom"):
        super(Male, self).leave_bathroom(bathroom, debug_message)
 
        
    def run(self, bathroom):
        logging.debug("Male queueing")
        self.enter_bathroom(bathroom)
        self.leave_bathroom(bathroom)

class Female(User):

    def __init__(self, same_sex_cv, opp_sex_cv):
        super(Female, self).__init__(same_sex_cv, opp_sex_cv)

    def enter_bathroom(self, bathroom, debug_message="Female entering bathroom"):
        super(Female, self).enter_bathroom(bathroom, debug_message)


    def leave_bathroom(self, bathroom, debug_message="Female leaving bathroom"):
        super(Female, self).enter_bathroom(bathroom, debug_message)


    def run(self, bathroom):
        logging.debug("Female queueing")
        self.enter_bathroom(bathroom)
        self.leave_bathroom(bathroom)
