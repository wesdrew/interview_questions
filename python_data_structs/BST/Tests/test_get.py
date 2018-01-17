
def test(BST):
    print "Testing get...",
    flag = True
    BST.add("wes", 4)
    if not BST.get("wes"):
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"
