import threading



class Bathroom:

    def __init__(self):
        """
        A wrapper for a lock that is passed to 
        conditional variables.

        count is used to switch between females and males
        """
        self.lock = threading.RLock()
        self.count = 0


