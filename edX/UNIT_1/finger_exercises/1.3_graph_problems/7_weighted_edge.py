class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

###

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        # self.weight = ...

    def getWeight(self):
        # Your code here
        pass

    def __str__(self):
        return f"{self.src} -> {self.dest} ({self.getWeight()})"
        
    def getWeight(self):
        pass