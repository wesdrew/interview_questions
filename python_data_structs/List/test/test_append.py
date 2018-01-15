
def test(List, data):
    print "\tTesting append...",
    for item in data:
        List.append(item)
    for item in data:
        if item != List.dequeue():
            print "failed!"
    print "passed!"

