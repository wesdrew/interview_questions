

def test(List, data):
    print "Testing add_to_tail...",
    for item in data:
        List.add_to_tail(item)
    flag = True
    for item in data:
        print item
        if item != List.dequeue():
            flag = False
            break
    if flag:
        print "passed!"
    else:
        print "failed!"
