"""

Full test. Every item should be greater than the item
previously removed. 


"""


def test(MinPQ, data):
    flag = True
    print "\tFull test...",
    for item in data:
        MinPQ.add(item)
    n = MinPQ.poll()
    while not MinPQ.is_empty():
        n_2 = MinPQ.poll()
        if n > n_2:
            print "failed!"
            break
        n = n_2
    print "passed!"
