class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.parent = None
        self.priority = None

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if(other == None):
            return False
        else:
            return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        if(other == None):
            return True
        else:
            return not(self == other)

    def __lt__(self, other):
        if(self.priority < other.priority):
            return True
        else:
            return False

    def __gt__(self, other):
        if(self.priority > other.priority):
            return True
        else:
            return False
