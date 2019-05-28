from modules.Board.Board import Board
from modules.Board.MapReader import *



class Timer:

    def __init__(self, time, x, y,c):
        self.time = time
        self.x = x
        self.y = y
        self.winable=True
        self.status=""
        self.steps=0
        self.tool=0
        if(c=="R"):
            self.steps = 1
        if(c=="B"):
            self.tool = 1
        if(c=="Y"):
            self.steps = 2
    def sprite(self):
        font = pygame.font.SysFont("comicsansms", 18)
        text = font.render(str(self.time), True, (255, 255, 255))
        if (self.status != ""):
            text = font.render(self.status, True, (255, 255, 255))
        sprite = text
        return sprite

    def Red(self):
        self.steps=1
    def Blue(self):
        self.tool=1
    def Yellow(self):
        self.steps=2
    #def Defuse(self):
     #   if(player near):
      #      if even key type space


