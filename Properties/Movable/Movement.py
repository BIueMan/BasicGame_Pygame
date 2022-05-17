import pygame
from Properties.HIT_BOX import *
from Levels import CorentLevel


class MovableHitBox(HitBox):
    def __init__(self, data=None):
        # copy constractor ( type(data) == tpe(class) )
        if isinstance(data, MovableHitBox):
            # [win, x=0, y=0, width=1, height=1, color=(255, 0, 0)]
            HitBox.__init__(self, data)
            self.gravity = data.gravity
            self.moveSpeed = data.moveSpeed
            self.jumpSpeed = data.jumpSpeed
        # normal constractor, data will need to be in the shape of [hit_box, move_speed=0, jump_speed=0, gravity=0.1]
        else:
            HitBox.__init__(self, data[0])
            self.moveSpeed = data[1]
            self.jumpSpeed = data[2]
            self.gravity = data[3]

        # save object speed
        self.x_speed = 0
        self.y_speed = 0

        # hiting floors
        self.onObject = None
        self._t_fall = 0
        self._move = 0  # -1 Left, 1 Right, 0 noMove
        self._v0 = 0

        # vertical knock off
        self._isKnockOff = False
        self.deceleration_knockOff = 0
        self.v0_knockOff = 0
        self._t_knockOff = 0

    def update(self):
        self.x_speed = self._initiateMove() + self._initiateKnockOff()
        self.y_speed = self._initiateFalling()
        self.update_speed(self.x_speed, self.y_speed)

        # chack if object still stand on floor
        if self.onObject is not None:  # if object on floor
            self.y += 1
            if where_collide(self, self.onObject) != "down":
                self.onObject = None
                self._v0 = 0  # cliff falling speed
            self.y -= 1

        # hit a floor
        for floor in CorentLevel.corentFloors:
            if (where_collide(self, floor) == "down") and self.y_speed > 0:
                self.y = floor.y - self.height - 1
                self.onObject = floor
                self._v0 = 0
                self._t_fall = 0
                break

        # hit wall
        for wall in CorentLevel.corentWalls:
            colide = where_collide(self, wall)
            if colide == "right": # object move right, can only hit wall from the left
                self.x = wall.x - self.width - 1
            elif colide == "left": # object move left
                self.x = wall.x + wall.width + 1

        # hit solide object
        for solide in CorentLevel.corentSpecial:
            colide = where_collide(self, solide)
            if colide == "right": # object move right, can only hit wall from the left
                self.x = solide.x - self.width - 1
            elif colide == "left": # object move left
                self.x = solide.x + solide.width + 1
            elif colide == "down":
                self.y = solide.y - self.height -1
                self.onObject = solide
                self._v0 = 0
                self._t_fall = 0
            elif colide == "up":
                self.y = solide.y + solide.height + 1
                self._v0 = 0
                self._t_fall = 0

        # reset tageling
        self._move = 0

    def reset(self, x, y):
        HitBox.reset(self, x, y)
        # reset  speed
        self.x_speed = 0
        self.y_speed = 0
        # reset floor floors
        self.onObject = None
        self._t_fall = 0
        self._move = 0  # -1 Left, 1 Right, 0 noMove
        self._v0 = 0
        # reset knock off
        self._isKnockOff = False
        self.deceleration_knockOff = 0
        self.v0_knockOff = 0
        self._t_knockOff = 0

    def moveRight(self):
        self._move += 1

    def moveLeft(self):
        self._move += -1

    def idle(self):
        self._move += 0

    def _initiateMove(self):
        if self._move > 0:
            return self.moveSpeed
        elif self._move < 0:
            return -self.moveSpeed
        else:
            return 0

    def jump(self):
        if self.onObject is not None:
            self.onObject = None
            self._t_fall = 0
            self._v0 = -self.jumpSpeed

    def _initiateFalling(self):
        if self.onObject is not None:  # if on floor
            return 0
        else:  # if not, then fall
            self._t_fall += 1
            return self._v0 + self.gravity * (self._t_fall - 1)

    # data must be in diffrent Direction
    def knockOff(self, v0, deceleration):
        if (v0 * deceleration <= 0):
            # up date
            self.v0_knockOff = v0
            self._t_knockOff = 0
            self.deceleration_knockOff = deceleration
            self._isKnockOff = True
        else:
            print("knockoff effect got values that could broke the game")

    def _initiateKnockOff(self):
        if not self._isKnockOff:
            return 0
        # if the next step will change the direction of the movement
        elif ((self.v0_knockOff + self.deceleration_knockOff * (self._t_knockOff)) *
              (self.v0_knockOff + self.deceleration_knockOff * (self._t_knockOff + 1)) <= 0):
            self._isKnockOff = False
            self.v0_knockOff = 0
            self._t_knockOff = 0
            self.deceleration_knockOff = 0
            return 0
        # else, continue to deceleration
        else:
            self._t_knockOff += 1
            return self.v0_knockOff + self.deceleration_knockOff * (self._t_knockOff - 1)
