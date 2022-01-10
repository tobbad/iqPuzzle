import pygame
from pygame.locals import *
import sys
import numpy as np
from scipy import linalg
import math


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
configurations[0]={'figOR':[[1,0,1], [11,0 ,0], [7,0,0]],'pos':((2,0), (3,2), (0,3),(5,3))}

print(configurations)

allKeysShow=True
gridSize=25
size =  gridSize-6
rotate=0
mirror=0
playField = ((0,11), (0,5))
placementRange=((12,16),(1,5))
identity=np.array([[1,0],[0,1]])
rot=np.array([[0,0.5],[0.5,0]])





class board:
    def __init__(self, xoffset, yoffset, size):
        self.size = size
        self.origin=(xoffset, yoffset)
        self.gridSize=25
        self.figure=[{}]*13
        self.figure[0]={'color':TRED, 'tile':[[1,1,1,1], [1,0,0,0]], 'pos':(7,0),  'defPlc':(10,2,1,0), 'text':'F1'} #RED
        self.figure[1]={'color':PINK , 'tile':[[1,1,0,0], [0,1,1,1]], 'pos':(10,0),  'defPlc':(0,0,0,0), 'text':'F2'} #PINK
        self.figure[2]={'color':CYAN, 'tile':[[1,1], [1,0]], 'pos':(13,0),  'defPlc':(0,0,0,0), 'text':'F3'} #HBLUE
        self.figure[3]={'color':DBLUE, 'tile':[[1,1,1], [1,0,0]], 'pos':(16,0),  'defPlc':(0,0,0,0), 'text':'F4'} #DRED
        self.figure[4]={'color':YELLOW, 'tile':[[1,1,1,1], [0,1,0,0]],  'defPlc':(0,0,0,0), 'pos':(7,5), 'text':'F5'}#YELLOW
        self.figure[5]={'color':DGREEN, 'tile':[[1,1,1], [1,0,1]],  'defPlc':(0,0,0,0), 'pos':(10,5), 'text':'F6'} #DGREEN
        self.figure[6]={'color':DVIOLET, 'tile':[[1,1,0], [0,1,0], [0,1,1]],  'defPlc':(0,0,0,0), 'pos':(7,10), 'text':'F8'}   #Violet
        self.figure[7]={'color':GREEN, 'tile':[[1,1,1], [0,1,0]],  'defPlc':(0,0,0,0), 'pos':(11,10) , 'text':'F7'}#GREEN
        self.figure[8]={'color':ORANGE, 'tile':[[1,1,0], [0,1,1]],  'defPlc':((0,0,0,0), (0,1,0)), 'pos':(15,10), 'text':'F9'} #ORANGE
        self.figure[9]={'color':DRED, 'tile':[[1,0], [1,1], [0,1]], 'defPlc':(0,0,0,0), 'pos':(7,14), 'text':'F10'} #ORANGE
        self.figure[10]={'color':DCYAN, 'tile':[[1,1,1], [0,1,1]], 'defPlc':(0,0,0,0), 'pos':(11,14), 'text':'F11'} #HGREEN
        self.figure[11]={'color':BLUE, 'tile':[[1,1,1], [0,0,1], [0,0,1]],  'defPlc':(0,0,0,0), 'pos':(14,14), 'text':'F11'} #DBLUE
        self.figure[12]={'color':BLACK, 'tile':[[1,1,1,1], [1,1,1,1], [1,1,1,1]],  'defPlc':(0,0,0,0), 'pos':(-1,-1), 'text':'F11'} #DBLUE
        self.board=[[(0,0,0) for i in range(self.size[0])] for j in range(self.size[1])]
        if size[0]==19 and size[1]==19:
            self.showKeys()
            self.graphicInit()
            print("Graphic init")

    def graphicInit(self):
            pygame.init()
            self.surface = pygame.display.set_mode(  (self.gridSize*self.size[0]+gridSize, gridSize*self.size[1]+self.gridSize), 0 ,32)
            pygame.display.set_caption("IQ Puzzler")
            pygame.font.init()
            basicFont=pygame.font.SysFont(None, 48)


    def initPlayField(self, color=BLACK):
        for x in range(self.xoffset, self.xoffset+self.size[0]) :
            for y in range(self.yoffset, self.yoffset+self.size[1]):
                xp=self.gridSize*x
                yp=self.gridSize*y
                self.board[xp][yp] = color

    def getRange(self):
        return ((self.origin[0], self.origin[0]+self.size[0]),(self.origin[1], self.origin[1]+self.size[1]))

    def isInPlacementRange(self, x,y):
        #print(x,y, posRange,)
        isPlacement= x>=self.origin[0] and x<self.origin[0]+self.size[0]
        #print("IsPlacment range x %d" % isPlacement)
        isPlacement&= y>=self.origin[1] and y<self.origin[1]+self.size[1]
        #print("IsPlacment range x and y %d" % isPlacement)
        return isPlacement

    def transformMatrix(self, rotationGrad):
        rotationPi=rotationGrad/180.0*math.pi
        R = np.array([[math.cos(rotationPi),-math.sin(rotationPi)],[math.sin(rotationPi),math.cos(rotationPi)]])
        return R

    def rotateKey(self, key, rotationGrad):
        rot = self.transformMatrix(rotationGrad)
        xSize = len(key['tile'][0])
        xCenter = 0.5*xSize
        ySize = len(key['tile'])
        yCenter = 0.5*ySize
        xvec = np.zeros(2)
        print(key)
        if rotationGrad in (0,180):
            rKey = np.array([xSize, ySize], dtype=float)
        else:
            rKey = np.array([ySize, xSize], dtype=float)
        for x in range(len(key['tile'])):
            for y in range(len(key['tile'][0])):
                xvec[0] = x+xCenter
                xvec[1] = y+yCenter
                xRr =np.dot(rot, xvec)
                print("x,y %d, %d->  %d %d" % (x,y,xRr[0], xRr[1]))
        return rKey

    def checkFigurePlacement(self, figure, xpos, ypos):
        print(figure, xpos, ypos)
        return True


    def addFigure(self ,fig, xpos, ypos ,lmirror, rotationGrad, alwaysPlace):
        # self: Class to apply  Method on
        # figure: what to paint
        # x,y: origin of figure
        # Miror up/down
        # orientation:
        # Rotate in degree counter clock wise
        # always place key at given location on the board
        xposMax=xpos
        yposMax=ypos
        sizex=len(fig['tile'][0])
        sizey=len(fig['tile'])
        bsizex=playField[0][1]
        bsizey=playField[1][1]
        print("x:%d< %d bsizex=%d" %(xpos, xposMax, bsizex))
        print("y:%d<%d, bsizey=%d" %(ypos, yposMax, bsizey))
        if not alwaysPlace:
            if not (xpos<bsizex and xposMax<=bsizex):
                print("x: x%d, bsize=%d, xposMax %d<%d"%(xpos, bsizex, xposMax, xposMax+bsizex))
                print("Drop figure due to xpos")
                return -1,-1
            if not (ypos<bsizey and yposMax<=bsizey) :
                print("y: %d, %d<=%d"%(ypos, yposMax, bsizey))
                print("Drop figure due to ypos")
                return -1,-1
        print('figure', fig, sizex, sizey)
        placeKey = fig#self.rotateKey(fig, rotationGrad)
        print("PlaceKey: %s" %str(placeKey))
        xseq=list(range(sizex))
        xPlcSeq=xseq[:]
        xPickSeq=xseq[:]
        if lmirror:
            xPickSeq.reverse()
        yseq= list(range(sizey))
        yPlcSeq=yseq[:]
        yPickSeq=yseq[:]
        for xPl, xPi in zip(xPlcSeq,xPickSeq):
            for yPl,yPi in zip(yPlcSeq, yPickSeq):
                #print(x,y, fig['color'], fig['tile'][y])
                if fig['tile'][yPi][xPi]==1:
                    self.board[xPl+xpos][yPl+ypos] =  fig['color']
                else:
                    self.board[xPl+xpos][yPl+ypos] =  WHITE
                #print("Set at %d, %d %s m=%d o=%d" % (xPl+xpos,yPl+ypos, str(self.board[xPl+xpos][yPl+ypos]), lmirror, lorientation  ))

                print("O: rot:%d (%d, %d) -> (%d, %d)" %(rotationGrad, xPl,yPl, xPi, yPi))

    def showKeys(self):
        for i in range(len(self.figure)):
            print("Place Tile %d"%i)
            if self.figure[i]['pos'][1]<0:
                continue
            self.addFigure( self.figure[i], self.figure[i]['pos'][1], self.figure[i]['pos'][0], 0, 0, True)

    def getPlaygroundPos(self, x, y):
        x=int(x/self.gridSize)
        y=int(y/self.gridSize)
        return x,y

    def getFigureCode(self, x,y):
        for i in range(len(self.figure)):
            ymin=figure[i]['pos'][0]*self.gridSize
            ymax=(figure[i]['pos'][0]+len(figure[i]['tile'])+1)*self.gridSize
            print(i,'y',ymin, "<",y,"<",ymax)
            if ymin<y and y < ymax:
                xmin=figure[i]['pos'][1]*self.gridSize
                xmax=(figure[i]['pos'][1]+len(figure[i]['tile'])+1)*self.gridSize
                print(i, 'x', xmin, "<", x, "<", xmax)
                if xmin<x and x<xmax:
                    print("Key is %d" % i)
                    return i
        return -1


class placeRange(board):
        def __init__(self, xoffset=12, yoffset=1):
            super().__init__(xoffset, yoffset, (4,4))

        def draw(self):
            pass



class  playGround(board):
        def __init__(self, xoffset=0, yoffset=0):
            super().__init__(xoffset, yoffset, (11,5))

        def draw(self):
            pass

def addKeystoneName(key):
    text=basicFont.render(key['text'],True, WHITE, BLACK)
    textBox=text.get_rect()
    print(key['pos'][0])
    #pygame.draw.rect(surface, RED,(key['pos'][0]*gridSize, key['pos'][1]*gridSize* (textBox.left+ 20),textBox.right+20, textBox.height+40))
    surface.blit(text,textBox)



class game:
    def __init__(self):
        self.full=board(0,0,(19,19))
        self.placeRange=placeRange()
        self.placementRange = self.placeRange.getRange()
        self.playGround=playGround()
        self.selectedKey=-1
        self.rotateKeys=[pygame.locals.K_r]
        self.inPlacementRange=True
        self.drawKeys()

    def draw(self):
        self.placeRange.draw()
        self.playGround.draw()


    def drawKeys(self):
        for i in range(len(self.full.figure)):
            print("Place figOR", self.full.figure[i] )
            x=self.full.figure[i]['pos'][0]
            y=self.full.figure[i]['pos'][1]
            self.full.addFigure(figure[i], x, y, 0,0, True)


    def run(self):
        while True:
            self.inPlacementRange=False
            for event in pygame.event.get():
                self.draw()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    selectedKey=self.full.getFigureCode(event.pos[0], event.pos[1])
                    print("Selected key is nr: %d" % selectedKey)
                    self.full.addFigure( figure[-1], self.placementRange[0][0], self.placementRange[1][0], 0,0, True)
                    self.full.addFigure( figure[selectedKey], self.placementRange[0][0], self.placementRange[1][0], 0,0, True)
                    self.isPlaceRange=self.full.isInPlacementRange(x,y)
                    if self.isPlaceRange:
                        print("in range")

                if event.type == MOUSEBUTTONDOWN:
                    print(event.pos[0], event.pos[1])
                    x,y=self.full.getPlaygroundPos(event.pos[0], event.pos[1])
                    isPlayGroundRange=self.playGround.isInPlacementRange(x,y)
                    self.isPlaceRange=self.placeRange.isInPlacementRange(x,y)
                    if selectedKey>=0:
                        print("Place at Location (%d, %d), inRange %d, inPlace %d" % (x, y,isPlayGroundRange,self.isPlaceRange))
                        if isPlayGroundRange:
                            self.full.addFigure( figure[selectedKey], x, y, 0,0, True)
                        if self.isPlaceRange:
                            print("Place in Placerange")
                            self.full.addFigure( figure[selectedKey], placementRange[0][0], placementRange[1][0], 0,rotate, True)
                if event.type == MOUSEBUTTONUP:
                    x,y=self.placeRange.getPlaygroundPos(event.pos[0], event.pos[1])
                    print("BTN UP (%d, %d)" %(x,y))

                if pygame.mouse.get_focused() and event.type==4:
                    x,y=self.full.getPlaygroundPos(event.pos[0], event.pos[1])
                    inPlacementRange = self.full.isInPlacementRange(x,y)
                    print("focused %s " % (str(self.full.getPlaygroundPos(event.pos[0], event.pos[1]))))
                if event.type == KEYUP:
                    print(event.key, K_ESCAPE)
                    if event.key == K_ESCAPE:
                        pygame.quit()
                if event.type == KEYDOWN:
                    print(event.key, K_ESCAPE)
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    x,y = pygame.mouse.get_pos()
                    x/=gridSize
                    y/=gridSize
                    if event.key in rotateKeys:
                        rotate =(rotate+90)%360
                        print("R or r at (%d, %d) Range((%d,%d),(%d %d)), rotate %d" % (x,y,self.placementRange[0][0],self.placementRange[1][0],  self.placementRange[1][1], self.placementRange[1][1], rotate))
                        self.full.addFigure( figure[selectedKey], self.placementRange[0][0],self.placementRange[1][0], mirror,rotate, True)
                    if event.key == pygame.locals.K_m:
                        mirror =(mirror+1)%2
                        print("S or s at (%d, %d) Range((%d,%d),(%d %d)), mirror %d" % (x,y,self.placementRange[0][0],self.placementRange[1][0],  self.placementRange[1][1], self.placementRange[1][1], mirror))
                        self.full.addFigure( figure[selectedKey], self.placementRange[0][0],self.placementRange[1][0], mirror ,rotate, True)
                    if (x > self.placementRange[0][0] and x<self.placementRange[1][0]) and ( y > self.placementRange[1][1] and y<self.placementRange[1][1]):
                            print("In range")




        for i in range(len(configurations[0]['figOR'])):
            print("Place figOR", configurations[0]['figOR'] )
            figIdx= configurations[0]['figOR'][i][0]
            x=configurations[0]['pos'][i][0]
            y=configurations[0]['pos'][i][1]
            addFigure(board, figure[figIdx], x, y, configurations[0]['figOR'][i][1],configurations[0]['figOR'][i][2], True)


myGame=game()
myGame.run()