# removes the minimum value from MinPQ. MinPQ should be
# empty after removing minimum value

def test(MinPQ):
    print "\tTesting poll...",
    flag = True
    MinPQ.add("testing")
    MinPQ.add("zephyr")
    if not "testing" == MinPQ.poll():
        flag = False
    if not "zephyr" == MinPQ.poll():
        flag = False
    if not MinPQ.is_empty():
        flag = False
    if flag:
        print "passed!"
    else:
        print "failed!"
