import pygame
from Properties.Static.Solide import Solide
from Levels import CorentLevel
from Properties.HIT_BOX import *

hoxColor = (246, 38, 129)

class Colide(HitBox):
    def __init__(self, data):
        HitBox.__init__(self, data)
        self.state = False
        self.color = hoxColor

    def reset(self):
        pass

    def update(self):
        if is_collide(self, CorentLevel.corentPlayer):
            self.state = True
        else:
            self.state = False