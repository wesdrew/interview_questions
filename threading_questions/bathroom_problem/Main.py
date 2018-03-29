from Bathroom import Bathroom
from Users import Male, Female
import logging
import random
import threading


""""

Create 10 threads of Users, randomly assigned male or female,
and have them attempt to use the bathroom. If implemented correctly,
the opposite sexes should not use the bathroom at the same time

"""

MALE=1
FEMALE=0


def Main():
    logging.basicConfig(format='%(threadName)s, %(asctime)s, %(message)s', datefmt='%M:%S', level=logging.DEBUG)
    # create Bathroom
    b = Bathroom()
    # create whatever threading objects we need
    males_can_enter, females_can_enter = get_cvs()
    line_full = threading.Event()
    for i in range(10):
        if random.randint(0,1) == MALE:
            # create Male user
            user =  Male(males_can_enter, MALE, line_full)
        else:
            # create Female user
            user = Female(females_can_enter, FEMALE, line_full)
        t = threading.Thread(target=user.go, args=(b,))
        t.start()
    logging.debug("we're off to the races!")
    line_full.set() 

def get_cvs():
    return (threading.Condition(), threading.Condition())
    

if __name__ == '__main__':
    Main()
