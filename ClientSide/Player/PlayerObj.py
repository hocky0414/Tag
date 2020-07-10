from Player.PlayerStatic import *
import pygame


class PlayerObj:
    def __init__(self, x, y,width,height,color,obsInfo):
        self.x = x
        self.y = y
        self.width=width
        self.height=height
        self.color=color
        self.rect=(x,y,width,height)
        self.obsInfo=obsInfo
        self.__parseObs()
    # get player position in a String
    def getPos(self):
        ret = self.x + ":" + self.y
        return ret
    def moveable(self,x,y):
        ret=True
        for block in range(0,len(self.obsX)):
            posX= self.obsX[block]
            posY=self.obsY[block]
            if x >= posX and x <=posX+self.objW and y>= posY and y <=posY+self.objH:
                ret=False;
                break;
        return ret
    def __parseObs(self):
        self.objH = self.obsInfo["height"]
        self.objW = self.obsInfo["width"]
        self.obsInfo.pop("height")
        self.obsInfo.pop("width")
        x=self.__blockX()
        y=self.__blockY()
        self.obsX=x
        self.obsY=y
    def __blockX(self):
        posX= self.obsInfo
        ret=[]
        for block in posX:
            if("x" in block):
                ret.append(posX[block])
        return ret
    def __blockY(self):
        posY = self.obsInfo
        ret = []
        for block in posY:
            if ("y" in block):
                ret.append(posY[block])
        return ret

    def move(self):
        key= pygame.key.get_pressed()

        if(key[pygame.K_LEFT]):
            dist=self.x - getVel()
            if self.moveable(dist,self.y):
                self.x-=getVel()
        if (key[pygame.K_RIGHT]):
            dist = self.x + getVel()
            if self.moveable(dist, self.y):
                self.x += getVel()
        if (key[pygame.K_UP]):
            dist = self.y - getVel()
            if self.moveable(self.x, dist):
                self.y -= getVel()
        if key[pygame.K_DOWN]:
            dist = self.y + getVel()
            if self.moveable(self.x, dist):
                self.y += getVel()
        self.rect=(self.x,self.y,self.width,self.height)
    def draw(self,win,FOV):
        #TODO:add stuff in FOV here

        pygame.draw.circle(win, (255, 255, 255), (int(self.x+0.5*self.width),int(self.y+0.5*self.height)), FOV)
        pygame.draw.rect(win,self.color,self.rect)


