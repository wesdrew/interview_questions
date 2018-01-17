# return a list of all keys in BST, returned in whatever order 
# a breadth first search returns them

def test(BST):
    flag = True
    BST.add("C", 3)
    BST.add("A", 6)
    BST.add("Z", 10)
    print "Testing get_keys...",
    l = BST.get_keys()
    if l[0] != "C" or l[1] != "A" \
            or l[2] != "Z":
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"

