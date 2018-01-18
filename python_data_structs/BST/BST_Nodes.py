"""

A simple search tree node with key, value pair saved as a tuple

"""

class BST_Nodes:
    
    def __init__(self, key, value):
        self._data = (key, value)


####################################################
#
#    public methods
#
#    get_key(): return key in key, value pair
#
#    get_value(): return value in k, v pair
#
#    set_value(new_value): save key, new_value pair at _data reference
#
#    size(): return size of subtree / tree
#
#    _resize(): called after every insertion / deletion
#
####################################################

    def _get_key(self):
        return self._data[0]

    def _get_value(self):
        return self._data[1]

    def _set_value(self, new_value):
        self._data = (self._data[0], new_value)
        return None

 
################################################################
#
# Overwritten comparison methods compare on the key 
# 
# __lt__
#
# __gt__
#
# __eq__
#
# __ne__
#
################################################################
    
    def __lt__(self, other):
        return self._data[0] < other._data[0]

    def __gt__(self, other):
        return self._data[0] > other._data[0]

    def __eq__(self, other):
        return self._data[0] == other._data[0]
    
    def __ne__(self, other):
        return self._data[0] != other._data[0]

################################################################
#
# Other overwritten methods
#
# __str__
#
################################################################

    def __str__(self):
        string = "{'" + str(self._data[0]) + "':'" + str(self._data[1]) + "'}"
        return string

