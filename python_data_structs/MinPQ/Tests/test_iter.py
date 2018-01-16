"""

Returns heap-sorted list for iteration


"""

def test(MinPQ):
    flag = True
    print "\tTesting __iter__...",
    for i in range(4, 0, -1):
        MinPQ.add(i)
    test_data = [1, 2, 3, 4]
    test_data_iter = iter(test_data)
    for item in MinPQ:
        if not item == next(test_data_iter):
            flag = False
            break
    if flag:
        print "passed!"
    else:
        print "failed!"


