# return a list of all keys in BST, returned in whatever order 
# a breadth first search returns them

def test(BST):
    flag = True
    BST.add("C", 3)
    BST.add("A", 6)
    BST.add("Z", 10)
    print "\tTesting __iter__...",
    i = iter(BST)
    if next(i) != ("C", 3):
        flag == False
    if next(i) != ("A", 6):
        flag == False
    if next(i) != ("Z", 10):
        flag == False
    if flag:
        print "passed!"
    else:
        print "failed!"
    i2 = iter(BST)
