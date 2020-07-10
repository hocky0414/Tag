import pygame
from Player.PlayerObj import *
from MapObj.map import *
#TODO:move to some other File

def drawWindow(win,player,map,FOV):
    win.fill((155,155,155))
    player.draw(win,FOV)
    map.drawMap(win)
    pygame.display.update()

def main():
    width = 1000
    height = 1000
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Player")
    run=True
    initFov=getFOV()
    clock=pygame.time.Clock()
    counter=0;
    map = Map(width, height)
    obsInfo=map.block()
    player= PlayerObj(50,50,getWid(),getHeight(),getColor(),obsInfo)
    print(player.obsInfo)
    print (player.obsX)
    while(run):
        clock.tick(60)
        frame=clock.get_fps()

        if counter>=frame*10 and frame!=0:
            initFov+=5
            counter=0;
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        drawWindow(win,player,map,initFov)
        counter+=1;
main()