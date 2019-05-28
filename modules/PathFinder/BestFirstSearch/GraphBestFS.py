from modules.PathFinder.BestFirstSearch.Vertex import Vertex
from modules.Board.Direction import Direction
from modules.Board.DirectionCalculator import DirectionCalculator
from queue import PriorityQueue
import math


class GraphBestFS:
    def __init__(self, successorsList):
        self.successorsList = successorsList
        self.q = PriorityQueue()

    def setDestinations(self, destinations):
        self.destinations = destinations

    def setPriorities(self):
        for v in self.successorsList:
            for successor in self.successorsList[v]:
                direction = DirectionCalculator.getDirectionByChords(
                    v.x, v.y, successor.x, successor.y)
                distance = self.getNearestDestination(v, direction)
                successor.priority = distance

    def getNearestDestination(self, v, direction):
        distance = math.inf
        for destination in self.destinations:
            if(direction == Direction.UP):
                if(destination.y > v.y):
                    current_distance = abs(
                        destination.x-v.x) + abs(destination.y - v.y)
                    distance = min(distance, current_distance)
            elif(direction == Direction.DOWN):
                if(destination.y < v.y):
                    current_distance = abs(
                        destination.x-v.x) + abs(destination.y - v.y)
                    distance = min(distance, current_distance)
            elif(direction == Direction.LEFT):
                if(destination.x < v.x):
                    current_distance = abs(
                        destination.x-v.x) + abs(destination.y - v.y)
                    distance = min(distance, current_distance)
            elif(direction == Direction.RIGHT):
                if(destination.x > v.x):
                    current_distance = abs(
                        destination.x-v.x) + abs(destination.y - v.y)
                    distance = min(distance, current_distance)
        return distance

    def bestFirstSearch(self):
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
