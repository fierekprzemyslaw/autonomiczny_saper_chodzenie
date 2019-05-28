from modules.PathFinder.BestFirstSearch.Vertex import Vertex
from modules.PathFinder.BestFirstSearch.GraphBestFS import GraphBestFS
from modules.MapObjects.Tool import Tool
from modules.PathFinder.Destination import Destination
from modules.MapObjects.Bomb import Bomb


class GraphCreatorBestFS:
    def __init__(self, board):
        self.vertices = []
        self.board = board
        for indexline, line in enumerate(self.board.board):
            for indexrow, row in enumerate(line):
                if(row == None or type(row) is Tool):
                    v = Vertex(indexrow, indexline)
                    self.vertices.append(v)

    def getVertexByCords(self, x, y):
        for v in self.vertices:
            if(v.x == x and v.y == y):
                return v
        return False

    def getSuccsessorsList(self, v):
        successors = []
        if v.y < 7 and self.board.board[v.y+1][v.x] == None or type(self.board.board[v.y+1][v.x]) is Tool:
            successor = self.getVertexByCords(v.x, v.y+1)
            successors.append(successor)
        if v.y > 0 and self.board.board[v.y-1][v.x] == None or type(self.board.board[v.y-1][v.x]) is Tool:
            successor = self.getVertexByCords(v.x, v.y-1)
            successors.append(successor)
        if v.x < 11 and self.board.board[v.y][v.x + 1] == None or type(self.board.board[v.y][v.x + 1]) is Tool:
            successor = self.getVertexByCords(v.x + 1, v.y)
            successors.append(successor)
        if v.x > 0 and self.board.board[v.y][v.x - 1] == None or type(self.board.board[v.y][v.x - 1]) is Tool:
            successor = self.getVertexByCords(v.x - 1, v.y)
            successors.append(successor)
        return successors

    def getAllSuccessorsList(self):
        dictionary = {}
        for v in self.vertices:
            successors = self.getSuccsessorsList(v)
            dictionary[v] = successors
        return dictionary

    def getAllDestinations(self):
        destinations = []
        for indexline, line in enumerate(self.board.board):
            for indexrow, row in enumerate(line):
                if(type(row) is Tool):
                    d = Destination(indexrow, indexline)
                    destinations.append(d)
                elif(type(row) is Bomb):
                    v = self.getBombNextVertex(indexrow, indexline)
                    d = Destination(v.x, v.y)
                    destinations.append(d)
        return destinations

    def getBombNextVertex(self, x, y):
        if not (self.getVertexByCords(x+1, y) == False):
            return self.getVertexByCords(x+1, y)
        elif not(self.getVertexByCords(x-1, y) == False):
            return self.getVertexByCords(x-1, y)
        elif not(self.getVertexByCords(x, y+1)):
            return self.getVertexByCords(x, y+1)
        elif not(self.getVertexByCords(x, y-1)):
            return self.getVertexByCords(x, y-1)

    def createGraph(self):
        graph = GraphBestFS(self.getAllSuccessorsList())
        graph.setDestinations(self.getAllDestinations())
        graph.setPriorities()
        return graph
