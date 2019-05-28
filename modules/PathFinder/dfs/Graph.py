from modules.PathFinder.dfs.Vertex import Vertex
from modules.Board.Direction import Direction


class Graph:
    def __init__(self, successorsList):
        self.successorsList = successorsList

    def dfs(self):
        for v in self.successorsList:
            if(v.visited == False):
                self.visiteVertex(v, None)

    def visiteVertex(self, v, parent):
        v.visited = True
        v.parent = parent
        for successor in self.successorsList[v]:
            if(successor.visited == False):
                self.visiteVertex(successor, v)

    def getPathTo(self, v):
        vpoint = v
        path = []
        while(vpoint.parent != None):
            if(vpoint.x < vpoint.parent.x):
                path.append(Direction.LEFT)
            elif(vpoint.x > vpoint.parent.x):
                path.append(Direction.RIGHT)
            elif(vpoint.y > vpoint.parent.y):
                path.append(Direction.DOWN)
            else:
                path.append(Direction.UP)
            vpoint = vpoint.parent
        path.reverse()
        return path
