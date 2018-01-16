

def test(MinPQ):

    print "\tString rep of MinPQ:"
    strings = ["in", "descending", "order"]
    print "\t\tdata == " + str(strings)
    for string in strings:
        MinPQ.add(string)
    print "\t\tMinPQ == " + str(MinPQ)
