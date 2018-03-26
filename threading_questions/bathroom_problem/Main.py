from Bathroom import Bathroom
import logging
import random
import threading
from Users import Male, Female

MALE = 1
FEMALE = 0



def Main():
    logging.basicConfig(format='%(threadName)s:%(message)s', level=logging.DEBUG)
    b = Bathroom()
    logging.debug("Bathroom created!")
    ready_for_men, ready_for_women = get_condition_variables(b)
    for i in range(0, 2):
        user= Male(ready_for_men, ready_for_women)
        threading.Thread(target=user.run, args=(b,)).start()
    for i in range(0, 10):
        if random.randint(0, 1) == MALE:
            user = Male(ready_for_men, ready_for_women)
        else:
            user = Female(ready_for_women, ready_for_men)
        t = threading.Thread(target=user.run, args=(b,))
        t.start()

def get_condition_variables(bathroom):
    return (threading.Condition(bathroom.lock),
            threading.Condition(bathroom.lock))


if __name__ == "__main__":
    Main()
    
