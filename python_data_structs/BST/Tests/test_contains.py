
def test(BST):
    flag = True
    print "\tTesting contains...",
    BST.add("test_key","test_value")
    if not BST.contains("test_key"):
        flag = False
    if BST.contains("false_key"):
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"
    
