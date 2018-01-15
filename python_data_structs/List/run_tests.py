from Lists import Lists
from Nodes import Nodes
from Test import test_data as test_data
from Test import test_add_to_head as test_add_to_head
from Test import test_append as test_append
from Test import test_iterator as test_iterator
from Test import test_is_empty as test_is_empty
from Test import test_reversed as test_reversed

#print test_data.strings

s = test_data.strings
#print s

list = Lists.Lists()
test_is_empty.test(list)
test_append.test(list, test_data.strings)
test_iterator.test(list)
test_reversed.test(list)


