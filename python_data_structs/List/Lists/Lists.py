# Linked List data structure

from Nodes import Nodes


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

    pop -> return and remove data from end of list

    dequeue -> return and remove data from front of list

    """
    def is_empty(self):
        return True if self._size <= 0 else False

    def get_head(self):
        return self._head
    
    def get_tail(self):
        return self._tail

    def get_size(self):
        return self._size

    def append(self, data):
        n = Nodes.Nodes(data)
        self._append(n)

    def add_to_head(self, data):
        n = Nodes.Nodes(data);
        self._add_to_head(n)

    def get_item(self, k):
        n = self.__getitem__(k)
        return n._data

    def pop(self):
        n = self._remove_from_tail()
        return n._data

    def dequeue(self):
        n = self._remove_from_head()
        return n._data

    """

    private helper methods

    _remove_from_head -> remove and return the item at the 
                         head of the list

    _remove_from_tail -> remove and return the item at the 
                        tail of the list

    _add_to_head -> add a new node to the front of the list

    _append -> add a new node to the end of the list


    """
    
    def _remove_from_head(self):
        if not self.is_empty():
            n = self._head
            self._head = n._next
            self._head._prev = None
            self._size = self._size - 1
            return n._unlink()
        else:
            return None

    def _remove_from_tail(self):
        if not self.is_empty():
            n = self._tail
            self._tail = n._prev
            self._tail._next = None
            self._size = self._size - 1
            return n._unlink()
        else:
            return None

    def _append(self, node):
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            node._prev = self._tail
            node._next = None 
            self._tail._next = node
            self._tail = node
        self._size = self._size + 1

    def _add_to_head(self, node):
        if self.is_empty():
            self._head = node 
            self._tail = node
        else:
            node._next = self._head
            node._prev = None
            self._head._prev = node
            self._head = node
        self._size = self._size + 1

    # create deep copy of our list
    def _copy(self):
        copy = Lists()
        n = self._head
        while n is not None:
            copy.append(n.get_data())
            n = n._next
        return copy


    """
    Overwritten methods


    __iter__ -> return read-only copy of list

    __reversed__ -> return read only copy of reversed list

    __str__ -> prints list as string: '[ n_1, n_2 , ..., n_k]' 

    __getitem__ -> returns kth node in list, raises IndexError
                   if k is greater than list size

    """

    def __iter__(self):
        copy = self._copy()
        return LinkedListIterator(copy)

    def __reversed__(self):
        copy = self._copy()
        return ReversedLinkedListIterator(copy)

    def __str__(self):
        str = "["
        to_print = self._head
        if self._size > 5:
            str = self._build_string(str, to_print, 5)
            str += "... "
        else:
            str = self._build_string(str, to_print, self._size - 1)
        str += "'" + self._tail.__str__() + "']\n"
        return str
        
            
    def _build_string(self, string, node, k):
        for i in range(0, k):
            string += "'" + node.__str__() + "', "
            node = node._next
        return string

    def __getitem__(self, k):
        if index > self.get_size():
            raise IndexError
        else:
            n = list._head
            while k is not 0:
                n = n._next
                k = k - 1                
            return n

    
class LinkedListIterator:
        
    def __init__(self, copy):
        self._current = copy._head

    def __iter__(self):
        return self

    def next(self):
        if self._current is None:
            raise StopIteration
        else:
            n = self._current
            self._current = n._next
            return n.get_data()

class ReversedLinkedListIterator:

    def __init__(self, copy):
        self._current = copy._tail

    def __iter__(self):
        return self

    def next(self):
        if self._current == None:
            raise StopIteration
        else: 
            n = self._current
            self._current = n._prev
            return n.get_data()
