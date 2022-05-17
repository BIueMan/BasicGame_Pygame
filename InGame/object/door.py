from Properties.Movable.Crate import CrateHitBox
from InGame.ImageExtractor import extractDirInFalder
from Properties.HIT_BOX import HitBox
from Properties.Static.WithState.Door import Door
import pygame

# ROOT_PATH form main
from Path import ROOT_PATH


DEFAULT_PATH = ROOT_PATH + "\\Sprites\\Objects\\door"
BOX_SIZE = (20,150)
SPRITE_DIR = extractDirInFalder(DEFAULT_PATH, (BOX_SIZE[0], BOX_SIZE[1]))

class SpriteDoor(Door):
    def __init__(self, win, name, x, y, trigger, speed=1, size=BOX_SIZE):
        Door.__init__(self, [name, win, x, y, size[0], size[1] ], trigger, speed)
        global SPRITE_DIR
        self.sprite_path = DEFAULT_PATH
        self.sprite_dir = SPRITE_DIR

    def blit(self):
        Door.blit(self)
        image = pygame.transform.scale(self.sprite_dir[0], [self.width, self.height])
        self.win.blit(image, (self.x, self.y))