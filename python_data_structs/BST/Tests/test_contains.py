
def test(BST):
    flag = True
    print "\tTesting contains...",
    BST.add("test_key","test_value")
    BST.add("A", 3)
    BST.add("Z", 100)
    BST.add("C", 10)
    if not BST.contains("test_key"):
        flag = False
    if BST.contains("false_key"):
        flag = False
    if not BST.contains("A") or not BST.contains("Z") or not BST.contains("C"):
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"
    
