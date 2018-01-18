"""

MinPQ implemented using Python list. Relationship between parents / children nodes
is:
    parent --> child_1    child_2
      n         (n*2)     (n*2)+1

Note: MinPQ never inserts at index 0.


@attributes
    size: number of elements in MinPQ
    _queue: represented as List
    _next: next index to insert at it
    _HEAD: constant equal to 1
    
@public methods
    size(): return self.size
    poll(): return and remove head of MinPQ. Swaps head and last element of MinPQ
            and then calls _sink() on new head to restore MinPQ's order
    peek(): return but don't remove head of MinPQ
    add(item): append to _queue and _swim it to its proper place in the MinPQ
    is_empty(): return whether MinPQ contains any items 


@private methods

    _swim(index): compare child at index to parent. _swap if child is less than parent
    and call recursively until we reach _HEAD

    _sink(index): compare parent at index to children. _swap if parent is greater than child
    and call recursively until queryed children do not exist
    
    _swap(item_index_1, item_index_2): swap items at passed-in indices

    __iter__(self): return items in MinPQ heap_sorted into a MinPQIterator

    _copy(self): return deep-copy of MinPQ
    
    

"""

class MinPQ:

    # constructor
    def __init__(self):
        self._queue = list()    # insert None to prevent appending to index 0
        self._queue.append(None)
        self._HEAD = 1          # constant for head of MinPQ
        self._next = 1
        self._size = 0          # number of items currently enqueued


    # return but don't remove head of MinPQ
    def peek(self):
        return self._queue[self._HEAD]


    # return and remove head of MinPQ
    def poll(self):
        if self.is_empty():
            return None
        else:
            # swap _HEAD and last item but keep a reference to last item
            to_remove = self._next - 1
            self._swap(self._HEAD, to_remove)
            self._next = self._next - 1 # make sure that we lose former min priority item
            self._sink(self._HEAD) # sink new _HEAD
            self._size -= 1
            return self._queue.pop(to_remove) # return former minimum priority item

    def is_empty(self):
        return self._size == 0

    def add(self, item):
        self._queue.append(item) # add item to queue
        self._swim(self._next)        # find item's correct position in queue
        self._next += 1          # increment next index and size
        self._size += 1

    def _swap(self, i, j):
        temp = self._queue[i]
        self._queue[i] = self._queue[j]
        self._queue[j] = temp

    # helper method shared by _sink and _swim
    def _less(self, obj, obj_2):
        return obj < obj_2

    # helper method shared by _sink and _swim 
    def _exists(self, index):
        return index < self._next


################################################################################
#
#
#  _sink and _sink helper methods:
#
#  _sink -> called recursively. Returns None when no children exist for current 
#  item or item has found its correct place in the MinPQ
#
#  _sink_with_1_child -> compare _queue[index] and _queue[child_index]. If 
#  _queue[child_index] is less than, _swap them and call _sink
#
#  _sink_with_2_children -> choose lesser child and call _sink_with_1_child to
#  handle any _swap-ing or _sink-ing
#
###############################################################################



    # 4 cases - both children exist, only left exists, only right exists
    # or no child exists
    def _sink(self, index):
        left_index = index * 2
        right_index = index * 2 + 1
        #base case - no child exists
        if not (self._exists(left_index) and self._exists(right_index)) :
            return None
        # both exist -- identify lesser child and compare to _queue[index]
        elif (self._exists(left_index) and self._exists(right_index)) :
            self._sink_with_2_children(index, left_index, right_index)
        # only left child exists
        elif self._exists(left_index):
            self._sink_with_1_child(index, left_index)
        # only right child exists
        else:
            self._sink_with_1_child(index, right_index)

    def _sink_with_1_child(self, index, child_index):
        if self._less(self._queue[child_index], self._queue[index]):
            self._swap(index, child_index)
            return self._sink(child_index) # do we have to sink further?
        return None                  # item has found correct place in MinPQ 
    
    def _sink_with_2_children(self, index, left_index, right_index):
        to_compare = left_index if self._less(self._queue[left_index], self._queue[right_index]) \
            else right_index
        self._sink_with_1_child(index, to_compare)

#################################################################################
#
# _swim(index) -> compare _queue[index] to its parent _queue[index/2]. Call
# _swim recursively until _queue[index/2] >= _queue[index] or index == self._HEAD
#
#################################################################################        
            

    def _swim(self, index):
        if index == self._HEAD:
            return None             # item at index is min val in _queue
        parent = index / 2

        if self._less(self._queue[index], self._queue[parent]): # if true, we should exchange child and parent
            self._swap(parent, index)
            self._swim(parent)
            return None                 # child is not less than parent, so it is in right place


################################################################
#
#  __iter__ -> create a heap-sorted list of this MinPQ's _queue
#
#  _copy -> create a deep copy of MinPQ
#
#  __str__ -> return __str__ of self._queue
#
#
###############################################################

    def __iter__(self):
        copy = self._copy()
        sorted = list()
        while not copy.is_empty():
            sorted.append(copy.poll())
        return iter(sorted)           # let list methods handle next()

    def _copy(self):
        copy = MinPQ()
        for i in range(1, self._next):
            copy.add(self._queue[i])
        return copy

    def __str__(self):
        return str(self._queue[1:self._next])

    


