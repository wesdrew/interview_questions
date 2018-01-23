""""

Union find data structure using three lists:

    @properties

    Lists:
        _size -> number of items in set
        _parent -> id of enclosing set for each set

    _components: number of disjoint sets, initially equal to 
    number of items in UF

    @public methods

    components(self): return the number of components in UF
    
    connected(self, id_1, id_2): return whether the two items
    are in the same set

    @private methods

    _find(self, id): return the largest enclosing set for id.
    Essentially, find the entry in the _parent list that is its
    own parent

    _size(self, id): return the number of items in set id

    union(self, id_1, id_2): compare the size of id_1 and id_2 
    and union the two sets by:
        1. finding the parent of the lesser set and change it to 
        the id of the greater set

        2. updating the size of the new parent set by adding the size
        of the lesser set to the size of the greater set

        3. decrementing the number of components

"""

class UF:
    
    # constructor
    def __init__(self, item_count):
        # create lists
        self._sz = list()
        self._parent = list()
        self.components = 0
        for i in range(0, item_count):
            self._parent.append(i) # every item is, initially, its own parent
            self._sz.append(1)
            self.components += 1 # initially have item_count size componenets

    ######################################################################
    # find methods:                                                      #
    #                                                                    #
    # _find(self, id): move through the _parent list to find the parent  #
    # of the id set                                                      #
    #                                                                    #
    # _size(self, id): give the number of items in id set                #
    ######################################################################

    def _find(self, id):
        while self._parent[id] is not id: # jump around the _parent list until child == parent
            id = self._parent[id]
        return id

    def _size(self, id):
        return self._sz[id]

    
    ########################################################################
    # union methods:                                                       #
    #                                                                      #
    # connected(self, id_1, id_2): return if id's have the same parent     #
    #                                                                      #
    # union(self, id_1, id_2): find the lesser parent and reassign to the  #
    # parent of the greater set. Update the size of the greater set        #
    # decrement components attribute                                       #
    ########################################################################

    def connected(self, id_1, id_2):
        return self._parent[id_1] is self._parent[id_2]

    def union(self, id_1, id_2):
        if self.connected(id_1, id_2):
            return None         # don't do anything! they're already connected
        else:
            parent_1 = self._find(id_1) # parent of id_1
            parent_2 = self._find(id_2) # parent of id_2
            if self._sz[parent_1] > self._sz[parent_2]: # parent_1 is the greater parent
                self._parent[parent_2] = parent_1           # parent_2 is now child of parent_1
                self._sz[parent_1] += self._sz[parent_2] # increase the size of the parent_1 set
            else:
                self._parent[parent_1] = parent_2
                self._sz[parent_2] += self._sz[parent_1]
            self.components -= 1 # we lost a component, so decrement


# unit test
if __name__ == "__main__":

    u = UF(10)
    u.union(1, 3)
    u.union(1, 5)
    u.union(9,9)
    u.union(8,9)
    print "parents list"
    print "================"
    print u._parent
    print "size list"
    print "================"
    print u._sz
    print "are 3, 5 connected? : ",
    print u.connected(3, 5)
    print "the number of components: ",
    print u.components
    print "size of id 3:", 
    print u._size(3)
