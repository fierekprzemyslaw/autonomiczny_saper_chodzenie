from typing import List, Any

import pygame
from pygame.locals import *
from random import *

pygame.init()

win = pygame.display.set_mode((1480,900))
pygame.display.set_caption("Bomberman Pepega")

scrWidth=1280
scrLength=900

x = 544
y = 720
width = 68
height = 92
vel = 100

walkRight=pygame.image.load('../sprites/r.png').convert_alpha()
walkLeft = pygame.image.load('../sprites/l.png').convert_alpha()
walkUp=pygame.image.load('../sprites/u.png').convert_alpha()
walkDown=pygame.image.load('../sprites/d.png').convert_alpha()

bombY=pygame.image.load('../sprites/bombY.png').convert_alpha()
bombB=pygame.image.load('../sprites/bombB.png').convert_alpha()
bombR=pygame.image.load('../sprites/bombR.png').convert_alpha()
stone=pygame.image.load('../sprites/stone.png').convert_alpha()

bg=pygame.image.load('../sprites/pole.png')


run = True
isable=True
left = False
right = False
up = False
down = False
stepsCount = 0




b1=[45+randint(0,11)*100,60+randint(0,7)*100]
b2=[45+randint(0,11)*100,60+randint(0,7)*100]
b3=[45+randint(0,11)*100,60+randint(0,7)*100]
s1=[33+randint(0,11)*100,50+randint(0,7)*100]

def redrawGameWindow():
    win.blit(bg,(0,0))
    win.blit(bombB, ( b1[0], b1[1]))
    win.blit(bombR, ( b2[0], b2[1]))
    win.blit(bombY, ( b3[0], b3[1]))
    win.blit(stone, ( s1[0], s1[1]))

    if left:
        win.blit(walkLeft,(x,y))
    elif right:
        win.blit(walkRight,(x,y))
    elif up:
        win.blit(walkUp,(x,y))
    elif down:
        win.blit(walkDown,(x,y))
    else:
        win.blit(walkUp,(x,y))
    pygame.display.update()

while run:
    pygame.time.delay(100)

    #manual controlers for player (moving in the area)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN :
            if (event.key == K_LEFT) and x>vel :
                x -= vel
                up=False
                down = False
                right = False
                left = True
            if (event.key == K_RIGHT) and x<1280 -width - vel:
                x += vel
                up = False
                down = False
                right = True
                left = False
            if (event.key == K_DOWN) and y< 900 -height-vel:
                y += vel
                up = False
                down = True
                right = False
                left = False
            if (event.key == K_UP) and y>vel:
                y -= vel
                up = True
                down = False
                right = False
                left = False
        redrawGameWindow()


pygame.quit()
