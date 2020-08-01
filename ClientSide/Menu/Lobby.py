import pygame
import mainStatic

resolution_width = mainStatic.getResolution_width()
resolution_height = mainStatic.getResolution_height()
black = (0, 0, 0)
green=(0,255,0)
red= (255,0,0)
class lobby:
    def __init__(self):
        self.ready=False
        self.init=False
    def draw(self, win,font):
        pygame.draw.line(win, black, (0, resolution_height / 5), (resolution_width, resolution_width / 5), 10)
        pygame.draw.line(win, black, (resolution_width / 2, resolution_height / 5),
                         (resolution_width / 2, resolution_height / 5 * 4), 10)
        pygame.draw.line(win, black, (0, resolution_height / 5 * 4), (resolution_width, resolution_width / 5 * 4), 10)

        #pygame.draw.rect(win,green,(resolution_width / 2-resolution_width/10,resolution_height / 5 * 4*1.1,resolution_width/5,resolution_height/10))
        #From Geeksforgeeks
        if not self.ready:
            text = font.render('Ready', True, black, green)
        else:
            text = font.render('Cancel', True, black, red)
        rect = text.get_rect()
        rect.center = (resolution_width // 2, resolution_height * 6 / 7)
        if not self.init:
            self.rect_left=rect.left
            self.rect_right = rect.right
            self.rect_bottom=rect.bottom
            self.rect_top=rect.top
            self.init=True
        win.blit(text, rect)
        return
    def changeReady(self):
        if self.init:
            (x, y) = pygame.mouse.get_pos()
            if (x >= self.rect_left and x <= self.rect_right and y >= self.rect_top and y <= self.rect_bottom):
                if (not self.ready):
                    self.ready = True
                else:
                    self.ready = False
        return