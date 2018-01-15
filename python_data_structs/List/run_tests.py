from Lists import Lists
from Nodes import Nodes
from Test import test_data as test_data
from Test import test_add_to_head as test_add_to_head
from Test import test_append as test_append
from Test import test_iterator as test_iterator
from Test import test_is_empty as test_is_empty
from Test import test_reversed as test_reversed
from Test import test_add_to_head as test_add_to_head
from Test import test_get_item as test_get_item



#print test_data.strings

s = test_data.strings
#print s

test_is_empty.test(Lists.Lists())
test_append.test(Lists.Lists(), test_data.strings)
test_iterator.test(Lists.Lists(), test_data.strings)
test_reversed.test(Lists.Lists(), test_data.strings)
test_add_to_head.test(Lists.Lists(), test_data.strings)
test_get_item.test(Lists.Lists(), test_data.strings, 2)



