from Properties.HIT_BOX import *
import pygame

DEFAULT_FLOOR = (0, 255, 0)
DEFAULT_WALL = (0, 0, 255)
DEFAULT_SOLID = (255, 255, 0)

class Solide(HitBox):
    def __init__(self, data):
        # copy constractor ( type(data) == class )
        if isinstance(data, HitBox):
            HitBox.__init__(self, data)
        # easy to use constractor. [name, win, x=0, y=0, width=1, height=1]
        else:
            HitBox.__init__(self, [data[0], data[1], data[2], data[3], data[4], data[5]])

        # so it stay static
        self.x_past = self.x
        self.y_past = self.y
        self.color = DEFAULT_SOLID

    def update(self):
        pass

    def reset(self):
        pass


class Floor(Solide):
    def __init__(self, data):
        # copy constractor ( type(data) == class )
        if isinstance(data, HitBox):
            HitBox.__init__(self, data)
        # easy to use constractor. [name, win, x=0, y=0, width=1, height=1]
        else:
            HitBox.__init__(self, [data[0], data[1], data[2], data[3], data[4], data[5]])

        # so it stay static
        self.x_past = self.x
        self.y_past = self.y
        self.color = DEFAULT_FLOOR

class Wall(Solide):
    def __init__(self, data):
        # copy constractor ( type(data) == class )
        if isinstance(data, HitBox):
            HitBox.__init__(self, data)
        # easy to use constractor. [name, win, x=0, y=0, width=1, height=1]
        else:
            HitBox.__init__(self, [data[0], data[1], data[2], data[3], data[4], data[5]])

        # so it stay static
        self.x_past = self.x
        self.y_past = self.y
        self.color = DEFAULT_WALL



