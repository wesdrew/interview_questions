
def test(BST):
   
    print "\tTesting remove...",
    flag = True
    BST.add("test", 5)
    BST.add("A", 4)
    BST.add("DD", 1000)
    BST.add("CCC", 50)
    print BST.size()
    print BST._root
    print BST._left._root
    print BST._left._right._root
    print BST._left._right._left._root
    BST.remove("test")
    print BST._root
"""
    BST.remove("test")
    if BST.contains("test"):
        flag = False
    BST.contains("test")    # test that this will not cause error
    if BST.size() != 3:
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"
"""
