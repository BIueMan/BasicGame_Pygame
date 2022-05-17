from Properties.Movable.Crate import CrateHitBox
from InGame.ImageExtractor import extractDirInFalder
from Properties.Static.WithState.Button import Button
import pygame

# ROOT_PATH form main
from Path import ROOT_PATH


DEFAULT_PATH = ROOT_PATH + "\\Sprites\\Objects\\button"
BOX_SIZE = [100, 20]
SPRITE_DIR = extractDirInFalder(DEFAULT_PATH, (BOX_SIZE[0], BOX_SIZE[1]))

class SpriteButton(Button):
    def __init__(self, win, name, x, y):
        Button.__init__(self, [name, win, x, y, BOX_SIZE[0], BOX_SIZE[1] ])
        global SPRITE_DIR
        self.sprite_path = DEFAULT_PATH
        self.sprite_dir = SPRITE_DIR



    def blit(self):
        Button.blit(self)
        image = pygame.transform.scale(self.sprite_dir[0], [BOX_SIZE[0], BOX_SIZE[1] ])
        self.win.blit(image, (self.x, self.y))
        image = pygame.transform.scale(self.sprite_dir[1], [BOX_SIZE[0], BOX_SIZE[1]])
        self.win.blit(image, (self.x, self.y_off))