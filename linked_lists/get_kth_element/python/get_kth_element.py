import sys

from Nodes import Nodes as Nodes

def get_kth_element(k, node):
    if k == 0:
        return node.data
    else:
        return get_kth_element(k-1, node.next())


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print "Not enough arguments to get_kth element"
    else:
        k = int(sys.argv[1])    # get kth element from end of list
        head = Nodes(sys.argv[2])
        node = head
        for i in range(3, len(sys.argv)):
            next = Nodes(sys.argv[i])
            node.set_next(next)
            node = next
        print "the kth element is " + str(get_kth_element(len(sys.argv) - 2 - k, head))

                       
