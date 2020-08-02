import Menu.Lobby as Lobby
import pygame
def main():
    if __name__ == '__main__':
        pygame.init()
        win = pygame.display.set_mode((Lobby.resolution_width, Lobby.resolution_height))
        lob = Lobby.lobby()

        pygame.display.set_caption("Lobby")
        font = pygame.font.Font('freesansbold.ttf', 50)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    lob.changeReady()
                    lob.chooseC()
            win.fill((255, 255, 255))
            lob.draw(win,font)
            pygame.display.update()

main()