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

placedFigures=[(None, None, None )]*13
configurations=[{}]*5
#confiurations[0]={'figOR':[[0,1,1], [1,0,0], [11,0,0], [7,1,1]],'pos':((0,0), (3, 3),(5,0),(5,3))}
configurations[0]={'figOR':[[1,0,1], [11,0 ,0], [7,0,0]],'pos':((2,0), (3,2), (0,3),(5,3))}


allKeysShow=True
gridSize=25
rotate=0
mirror=0
playField = ((0,11), (0,5))
placementRange=((12,16),(1,5))
identity=np.array([[1,0],[0,1]])
rot=np.array([[0,0.5],[0.5,0]])


def transformMatrix(rotationGrad):
    rotationPi=rotationGrad/180.0*math.pi
    R = np.array([[math.cos(rotationPi),-math.sin(rotationPi)],[math.sin(rotationPi),math.cos(rotationPi)]])
    return R

def rotateKey(key, rotationGrad):
     print(key)
     rot =transformMatrix(rotationGrad)
     xSize = len(key['tile'][0])
     xCenter = 0.5*xSize
     ySize = len(key['tile'])
     yCenter = 0.5*ySize
     xvec = np.zeros(2)
     if rotationGrad in (0,180):
         rKey = np.array([xSize, ySize], dtype=float)
     else:
         rKey = np.array([ySize, xSize], dtype=float)
     for x in range(len(key['tile'])):
         for y in range(len(key['tile'][0])):
             xvec[0] = x+xCenter
             xvec[1] = y+yCenter
             xRr =np.dot(rot, xvec)
             xRr[0]-=xCenter
             xRr[1]-=yCenter
             key[int(rKey[x-xCenter])[0]
             print("x,y %d, %d->  %d %d" % (x,y,xRr[0], xRr[1]))
     return key




class board:
    def __init__(self, xoffset, yoffset):
        self.size=(19, 19)
        self.offset=(xoffset, yoffset)
        self.gridSize=25
        self.circleRadius= 10
        self.figure=[{}]*13
        self.figure[0]={'color':TRED, 'tile':[[1,1,1,1], [1,0,0,0]], 'pos':(7,1), 'text':'F1'} #RED
        self.figure[1]={'color':PINK , 'tile':[[1,1,0,0], [0,1,1,1]], 'pos':(10,1), 'text':'F2'} #PINK
        self.figure[2]={'color':CYAN, 'tile':[[1,1], [1,0]], 'pos':(13,1), 'text':'F3'} #HBLUE
        self.figure[3]={'color':YELLOW, 'tile':[[1,1,1,1], [0,1,0,0]], 'pos':(7,6), 'text':'F5'}#YELLOW
        self.figure[4]={'color':DGREEN, 'tile':[[1,1,1], [1,0,1]], 'pos':(10,6), 'text':'F6'} #DGREEN
        self.figure[5]={'color':DVIOLET, 'tile':[[1,1,0], [0,1,0], [0,1,1]]  , 'pos':(13,6), 'text':'F8'}   #Violet
        self.figure[6]={'color':ORANGE, 'tile':[[1,1,0], [0,1,1]], 'pos':(7,11), 'text':'F9'} #ORANGE
        self.figure[7]={'color':GREEN, 'tile':[[1,1,1], [0,1,0]], 'pos':(10,11) , 'text':'F7'}#GREEN
        self.figure[8]={'color':DRED, 'tile':[[1,0], [1,1], [0,1]], 'pos':(13,11), 'text':'F10'} #ORANGE
        self.figure[9]={'color':DCYAN, 'tile':[[1,1,1], [0,1,1]], 'pos':(7,15), 'text':'F11'} #HGREEN
        self.figure[10]={'color':DBLUE, 'tile':[[1,1,1], [1,0,0]], 'pos':(10,15), 'text':'F4'} #DRED
        self.figure[11]={'color':BLUE, 'tile':[[1,1,1], [0,0,1], [0,0,1]], 'pos':(13,15), 'text':'F11'} #DBLUE
        self.figure[12 ]={'color':BLACK, 'tile':[[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]], 'pos':(-1,-1), 'text':'F11'} #DBLUE
        print("Base class")

        self.board=[[(0,0,0) for i in range(self.size[0])] for j in range(self.size[1])]
        if self.size[0]==19 and self.offset[0]==1 and self.size[1]==19 and self.offset[1]==1:
            self.graphicInit()
            self.resetBoard((255,255,255))
            print("Graphic init (%d, %d)"%(self.size[0],self.size[1]))

    def graphicInit(self):
            pygame.init()
            print("Surface size (%d,%d)" % (self.gridSize*(self.offset[0]+self.size[0])+gridSize, gridSize*(self.offset[1]+self.size[1])+self.gridSize))
            self.surfaceA =pygame.display.set_mode( (self.gridSize*(self.offset[0]+self.size[0])+gridSize, gridSize*(self.offset[1]+self.size[1])+self.gridSize), 0 ,32)
            pygame.display.set_caption("IQ Puzzler")
            pygame.font.init()
            basicFont=pygame.font.SysFont(None, 24)

    @property
    def surface(self):
        return self.surfaceA

    def resetBoard(self, color=BLACK):
        for x in range(len(self.board)) :
            for y in range( len(self.board[0])):
                xp=self.gridSize*(x+1)
                yp=self.gridSize*(y+1)
                if self.surface:
                    pygame.draw.circle(self.surface, color ,(xp,yp), self.circleRadius)
        pygame.display.update()


    def getRange(self):
        return ((self.offset[0], self.offset[0]+self.size[0]),(self.offset[1], self.offset[1]+self.size[1]))

    def isInPlacementRange(self, x,y):
        #print(x,y, posRange,)
        isPlacement= x>=self.offset[0] and x<self.offset[0]+self.size[0]
        #print("IsPlacment range x %d" % isPlacement)
        isPlacement&= y>=self.offset[1] and y<self.offset[1]+self.size[1]
        #print("IsPlacment range x and y %d" % isPlacement)
        return isPlacement

    def rotateKey(self, key, rotationGrad):
        return rotateKey(key, rotationGrad)

    def checkFigurePlacement(self, figure, xpos, ypos):
        print(figure, xpos, ypos)
        return True


    def addFigure(self ,fig, xpos, ypos ,lmirror, rotationGrad, alwaysPlace):
        # self: Class to apply  Method on
        # fig: what to paint
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
        placeKey = fig#self.rotateKey(fig, rotationGrad)
        #print("PlaceKey: %s" %( str(placeKey)))
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
                #print(xPl,yPl, fig['color'], fig['tile'][yPi])
                print("rot:%d (%d, %d) -> (%d, %d)" %(rotationGrad, xPi, yPi,xPl+xpos, yPl+ypos))
                if fig['tile'][yPi][xPi]==1:
                    self.board[xPl+xpos][yPl+ypos] =  fig['color']
                else:
                    self.board[xPl+xpos][yPl+ypos] =  WHITE
                #print("Set at %d, %d %s m=%d o=%d" % (xPl+xpos,yPl+ypos, str(self.board[xPl+xpos][yPl+ypos]), mirror, rotationGrad  ))

        #self.draw()

    def setKeys(self):
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
            ymin=self.figure[i]['pos'][0]*self.gridSize-self.gridSize/2
            ymax=(self.figure[i]['pos'][0]+len(self.figure[i]['tile'])+1)*self.gridSize+self.gridSize/2
            #print(i,'y',ymin, "<",y,"<",ymax)
            if ymin<y and y < ymax:
                xmin=self.figure[i]['pos'][1]*self.gridSize-self.gridSize/2
                xmax=(self.figure[i]['pos'][1]+len(self.figure[i]['tile'])+1)*self.gridSize+self.gridSize/2
                #print(i, 'x', xmin, "<", x, "<", xmax)
                if xmin<x and x<xmax:
                    print("Key is %d" % i)
                    return i
        return -1

    def draw(self):
        for x in range( self.size[0]):
            for y in range(self.size[1]):
                xp=self.gridSize*(x+1)
                yp=self.gridSize*(y+1)
                #print(x,y,xp,yp,len(self.board),len(self.board[1]))
                pygame.draw.circle(self.surface, self.board[x][y] ,(xp,yp), self.circleRadius)
        pygame.display.update()

    def addKey(xpos, ypos, lmirror, rotationGrad):
        self.keys.append((xpos, ypos, lmirror, rotationGrad))


class placeRange(board):
        def __init__(self, xoffset=13, yoffset=1):
            super().__init__(xoffset, yoffset)
            print(self)
            print("placeRange")
            self.size=(4,4)
            self.keys=[]


        def clearArea(self):
            print("placeRange",x,y)
            for x in range(self.offset[0], self.offset[0]+self.size[0]):
                for y in range(self.offset[1], self.offset[1]+self.size[1]):
                    self.board[x][y] =  WHITE

class  playGround(board):
        def __init__(self, xoffset=1, yoffset=1):
            super().__init__(xoffset, yoffset)
            print("playGround")
            self.size=(11,5)
            self.keys=[]


        def clearArea(self):
            print("playGround")
            for x in range(self.offset[0], self.offset[0]+self.size[0]):
                for y in range(self.offset[1], self.offset[1]+self.size[1]):
                    self.board[x][y]=(255,255,255)

def addKeystoneName(key):
    text=basicFont.render(key['text'],True, WHITE, BLACK)
    textBox=text.get_rect()
    print(key['pos'][0])
    #pygame.draw.rect(surface, RED,(key['pos'][0]*gridSize, key['pos'][1]*gridSize* (textBox.left+ 20),textBox.right+20, textBox.height+40))
    surface.blit(text,textBox)



class game:
    def __init__(self):
        self.full=board(1,1)
        self.full.resetBoard((255,255,255))
        self.full.setKeys()
        self.playGround=playGround()
        #self.playGround.resetBoard((255, 255, 255))
        self.placeRange=placeRange()
        #self.placeRange.resetBoard(RED)
        self.placementRange = self.placeRange.getRange()
        self.selectedKey=-1
        self.rotateKeys=[pygame.locals.K_r]
        self.inPlacementRange=True
        self.rotate=0
        self.mirror=False
        self.draw()

    def draw(self):
        self.placeRange.draw()
        self.playGround.draw()

    def run(self):
        while True:
            self.inPlacementRange=False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    self.selectedKey=self.full.getFigureCode(event.pos[0], event.pos[1])
                    print("Selected key is nr: %d" % self.selectedKey)
                    #Clear Placement range
                    self.full.addFigure( self.full.figure[-1], self.placementRange[0][0], self.placementRange[1][0], 0,0, True)
                    self.full.addFigure( self.full.figure[self.selectedKey], self.placementRange[0][0], self.placementRange[1][0], 0,0, True)
                    x,y=self.full.getPlaygroundPos(event.pos[0], event.pos[1])
                    if self.placeRange.isInPlacementRange(x,y):
                        print("In place range (%d, %d)" % (event.pos[0], event.pos[1]))
                    if self.selectedKey>=0:
                        print("Place at Location (%d, %d), inRange %d, inPlace %d" % (self.placementRange[0][0], self.placementRange[1][0],self.placeRange.isInPlacementRange(x,y),self.placeRange.isInPlacementRange(x,y)))
                        if self.placeRange.isInPlacementRange(x,y):
                            self.full.addFigure( self.full.figure[self.selectedKey], x, y, 0,0, True)
                        if self.placeRange.isInPlacementRange(x,y):
                            print("Place in Placerange")
                            self.full.addFigure( self.full.figure[self.selectedKey], placementRange[0][0], placementRange[1][0], 0,self.rotate, True)

                if event.type == MOUSEBUTTONUP:
                    x,y=self.placeRange.getPlaygroundPos(event.pos[0], event.pos[1])
                    print("BTN UP (%d, %d)" %(x,y))

                if pygame.mouse.get_focused() and event.type==4:
                    x,y=self.full.getPlaygroundPos(event.pos[0], event.pos[1])
                    self.inPlacementRange = self.full.isInPlacementRange(x,y)
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
                    if event.key in self.rotateKeys:
                        self.rotate =( self.rotate+90)%360
                        print("R or r at (%d, %d) Range((%d,%d),(%d %d)), rotate %d" % (x,y,self.placementRange[0][0],self.placementRange[1][0],  self.placementRange[1][1], self.placementRange[1][1],  self.rotate))
                        self.full.addFigure( self.full.figure[self.selectedKey], self.placementRange[0][0],self.placementRange[1][0], self.mirror, self.rotate, True)
                        self.placeRange.draw()
                    if event.key == pygame.locals.K_m:
                        self.mirror =not self.mirror
                        print("S or s at (%d, %d) Range((%d,%d),(%d %d)), mirror %d" % (x,y,self.placementRange[0][0],self.placementRange[1][0],  self.placementRange[1][1], self.placementRange[1][1], self.mirror))
                        self.full.addFigure( self.full.figure[self.selectedKey], self.placementRange[0][0],self.placementRange[1][0], mirror , self.rotate, True)
                        self.full.draw()
                    if (x > self.placementRange[0][0] and x<self.placementRange[1][0]) and ( y > self.placementRange[1][1] and y<self.placementRange[1][1]):
                            print("In range")
        for i in range(len(configurations[0]['figOR'])):
            print("Place figOR", configurations[0]['figOR'] )
            figIdx= configurations[0]['figOR'][i][0]
            x=configurations[0]['pos'][i][0]
            y=configurations[0]['pos'][i][1]
            addFigure(board, figure[figIdx], x, y, configurations[0]['figOR'][i][1],configurations[0]['figOR'][i][2], True)

class Parent:
    def __init__(self, name):
        self.name=name
        self.pattr="Klaus"

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

if 1==0:
    p=Parent("Paul")
    print(p.name)
    print(p.pattr)
    c=Child("Franz")
    print(c.name)
    print(c.pattr)

if __name__=="main":
    myGame=game()
    myGame.run()