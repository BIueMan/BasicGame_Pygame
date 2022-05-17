from Properties.Orea.Colide import Colide
from Properties.Orea.Text import Text
import pygame

# BOX_COLOR = (150,150,150)
COLIDE_SIZE = (70, 150)
TEXT_OFFSET = [33, 30]

class Exit(Colide):
    def __init__(self, win, x, y):
        Colide.__init__(self,["exit", win, x, y, COLIDE_SIZE[0], COLIDE_SIZE[1]])
        self.text = Text(["exit text", win, x + TEXT_OFFSET[0], y + TEXT_OFFSET[1], 0, 0], "Exit")

    def blit(self):
        Colide.blit(self)
        self.text.blit()
        pygame.draw.rect(self.win, self.color, self.get(), 1)
