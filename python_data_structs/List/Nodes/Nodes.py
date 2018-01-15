# Node class for doubly linked list
class Nodes:
    def __init__(self, data, next = None, prev = None):
        self._data = data
        self._next = next
        self._prev = prev

    def get_data(self):
        return self._data

    def has_prev(self):
        return True if self.prev is not None else False

    def has_next(self):
        return True if self.next is not None else False

    def __str__(self):
        return self._data.__str__()

    def _unlink(self):
        self.next = None
        self.prev = None

        

        
