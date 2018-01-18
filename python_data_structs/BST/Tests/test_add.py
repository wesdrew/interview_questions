
def test(BST):
    print "\tTesting add...",
    flag = True
    BST.add("test", "test_value")
    if BST.is_empty():
        flag = False
    if not BST.get("test"):
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"

