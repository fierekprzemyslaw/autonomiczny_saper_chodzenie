import pygame



from pygame.locals import *
from modules.MapObjects.BombRed import *
from modules.MapObjects.BombBlue import *
from modules.MapObjects.BombYellow import *
from modules.Board.Board import *
from modules.MapObjects.Stone import *
from modules.MapObjects.Tool import Tool
from modules.MapObjects.Water import Water
from modules.Board.Timer import Timer



class MapReader:
    @staticmethod
    def read(mapfile, board):
        f = open(mapfile, "r")
        mapa = f.read().split("\n")
        for indexline, line in enumerate(mapa):
            for indexrow, row in enumerate(line):
                #print(indexline, indexrow)
                if row == "R":
                    bomb = BombRed()
                    board.addObject(bomb, indexrow, indexline)
                    timers.append(Timer(30,indexrow*100+100,indexline*100+50,"R"))

                    board.points+=1
                elif row == "B":
                    bomb = BombBlue()
                    board.addObject(bomb, indexrow, indexline)
                    timers.append(Timer(30,indexrow*100+100,indexline*100+50,"B"))
                    board.points += 1
                elif row == "Y":
                    bomb = BombYellow()
                    board.addObject(bomb, indexrow, indexline)
                    timers.append(Timer(30,indexrow*100+100,indexline*100+50,"Y"))
                    board.points += 1
                elif row == "S":
                    stone = Stone()
                    board.addObject(stone, indexrow, indexline)
                elif row == "T":
                    tool = Tool()
                    board.addObject(tool, indexrow, indexline)
                elif row == "W":
                    water = Water()
                    board.addObject(water, indexrow, indexline)

        f.close()
