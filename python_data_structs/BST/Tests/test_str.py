# return nodes concatenated as a string. Nodes are concatentaed in the order
# they are visited in a breadth first traversal

def test(BST):
    print "\tPrinting BST:"
    BST.add("test", 1)
    BST.add("string", 2)
    BST.add("good", 3)
    BST.add("for", 4)
    BST.add("you", 5)
    print "\t\t" +  str(BST)
    
