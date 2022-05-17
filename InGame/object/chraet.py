from Properties.Movable.Crate import CrateHitBox
from InGame.ImageExtractor import extractDirInFalder
from Properties.HIT_BOX import HitBox
from Properties.Movable.Movement import MovableHitBox
import pygame

# ROOT_PATH form main
from Path import ROOT_PATH


DEFAULT_PATH = ROOT_PATH + "\\Sprites\\Objects\\crate"
BOX_SIZE = 70
CRATE_COLOR = (0,255,255)
SPRITE_DIR = extractDirInFalder(DEFAULT_PATH, (BOX_SIZE, BOX_SIZE))

class SpriteCrate(CrateHitBox):
    def __init__(self, win, x, y, size = BOX_SIZE):
        rect = MovableHitBox([HitBox(["crate_02", win, x, y, size, size, CRATE_COLOR]), 2, 10, 0.15])
        CrateHitBox.__init__(self, [rect])
        global SPRITE_DIR
        self.sprite_path = DEFAULT_PATH
        self.sprite_dir = SPRITE_DIR

    def blit(self):
        CrateHitBox.blit(self)
        image = pygame.transform.scale(self.sprite_dir[0], [self.width, self.height])
        self.win.blit(image, (self.x, self.y))