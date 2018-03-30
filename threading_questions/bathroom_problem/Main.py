#!/usr/bin/python3

import logging, random, threading
from Bathroom import Bathroom
from User import User



def Main():
    logging.basicConfig(format='%(threadName)s, %(message)s', level = logging.DEBUG)

    b = Bathroom()

    logging.debug("we're off to the races!")
    for i in range(20):
        user = User(random.randint(0, 1))
        t = threading.Thread(target=user.go, args=(b,))
#        logging.debug("Starting a thread")
        t.start()

if __name__ == '__main__':
    Main()
