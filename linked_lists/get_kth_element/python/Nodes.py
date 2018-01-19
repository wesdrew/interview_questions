class Nodes:

    def __init__(self, data, Node=None):
        self.data = data
        self._next = Node

    def next(self):
        return self._next

    def set_next(self, Node):
        self._next = Node
