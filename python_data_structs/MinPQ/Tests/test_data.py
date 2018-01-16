ints = [4, 10, 1, 100, 20, -5]

strings = ['peter', 'paul', 'ringo', 'johannes']

"""
arbitrary user defined class. Comparison functions 
will only compare on the second member of tuple

"""

class UserClass:

    def __init__(self, some_tuple):
        self._tuple = some_tuple

    def __eq__(self, other):
        return self._tuple[1] == other._tuple[1] 

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self._tuple[1] < other._tuple[1]

    def __gt_(self, other):
        return self._tuple[1] > other._tuple[1]

    def __ge__(self, other):
        return self._tuple[1] >= other._tuple[1]

    def __le__(self, other):
        return self._tuple[1] <= other._tuple[1]

        
objects = [UserClass((4,0)), UserClass((1, 34)), UserClass((2, 5))]
    
