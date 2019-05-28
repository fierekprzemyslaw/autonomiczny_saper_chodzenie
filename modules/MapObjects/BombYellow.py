import pygame
from pygame.locals import *
from random import *
from modules.MapObjects.Bomb import Bomb


class BombYellow(Bomb):
    def __init__(self):
        # dodaj .convert_alpha() w board
        self.sprite = 'sprites/bombY.png'
        self.code = 0
