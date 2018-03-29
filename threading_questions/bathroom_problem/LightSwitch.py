import logging
from threading import Lock 


"""

Design pattern from "Little Book of Semaphores"


"""

class LightSwitch:

    def __init__(self):
        self.mutex = Lock()
        self.count = 0
    
    def inc(self, cv):
        with self.mutex:
            self.count += 1
            logging.debug("inc-ing! count == %d", self.count)
            if self.count == 1:
                cv.acquire()

    
    def dec(self, cv):
        with self.mutex:
            self.count -= 1
            logging.debug("dec-ing! count == %d", self.count)
            if self.count == 0:
                cv.notify_all()
                cv.release()





    
