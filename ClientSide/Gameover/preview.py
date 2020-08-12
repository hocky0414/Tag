import Gameover.Win as Win
import Gameover.Lose as Lose
import pygame
def main():
    if __name__ == '__main__':
        pygame.init()
        win = pygame.display.set_mode((Win.resolution_width, Win.resolution_height))
        lob =Lose.lose()

        pygame.display.set_caption("Win")
        font = pygame.font.Font('freesansbold.ttf', 50)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            win.fill((255, 255, 255))
            lob.draw(win,font)
            pygame.display.update()

main()