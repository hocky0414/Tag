import pygame
import Communication.Client as com
from Static import mainStatic

resolution_width = mainStatic.getResolution_width()
resolution_height = mainStatic.getResolution_height()
black = (0, 0, 0)
green=(0,255,0)
red= (255,0,0)
class lose:
    def __init__(self):
        self.textd = ""
    def draw(self, win,font):
        pygame.draw.line(win, black, (0, resolution_height / 5), (resolution_width, resolution_height / 5), 10)
        pygame.draw.line(win, black, (0, resolution_height / 5 * 4), (resolution_width, resolution_height / 5 * 4), 10)
        #From Geeksforgeeks
        myfont = pygame.font.Font('freesansbold.ttf', 30)
        self.textd = myfont.render("You lose", 1, black)
        win.blit(self.textd, (resolution_width *2/5 , resolution_height / 2))
        return