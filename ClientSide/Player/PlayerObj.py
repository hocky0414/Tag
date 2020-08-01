from Player.PlayerStatic import *
from mainStatic import *
from Communication.Client import *
import math
import pygame


class PlayerObj:
    def __init__(self,x,y,width, height, color,obsInfo):
        self.communicator = communication_client()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.getPos()
        self.rect = (self.x, self.y, width, height)
        self.obsInfo = obsInfo

        self.__parseObs()

    # get player position in a String
    # def getPos(self):
    #     getX = self.communicator.getPos()
    #     self.x = int(getX.split("&")[0].split("=")[1])
    #     self.y = int(getX.split("&")[1].split("=")[1])
    #     return

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
                self.__sendMessage()
        if (key[pygame.K_RIGHT]):
            dist = self.x + getVel()
            if self.moveable(dist, self.y) and self.moveable(dist + self.width, self.y):
                self.x += getVel()
                self.__sendMessage()
        if (key[pygame.K_UP]):
            dist = self.y - getVel()
            if self.moveable(self.x, dist) and self.moveable(self.x, dist + self.height):
                self.y -= getVel()
                self.__sendMessage()
        if key[pygame.K_DOWN]:
            dist = self.y + getVel()
            if self.moveable(self.x, dist) and self.moveable(self.x, dist + self.height):
                self.y += getVel()
                self.__sendMessage()
        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self, win, FOV):
        # draw player on screen
        self.FOV = FOV
        selfPos=[self.x,self.y]
        oppPos=[self.opp_x,self.opp_y]

        pygame.draw.circle(win, (255, 255, 255), (int(self.x + 0.5 * self.width), int(self.y + 0.5 * self.height)), FOV)
        pygame.draw.rect(win, self.color, self.rect)
        if math.sqrt(((selfPos[0]-oppPos[0])**2)+((selfPos[1]-oppPos[1])**2)) <= FOV:
            oppRect = (self.opp_x, self.opp_y, self.width, self.height)
            pygame.draw.rect(win, self.color, oppRect)

    def __sendMessage(self):
        # send message to server
        # a string have current position of the player
        ret = "posX=" + str(self.x) + "&posY=" + str(self.y)
        self.communicator.send(ret)
        return ret

    def getMessage(self):
        # recieve message from server
        str=self.communicator.receive()
        if(str != ""):
            self.opp_x=int(str.split("&")[0].split("=")[1])
            self.opp_y=int(str.split("&")[1].split("=")[1])

        # this is stub
        # self.opp_x = 500
        # self.opp_y = 500
        return
