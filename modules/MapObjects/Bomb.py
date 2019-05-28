
from typing import List, Any

import pygame
from pygame.locals import *
from random import *

class Bomb:

    def defuse(self,code):
        if(self.code == code):
            return True
        else:
            return False



