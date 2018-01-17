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

    def __init__(self):
        self._head = None

    def add(self, key, value):
        _add(self, key, value, self._head)
        self._head._resize()    # calculate new size of tree

    def _add(self, key, value, tree_node):
        if tree_node._head is None:  # we can insert here! 
            self._head = Nodes(key, value)
        else:
            to_compare = tree_node._head.get_key()
            if key < to_compare: # we should insert on left 
                self._add(key, value, tree_node._head._left_tree)
            elif key > to_compare: # we should insert on right
                self._add(key, value, tree_node._head._right_tree)
            elif key == to_compare: # we should reset this key, value pair
                self._head.set_value()

    def remove(self, key):
        if self.contains(key):
            self._head = _remove(self._head, key)
            self._head._resize()        # recalculate size of tree

    # remove node and attempt to promote one of its subtrees in its place
    # Then, place the other subtree in the promoted tree if necessary
    def _remove(self, key, node):
        left = node._head._left_tree
        right = node._head._right_tree
        to_compare = node.get_key()
        if key == to_compare: # base case - found the node to remove
            if left is not None:
                node._head = node._head._left_tree
                self._place(node, right) # place right hand side in new subtree
            if right is not None: # left subtree did not exist, so just replace
                node._head = node._head._right_tree
        elif key < to_compare:
            self._remove(key, left)
        else:
            self._remove(key, right)

    # Given a tree, find a leaf where sub_tree can be assigned
    def _place(self, tree, sub_tree):
        if tree is None:        # base case - found an empty leaf
            return sub_tree
        if sub_tree._head < tree._head:
            tree._head._left_tree = self._place(tree._head._left_tree, sub_tree)
        elif sub_tree._head > tree._head:
            tree._head._right_tree = self._place(tree._head._right_tree, sub_tree)
    
        
            
            
        
