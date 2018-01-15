

def test(List, data):    
    print "\tTesting List reversed iterator...",
    for item in data:
        List.append(item)
    r = reversed(data)
    test = reversed(List)
    flag = True
    for item in r:
        if item != next(test):
            flag = False
            break
    if flag:
        print "passed!"
    else:
        print "failed!"
