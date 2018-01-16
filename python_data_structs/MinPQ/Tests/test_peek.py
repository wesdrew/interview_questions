# testing peek -- can see the minimum value of MinPQ but does not 
# remove it

def test(MinPQ):
    flag = True
    print "\tTesting peek...",
    MinPQ.add("testing")
    if not "testing" == MinPQ.peek():
        flag = False
    if MinPQ.is_empty():        # is false if the object is removed
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"

