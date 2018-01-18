
def test(BST):
    flag = True
    print "\tTesting resize...",
    BST.add("test_key","test_value")
    BST.add("A", 3)
    BST.add("Z", 100)
    BST.add("C", 10)
    if BST.size() != 4:
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"
    
