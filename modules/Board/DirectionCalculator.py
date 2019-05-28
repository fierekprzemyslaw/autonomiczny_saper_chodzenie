from modules.Board.Direction import Direction
from modules.Board.Point import Point


class DirectionCalculator:
    @staticmethod
    def getCordsByDirection(x, y, direction):
        if(direction == Direction.LEFT):
            return Point(x-1, y)
        elif(direction == Direction.RIGHT):
            return Point(x+1, y)
        elif(direction == Direction.UP):
            return Point(x, y-1)
        elif(direction == Direction.DOWN):
            return Point(x, y+1)
        else:
            raise ValueError("Argument has to be Direction enum")

    @staticmethod
    def getDirectionByChords(x1, y1, x2, y2):
        if(y1 > y2):
            return Direction.DOWN
        elif(y1 < y2):
            return Direction.UP
        elif(x1 > x2):
            return Direction.LEFT
        else:
            return Direction.RIGHT
