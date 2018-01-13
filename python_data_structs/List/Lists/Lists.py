# Linked List data structure

class Lists:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    """
    public methods 

    is_empty -> returns True if list contains any item
                , False otherwise

    get_head -> return, but don't remove, list head

    get_tail -> return, but don't remove, list tail

    get_size -> return number of items in list

    get_item -> return but don't remove data from 
                k-th item in the list

    append -> add data to end of the list

    """
    def is_empty(self):
        return True if self._size > 0 else False

    def get_head(self):
        return self._head
    
    def get_tail(self):
        return self._tail

    def get_size(self):
        return self._size

    def append(self, data):
        n = Node(data)
        self._append(n)

    def get_item(self, k):
        n = self.__getitem(k)
        return n.get_data()

    """

    private helper methods

    _remove_from_head -> remove and return the item at the 
                         head of the list

    _remove_from_tail -> remove and return the item at the 
                        tail of the list

    _set_head -> set head reference to point to new node

    _set_tail -> set tail reference to point to new node

    _add_to_front -> add a new node to the front of the list

    _append -> add a new node to the end of the list


    """


    
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



    """
    Overwritten methods


    __iter__ -> return read-only copy of list

    __reversed__ -> return read only copy of reversed list

    __str__ -> prints list as string: '[ n_1, n_2 , ..., n_k]' 

    __getitem__ -> returns kth node in list, raises IndexError
                   if k is greater than list size

    """



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
        print "\'["
        for item in self:
            print item + ", "
        print "]\'\n"

    def __getitem__(self, k):
        if index > self.get_size():
            raise IndexError
        else:
            n = list.get_head()
            while k is not 0:
                n = n.get_next()
                k = k - 1                
            return n

    
