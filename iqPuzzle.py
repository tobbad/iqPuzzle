import pygame
from pygame.locals import *
import sys

PINK=(255, 105, 180)
ORANGE=(255, 162, 0)
BLACK=(0,0,0)
RED=(255,0,0)
TRED=(255,99,71)
DRED=(165,42,42)
GREEN=(0,255,0)
DGREEN=(0,100,0)
HGREEN=(0,199,7)
HBLUE=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
VIOLET=(193,0,248)
CYAN=(125, 249, 255)
DCYAN=(41,91,64)
DBLUE=(0, 0,139)
BLUE=(0, 0, 255)
VIOLET=(90, 0, 100)
DVIOLET=(148, 0, 255)
ORANGE=(255, 165, 0)
WHITE=(255, 255, 255)

figure=[{}]*13
figure[0]={'color':TRED, 'tile':[[1,1,1,1], [1,0,0,0]], 'pos':(7,0),  'defPlc':(10,2,1,0), 'text':'F1'} #RED
figure[1]={'color':PINK , 'tile':[[1,1,0,0], [0,1,1,1]], 'pos':(10,0),  'defPlc':(0,0,0,0), 'text':'F2'} #PINK
figure[2]={'color':CYAN, 'tile':[[1,1], [1,0]], 'pos':(13,0),  'defPlc':(0,0,0,0), 'text':'F3'} #HBLUE
figure[3]={'color':DBLUE, 'tile':[[1,1,1], [1,0,0]], 'pos':(16,0),  'defPlc':(0,0,0,0), 'text':'F4'} #DRED
figure[4]={'color':YELLOW, 'tile':[[1,1,1,1], [0,1,0,0]],  'defPlc':(0,0,0,0), 'pos':(7,5), 'text':'F5'}#YELLOW
figure[5]={'color':DGREEN, 'tile':[[1,1,1], [1,0,1]],  'defPlc':(0,0,0,0), 'pos':(10,5), 'text':'F6'} #DGREEN
figure[6]={'color':DVIOLET, 'tile':[[1,1,0], [0,1,0], [0,1,1]],  'defPlc':(0,0,0,0), 'pos':(7,10), 'text':'F8'}   #Violet
figure[7]={'color':GREEN, 'tile':[[1,1,1], [0,1,0]],  'defPlc':(0,0,0,0), 'pos':(11,10) , 'text':'F7'}#GREEN
figure[8]={'color':ORANGE, 'tile':[[1,1,0], [0,1,1]],  'defPlc':((0,0,0,0), (0,1,0)), 'pos':(15,10), 'text':'F9'} #ORANGE
figure[9]={'color':DRED, 'tile':[[1,0], [1,1], [0,1]], 'defPlc':(0,0,0,0), 'pos':(7,14), 'text':'F10'} #ORANGE
figure[10]={'color':DCYAN, 'tile':[[1,1,1], [0,1,1]], 'defPlc':(0,0,0,0), 'pos':(11,14), 'text':'F11'} #HGREEN
figure[11]={'color':BLUE, 'tile':[[1,1,1], [0,0,1], [0,0,1]],  'defPlc':(0,0,0,0), 'pos':(14,14), 'text':'F11'} #DBLUE
figure[12]={'color':BLACK, 'tile':[[1,1,1,1], [1,1,1,1], [1,1,1,1]],  'defPlc':(0,0,0,0), 'pos':(-1,-1), 'text':'F11'} #DBLUE

placedFigures=[(None, None, None )]*len(figure)
configurations=[{}]*5
#confiurations[0]={'figOR':[[0,1,1], [1,0,0], [11,0,0], [7,1,1]],'pos':((0,0), (3, 3),(5,0),(5,3))}
configurations[0]={'figOR':[[1,1,0], [11,0 ,0], [7,0,0]],'pos':((0,0), (3,2), (0,3),(5,3))}
print(configurations)

gridSize=25
size =  gridSize-6
playField = ((0,11), (0,5))
 =((12,16),(1,5))
boardSize =(19,19)

pygame.init()
surface = pygame.display.set_mode(  (gridSize*boardSize[0]+gridSize, gridSize*boardSize[1]+gridSize), 0 ,32)
pygame.display.set_caption("IQ Puzzler")
board=[[(0,0,0) for i in range(boardSize[0])] for j in range(boardSize[1])]
pygame.font.init()
basicFont=pygame.font.SysFont(None, 48)

def draw(surface ,pf):
    for x in range(len(pf)):
        for y in range(len(pf[0])):
            xp=gridSize*x
            yp=gridSize*y
            pygame.draw.circle(surface, pf[x][y], (xp+size,yp+size),size>>1,0)
    pygame.display.update()

def initPlayField(board):
    for x in range(playField[0][1]) :
        for y in range(playField[1][1]):
            xp=gridSize*x
            yp=gridSize*y
            board[x][y] = WHITE

def addFigure(board,fig, xpos, ypos ,mirror, orientation, alwaysPlace):
    #playfield: where to paint to
    # figure: what to paint
    # x,y: origin of figure
    # Miror up/down
    # orientation: 
    # -1 : Rotate counter clock wise
    #  0 : Place as it is
    #  1 : Rotate clock wise
    # always place
    xposMax=xpos
    yposMax=ypos
    sizex=len(fig['tile'][0])
    sizey=len(fig['tile'])
    bsizex=playField[0][1]
    bsizey=playField[1][1]
    if orientation==0:
        xposMax+=sizex
        yposMax+=sizey
    else:
        xposMax+=sizey
        yposMax+=sizex
    print(xpos, xposMax, ypos, yposMax, playField, alwaysPlace)
    if not (xpos<bsizex and xposMax<=bsizex) :
        print("x: %d, %d<%d"%(xpos, xposMax, bsizex))
        print("Drop figure due to xpos")
    if not (ypos<bsizey and yposMax<=bsizey) :
        print("y: %d, %d<=%d"%(ypos, yposMax, bsizey))
        print("Drop figure due to ypos")
    if not alwaysPlace:
        if not (xpos<bsizex and xposMax<=bsizex and ypos<= bsizey and yposMax<=bsizey):
            print("Drop figure due to not in valid range")
            return -1,-1
    print('figure', fig, sizex, sizey)
    xseq=list(range(sizex))
    print(xseq)
    if mirror:
        xseq.reverse()
    print(xseq)
    for x in xseq:
        yseq= list(range(sizey))
        if orientation:
            yseq.reverse()
        
        for y in yseq:
            print(x,y, fig['color'], fig['tile'][y])
            if fig['tile'][y][x]==1:
                board[x+xpos][y+ypos] =  fig['color']
            else:
                board[x+xpos][y+ypos] =  WHITE
            #print(x+xpos,y+ypos, playField[x+xpos][y+ypos] )

def addKeystoneName(key):
    text=basicFont.render(key['text'],True, WHITE, BLACK)
    textBox=text.get_rect()
    print(key['pos'][0])
    #pygame.draw.rect(surface, RED,(key['pos'][0]*gridSize, key['pos'][1]*gridSize* (textBox.left+ 20),textBox.right+20, textBox.height+40))
    surface.blit(text,textBox)

def getFigureCode(x,y):
    for i in range(len(figure)):
        ymin=figure[i]['pos'][0]*gridSize
        ymax=(figure[i]['pos'][0]+len(figure[i]['tile'])+1)*gridSize
        print(i,'y',ymin, "<",y,"<",ymax)
        if ymin<y and y < ymax:
            xmin=figure[i]['pos'][1]*gridSize
            xmax=(figure[i]['pos'][1]+len(figure[i]['tile'])+1)*gridSize
            print(i, 'x', xmin, "<", x, "<", xmax)
            if xmin<x and x<xmax:
                print("Key is %d" % i)
                return i
    return -1

def getPlaygroundPos(x,y):
    x=int(x/gridSize)
    y=int(y/gridSize)
    print(x,y)
    return x,y

def isInisPlacementRange(x,y,posRange):
    print(x,y, posRange,)
    isPlacement= x>=posRange[0][0] and x<posRange[0][1]
    print(isPlacement)
    isPlacement&= y>=posRange[1][0] and y<posRange[1][1]
    print(isPlacement)
    return isPlacement
    
#initPlayField(board)
#print(board)

initPlayField(board)
for i in range(len(figure)):
    print(figure[i])
    if figure[i]['pos'][1]<0: 
        continue
    addFigure(board, figure[i],figure[i]['pos'][1], figure[i]['pos'][0],0,0, True)
    addKeystoneName(figure[i])

for i in range(len(configurations[0]['figOR'])):
    print( "figOR", configurations[0]['figOR'] )
    figIdx= configurations[0]['figOR'][i][0]
    x=configurations[0]['pos'][i][0]
    y=configurations[0]['pos'][i][1]
    addFigure(board, figure[figIdx], x, y, configurations[0]['figOR'][i][1],configurations[0]['figOR'][i][2], True)

selectedKey=-1
rotateKeys=[pygame.locals.K_r]
while True:
    for event in pygame.event.get():
        draw(surface, board )
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            print(event.pos[0], event.pos[1])
            selectedKey=getFigureCode(event.pos[0], event.pos[1])
            print("Is key nr: %d" % selectedKey)
            addFigure(board, figure[-1], placementRange[0][0], placementRange[1][0], 0,0, True)
            addFigure(board, figure[selectedKey], placementRange[0][0], placementRange[1][0], 0,0, True)
            isPlaceRange=isInisPlacementRange(x,y,placementRange)
            if isPlaceRange:
                print("in range")
                
        if event.type == MOUSEBUTTONUP:
            print(event.pos[0], event.pos[1])
            x,y=getPlaygroundPos(event.pos[0], event.pos[1])
            isPlayGroundRange=isInisPlacementRange(x,y,playField)
            isPlaceRange=isInisPlacementRange(x,y,placementRange)
            if selectedKey>=0:
                print("Place at Location (%d, %d), inRange %d, inPlace %d" % (x, y,isPlayGroundRange,isPlaceRange))
                if isPlayGroundRange:
                    addFigure(board, figure[selectedKey], x, y, 0,0, True)
                if isPlaceRange:
                    print("Place in Placerange")
                    addFigure(board, figure[selectedKey], placementRange[0][0], placementRange[1][0], 0,0, True)

        if pygame.mouse.get_focused():
            print(event)
        if event.type == KEYDOWN:
            print(event.key)

            x,y = pygame.mouse.get_pos()
            x/=gridSize
            y/=gridSize
            if event.key in rotateKeys:
                print("R or r at %d, %d Range((%d,%d),(%d %d))" % (x,y,placementRange[0][0],placementRange[1][0],  placementRange[1][1], placementRange[1][1]))
            if (x > placementRange[0][0] and x<placementRange[1][0]) and ( y > placementRange[1][1] and y<placementRange[1][1]):
                print("In range")
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

