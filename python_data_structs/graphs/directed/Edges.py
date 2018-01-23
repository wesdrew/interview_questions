###################################################################                                  
# Helper class for Graphs. Represents an edge from start node to  #                                  
# dest node with cost weight. Internally represented as tuple     #                                  
###################################################################                                  


class Edges:

    def __init__(self, start, dest, weight):
        self._edge = (start, dest, weight)
        
    def start(self):
        return self._edge[0]
    
    def dest(self):
        return self._edge[1]

    def weight(self):
        return self._edge[2]

   #Overloaded comparison operators                                                                       

    def __gt__(self, other):
        return self.weight() > other.weight()
    
    def __lt__(self, other):
        return self.weight() < other.weight()

    def __ge__(self, other):
        return self.weight() >= other.weight()

    def __le__(self, other):
        return self.weight() <= other.weight()

    def __eq__(self, other):
        return self.weight() == other.weight()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._edge)

    def __str__(self):
        return str(self._edge)

