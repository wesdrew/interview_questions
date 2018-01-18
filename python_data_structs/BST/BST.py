"""

Second draft!

Simple BST using wrapper class BST_Node. BST_Node wraps a tuple and has its 
comparison operators overwritten to make traversal choices easier to
understand.

@attributes

_root : BST_Node stored at this particular tree leaf
_left: reference to left sub_tree
_right: reference to right sub_tree
_size: size of left sub_tree + right_subtree + 1

@public methods

get(key): return value for key. If key does not exist return None
add(key, value): put key, value pair in the BST. None is not an acceptable value
                 for add
set(key, value): reset key, value pair in the BST. If key is not in the BST, 
                 and value != None, it is added to the tree. A value of None
                 triggers removal from the tree
contains(key): return True if key is stored in BST, False otherwise


"""
from BST_Nodes import BST_Nodes as Nodes


class BST:

    # constructor
    def __init__(self, Node = None):
        self._root = Node
        self._left = None
        self._right = None
        if Node is None:
            self._size = 0
        else:
            self._size = 1      # if created at a leaf, size of subtree is necessarily 1


#####################################################################
#
#    size methods 
#
#    size(): return current size of tree
#
#    is_empty(): return True if size == 0 else False
#
#
#
###################################################################


    def size(self):
        return self._size

    def is_empty(self):
        return True if self._size == 0 else False


##################################################################
#
#    get methods
#                                           
#    get: calls _get to traverse the tree and return value at correct
#        sub-root
#                                                        
#    _get: visits as many subroots as necessary to find matching key. 
#          returns value associated with key. 
#          
#                                                               
#                                                               
##################################################################


    def get(self, key):
        if self.contains(key):
            return self._get(key)
        else:
            return None
   
    def _get(self, key):
        if key == self._root._get_key():
            return self._root._get_value()
        else:
            if key < self._root:
                return self._left._get(key)
            if key > self._root:
                return self._right._get(key)

    
            
################################################################
#
#    Addition methods
#
#    add(key, value): creates a Node for key/value pair and calls
#    _add(root, node) to place and create the subtree. increment
#    size after insertion 
#
#    Edge cases: 
#    if contains(key) evaluates to True:
#    1. if value == None, trigger a remove operation 
#    2. otherwise, reset the key, value pair in the tree
#
#
#    _add(sub_root, node): traverse a sub-tree to find an appropriate
#    leaf node (ie. - a None reference). Create a subtree at that leaf 
#
#    
#################################################################


    def add(self, key, value):
        if self.contains(key):
            if value:           # value is not None
                return self.set(key, value)
            else:
                return self.remove(key)
        else:
            node = Nodes(key, value)
            self._add(node)
            self._size += 1

    def _add(self, node):
        if self._root:          # is this node already populated?
            if node < self._root:
                if self._left:            # subtree exists
                    self._left._add(node) # let the subtree handle adding node
                else:
                    self._left = BST(node) # create the subtree
            if node > self._root:
                if self._right:
                    self._right._add(node)
                else:
                    self._right = BST(node)
        else:                   # this leaf is None
            self._root = node   # not sure if this is correct

##################################################################
#
#    contains(key): traverse the tree until a None node is reached or 
#    a Node containing key is found
#
#
#################################################################

    def contains(self, key):
        if self._root:          # does this BST exist?
            root_key = self._root._get_key()
            if key < root_key:
                if self._left:
                    return self._left.contains(key)
                else:
                    return False
            if key > root_key:
                if self._right:
                    return self._right.contains(key)
                else:
                    return False
            else:               # key == root_key. key is in the tree
                return True
        else:
            return False        # edge case: tree is empty

    
################################################################
#
#    remove methods
#
#    remove(key): call _remove to prune tree and then _resize()
#    tree
#
#    _remove(key): if key is found in the tree:
#                    1st case: no children --> destroy the node
#                    2nd: 1 child -> promote the child to take place
#                         of the node
#                    3rd: both children exist: so search the right sub
#                         tree for a successor node, overwrite the to 
#                         be deleted node. Then delete the successor node
#
#    _min(tree): return the minimum value in a BST 
#
#    _delete(node): redefine node to be None
#
#
#
#################################################################

    def remove(self, key):
        if self.contains(key):
            self._remove(key)
            self._size = self._size - 1

    def _remove(self, key):
        if self._left and self._right: # both children exist
            successor = self._right._min() # get the minimum key, value in tree    
            self._root = successor
            self._delete(successor._get_key())
        elif self._left:        # only left child exists
            self = self._left
        elif self._right:       # only right child exists
            self = self._right
        else:
            self._root = None

    def _min(self):
        if self._left:
            return self._left._min() # there is still lesser values
        return self._root # there is no left tree, so this must be the min

    def _delete(self, key):     # this will travel to a leaf and assign it to None
        node = self._right
        while node:
            node_key = node._root._get_key()
            if key == node_key:
                node = None               
            elif key < node_key:
                node = node._left
            elif key > node_key:
                node = node._right

