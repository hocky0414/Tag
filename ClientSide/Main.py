from Player.PlayerObj import *
from MapObj.map import *
import Communication.Client as com

def drawWindow(win,player,map,FOV,p2x,p2y,p2c):
    win.fill((155,155,155))
    player.draw(win,FOV,p2x,p2y,p2c)
    map.drawMap(win)
    pygame.display.update()

def main():

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tag")
    run=True
    initFov=getFOV()
    clock=pygame.time.Clock()
    counter=0
    comm=com.communication_client()

    player= comm.player


    while(run):
        player2=comm.send(player)
        clock.tick(60)
        frame=clock.get_fps()
        if counter>=frame*10 and frame!=0:
            initFov+=5
            counter=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        drawWindow(win,player,player.map,initFov,player2.x,player2.y,player2.color)
        counter+=1
main()