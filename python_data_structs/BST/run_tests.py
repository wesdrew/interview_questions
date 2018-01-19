from Tests import test_contains
from Tests import test_add
from Tests import test_size
from Tests import test_remove
from Tests import test_keys
from Tests import test_values
from Tests import test_iter
from BST import BST as BST


print "Testing BST methods..."
test_contains.test(BST())
test_add.test(BST())
test_size.test(BST())
test_remove.test(BST())
test_keys.test(BST())
test_values.test(BST())
test_iter.test(BST())
