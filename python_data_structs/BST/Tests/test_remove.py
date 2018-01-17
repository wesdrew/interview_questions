
def test(BST):
    try:
        print "Testing remove...",
        flag = False
        BST.add("test", 5)
        BST.remove("test")
        BST.get("test")         # should throw a KeyError 
    except KeyError:
        print "passed!"
        flag = True
    finally:
        if flag:
            pass
        else:
            print "failed!"
