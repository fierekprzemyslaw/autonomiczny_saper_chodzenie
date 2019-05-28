import pygame
from pygame.locals import *
from random import *
from modules.MapObjects.Bomb import Bomb


class BombBlue(Bomb):
    def __init__(self):
        self.sprite = 'sprites/bombB.png'
        self.code = 0
