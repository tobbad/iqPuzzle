#import sys.path.append('../parentdirectory')
import pygame
import pygame.locals as pl 
import numpy as np
import math
import copy
import color_constants as cc


PINK=(255, 105, 180)
ORANGE=cc.colors['orange1']
BLACK=(0,0,0)
RED=(255,0,0)
TRED=(255,99,71)
DRED=(165,42,42)
GREEN=(0,255,0)
DGREEN=cc.colors['olivedrab3']
HGREEN=(0,199,7)
HBLUE=(0,255,0)
BLUE=cc.colors['steelblue3']=(0,0,255)
YELLOW=(255,255,0)
VIOLET=(193,0,248)
CYAN=cc.colors['aqua']
DCYAN=cc.colors['palegreen2']
DBLUE=cc.colors['royalblue4']
BLUE=(0, 0, 255)
VIOLET=(90, 0, 100)
DVIOLET=(148, 0, 255)
ORANGE=cc.colors['cadmiumorange']
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

def rotateKey(key, rotationGrad, p=True):
     rotationGrad=int(rotationGrad)
     if p:
         print("In key rotate by %d degree" %(rotationGrad) )
         print(key)
     rot =transformMatrix(rotationGrad)
     inCenter = ( 0.5*(key.shape[0]-1), 0.5*(key.shape[1]-1))
     #print("inCenter", inCenter)
     xvec = np.zeros(2)
     rKey=copy.deepcopy(key)
     if rotationGrad in (0,180, 360):
         rKey.figure = np.zeros([key.shape[0], key.shape[1]], dtype=float)
     elif rotationGrad in (90,270):
         rKey.figure = np.zeros([key.shape[1], key.shape[0]], dtype=float)
     outCenter = (0.5*(rKey.xSize-1), 0.5*(rKey.ySize-1))
     #print("outCenter", outCenter)
     #print(rKey)
     for x in range(key.shape[0]):
         for y in range(key.shape[1]):
             xvec[0] = x-inCenter[0]
             xvec[1] = y-inCenter[1]
             
             xRr =rot.dot(xvec)
             #print(xRr)
             xRr[0] += outCenter[0] 
             xRr[1] += outCenter[1]
             xRr = (int(round(xRr[0])), int(round(xRr[1])))
             if p:
                 print("x,y  %d, %d (%.1f, %.1f)-> (%d)" % ( x,y, xRr[0], xRr[1], key.figure[x][y]))
             rKey.figure[xRr[0]][xRr[1]]=key.figure[x][y]
             #print(rKey.figure[round(xRr[0])][round(xRr[1])])
     if p:
         print("OutKey at %d Degree " %(rotationGrad))
         print(rKey)
     return rKey


class key:
    
    def __init__(self):
        self.pos=(0,0)
        self.color=BLACK 
        self.figure=np.transpose(np.array([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]))
        self.mirror=False
        self.rotationGrad=0
    
    @property
    def shape(self):
        return self.figure.shape 
    
    @property
    def ySize(self):
        return self.figure.shape[1]
   
    @property
    def xSize(self):
        return self.figure.shape[0]
    
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
        for y in range(self.figure.shape[1]):
            for x in range(self.figure.shape[0]):
                line+="%d"%self.figure[x][y]
            line+='\n'
        line=line[:-1]
        return line
    
    def mirror(self):
        retKey = copy.deepcopy(self)
        xPiSeq=list(range(self.xSize))
        xPlSeq=list(range(retKey.xSize))
        xPiSeq.reverse()
        yPlSeq=list(range(retKey.ySize))
        #print(xPiSeq, yPiSeq, xPlSeq, yPlSeq)
        for xPl,xPi in zip(xPlSeq, xPiSeq):
            for yPl in yPlSeq:
                retKey.figure[xPl][yPl]=self.figure[xPi][yPl]
        return retKey

class key01(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,1,0,0], [0,1,1,1]]))
        self.color=PINK
        self.pos=(1, 7)

class key02(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,0,0], [1,0,0], [1,1,1]]))
        self.color=BLUE
        self.pos=(1 ,10)
    
class key03(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,1,1,1], [0,1,0,0]]))
        self.color=YELLOW
        self.pos=(1, 14)

class key04(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,0,0], [1,1,0], [0,1,1]]))
        self.color=DVIOLET
        self.pos=(6,10)

class key05(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,1,1], [0,1,0]]))
        self.color=GREEN
        self.pos=(6,7)

class key06(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,1,1], [0,1,1]]))
        self.color=DCYAN
        self.pos=(6,14)
    
class key07(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,0], [1,1]]))
        self.color=CYAN
        self.pos=(10,7)
    
class key08(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,1,0], [0,1,1], [0,1,0]]))
        self.color=ORANGE
        self.pos=(10,10)

class key09(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,0,1], [1,1,1]]))
        self.color=DGREEN
        self.pos=(10,14)
    
class key10(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,0,0], [1,1,1]]))
        self.color=DBLUE
        self.pos=(14,7)
    
class key11(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,0], [1,1], [0,1]]))
        self.color=DRED
        self.pos=(14,10)
    
    
class key12(key):
    def __init__(self):
        super().__init__()       
        self.figure=np.transpose(np.array([[1,0,0,0], [1,1,1,1]]))
        self.color=RED, 
        self.pos=(14,14)
    
class keyBlank(key):
    def __init__(self):
        super().__init__()
        self.figure=np.transpose(np.array([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]))
        self.color=BLACK
        self.pos=(-1,-1)
    


class board:
    
    board = None
    def __init__(self, xoffset=-1, yoffset=-1):
        self.size = (19,19)
        self.offset=(xoffset, yoffset)
        self.gridSize=25
        self.circleRadius= 10
        self.keys=[key01(), key02(), key03(), key04(), key05(), key06(), key07(), key08(), key09(), key10(), key11(), key12(), keyBlank()]
        if self.offset[0]<0 or self.offset[1]<0:
            type(self).board=[[(0,0,0) for i in range(self.size[0])] for j in range(self.size[1])]
            self.graphicInit()
            self.resetBoard((255,255,255))
            print("Graphic init")
        #print(self.__dict__)
        print(self, self.__dict__)

    def graphicInit(self):
            pygame.init()
            self.surface = pygame.display.set_mode(  (self.gridSize*self.size[0]+gridSize, gridSize*self.size[1]+self.gridSize), 0 ,32)
            pygame.display.set_caption("IQ Puzzler")
            pygame.font.init()
            self.basicFont=pygame.font.SysFont(None, 24)

    def __str__(self):
        ret = "%s"%type(self)
        return ret
        
    def resetBoard(self, color=BLACK):
        for x in range(self.offset[0], self.offset[0]+self.size[0]+1) :
            for y in range(self.offset[1], self.offset[1]+self.size[1]+1):
                xp=self.gridSize*x
                yp=self.gridSize*y
                pygame.draw.circle(self.surface, color ,(xp,yp), self.circleRadius)
        pygame.display.update()

    def setArea(self, color):
        if self.offset[0]<0:
            offset=(0,0)
        else:
            offset=self.offset
        print("Set Area x: (%d,%d) y:(%d,%d) with (%d, %d,%d)" %(offset[0], offset[0]+self.size[0],offset[1], offset[1]+self.size[1], color[0], color[1], color[2]))
        for x in range(offset[0], offset[0]+self.size[0]):
            for y in range(offset[1], offset[1]+self.size[1]):
                #print("SetArea @ (%d,%d)" %(x,y))
                self.board[x][y]=color
                #print("SetArea @ (%s)" %(str(self.board[y][x])))
        

    def getRange(self):
        return ((self.offset[0], self.offset[0]+self.size[0]),(self.offset[1], self.offset[1]+self.size[1]))

    def isInPlacementRange(self, x,y):
        #print(x,y, posRange,)
        isPlacement= x>=self.offset[0] and x<self.offset[0]+self.size[0]
        #print("IsPlacment range x %d" % isPlacement)
        isPlacement&= y>=self.offset[1] and y<self.offset[1]+self.size[1]
        print("IsPlacment range x and y %d" % isPlacement)
        return isPlacement

    def rotateKey(self, key, rotationGrad):
        rKey = rotateKey(key, rotationGrad)
        return rKey

    def checkFigurePlacement(self, figure, xpos, ypos):
        print(figure, xpos, ypos)
        return True


    def addKey(self ,key, xpos, ypos ,mirror, rotationGrad, alwaysPlace):
        # self: Class to apply  Method on
        # key: what to paint
        # x,y: origin of figure
        # Miror up/down
        # orientation:
        # Rotate in degree counter clock wise
        # always place key at given location on the board
        isPlaceable =True
        rotationGrad=int(rotationGrad)
        xposMax=xpos+key.xSize
        yposMax=ypos+key.ySize
        bsizex=playField[0][1]
        bsizey=playField[1][1]
        retKey=copy.deepcopy(key)
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
        retKey= rotateKey(key, rotationGrad, False)
        if mirror:
            retKey=retKey.mirror()
        xPlSeq=list(range(retKey.xSize))
        yPlSeq=list(range(retKey.ySize))
        #print(xPiSeq, yPiSeq, xPlSeq, yPlSeq)
        print("OutKey: %s\nwith %d Degree @ (%d,%d)" %( str(retKey), rotationGrad, xpos, ypos))
        print(xPlSeq, yPlSeq )
        for xPl in xPlSeq:
            for yPl in yPlSeq:
                #print("xPi %d, yPi %d, xPl %d yPl %d  %s"%(xPi,yPi,xPl, yPl, str(retKey.shape)))
                if retKey.figure[xPl][yPl]==1:
                    self.board[xPl+xpos][yPl+ypos] =  key.color
                else:
                    self.board[xPl+xpos][yPl+ypos] =  WHITE
                print("Set at %d, %d %s m=%d o=%d" % (xPl+xpos,yPl+ypos, str(self.board[xPl+xpos][yPl+ypos]), mirror, rotationGrad  ))
                #print("O: rot:%d (%d, %d) -> (%d, %d)" %(rotationGrad, xPl,yPl, xPi, yPi))
        self.draw()
        return isPlaceable

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
            xmin=self.keys[i].pos[0]*self.gridSize
            xmax=(self.keys[i].pos[0]+self.keys[i].xSize+1)*self.gridSize
            print(i,'x',xmin, "<",x,"<",xmax)
            if xmin<x and x < xmax:
                ymin=self.keys[i].pos[1]*self.gridSize
                ymax=(self.keys[i].pos[1]+self.keys[i].ySize+1)*self.gridSize
                print(i, 'x', ymin, "<", y, "<", ymax)
                if ymin<y and y<ymax:
                    print("Key is %d" % i)
                    return i
        return -1

    def draw(self):
        print("Draw")
        for x in range(self.offset[0], self.offset[0]+self.size[0]):
            for y in range(self.offset[1], self.offset[1]+self.size[1]):
                #if x==13 and y==1:
                #    print("Color at %d, %d =  %s"%(x,y, str( self.board[x][y]) ))
                xp=self.gridSize*(x+1)
                yp=self.gridSize*(y+1)
                #print(x,y,xp,yp)
                pygame.draw.circle(self.surface, self.board[x][y] ,(xp,yp), self.circleRadius)
        pygame.display.update()

    def addKeyName(self, key):
        text=basicFont.render(key.text,True, WHITE, BLACK)
        textBox=text.get_rect()
        print(key['pos'][0])
        #pygame.draw.rect(surface, RED,(key['pos'][0]*gridSize, key['pos'][1]*gridSize* (textBox.left+ 20),textBox.right+20, textBox.height+40))
        self.surface.blit(text,textBox)


class placeRange(board):
        def __init__(self, xoffset=13, yoffset=1):
            super().__init__(xoffset, yoffset)
            self.size=(4,4)
            print(self.board)
            
        

class  playGround(board):
        def __init__(self, xoffset=1, yoffset=1):
            super().__init__(xoffset, yoffset)
            self.size=(11,5)
        
        def config(self):
            res = []
            return res
        
        def addKey(self, x , y, key):
            return



class game:
    def __init__(self):
        self.board=board()
        self.board.resetBoard((255,0,0))
        self.board.setKeys()
        self.placeRange=placeRange()
        #self.placeRange.draw()
        self.placementRange = self.placeRange.getRange()
        self.playGround=playGround()
        self.playGround.setArea(cc.COLDGREY)
        #self.playGround.resetBoard((255, 255, 255))
        self.selectedKey=-1
        self.rotateKeys=[pygame.locals.K_r]
        self.mirrorKeys=[pygame.locals.K_s,pygame.locals.K_m]
        self.inPlacementRange=True
        self.board.draw()
        self.key=None

    def run(self):
        while True:
            self.isPlaceRange=False
            for event in pygame.event.get():
                #self.draw()
                if event.type == pl.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pl.MOUSEBUTTONDOWN:
                    self.selectedKey=self.board.getKeyCode(event.pos[0], event.pos[1])
                    x,y=self.board.getPlaygroundPos(event.pos[0], event.pos[1])
                    if y>7:
                        print("Selected key is nr: %d" % self.selectedKey)
                        #Clear Placement range
                        self.key=copy.deepcopy(self.board.keys[self.selectedKey])
                        self.placeRange.setArea(BLACK)
                        self.board.draw()
                        self.board.addKey( self.key, self.placementRange[0][0], self.placementRange[1][0], self.key.rotationGrad, self.key.mirror, True)
                    if self.selectedKey>=0:
                        print("Place at Placementrange (%d, %d), inRange %d, inPlace %d" % (self.placementRange[0][0], self.placementRange[1][0],self.playGround.isInPlacementRange(x,y),self.isPlaceRange))
                        if self.placeRange.isInPlacementRange(x,y):
                            print("Place in Placerange")
                            self.board.addKey( self.key, placementRange[0][0], placementRange[1][0], self.key.rotationGrad, self.key.mirror, True)
                    self.board.draw()
                if event.type == pl.MOUSEBUTTONUP:
                    x,y=self.board.getPlaygroundPos(event.pos[0], event.pos[1])
                    print("BTN UP (%d, %d)" %(x,y))
                    x,y=self.board.getPlaygroundPos(event.pos[0], event.pos[1])
                    print(self.playGround.isInPlacementRange(x,y), self.selectedKey)
                    if self.playGround.isInPlacementRange(x,y) and self.selectedKey>=0:
                        print("Place at Playfield (%d, %d), inRange %d, inPlace %d" % (x, y,self.playGround.isInPlacementRange(x,y),self.isPlaceRange))
                        if self.playGround.isInPlacementRange(x,y):
                            self.board.addKey( self.key, x, y, self.key.mirror, self.key.rotationGrad, True)
                        if self.isPlaceRange:
                            print("Place in Placerange")
                            if self.board.addKey( self.board.keys[self.selectedKey], placementRange[0][0], placementRange[1][0], self.key.rotationGrad, self.key.mirror, True):
                                self.playGround.append(self.key)
                    self.board.draw()
 
                if pygame.mouse.get_focused() and event.type==4:
                    x,y=self.board.getPlaygroundPos(event.pos[0], event.pos[1])
                    self.inPlacementRange = self.board.isInPlacementRange(x,y)
                    #print("focused %s " % (str(self.board.getPlaygroundPos(event.pos[0], event.pos[1]))))
                if event.type == pl.KEYUP:
                    print(event.key, pl.K_ESCAPE)
                    if event.key == pl.K_ESCAPE:
                        pygame.quit()
                if event.type == pl.KEYDOWN:
                    print(event.key, pl.K_ESCAPE)
                    if event.key == pl.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    x,y = pygame.mouse.get_pos()
                    x/=gridSize
                    y/=gridSize
                    if event.key in self.rotateKeys:
                        self.key.rotationGrad =(self.key.rotationGrad+90)%360
                        print("R or r at (%d, %d) Range((%d,%d),(%d %d)), rotate %d" % (x,y,self.placementRange[0][0],self.placementRange[1][0],  self.placementRange[1][1], self.placementRange[1][1], self.rotate))
                        self.placeRange.setArea(BLACK)
                        self.board.addKey( self.key, self.placementRange[0][0],self.placementRange[1][0], self.key.mirror,self.key.rotationGrad, True)
                    if event.key == pygame.locals.K_m:
                        self.key.mirror =(self.key.mirror+1)%2==1
                        print("S or s at (%d, %d) Range((%d,%d),(%d %d)), mirror %d" % (x,y,self.placementRange[0][0],self.placementRange[1][0],  self.placementRange[1][1], self.placementRange[1][1], self.mirror))
                        self.placeRange.setArea(BLACK)
                        self.board.addKey( self.board.keys[self.selectedKey], self.placementRange[0][0],self.placementRange[1][0], self.mirror ,self.rotationGrad, True)
                        self.board.draw()
                    if (x > self.placementRange[0][0] and x<self.placementRange[1][0]) and ( y > self.placementRange[1][1] and y<self.placementRange[1][1]):
                            print("In range")




        # for figIdx in range(len(self.board.keys)):
        #     x=self.board.keys.pos[0]
        #     y=self.board.keys.pos[1]
        #     self.addKey(board, self.board.keys[figIdx], x, y, configurations[0]['figOR'][i][1],configurations[0]['figOR'][i][2], True)


if __name__=="__main__":
    myGame=game()
    myGame.run()