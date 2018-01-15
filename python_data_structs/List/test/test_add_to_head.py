# testing add_to_head


def test(List, data):
    print "\tTesting add_to_head...",
    for item in data:
        List.add_to_head(item)
    flag = True
    for item in reversed(data):
        if item != List.dequeue():
            flag = False
            break
    if flag:
        print "passed!"
    else:
        print "failed!"

        
