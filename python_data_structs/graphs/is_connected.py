"""


Given an undirected graph, determine whether it is a connected graph 
by running either depth first search or breadth first search 


"""
import sys
from graphs import Graphs
    

###########################################################################
# Search methods:                                                         #
#                                                                         #
#     Both search methods return a "visited" set. A graph is strongly     #
#     connected if every node in the Graph appears in the visited set     #
#                                                                         #
#     breadth_first(Graph): visits nodes in BFS, returns a set of visited #
#     nodes.                                                              #
#                                                                         #
#     depth_first(Graph): visits nodes in DFS, returns a set of visited   #
#     nodes.                                                              #
###########################################################################


def breadth_first(Graph):
    visited = set()
    to_visit = list()
    to_visit.append(Graph.nodes()[0]) # since this an undirected graph, pick start randomly
    while to_visit:
        node = to_visit.pop()
        visited.add(node)       # mark that node as visited
        for neighbor in Graph.adjacent(node):
            if neighbor not in visited:
                to_visit.append(neighbor)
    return visited

def depth_first(Graph):
    start = Graph.nodes()[0]
    visited = set()
    _dfs(Graph, visited, start)
    return visited

def _dfs(Graph, visited_set, node):
    if node not in visited_set:
        visited_set.add(node)
        for neighbor in Graph.adjacent(node):
            _dfs(Graph, visited_set, neighbor)

# return True if a Graph is strongly connected (every node of the graph can
# visited in bfs or dfs 
def is_connected(Graph):
    visited = breadth_first(Graph)
    all_nodes = set()
    for node in Graph.nodes():
        all_nodes.add(node)
    # if symmetric_difference exists than some nodes were not reachable
    if all_nodes.symmetric_difference(visited):
        return False
    else:
        return True

# unit test
if __name__ == "__main__":
    g = Graphs.Graphs(sys.argv[1])
    print g
    flag = is_connected(g)
    if flag:
        print "Graph is connected!"
    else:
        print "Graph is not connected!"

