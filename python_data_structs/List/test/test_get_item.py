

def test(List, data, k):
    print "\tTesting get_item...",
    for item in data:
        List.append(item)
    i = List.get_item(k)
    if i != data[k]:
        print "failed!"
    else:
        print "passed!"
        
