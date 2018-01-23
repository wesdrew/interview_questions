import sys
from Edges import Edges


"""

a simple representation of a weighted directed graph using adjacency lists. Input is 
in the form a text file where lines are formatted:

(Node n)  (adjacent node 1) ... (adjacent node k) (newline terminator)


@properites

    vertices: number of vertices in graph
    adjacent: store edges adjacent on each vertex. for each vertex store
    if vertex is dest and if vertex is start (so edges will be double counted)

"""


class DirectedGraphs:

    def __init__(self, file):
        
        ########################################################
        # 1. loading graph from file                           #
        # 2. reading lines from file to build adjacency lists  #
        ########################################################

        f = open(file, "r")
        number_of_nodes = int(f.readline().rstrip())
        edges = f.readlines()
        f.close()
        self._order = number_of_nodes
        self._adjacencies = dict()
        self._size = 0
        
        edges = [list.rstrip().split(" ") for list in edges]
        for edge in edges:
            # START = 0, DEST = 1, WEIGHT = 2
            self._add_edge(edge[0], edge[1], edge[2])
    
    
    def _add_edge(self, start, end, weight):
        edge = Edges(start, end, weight)
        if not self._adjacencies.has_key(start): # if these adj lists are not initialized, init them
            self._adjacencies[start] = list()
        if not self._adjacencies.has_key(end):
            self._adjacencies[end] = list()
        self._adjacencies[start].append(edge)
        self._adjacencies[end].append(edge)
        self._size += 1

    
    def edges(self):
        ret = set()
        for list in self._adjacencies.itervalues():
            for edge in list:
                ret.add(edge)
        return ret

    def size(self):
        return self._size

    def order(self):
        return self._order

    def _get_outgoing_edges(self, node):
        edges = list(set(self._adjacencies[node]))
        for edge in edges:
            if edge.dest() is node:
                edges.remove(edge)
        return edges

    def _get_incoming_edges(self, node):
        edges = list(set(self._adjacencies[node]))
        for edge in edges:
            if edge.start() is node:
                edges.remove(edge)
        return edges

    def __str__(self):
        string = "Node     :    Edge to...\n"
        string += "================================\n"
        nodes = self._adjacencies.keys()
        nodes.sort()
        for node in nodes:
            string += str(node) + "\t :\t"
            for edge in self._get_outgoing_edges(node):
                string += str(edge.dest()) + " "
            string += "\n"
        string += "\n"
        string += "Edges -> (start, dest, weight)\n"
        string += "================================\n"
        for edge in self.edges():
            string += str(edge) + "\n" 
        return string
    
if __name__ == "__main__":

    g = DirectedGraphs(sys.argv[1])
    print g
#    print g._get_outgoing_edges(2)
 #   print g._get_incoming_edges(2)
    print g._adjacencies
