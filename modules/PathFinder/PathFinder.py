from modules.PathFinder.dfs.GraphCreator import GraphCreator
from modules.PathFinder.dfs.Graph import Graph
from modules.PathFinder.BreathFirstSearch.GraphCreatorBFS import GraphCreatorBFS
from modules.PathFinder.BreathFirstSearch.GraphBFS import GraphBFS
from modules.PathFinder.BestFirstSearch.GraphBestFS import GraphBestFS
from modules.PathFinder.BestFirstSearch.GraphCreatorBestFS import GraphCreatorBestFS


class PathFinder:

    @staticmethod
    def getPathToByDfs(board, x, y):
        graphCreator = GraphCreator(board)
        graph = graphCreator.createGraph()
        graph.dfs()
        steps = graph.getPathTo(graphCreator.getVertexByCords(x, y))
        return steps

    @staticmethod
    def getPathToByBFS(board, x, y):
        graphCreator = GraphCreatorBFS(board)
        graph = graphCreator.createGraph()
        graph.bfs()
        steps = graph.getPathTo(graphCreator.getVertexByCords(x, y))
        return steps

    @staticmethod
    def getPathToByBestFirstSearch(board, x, y):
        graphCreator = GraphCreatorBestFS(board)
        graph = graphCreator.createGraph()
        graph.bestFirstSearch()
        steps = graph.getPathTo(graphCreator.getVertexByCords(x, y))
        return steps
