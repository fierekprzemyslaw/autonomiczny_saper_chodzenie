import pygame
from pygame.locals import *
from random import *
from modules.Board.Direction import Direction
import queue


class Saper:
    def __init__(self):
        self.walkRight = 'sprites/r.png'
        self.walkLeft = 'sprites/l.png'
        self.walkUp = 'sprites/u.png'
        self.walkDown = 'sprites/d.png'
        self.sprite = self.walkDown
        self.steps = queue.Queue()
        self.equipment = []

    def addSteps(self, stepsList):
        for step in stepsList:
            self.steps.put(step)

    def pickUp(self, item):
        self.equipment.append(item)

    def setSpriteDirection(self, direction):
        if(direction == Direction.LEFT):
            self.sprite = self.walkLeft
        elif(direction == Direction.RIGHT):
            self.sprite = self.walkRight
        elif(direction == Direction.UP):
            self.sprite = self.walkUp
        elif(direction == Direction.DOWN):
            self.sprite = self.walkDown
        else:
            raise ValueError("Argument has to be Direction enum")
