"""

BST using nodes storing key, value pairs as tuples


@attributes:
    self._head -> head of this tree or sub-tree

@methods:
    add(self, key, value): add this key, value pair to tree.
    If current node is None add Node and re-calculate size of 
    tree. add replaces a key,value pair if already exists in the tree
    helper method _add hides tree traversal and comparisons

    remove(self, key): remove this key from the tree. Calls _remove which
    handles node deletion and tree cleanup

    set(self, key, value): reset this key, value pair in the tree. If it's
    not there, add it to the tree

    contains(self, key): return True if this key is found in the tree

"""

from BST_Nodes import BST_Nodes as Nodes


class BST:

    def __init__(self, BST = None): # default
        self._root = BST

################################################################
#
#    adding to tree:
#
#        add: calls _add to place a key, value in the tree and
#             recalculates the size of the tree. 
#             Note: None is not a legal value!
#
#        _add: traverses tree starting at root until it finds 
#              an empty leaf. When an empty leaf is found, a new
#              subtree is created and we unwind back to add()
#
#
#
################################################################



    # search for an empty leaf node in the tree, starting at head
    def add(self, key, value):
        if value is not None:
            self._root = self._add(key, value, self._root)
            self._root._resize()    # calculate new size of tree
        else:
            raise KeyError("None is not a legal value")

    def _add(self, key, value, sub_root):
        if sub_root is None:  # we can insert here! 
            return Nodes(key, value) # create new subtree here
        else:                                        # this subtree already exists
            sub_key = sub_root.get_key()             # key stored at node
            left_tree = sub_root._left_tree          # node's reference to its left subtree
            right_tree = sub_root._right_tree        # node's reference to its right subtree
            if key < sub_key: # we should insert on left
                return self._add(key, value, left_tree)
            elif key > sub_key: # we should insert on right
                return self._add(key, value, right_tree)
            elif key == sub_key: # we should reset this key, value pair
                sub_root.set_value(value)
                return sub_root

################################################################
#
#    Removing from tree:
#
#        remove(): checks if key is stored in the search tree. If 
#                it is, it calls _remove() to prune the BST, and 
#                then recalculates the size of the BST
#
#        _remove(): visits subtrees in the BST. When a sub_root 
#                   for our key is found, we remove the sub_root by 
#                   promoting that node's left subtree to 
#                   take it's place and then calling _place to
#                   place the right subtree within the left subtree.
#                   If no left subtree exists, we promote the right
#                   subtree and return.
#                   If neither left or right subtree exists, we simply
#                   replace a subtree with None
#
################################################################


    def remove(self, key):
        if self.contains(key):
            self._root = self._remove(key, self._root)
            self._root._resize()        # recalculate size of tree

    # remove node and attempt to promote one of its subtrees in its place
    # Then, place the other subtree in the promoted tree if necessary
    def _remove(self, key, sub_root):
        left_tree = sub_root._left_tree
        right_tree = sub_root._right_tree
        sub_key = sub_root.get_key()
        if key == sub_key: # base case - found the node to remove
            if left is not None:
                sub_root = left_tree
                sub_tree._place(sub_root, right_tree) # place right hand side in new subtree
            elif right is not None: # left subtree did not exist, so just replace
                sub_root = right_tree
            else:               # no tree to promote, delete this leaf
                sub_root = None
        elif key < sub_key:  # search left subtree for node to remove
            left_tree = self._remove(key, left_tree)
        else:                   # search right subtree for node
            right_tree = self._remove(key, right_tree)

    # Given a tree, find a leaf where sub_tree can be assigned
    def _place(self, tree, sub_tree):
        if tree is None:        # base case - found an empty leaf
            return sub_tree
        else:
            left_tree = sub_tree._left_tree
            right_tree = sub_tree._right_tree
            if sub_tree < tree:
                left_tree = tree._place(left_tree, sub_tree)
            elif sub_tree  > tree:
                right_tree = self._place(right_tree, sub_tree)

################################################################
#
#    Search / get functions:
#
#        contains(): return True if a key is in the search-tree, 
#                    False otherwise. Calls _contains to traverse
#                    BST
#
#        _contains(): check if this sub_root contains key, traverse
#                     BST until an empty leaf or key is found
#
#
#        get(): check if BST contains() key, call _get() to  
#               traverse BST and return value for key. Return None
#               if key is not found in BST
#
#        _get(): traverse tree starting from root. Return value when
#                key matches key stored at subroot
#
#
#################################################################
            
            
    def contains(self, key):
        return self._contains(key, self._root)

    def _contains(self, key, sub_tree):
        if sub_tree is None:
            return False
        else:
            sub_key = sub_tree.get_key()
            left_tree = sub_tree._left_tree
            right_tree = sub_tree._right_tree
            if key < sub_key:
                return self._contains(key, left_tree)
            elif key > sub_key:
                return self._contains(key, right_tree)
            else:
                return True # we must have found key
    
    def get(self, key):
        if self.contains(key):
            return self._get(key)
        else:
            return None

    def _get(self, key):
        root = self._root
        left_tree = root._left_tree
        right_tree = root._right_tree
        sub_key = root.get_key()
        if key < sub_key:
            return left_tree.get(key)
        elif key > sub_key:
            return right_tree.get(key)
        else:
            return root.get_value()
