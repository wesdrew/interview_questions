# testing is_empty on MinPQ

def test(MinPQ): 
    flag = True
    print "\tTesting is_empty on MinPQ...",
    if not MinPQ.is_empty():
        flag = False
    MinPQ.add("testing")
    if MinPQ.is_empty():
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"
