from modules.PathFinder.BreathFirstSearch.Vertex import Vertex
from modules.PathFinder.BreathFirstSearch.GraphBFS import GraphBFS
from modules.MapObjects.Tool import Tool


class GraphCreatorBFS:
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

    def createGraph(self):
        return GraphBFS(self.getAllSuccessorsList())
