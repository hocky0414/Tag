from PlayerStatic import *
from Player.mainStatic import *
import Player.PlayerObjInterface as interface
import math
import pygame


class PlayerObj(interface.playerInterface):
    def __init__(self, x, y, width, height, color, obsInfo, map):
        super().__init__(x, y, width, height, color, obsInfo, map)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x, self.y, width, height)
        self.obsInfo = obsInfo
        self.map=map
        self.__parseObs()


    def moveable(self, x, y):
        ret = True
        if (x <= 0 or x >= getResolution_width() or y <= 0 or y >= getResolution_height()):
            return False
        for block in range(0, len(self.obsX)):
            posX = self.obsX[block]
            posY = self.obsY[block]
            if (x >= posX and x <= posX + self.objW and y >= posY and y <= posY + self.objH):
                ret = False
                break
        return ret
    def getPosition(self):
        return [self.x,self.y]
    def __parseObs(self):
        self.objH = self.obsInfo["height"]
        self.objW = self.obsInfo["width"]
        self.obsInfo.pop("height")
        self.obsInfo.pop("width")
        x = self.__blockX()
        y = self.__blockY()
        self.obsX = x
        self.obsY = y

    def __blockX(self):
        posX = self.obsInfo
        ret = []
        for block in posX:
            if ("x" in block):
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
        key = pygame.key.get_pressed()

        if (key[pygame.K_LEFT]):
            dist = self.x - getVel()
            if self.moveable(dist, self.y) and self.moveable(dist + self.width, self.y):
                self.x -= getVel()
        if (key[pygame.K_RIGHT]):
            dist = self.x + getVel()
            if self.moveable(dist, self.y) and self.moveable(dist + self.width, self.y):
                self.x += getVel()
        if (key[pygame.K_UP]):
            dist = self.y - getVel()
            if self.moveable(self.x, dist) and self.moveable(self.x, dist + self.height):
                self.y -= getVel()
        if key[pygame.K_DOWN]:
            dist = self.y + getVel()
            if self.moveable(self.x, dist) and self.moveable(self.x, dist + self.height):
                self.y += getVel()
        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self, win, FOV,opp_x,opp_y,opp_color):
        # draw player on screen
        self.FOV = FOV
        selfPos=[self.x,self.y]
        oppPos=[opp_x,opp_y]

        pygame.draw.circle(win, (255, 255, 255), (int(self.x + 0.5 * self.width), int(self.y + 0.5 * self.height)), FOV)
        pygame.draw.rect(win, self.color, self.rect)
        if math.sqrt(((selfPos[0]-oppPos[0])**2)+((selfPos[1]-oppPos[1])**2)) <= FOV:
            oppRect = (opp_x, opp_y, self.width, self.height)
            pygame.draw.rect(win, opp_color, oppRect)
        return
