import pygame
from pygame.locals import *
import sys

PINK=(85,0,93)
ORANGE=(93, 45, 0)
ORANGE=(255, 162, 0)
BLACK=(0,0,0)
RED=(255,0,0)
DRED=(140,0,92)
GREEN=(0,255,0)
HGREEN=(50,199,7)
HBLUE=(0,16,110)
BLUE=(0,0,255)
YELLOW=(0,255,255)
VIOLET=(193,0,248)
CYAN=(0,248,255)

# figure=[]
# figure[1]=[[1,1,1,1], [1,0,0,0]] #RED
# figure[0]=[[1,1], [1,0]] #HBLUE
# figure[2]=[[1,1,1], [1,0,0]] #DRED
# figure[3]=[[1,1,0,0], [0,1,1,1]] #PINK
# figure[4]=[[1,1,1,1], [0,1,0,0]] #YELLOW
# figure[4]=[[1,1,0],[0,1,0] [0,1,0]] #ORANGE
# figure[5]=[[1,1,1,1], [1,0,0,0]] #HGREEN
# figure[6]=[[1,1,1], [1,0,1]] #DGREEN
# figure[7]=[[1,1,1], [0,1,1]] #CYAN
# figure[8]=[[1,1,1], [1,0,0]] #DBLUE
# figure[7]=[[1,1,1,1], [1,0,0,0]] #BLUE
# figure[9]=[[1,1,1], [0,1,0]]#GREEN
# figure[10]=[[1,1,0], [0,1,0],[0,0,1]] #Violet

size =  (8, 8)
playField = (11, 5)
board=[[BLACK] * playField[0]] * playField[1]
print(board)

def draw(surface ,pf):
    for x in range(len(pf[0])):
        for y in range(len(pf[1])):
            print(x)

def addFigure(playField):
    pass

pygame.init()
surface = pygame.display.set_mode((500, 400), 0 ,32)
pygame.display.set_caption("ID Puzzler")
while True:
    for event in pygame.event.get():
        draw(surface, board )
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


