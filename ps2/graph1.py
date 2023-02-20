class Node(object):
    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    
    
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return '{}->{}'.format(self.src, self.dest)


class WeigthedEdge(Edge):
    def __init__(self, src, dest, outdoor_distance, total_distance):
        super().__init__(src, dest)
        self.outdoor_distance = outdoor_distance
        self.total_distance = total_distance

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {} # must be a dictionary of Node -> list of edges

    def add_node(self):
        '''
        self: ...
        return: ...
        '''