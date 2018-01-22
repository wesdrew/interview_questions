"""

a simple representation of an undirected graph using adjacency lists. Input is 
in the form a text file where lines are formatted:

(Node n)  (adjacent node 1) ... (adjacent node k) (newline terminator)


"""

    

class Graphs:

    ######################################################################
    # Functions on graphs:                                               #
    #                                                                    #
    #     __init__(file): constructor. Reads from files of               #
    #     format:                                                        #
    #         "                                                          #
    #          0 1 2        from node 0 there are edges to nodes 1 and 2 #
    #          1 2          from node 1 there is an edge to 2            #
    #          4        "   from node 4 there are no outgoing edges      #
    #                                                                    #
    #     size(): returns number of edges in graph                       #
    #                                                                    #
    #     order(): returns number of nodes in graph                      #
    ######################################################################
 
        
    def __init__(self, file):
        self._nodes = dict()
        
        ########################################################
        # 1. loading graph from file                           #
        # 2. reading lines from file to build adjacency lists  #
        ########################################################

        f = open(file, "r")
        adjaceny_lists = f.readlines()
        f.close()
        adjacency_lists = [list.rstrip().split(" ") for list in adjaceny_lists] # remove trailing newline
        for list in adjacency_lists: # init each node in graph 
            self._populate_adj_lists(list[0], list[1:len(list)])

        # calculate size, order of the graph
        self._size = len(self.get_edges())
        self._order = len(self._nodes.keys())

    def size(self):
        return self._size

    def order(self):
        return self._order
    
    ###############################################################################
    # helper functions for populating the adjacency list (actually dictionaries)  #
    # at self._nodes                                                              #
    #                                                                             #
    # representation:  {n_1 : [n_2, n_3, ... n_k] }                               #
    ###############################################################################


    # 1. check if entry for n already exists. if not, add it to self._nodes
    # 2. for each to_n in adj_list, check if it is saved already at self._nodes[n]
    #    if not, add it to self._nodes[n]. 
    # 3. record the edge from to_n -> n in self._nodes[to_n]
    
    def _populate_adj_lists(self, n, adj_list):
        self._add_node(n)       # the check if is dictionary is done inside _add_node
        for to_n in adj_list:
            self._add_node(to_n)
            self._add_edge(n, to_n) # likewise, exists checks are done inside _add_edge
            self._add_edge(to_n, n)
    
             
    # checks whether this node is in the dictionary
    def _node_exists(self, n):
        return self._nodes.has_key(n)

    # adds node to the dictionary, if necessary
    def _add_node(self, n):
        if not self._node_exists(n):
            self._nodes[n] = list() # empty adjacency list

    # checks whether this edge is already represented, eg {from_n : [...to_n] }
    def _edge_exists(self, from_n, to_n):
        return to_n in self._nodes[from_n]
        
    # adds edge to to_n in the adj. list stored at from_n
    def _add_edge(self, from_n, to_n):
        if not self._edge_exists(from_n, to_n):
            self._nodes[from_n].append(to_n)

    
    ##########################################################################
    # functions on nodes                                                     #
    #                                                                        #
    #     degree(node): return number edges on node                          #
    #     adjacent(node): return all nodes with an edge to node              #
    #     exists(node): return True if node is found in the graph            #
    ##########################################################################
        

    def degree(self, node):
        return len(self._nodes[node])

    def nodes(self):
        return self._nodes.keys()

    def adjacent(self, node):
        return self._nodes[node]

    def exists(self, node):
        return node in self._nodes

    ##############################################################
    # functions on edges:                                        #
    #                                                            #
    #     get_edges(): return a list of tuples representing all  #
    #                  edges in the graph                        #
    #     connected(n_1, n_2): return True if an edge connects   #
    #     n_1 and n_2                                            #
    ##############################################################

    def get_edges(self):
        edge_list = list()
        # make defensive copy
        copy = dict()           # couldn't make this work with dict comprehension
        for node in self._nodes.keys():
            copy[node] = list(self._nodes[node]) # list() prevents aliasing
        for n_1 in copy.keys():  # make tuple for all edges from n_1
            for n_2 in copy[n_1]:
                edge_list.append((n_1, n_2)) # create tuple
                copy[n_2].remove(n_1)       # don't double count
        return edge_list

    def connected(self, n_1, n_2):
        return n_2 in self._nodes[n_1]

    def __str__(self):
        string = "Node     :    Adjacent to...\n"
        string += "================================\n"
        for node in self._nodes.keys():
            string += str(node) + "\t :\t" + str(self._nodes[node]) + "\n"
        return string

        
