from Graphs import Graphs
from tests import test_str
import sys


# create a sample graph from file
g = Graphs(sys.argv[1])
test_str.test(g)
