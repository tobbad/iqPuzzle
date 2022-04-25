import pygame
from pygame.locals import *
import sys
import numpy as np
import math
import copy


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

# configurations=[{}]*5
# #confiurations[0]={'figOR':[[0,1,1], [1,0,0], [11,0,0], [7,1,1]],'pos':((0,0), (3, 3),(5,0),(5,3))}
# configurations[0]={'figOR':[[1,0,1], [11,0,0], [7,0,0]],'pos':((2,0), (3,2), (0,3),(5,3))}


gridSize=25

playField = ((1,11), (1,5))
placementRange=((12,15),(2,5))

def transformMatrix(rotationGrad):
    rotationPi=rotationGrad/180.0*math.pi
    R = np.array([[math.cos(rotationPi),-math.sin(rotationPi)],[math.sin(rotationPi),math.cos(rotationPi)]])
    print("| %.1f  %.1f |" % (R[0][0], R[0][1]))
    print("| %.1f  %.1f |" % (R[1][0], R[1][1]))
    return R

def rotateKey(key, rotationGrad):
     rotationGrad=int(rotationGrad)
     print("In key")
     print(key)
     rot =transformMatrix(rotationGrad)
     inCenter = ( 0.5*(key.shape[0]-1), 0.5*(key.shape[1]-1))
     print("inCenter", inCenter)
     xvec = np.zeros(2)
     if rotationGrad in (0,180):
         rKey = np.zeros([key.shape[0], key.shape[1]], dtype=float)
     else:
         rKey = np.zeros([key.shape[1], key.shape[0]], dtype=float)
     outCenter = (0.5*(rKey.shape[0]-1), 0.5*(rKey.shape[1]-1))
     print("outCenter", outCenter)
     for x in range(key.shape[0]):
         for y in range(key.shape[1]):
             xvec[0] = x-inCenter[0]
             xvec[1] = y-inCenter[1]
             
             xRr =rot.dot(xvec)
             xRr[0] += outCenter[0] 
             xRr[1] += outCenter[1]
             xRr = (int(round(xRr[0])), int(round(xRr[1])))
             print("x,y  %d, %d (%.1f, %.1f)-> (%d) %d %d" % ( x,y, xvec[0], xvec[1],key.figure[x][y],xRr[0], xRr[1]))
             rKey[xRr[0]][xRr[1]]=key.figure[x][y]
     key.figure=rKey
     print("Rotated Key",)
     print(key)
     return key


class key:
    
    @property
    def shape(self):
        return self.figure.shape 
    
    @property
    def ySize(self):
        return self.figure.shape[0]
   
    @property
    def xSize(self):
        return self.figure.shape[1]
    
    def __eq__(self, other):
        if self.figure.shape[0] != other.figure.shape[0]:
            print("XSize does not match (%d!=%d)" %(self.figure.shape[1], other.figure.shape[1]))
            return False
        if self.figure.shape[1] != other.figure.shape[1]:
            print("YSize does not match (%d!=%d)" %(self.figure.shape[1], other.figure.shape[1]))
            return False
        for x in range(self.figure.shape[0]):
            for y in range(self.figure.shape[1]):
                if self.figure[x][y] != other.figure[x][y]:
                    print("Location (%d,%d) does not match (%d!=%d)" % (x,y,  self.figure[x][y], other.figure[x][y]))
                    return False
        return True
    
    def __str__(self):
        line="Key:\n"
        for x in range(self.figure.shape[0]):
            for y in range(self.figure.shape[1]):
                line+="%d"%self.figure[x][y]
            line+='\n'
        line=line[:-1]
        return line
                

class key01(key):
    def __init__(self):
        self.figure=np.array([[1,1,0,0], [0,1,1,1]])
        self.color=PINK
        self.pos=(1,7)

class key02(key):
    def __init__(self):
        self.figure=np.array([[1,0,0], [1,0,0], [1,1,1]])
        self.color=BLUE
        self.pos=(1,13)
    
class key03(key):
    def __init__(self):
        self.figure=np.array([[1,1,1,1], [0,1,0,0]])
        self.color=YELLOW
        self.pos=(6,7)

class key04(key):
    def __init__(self):
        self.figure=np.array([[1,1,1], [0,1,0]])
        self.color=GREEN
        self.pos=(11,7)
    
class key05(key):
    def __init__(self):
        self.figure=np.array([[1,0], [1,1]])
        self.color=CYAN
        self.pos=(15,7)
    
class key06(key):
    def __init__(self):
        self.figure=np.array([[1,0,0], [1,1,1]])
        self.color=DBLUE
        self.pos=(1,10)
    
class key07(key):
    def __init__(self):
        self.figure=np.array([[1,0,0], [1,1,0], [0,1,1]])
        self.color=DVIOLET
        self.pos=(6,13)
    
class key08(key):
    def __init__(self):
        self.figure=np.array([[1,1,0], [0,1,1], [0,1,0]])
        self.color=ORANGE
        self.pos=(11,13)
    
class key09(key):
    def __init__(self):
        self.figure=np.array([[1,0], [1,1], [0,1]])
        self.color=DRED
        self.pos=(15,13)
    
class key10(key):
    def __init__(self):
        self.figure=np.array([[1,1,1], [0,1,1]])
        self.color=DCYAN
        self.pos=(6,10)
    
class key11(key):
    def __init__(self):
        self.figure=np.array([[1,0,1], [1,1,1]])
        self.color=DGREEN
        self.pos=(11,10)
    
class key12(key):
    def __init__(self):
        
        self.figure=np.array([[1,0,0,0], [1,1,1,1]])
        self.color=RED, 
        self.pos=(15,10)
    
class keyBlank(key):
    def __init__(self):
        self.figure=np.array([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]])
        self.color=BLACK
        self.pos=(-1,-1)
    


class board:
    def __init__(self, xoffset=-1, yoffset=-1):
        self.size = (19,19)
        self.offset=(xoffset, yoffset)
        self.gridSize=25
        self.circleRadius= 10
        self.keys=[key01()]#, key02(), key03()]#, key04(), key05(), key06(), key07(), key08(), key09(), key10(), key11(), key12(), keyBlank()]
        self.board=[[(0,0,0) for i in range(self.size[0])] for j in range(self.size[1])]
        if self.offset[0]<0 and self.offset[1]<0:
            self.graphicInit()
            self.resetBoard((255,255,255))
            print("Graphic init")

    def graphicInit(self):
            pygame.init()
            self.surface = pygame.display.set_mode(  (self.gridSize*self.size[0]+gridSize, gridSize*self.size[1]+self.gridSize), 0 ,32)
            pygame.display.set_caption("IQ Puzzler")
            pygame.font.init()
            basicFont=pygame.font.SysFont(None, 24)



    def resetBoard(self, color=BLACK):
        for x in range(self.offset[0], self.offset[0]+self.size[0]) :
            for y in range(self.offset[1], self.offset[1]+self.size[1]):
                xp=self.gridSize*x
                yp=self.gridSize*y
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
        rKey = rotateKey(key, rotationGrad)
        return rKey

    def checkFigurePlacement(self, figure, xpos, ypos):
        print(figure, xpos, ypos)
        return True


    def addKey(self ,key, xpos, ypos ,lmirror, rotationGrad, alwaysPlace):
        # self: Class to apply  Method on
        # key: what to paint
        # x,y: origin of figure
        # Miror up/down
        # orientation:
        # Rotate in degree counter clock wise
        # always place key at given location on the board
        rotationGrad=int(rotationGrad)
        xposMax=xpos
        yposMax=ypos
        bsizex=playField[0][1]
        bsizey=playField[1][1]
        retKey=copy.deepcopy(key)
        #print("x:%d< %d bsizex=%d" %(xpos, xposMax, bsizex))
        #print("y:%d<%d, bsizey=%d" %(ypos, yposMax, bsizey))
        print("In %s" %( str(key)))
        if not alwaysPlace:
            if not (xpos<bsizex and xposMax<=bsizex):
                print("x: x%d, bsize=%d, xposMax %d<%d"%(xpos, bsizex, xposMax, xposMax+bsizex))
                print("Drop figure due to xpos")
                return -1,-1
            if not (ypos<bsizey and yposMax<=bsizey) :
                print("y: %d, %d<=%d"%(ypos, yposMax, bsizey))
                print("Drop figure due to ypos")
                return -1,-1
        if rotationGrad in (0,180):
            retKey.figure=np.zeros((key.xSize, key.ySize))
        else:
            retKey.figure=np.zeros((key.ySize, key.xSize))
        xPlSeq=list(range(retKey.xSize))
        xPiSeq=list(range(key.xSize))
        if lmirror:
            xPiSeq.reverse()
        yPiSeq=list(range(key.ySize))
        yPlSeq=list(range(retKey.ySize))
        print(yPlSeq, yPiSeq)
        for xPl, xPi in zip(xPlSeq,xPiSeq):
            for yPl,yPi in zip(yPlSeq, yPiSeq):
                print("xPi %d, yPi %d, xPl %d yPl %d  %s"%(xPi,yPi,xPl, yPl, str(retKey.shape)))
                if key.figure[yPi][xPi]==1:
                    self.board[yPl+ypos][xPl+xpos] =  key.color
                else:
                    self.board[yPl+ypos][xPl+xpos] =  WHITE
                print("Set at %d, %d %s m=%d o=%d" % (xPl+xpos,yPl+ypos, str(self.board[xPl+xpos][yPl+ypos]), mirror, rotationGrad  ))
                #print("O: rot:%d (%d, %d) -> (%d, %d)" %(rotationGrad, xPl,yPl, xPi, yPi))
        print("OutKey: %s\nwith %d Degree @ (%d,%d)" %( str(retKey), rotationGrad, xpos, ypos))
        self.draw()

    def setKeys(self):
        for i in range(len(self.keys)):
            print("Place Tile %d"%i)
            if self.keys[i].pos[0]<0:
                continue
            self.addKey( self.keys[i],self.keys[i].pos[0], self.keys[i].pos[1], 0, 0, True)

    def getPlaygroundPos(self, x, y):
        x=int(x/self.gridSize)
        y=int(y/self.gridSize)
        return x,y

    def getKeyCode(self, x,y):
        for i in range(len(self.keys)):
            ymin=self.keys[i].pos[0]*self.gridSize
            ymax=(self.keys[i].pos[0]+self.keys[i].xSize+1)*self.gridSize
            print(i,'y',ymin, "<",y,"<",ymax)
            if ymin<y and y < ymax:
                xmin=self.keys[i].pos[1]*self.gridSize
                xmax=(self.keys[i].pos[1]+self.keys[i].ySize+1)*self.gridSize
                print(i, 'x', xmin, "<", x, "<", xmax)
                if xmin<x and x<xmax:
                    print("Key is %d" % i)
                    return i
        return -1

    def draw(self):
        for x in range(self.offset[0], self.offset[0]+self.size[0]):
            for y in range(self.offset[1], self.offset[1]+self.size[1]):
                xp=self.gridSize*(x+1)
                yp=self.gridSize*(y+1)
                #print(x,y,xp,yp)
                pygame.draw.circle(self.surface, self.board[x][y] ,(xp,yp), self.circleRadius)
        pygame.display.update()

class placeRange(board):
        def __init__(self, xoffset=13, yoffset=1):
            super().__init__(xoffset, yoffset)
            self.size=(4,4)

        def clearArea(self):
            for x in range(self.offset[0], self.offset[0]+self.size[0]):
                for y in range(self.offset[1], self.offset[1]+self.size[1]):
                    print("placeRange", x,y)
                    self.board[x][y]=(255,255,255)



class  playGround(board):
        def __init__(self, xoffset=1, yoffset=1):
            super().__init__(xoffset, yoffset)
            self.size=(11,5)


        def clearArea(self):
            for x in range(self.offset[0], self.offset[0]+self.size[0]):
                for y in range(self.offset[1], self.offset[1]+self.size[1]):
                    print("playGround",x,y)
                    self.board[x][y]=(255,255,255)

def addKeyName(key):
    text=basicFont.render(key['text'],True, WHITE, BLACK)
    textBox=text.get_rect()
    print(key['pos'][0])
    #pygame.draw.rect(surface, RED,(key['pos'][0]*gridSize, key['pos'][1]*gridSize* (textBox.left+ 20),textBox.right+20, textBox.height+40))
    surface.blit(text,textBox)



class game:
    def __init__(self):
        self.board=board()
        self.board.resetBoard((255,0,0))
        self.board.setKeys()
        self.placeRange=placeRange()
        #self.placeRange.resetBoard(RED)
        self.placementRange = self.placeRange.getRange()
        self.playGround=playGround()
        #self.playGround.resetBoard((255, 255, 255))
        self.selectedKey=-1
        self.rotateKeys=[pygame.locals.K_r]
        self.inPlacementRange=True
        self.rotate=0
        self.mirror=False

    def draw(self):
        self.placeRange.draw()
        self.playGround.draw()

    def run(self):
        while True:
            self.inPlacementRange=False
            for event in pygame.event.get():
                #self.draw()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    selectedKey=self.board.getKeyCode(event.pos[0], event.pos[1])
                    print("Selected key is nr: %d" % selectedKey)
                    #Clear Placement range
                    self.board.addKey( self.board.keys[-1], self.placementRange[0][0], self.placementRange[1][0], self.rotate,self.mirror, True)
                    self.board.addKey( self.board.keys[selectedKey], self.placementRange[0][0], self.placementRange[1][0], self.rotate, self.mirror, True)
                    self.isPlaceRange=self.board.isInPlacementRange(x,y)
                    if self.isPlaceRange:
                        print(event.pos[0], event.pos[1])
                    x,y=self.board.getPlaygroundPos(event.pos[0], event.pos[1])
                    isPlayGroundRange=self.playGround.isInPlacementRange(x,y)
                    self.isPlaceRange=self.placeRange.isInPlacementRange(x,y)
                    if selectedKey>=0:
                        print("Place at Location (%d, %d), inRange %d, inPlace %d" % (self.placementRange[0][0], self.placementRange[1][0],isPlayGroundRange,self.isPlaceRange))
                        if isPlayGroundRange:
                            self.board.addKey( self.board.keys[selectedKey], x, y, 0,0, True)
                        if self.isPlaceRange:
                            print("Place in Placerange")
                            self.board.addKey( self.board.keys[selectedKey], placementRange[0][0], placementRange[1][0], self.rotate, self.mirror, True)

                if event.type == MOUSEBUTTONUP:
                    x,y=self.placeRange.getPlaygroundPos(event.pos[0], event.pos[1])
                    print("BTN UP (%d, %d)" %(x,y))

                if pygame.mouse.get_focused() and event.type==4:
                    x,y=self.board.getPlaygroundPos(event.pos[0], event.pos[1])
                    self.inPlacementRange = self.board.isInPlacementRange(x,y)
                    print("focused %s " % (str(self.board.getPlaygroundPos(event.pos[0], event.pos[1]))))
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
                        self.rotate =(self.rotate+90)%360
                        print("R or r at (%d, %d) Range((%d,%d),(%d %d)), rotate %d" % (x,y,self.placementRange[0][0],self.placementRange[1][0],  self.placementRange[1][1], self.placementRange[1][1], self.rotate))
                        self.board.addKey( self.board.keys[selectedKey], self.placementRange[0][0],self.placementRange[1][0], self.mirror,self.rotate, True)
                        self.placeRange.draw()
                    if event.key == pygame.locals.K_m:
                        self.mirror =(self.mirror+1)%2==0
                        print("S or s at (%d, %d) Range((%d,%d),(%d %d)), mirror %d" % (x,y,self.placementRange[0][0],self.placementRange[1][0],  self.placementRange[1][1], self.placementRange[1][1], self.mirror))
                        self.board.addKey( self.board.keys[selectedKey], self.placementRange[0][0],self.placementRange[1][0], self.mirror ,self.rotate, True)
                        self.placeRange.draw()
                    if (x > self.placementRange[0][0] and x<self.placementRange[1][0]) and ( y > self.placementRange[1][1] and y<self.placementRange[1][1]):
                            print("In range")




        # for figIdx in range(len(self.board.keys)):
        #     x=self.board.keys.pos[0]
        #     y=self.board.keys.pos[1]
        #     self.addKey(board, self.board.keys[figIdx], x, y, configurations[0]['figOR'][i][1],configurations[0]['figOR'][i][2], True)


if __name__=="__main__":
    myGame=game()
    myGame.run()