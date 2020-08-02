import pygame
import Communication.Client as com
from Static import mainStatic

resolution_width = mainStatic.getResolution_width()
resolution_height = mainStatic.getResolution_height()
black = (0, 0, 0)
green=(0,255,0)
red= (255,0,0)
class lobby:
    def __init__(self,comm):
        self.ready=False
        self.cap = False
        self.thief = False
        self.init =False
        self.com = comm
    def draw(self, win,font):
        pygame.draw.line(win, black, (0, resolution_height / 5), (resolution_width, resolution_height / 5), 10)
        pygame.draw.line(win, black, (resolution_width / 2, resolution_height / 5),
                         (resolution_width / 2, resolution_height / 5 * 4), 10)
        pygame.draw.line(win, black, (0, resolution_height / 5 * 4), (resolution_width, resolution_height / 5 * 4), 10)
        #From Geeksforgeeks
        myfont = pygame.font.Font('freesansbold.ttf', 30)
        textd = myfont.render("Waiting for Player...", 1, black)
        if not self.cap:
            textcap = font.render('Police', True, black, green)
        else:
            textcap = font.render('Police', True, black, red)
            textd = myfont.render("You choosed Police", 1, black)
        if not self.thief:
            textthe = font.render('Thief', True, black, green)
        else:
            textthe = font.render('Thief', True, black, red)
            textd = myfont.render("You choosed Thief", 1, black)
        if not self.ready:
            text = font.render('Ready', True,black, green)
        elif self.ready and self.cap:
            text = font.render('Cancel', True, black, red)
            textd = myfont.render("Police is ready to go", 1, black)
        elif self.ready and self.thief:
            text = font.render('Cancel', True, black, red)
            textd = myfont.render("Thief is ready to go", 1, black)
        readyB = text.get_rect()
        readyB.center = (500,500)#(resolution_width / 2, resolution_height * 6 / 7)
        capB = textcap.get_rect()
        capB.center = (resolution_width / 4, resolution_height/10)
        thiefB = textthe.get_rect()
        thiefB.center = (resolution_width*3 / 4, resolution_height / 10)
        if not self.init:
            self.readyB_left=readyB.left
            self.readyB_right = readyB.right
            self.readyB_bottom=readyB.bottom
            self.readyB_top=readyB.top
            self.capB_left = capB.left
            self.capB_right = capB.right
            self.capB_bottom = capB.bottom
            self.capB_top = capB.top
            self.thiefB_left = thiefB.left
            self.thiefB_right = thiefB.right
            self.thiefB_bottom = thiefB.bottom
            self.thiefB_top = thiefB.top
            self.init=True
        win.blit(textd, (resolution_width / 8, resolution_height / 2))
        win.blit(text, readyB)
        win.blit(textcap,capB)
        win.blit(textthe,thiefB)
        return
    def changeReady(self):
        if self.init:
            (x, y) = pygame.mouse.get_pos()
            if (x >= self.readyB_left and x <= self.readyB_right and y >= self.readyB_top and y <= self.readyB_bottom):
                if (not self.ready):
                    if (self.thief or self.cap):

                        data=self.com.sendMenu(self.cap,self.thief,True)
                        print (data)
                        if "taken" not in data:
                            self.ready = True
                        else:
                            self.ready= False
                else:
                    self.ready = False
                    data=self.com.sendMenu(self.cap, self.thief, self.ready)
                    if "taken" in data:
                        self.ready = True
        return
    def chooseC(self):
        if self.init:
            (x, y) = pygame.mouse.get_pos()
            if (x >= self.capB_left and x <= self.capB_right and y >= self.capB_top and y <= self.capB_bottom):
                if (not self.cap):
                    if(not self.thief):
                        self.cap = True
                else:
                    self.cap = False
            if (x >= self.thiefB_left and x <= self.thiefB_right and y >= self.thiefB_top and y <= self.thiefB_bottom):
                if (not self.thief):
                    if(not self.cap):
                        self.thief = True
                else:
                    self.thief = False
        return
