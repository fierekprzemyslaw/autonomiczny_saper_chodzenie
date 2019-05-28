#!/usr/bin/python
from modules.Board.Board import Board

from modules.MapObjects.Saper import Saper
from modules.Board.MapReader import *
from modules.PathFinder.PathFinder import PathFinder

pygame.init()
board = Board(1480, 900)
MapReader.read("maps/map2.txt", board)
s = Saper()
#steps = PathFinder.getPathToByDfs(board, 3, 6)
#steps = PathFinder.getPathToByBFS(board, 3, 6)
#steps = PathFinder.getPathToByBestFirstSearch(board, 3, 6)
#s.addSteps(steps)
board.addPlayer(s, 5, 0)



board.start()
