# return all values in BST in a list, ordered as nodes are visited
# in a breadth-first traversal

def test(BST):
    flag = True
    print "Test get_values...",
    BST.add("B", 1)
    BST.add("A", 2)
    BST.add("C", 3)
    l = BST.get_values()
    if l[0] != 1 or l[1] != 2 or l[2] != 3:
        print "passed!"
    else:
        print "failed!"
