#!/usr/bin/python3 

import logging, threading

class Bathroom:
    def __init__(self):
        self.condition = threading.Condition()
        self.current_sex = None
        self.mutex = threading.Lock()
        self.count = 0

    def is_open(self, user):
        return self.current_sex is None or self.current_sex == user.sex

    def enter(self, user):
        assert(self.is_open(user))
        with self.mutex:
            self.current_sex = user.sex
            self.count += 1


    
    def leave(self, user):
        assert(user.sex == self.current_sex)
        with self.mutex:
            self.count -= 1
            assert(self.count >= 0)
            
            if self.count == 0:
                logging.debug("Bathroom is empty. Opening for anyone")
                self.current_sex = None
                with self.condition:
                    self.condition.notify_all()
    
