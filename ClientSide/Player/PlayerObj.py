from Player.PlayerStatic import *
import pygame


class PlayerObj:
    def __init__(self, x, y,width,height,color):
        self.x = x
        self.y = y
        self.width=width
        self.height=height
        self.color=color
        self.rect=(x,y,width,height)

    # get player position in a String
    def getPos(self):
        ret = self.x + ":" + self.y
        return ret
    def move(self):
        key= pygame.key.get_pressed()

        if(key[pygame.K_LEFT]):
            self.x -= getVel()
        if (key[pygame.K_RIGHT]):
            self.x+=getVel()
        if (key[pygame.K_UP]):
            self.y-=getVel()
        if key[pygame.K_DOWN]:
            self.y+=getVel()
        self.rect=(self.x,self.y,self.width,self.height)
    def draw(self,win,FOV):
        #TODO:add stuff in FOV here

        pygame.draw.circle(win, (255, 255, 255), (int(self.x+0.5*self.width),int(self.y+0.5*self.height)), FOV)
        pygame.draw.rect(win,self.color,self.rect)


#TODO:move to some other File
width=1000
height=1000
win= pygame.display.set_mode((width,height))
pygame.display.set_caption("Player")
def drawWindow(win,player,FOV):
    win.fill((0,0,0))
    player.draw(win,FOV)
    pygame.display.update()
def main():
    run=True
    initFov=getFOV()
    clock=pygame.time.Clock()
    counter=0;
    #TODO: move Const to Player Static
    player= PlayerObj(50,50,getWid(),getHeight(),getColor())

    while(run):
        clock.tick(60)
        frame=clock.get_fps()

        print(counter)
        if counter>=frame*10 and frame!=0:
            initFov+=5
            counter=0;
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        drawWindow(win,player,initFov)
        counter+=1;
main()