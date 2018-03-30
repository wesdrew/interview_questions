# !/usr/bin/python3

import logging, time

class User:

    def __init__(self, sex):
        self.sex = sex
        if self.sex == 1:       # kludgy, fix this later
            self.name = 'Male'
        else:
            self.name = 'Female'

    def go(self, bathroom):
        logging.debug("%s queueing up" % self.name)

        with bathroom.condition:
            while not bathroom.is_open(self):
                bathroom.condition.wait()
        
        logging.debug("%s entering the bathroom" % self.name)
        bathroom.enter(self)
        time.sleep(1)
        bathroom.leave(self)

