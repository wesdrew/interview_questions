
def test(List, data):
    print "\tTesting append..."
    print "\t\tOur data == ",
    print data
    for item in data:
        List.append(item)
    print "\t\tOur linked_list == ",
    print List

