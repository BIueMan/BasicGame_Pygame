from Properties.Static.WithState.SolideState import SolideState
from Levels import CorentLevel
from Properties.HIT_BOX import *

class Button(SolideState):
    def __init__(self, data, speed=None):
        SolideState.__init__(self, data)
        self.state = False
        self.y_off = self.y
        self.y_on = self.y + (self.height/2)
        if speed is None:
            speed = (1/self.height) * 10
        self.speed = (self.y_off-self.y_on)*speed/10

    def update(self):
        objectOnMe = False

        for object in CorentLevel.corentCrates + [CorentLevel.corentPlayer] + CorentLevel.corentRecord.records_clones:
            object.y += 1
            if where_collide(self, object) == "up":
                objectOnMe = True
            object.y -= 1


        if objectOnMe:
            # try to get down
            self.y -= self.speed
            if self.y > self.y_on:
                self.y = self.y_on
                self.state = True
        else:
            self.y += self.speed/2
            if self.y < self.y_off:
                self.y = self.y_off
            self.state = False

    def reset(self):
        self.y = self.y_off
        self.state = False
