from modules.PathFinder.BreathFirstSearch.Vertex import Vertex
from modules.Board.Direction import Direction
import queue


class GraphBFS:
    def __init__(self, successorsList):
        self.successorsList = successorsList
        self.q = queue.Queue()

    def bfs(self):
        startv = list(self.successorsList.keys())[0]
        self.q.put(startv)
        startv.visited = True
        while not self.q.empty():
            v = self.q.get()
            for successor in self.successorsList.get(v):
                if successor.visited == False:
                    self.q.put(successor)
                    successor.visited = True
                    successor.parent = v

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
