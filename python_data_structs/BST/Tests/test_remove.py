
def test(BST):
   
    print "\tTesting remove...",
    flag = True
    BST.add(10, 5)
    BST.add(3, 4)
    BST.add(100, 1000)
    BST.add(1, 50)
    BST.add(4, 60)
    BST.remove(10)
    if BST.contains(10):
        flag = False
    BST.contains("test")    # test that this will not cause error
    if BST.size() != 4:
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"

