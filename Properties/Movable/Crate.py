import pygame
from Properties.Movable.Movement import MovableHitBox
from Levels import CorentLevel
from Properties.HIT_BOX import *

ANIMET_SPEED = 30

class CrateHitBox(MovableHitBox):
    def __init__(self, data):
        MovableHitBox.__init__(self, data[0])
        self.static = True
        self.pickBy = None # how pick the crate

        # for picktime animeshen
        self.anime_pick_time = 0
        self.is_animete =False
        self.x_start = self.x
        self.y_start = self.y

    # crate can sit on crate. Moveble can sit on crate (but moveble cant sit on crate)
    def update(self):
        MovableHitBox.update(self)
        if not self.static:
            for otherCrate in CorentLevel.corentCrates:
                colide = where_collide(self, otherCrate)
                if self is otherCrate:
                    pass

                elif is_collide(self, otherCrate) and colide == "none" and otherCrate.static: # if we colide but we dont know where
                    self.y = otherCrate.y - self.height - 1
                    self.onObject = otherCrate
                    self._v0 = 0
                    self._t_fall = 0
                    self.static = True

                elif colide != "none" and otherCrate.static:
                    if colide == "right":  # object move right, can only hit wall from the left
                        self.x = otherCrate.x - self.width - 1
                    elif colide == "left":  # object move left
                        self.x = otherCrate.x + otherCrate.width + 1
                    elif colide == "up":  # object move up
                        self.y = otherCrate.y + otherCrate.height + 1
                    elif colide == "down":  # object move down
                        self.y = otherCrate.y - self.height - 1
                        self.onObject = otherCrate
                        self.y_speed = 0
                        self._v0 = 0
                        self._t_fall = 0
                        self.static = True



        # if sameone pick the crate
        if self.pickBy is not None:
            self.x = self.pickBy.x
            self.x_speed = self.pickBy.x_speed
            self.y = self._animeted_pickup()
            self.y_speed = self.pickBy.y_speed - ANIMET_SPEED
            # self._t_fall = 0 #counter the falling counter

        # if object did not move, and no one pick the crate
        if self.x_speed == 0  and self.y_speed == 0 and self.pickBy is None:
            self.static = True
        else:
            self.static = False

    def reset(self, x = None, y = None):
        # deffalt constract
        if x is None: x = self.x_start
        if y is None: y = self.y_start

        MovableHitBox.reset(self, x, y)
        self.static = True
        self.pickBy = None

        # reset animeshen
        self.anime_pick_time = 0
        self.is_animete = False

    def moveRight(self):
        MovableHitBox.moveRight(self)
        self.static = False

    def moveLeft(self):
        MovableHitBox.moveLeft(self)
        self.static = False

    def _animeted_pickup(self):
        global ANIMET_SPEED
        if self.anime_pick_time == ANIMET_SPEED:
            self.is_animete = False
            return self.pickBy.y - self.height - 1
        else:
            self.anime_pick_time += 1
            return self.anime_pick_time*(self.height+self.pickBy.height + 2)/(-ANIMET_SPEED) + self.pickBy.y+self.pickBy.height+1

    # under player = -1, inside it = 0
    def animeted_zeroing_time(self, state):
        if state == 0:
            self.anime_pick_time = int((self.height+1)*ANIMET_SPEED/(self.height+self.pickBy.height + 2))
        elif state == -1:
            self.anime_pick_time = 0


