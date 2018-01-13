# Linked List data structure

class Lists:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return True if self.size > 0 else False

    def get_head(self):
        return self._head
    
    def get_tail(self):
        return self._tail
    
    def _remove_from_head(self):
        if not self.is_empty():
            n = self.get_head()
            self._set_head(n.get_next())
            return n._unlink()
        else:
            return None
    def _remove_from_tail(self):
        if not self.is_empty():
            n = self.get_tail()
            self._set_tail(n.get_prev())
            return n._unlink()
        else:
            return None

    def __iter__(self):
        return_list = Lists()
        if not self.is_empty():
            node = self.get_head()
            while node is not None:
                return_list._append(node)
                node = node.get_next()
        return return_list

    def __reversed__(self):
        return_list = Lists()
        if not self.is_empty():
            node = self.get_tail()
            while node is not None:
                return_list._append(node)
                node = node.get_prev()
        return return_list


    def __str__(self):
        for item in self:
            print item
        
    def _set_head(self, node):
        self._head = node

    def _set_tail(self, node):
        self._tail = node

    def _append(self, node):
        if is_empty(self):
            self._set_head(node)
            self._set_tail(node)
        else:
            node._set_prev(self._tail)
            node._set_next(None)
            self._set_tail(node)

    def _add_to_front(self, node):
        if is_empty(self):
            self._set_head(node)
            self._set_tail(node)
        else:
            node._set_next(self.get_head())
            node._set_prev(None)
            self._set_head(node)

    
