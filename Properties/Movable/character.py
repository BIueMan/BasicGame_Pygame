import pygame
from Properties.Movable.Movement import MovableHitBox
from Levels import CorentLevel
from Properties.HIT_BOX import *

COMMENDS_LIST = ("right", "left", "jump", "pick/drop")

class CharacterHitBox(MovableHitBox):
    def __init__(self, data):
        MovableHitBox.__init__(self, data[0])
        self.pickedCrate = None
        self.commends_running_now = []
        self.commends_that_was_runs =[]


    def update(self):
        MovableHitBox.update(self)
        for crate in CorentLevel.corentCrates:
            colide = where_collide(self, crate)
            if colide is not "none" and self.y_speed > 0:
                if colide is "down":  # object move down
                    self.y = crate.y - self.height - 1
                    self.onObject = crate
                    self.y_speed = 0
                    self._v0 = 0
                    self._t_fall = 0
                    break

        # save the commend that was running
        self.commends_that_was_runs = self.commends_running_now
        self.commends_running_now = []




    def reset(self, x, y):
        MovableHitBox.reset(self, x, y)
        self.pickedCrate = None
        self.commends_running_now = []
        self.commends_that_was_runs = []

    # pick an object that the character stand on
    def pickCrate(self):
        # if character already picked a crate, pass
        if self.pickedCrate is not None:
            return

        # do character inside a crate
        for crate in CorentLevel.corentCrates:
            isColide = is_collide(lower_pixels(self), lower_pixels(crate))
            if isColide and crate.static:
                self.pickedCrate = crate

                # if we stand on crate, then we pick it up
                self.pickedCrate.pickBy = self
                self.pickedCrate.static = False
                self.pickedCrate.animeted_zeroing_time(0)
                self.pickedCrate.is_animete = True
                return

        # do character stand on crate, if yes save it
        self.y += 2
        for crate in CorentLevel.corentCrates:
            colide = where_collide(self, crate)
            if colide is "down" and crate.static:
                self.pickedCrate = crate

                # if we stand on crate, then we pick it up
                self.pickedCrate.pickBy = self
                self.pickedCrate.static = False
                self.pickedCrate.animeted_zeroing_time(-1)
                self.pickedCrate.is_animete = True
                if self.onObject is crate:
                    self.onObject = None
                break
        self.y -= 2
        return

    def dropCrate(self):
        # if character not holding anything
        if self.pickedCrate is None or self.pickedCrate.is_animete is True:
            return

        # release crate
        self.pickedCrate.pickBy = None
        self.pickedCrate.static = False
        self.pickedCrate._t_fall = 0 # zero the free fall
        self.pickedCrate = None

    def run_commend(self, commend):
        if commend not in COMMENDS_LIST:
            print("invalid commend: ", commend, ", for character:", self.character.name)
            return False

        if commend == "pick/drop" and commend not in self.commends_that_was_runs:
            if self.pickedCrate is None:
                self.pickCrate()
            else:
                self.dropCrate()

        if commend is "right":
            self.moveRight()
        if commend is "left":
            self.moveLeft()
        if commend is "jump":
            self.jump()

        self.commends_running_now.append(commend)
        return True