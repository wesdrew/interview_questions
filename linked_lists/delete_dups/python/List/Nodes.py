# Node class for doubly linked list
class Nodes:
    def __init__(self, data, next = None, prev = None):
        _set_data(self, data)
        self.next = next
        self.prev = prev

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_data(self):
        return self.data

    def has_prev(self):
        return True if self.get_prev() is not None else False

    def has_next(self):
        return True if self.get_next() is not None else False

    def __str__(self):
        return data.__str__

    def _set_data(self, data):
        self.data = data

    def _set_prev(self, node):
        self.prev = node

    def _set_next(self, node):
        self.next = node

    def _unlink(self):
        self.next = None
        self.prev = None

        

        
