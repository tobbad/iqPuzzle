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

figure=[{}]*12
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

confiurations=[{}]*5
#confiurations[0]={'figOR':[[0,1,1], [1,0,0], [11,0,0], [7,1,1]],'pos':((0,0), (3, 3),(5,0),(5,3))}
confiurations[0]={'figOR':[[0,0,0], [1,0,0]],'pos':((0,0), (3, 3),(5,0),(5,3))}
print(confiurations)

gridSize=25
size =  gridSize-6
playField = (11, 5)
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
    for x in range(playField[0]) :
        for y in range(playField[1]):
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
    print(xpos, ypos, playField,alwaysPlace)
    if (xpos<playField[0] and ypos<playField[1]) and not alwaysPlace:
        print("Drop figure")
        return -1,-1
    sizey=len(fig['tile'])
    sizex=len(fig['tile'][0])
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

#initPlayField(board)
#print(board)

initPlayField(board)
for i in range(len(figure)):
    print(figure[i])
    addFigure(board, figure[i],figure[i]['pos'][1], figure[i]['pos'][0],0,0, False)
    addKeystoneName(figure[i])
for i in range(len(confiurations[0]['figOR'])):
    print( "figOR", confiurations[0]['figOR'] )
    for j in range(len(confiurations[0]['figOR'])):
        figIdx= confiurations[0]['figOR'][i][0]
        x=confiurations[0]['pos'][j][0]
        y=confiurations[0]['pos'][j][1]
        addFigure(board, figure[figIdx], x, y, confiurations[0]['figOR'][j][1],confiurations[0]['figOR'][j][2], False)

selectedKey=-1
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
        if event.type == MOUSEBUTTONUP:
            print(event.pos[0], event.pos[1])
            x,y=getPlaygroundPos(event.pos[0], event.pos[1])
            print("Location (%d, %d)" % (x, y))
            addFigure(board, figure[selectedKey], x, y, confiurations[0]['figOR'][j][1],confiurations[0]['figOR'][j][2], True)
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

