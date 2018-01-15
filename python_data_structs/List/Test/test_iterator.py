
def test(List, data):
    print "\tTesting List iterator...",
    for item in data:
        List.append(item)
    i = iter(data)
    i2 = iter(List)
    flag = True
    for item in i:
        if item != next(i2):
            flag = False
            break
    if flag:
        print "passed!"
    else:
        print "failed!"
            
        
