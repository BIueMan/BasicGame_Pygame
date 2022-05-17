from Properties.Static.Solide import Floor
from InGame.ImageExtractor import extractDirInFalder
import pygame

# ROOT_PATH form main
from Path import ROOT_PATH
DEFAULT_PATH = ROOT_PATH + "\\Sprites\\Floor"
BOX_SIZE = 20
SPRITE_DIR = extractDirInFalder(DEFAULT_PATH, (BOX_SIZE, BOX_SIZE))

class SpriteFloor(Floor):
    def __init__(self, win, x, y, length, name="floor_undefined"):
        Floor.__init__(self, [name, win, x, y, length*BOX_SIZE, BOX_SIZE])
        self.length = length
        global SPRITE_DIR
        self.sprite_path = DEFAULT_PATH
        self.sprite_dir = SPRITE_DIR

    def blit(self):
        Floor.blit(self)
        # blit start
        image = pygame.transform.flip(self.sprite_dir[2], True, False)
        self.win.blit(image, (self.x, self.y) )
        # blit middle
        for i in range(self.length-2):
            self.win.blit(self.sprite_dir[0], (self.x + (i+1)*BOX_SIZE, self.y))
        # blit end
        self.win.blit(self.sprite_dir[2], (self.x + (self.length-1)*BOX_SIZE, self.y))

class SpriteHalfFloor(Floor):
    def __init__(self, win, x, y, length, name="floor_undefined"):
        Floor.__init__(self, [name, win, x, y, length*BOX_SIZE, BOX_SIZE])
        self.length = length
        global SPRITE_DIR
        self.sprite_path = DEFAULT_PATH
        self.sprite_dir = SPRITE_DIR

    def blit(self):
        Floor.blit(self)
        # blit start
        image = pygame.transform.flip(self.sprite_dir[4], True, False)
        self.win.blit(image, (self.x, self.y) )
        # blit middle
        for i in range(self.length-2):
            self.win.blit(self.sprite_dir[3], (self.x + (i+1)*BOX_SIZE, self.y))
        # blit end
        self.win.blit(self.sprite_dir[4], (self.x + (self.length-1)*BOX_SIZE, self.y))