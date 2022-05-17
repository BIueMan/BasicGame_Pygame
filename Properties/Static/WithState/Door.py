from Properties.Static.WithState.SolideState import SolideState
from Properties.HIT_BOX import *


class Door(SolideState):
    def __init__(self, data, inputObject ,speed=1):
        SolideState.__init__(self, data)
        self.state = False
        self.inputObject = inputObject
        self.y_off = self.y
        self.y_on = self.y - self.height + 4
        self.speed = (self.y_off-self.y_on)*speed/100

    def update(self):
        # update state
        self.state = self.inputObject.state

        if self.state:
            # try to get up
            self.y -= self.speed
            if self.y < self.y_on:
                self.y = self.y_on
        else:
            self.y += self.speed
            if self.y > self.y_off:
                self.y = self.y_off


    def reset(self):
        self.y = self.y_off
        self.state = False