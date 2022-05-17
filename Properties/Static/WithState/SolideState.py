import pygame
from Properties.Static.Solide import Solide
from Levels import CorentLevel
from Properties.HIT_BOX import *

class SolideState(Solide):
    def __init__(self, data):
        Solide.__init__(self, data)
        self.state = False
        self.y_off = self.y

    def reset(self):
        self.y = self.y_off
        self.state = False

    def update(self):
        pass