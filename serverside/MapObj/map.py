import pygame

# pygame.init()
#
# win = pygame.display.set_mode((1000,1000))
#
# pygame.display.set_caption("First game")

class Map:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def block(self):
        blockInfo = {

        }

        x1= self.width * 0.1
        y1= self.height * 0.1

        x2 = self.width * 0.6
        y2 = self.height * 0.1

        x3 = self.width * 0.1
        y3 = self.height * 0.6

        x4 = self.width * 0.6
        y4 = self.height * 0.6

        width = 150
        height = 100

        blockInfo["x1"] = x1
        blockInfo["y1"] = y1
        blockInfo["x2"] = x2
        blockInfo["y2"] = y2
        blockInfo["x3"] = x3
        blockInfo["y3"] = y3
        blockInfo["x4"] = x4
        blockInfo["y4"] = y4
        blockInfo["width"] = width
        blockInfo["height"] = height
        return blockInfo

    def drawMap(self, win):
        blockIn = self.block()
        pygame.draw.rect(win, (0, 0, 0), (blockIn["x1"], blockIn["y1"], blockIn["width"], blockIn["height"]))
        pygame.draw.rect(win, (0, 0, 0), (blockIn["x2"], blockIn["y2"], blockIn["width"], blockIn["height"]))
        pygame.draw.rect(win, (0, 0, 0), (blockIn["x3"], blockIn["y3"], blockIn["width"], blockIn["height"]))
        pygame.draw.rect(win, (0, 0, 0), (blockIn["x4"], blockIn["y4"], blockIn["width"], blockIn["height"]))

# run = True
# map = Map(1000,1000)
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     win.fill((255, 255, 255))
#     map.drawMap(win)
#     pygame.display.update()
# pygame.quit()