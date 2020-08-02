from Static.PlayerStatic import getFOV
from Static.mainStatic import *
from enum import Enum
from MapObj.map import *
import Communication.Client as com
from Menu import Lobby


class Status(Enum):
    waiting = 1
    in_game = 2
    game_over = 3


def drawWindow(win, player, map, FOV, p2x, p2y, p2c):
    win.fill((155, 155, 155))
    player.draw(win, FOV, p2x, p2y, p2c)
    map.drawMap(win)
    pygame.display.update()
    return


def drawMenu(win, menu,font):
    win.fill((155, 155, 155))
    menu.draw(win, font)
    pygame.display.update()
    return


def main():
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tag")
    run = True
    init=False
    initFov = getFOV()
    clock = pygame.time.Clock()
    counter = 0
    comm = com.communication_client()
    status = comm.status()
    player=None
    waiting = Lobby.lobby(comm)
    font = pygame.font.Font('freesansbold.ttf', 70)

    while (run):
        if status.value == Status.waiting.value:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting.changeReady()
                    waiting.chooseC()
            drawMenu(win, waiting, font)
        elif status.value ==Status.in_game.value:

            if not init:
                comm.initPlayer()
                player = comm.player
                init=True

            player2 = comm.send(player)
            clock.tick(60)
            frame = clock.get_fps()
            if counter >= frame * 10 and frame != 0:
                initFov += 5
                counter = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            player.move()
            drawWindow(win, player, player.map, initFov, player2.x, player2.y, player2.color)
            counter += 1
        status = comm.status()
main()
