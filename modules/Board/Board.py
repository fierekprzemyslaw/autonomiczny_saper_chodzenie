from typing import List, Any

import pygame
from pygame.locals import *
from random import *
from modules.Board.Direction import Direction
from modules.MapObjects.Tool import Tool
from modules.Board.Point import Point
from modules.Board.DirectionCalculator import DirectionCalculator
from modules.Board.EquipmentGui import EquipmentGui
from modules.GameStatus import *
import time

DISPLACEMENT_Y = 45
DISPLACEMENT_X = 33
SQUARE_SIZE = 100
timers = []
class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.winable = True
        self.points =0
        self.items=0
        self.board = [[None for j in range(12)]for i in range(8)]
        self.eq_gui = EquipmentGui(1280, 125)
        self.window = pygame.display.set_mode((self.x, self.y))

    def start(self):
        pygame.display.set_caption("Saper")
        self.background = pygame.image.load('sprites/pole.png')
        self.run = True

        while (self.run):


            pygame.time.delay(50)
            self.renderSprites()
            self.renderGui()
            self.renderTimers()
            self.GameStatus()
            pygame.display.update()

            if(not self.player.steps.empty()):
                direction = self.player.steps.get()
                self.walk(direction)
                self.timeupdate()

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.close()

            # Tymczasowe manulane chodzenie
                if event.type == KEYDOWN:
                    self.timeupdate()
                    if (event.key == K_LEFT):
                        self.walk(Direction.LEFT)
                    if (event.key == K_RIGHT):
                        self.walk(Direction.RIGHT)
                    if (event.key == K_DOWN):
                        self.walk(Direction.DOWN)
                    if (event.key == K_UP):
                        self.walk(Direction.UP)
                    if (event.key == K_SPACE):
                        x = self.getCordsOf(self.player)
                        for timer in timers:
                            if((x.x ==timer.x/100-1 and x.y==timer.y/100-1.5) or (x.x ==timer.x/100 and x.y==timer.y/100-0.5) or (x.x ==timer.x/100-2 and x.y==timer.y/100-0.5) or (x.x ==timer.x/100-1 and x.y==timer.y/100+0.5) ):
                                if(timer.steps!=0):
                                    timer.steps-=1
                                if(timer.tool!=0 and self.items!=0):
                                    timer.tool-=1
                                    self.items-=1
                                if(timer.steps==0 and timer.tool==0 and timer.status!="OK"):
                                    timer.status="OK"
                                    self.points -= 1

                if(self.winable==False):
                    if event.type == KEYDOWN:
                        self.close()


    def walk(self, direction):
        cords = self.getCordsOf(self.player)
        new_cords = DirectionCalculator.getCordsByDirection(
            cords.x, cords.y, direction)

        self.board[cords.y][cords.x].setSpriteDirection(direction)

        if(new_cords.x >= 0 and new_cords.x <= 11 and new_cords.y >= 0 and new_cords.y <= 7 and
           (self.board[new_cords.y][new_cords.x] == None or type(self.board[new_cords.y][new_cords.x]) is Tool)):
            if(type(self.board[new_cords.y][new_cords.x]) is Tool):
                self.player.pickUp(self.board[new_cords.y][new_cords.x])
            self.board[new_cords.y][new_cords.x] = self.board[cords.y][cords.x]
            self.board[cords.y][cords.x] = None
        else:
            return False

    def getCordsOf(self, object):
        for index_y, y in enumerate(self.board):
            for index_x, x in enumerate(y):
                if(x == self.player):
                    return Point(index_x, index_y)

    def addObject(self, game_object, x, y):
        self.board[y][x] = game_object


    def addPlayer(self, player_object, x, y):
        self.board[y][x] = player_object
        self.player = player_object
        self.eq_gui.setEquipment(self.player.equipment)

    def renderSprites(self):
        self.window.blit(self.background, (0, 0))
        for index_y, y in enumerate(self.board):
            for index_x, x in enumerate(y):
                if(x != None):
                    sprite = pygame.image.load(x.sprite).convert_alpha()
                    self.window.blit(sprite, (DISPLACEMENT_X + index_x*SQUARE_SIZE,
                                              DISPLACEMENT_Y + index_y*SQUARE_SIZE))
        if(self.winable==False):
            self.text("GAMEOVER",400,300)
        if (self.points == 0):
            self.text("YOU WIN", 400, 300)

    def renderGui(self):
        renderList = self.eq_gui.getRenderList()
        self.items = len(renderList)
        for control in renderList:
            sprite = pygame.image.load(control.sprite).convert_alpha()
            self.window.blit(
                sprite, (self.eq_gui.x + control.x, self.eq_gui.y + control.y))

    def renderTimers(self):
        for timer in timers:
            self.window.blit(timer.sprite(),(timer.x,timer.y))


    def GameStatus(self):
        for time in timers:
            if (time.time <= 0):
               self.winable=False

        return True

    def timeupdate(self):
        for time in timers:
            time.time -=1



    def text(self,text, x, y):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 90)
        self.window.blit(myfont.render(text, False, (255, 255, 255)), (x, y))

    def close(self):
        self.run = False
        pygame.quit()
