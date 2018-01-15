# testing add_to_head


def test(List, data):
    print "Testing add_to_head...",
    for item in data:
        List.add_to_head(item)
    for item in reversed(data):
        if item != List.dequeue():
            print "failed!\n"
            break
    print "passed!\n"


        
