# return all values in BST in a list, ordered as nodes are visited
# in a breadth-first traversal

def test(BST):
    print "\tTesting get_values...",
    BST.add("B", 1)
    BST.add("A", 2)
    BST.add("C", 3)
    l = BST.get_values()
    if l[0] == 1 and l[1] == 2 and l[2] == 3:
        print "passed!"
    else:
        print "failed!"
