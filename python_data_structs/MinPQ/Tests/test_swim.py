"""

MinPQ adds new items to end of MinPQ. swim compares child to parent and
swaps them if the child is less than its parent

MinPQ:

{ [1] [2] [3] [4] [5] }

1 is parent of children 2, 3

2 is parent of children 4, 5

for parent n, children are (n*2) and ((n*2) + 1)

note: MinPQ's start at index 1 

"""

def test(MinPQ):
    print "\tTesting swim function...",
    flag = True
    MinPQ.add(4)
    MinPQ.add(3)
    MinPQ.add(1)
    if not MinPQ.poll() == 1:
        print "failed!"
    else:
        print "passed!"
    
