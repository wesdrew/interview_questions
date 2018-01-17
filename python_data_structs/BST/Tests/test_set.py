# test that we can reset a key, value pair in the BST. Also calling 
# set on a key not in the BST should place it in the tree

def test(BST):
    flag = True
    print "Testing set...",
    BST.add("C", 4)
    BST.set("C", 5)
    if BST.get("C") != 5:
        flag = False
    BST.set("D", 100)
    if BST.get("D") != 100:
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"
