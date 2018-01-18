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
#    _resize(): calculate the size of the whole tree by recursively 
#    calculating the size of the left and right tree and adding the 
#    root node
#
#
#
###################################################################


    def size(self):
        return self._size

    def is_empty(self):
        return True if self._size == 0 else False

    def _resize(self):
        new_size = 0
        if self._left:          # if the left tree exists, calculate its size
            self._left._resize()
            new_size += self._left.size()
        if self._right:         # same for right tree
            self._right._resize()
            new_size += self.size()
        if self._root:          # edge case: user might call _resize on empty BST
            new_size += 1
        self._size = new_size
        

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
        if key == self._root.get_key():
            return self._root.get_value()
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
#    _add(root, node) to place and create the subtree. Calls _resize 
#    to recalculate sizes of all subtrees 
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
            self._resize()

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
            root_key = self._root.get_key()
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
#    _remove(key): if key is found in the tree, find the sub_root where 
#    key is stored. Promote the left sub_tree if it exists and then 
#    place the right subtree within the left sub_tree. If the left does
#    not exist, promote the right subtree
#
#
#################################################################

    def remove(self, key):
        if self.contains(key):  # only remove if key is already in tree 
            self._remove(key)
            self._resize()

    # replacing using sub-tree not working 
    def _remove(self, tree, key):
        root_key = tree._root.get_key()
        if key == root_key:
            if tree._left:  # does left tree exist?
                right = tree._right # save reference to right tree
                tree._left._place(self._left, right) # place right subtree in left subtree
                tree = tree._left
            elif tree._right: # left tree didn't exist, promote right subtree
                tree = self._right # just promote right subtree
            else:
                tree._root = None
        elif key < root_key:
            tree._left._remove(tree._left, key) # we know left subtree exists
        else:
            tree._right._remove(tree._right, key) # we know right subtree exists

    def _place(self, tree, sub_tree):
        if sub_tree:            # only place subtree exists
            root_key = tree._root.get_key()
            sub_key = sub_tree._root.get_key()
            if sub_key < root_key:
                if tree._left:
                    tree._left._place(tree._left, sub_tree)
                else:
                    tree._left = sub_tree
            if sub_key > root_key:
                if tree._right:
                    tree._right._place(tree._right, sub_tree)
                else:
                    tree._right = sub_tree

