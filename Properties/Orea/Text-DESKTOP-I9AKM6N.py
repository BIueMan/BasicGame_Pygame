import pygame
from Properties.Static.Solide import Solide
from Levels import CorentLevel
from Properties.HIT_BOX import *

hoxColor = (50, 38, 129)
class Text(HitBox):
    def __init__(self, data):
        HitBox.__init__(self, data)
        self.do_blit = True
        self.color = hoxColor

    def reset(self):
        pass

    def update(self):
        pass

