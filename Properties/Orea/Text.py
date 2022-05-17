import pygame
from Properties.Static.Solide import Solide
from Levels import CorentLevel
from Properties.HIT_BOX import *

COLOR = (150, 150, 150)

class Text(HitBox):
    def __init__(self, data, text, size = 20):
        HitBox.__init__(self, data)
        self.do_blit = True
        self.text = text
        self.color = COLOR
        self.size = size

    def reset(self):
        pass

    def update(self):
        pass

    def blit(self):
        font = pygame.font.Font("freesansbold.ttf", self.size)
        text = font.render(self.text, True, self.color)
        rect = text.get_rect()
        rect.center = (self.x, self.y)

        self.win.blit(text, rect)

