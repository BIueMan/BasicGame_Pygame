from Properties.Static.Solide import Wall
from InGame.ImageExtractor import extractDirInFalder
import pygame

# ROOT_PATH form main
from Path import ROOT_PATH
DEFAULT_PATH = ROOT_PATH + "\\Sprites\\Floor"
BOX_SIZE = 20
SPRITE_DIR = extractDirInFalder(DEFAULT_PATH, (BOX_SIZE, BOX_SIZE))

class SpriteWall(Wall):
    def __init__(self, win, x, y, length, name="floor_undefined"):
        Wall.__init__(self, [name, win, x, y, BOX_SIZE, length*BOX_SIZE])
        self.length = length
        global SPRITE_DIR
        self.sprite_path = DEFAULT_PATH
        self.sprite_dir = SPRITE_DIR

    def blit(self):
        Wall.blit(self)
        # blit start
        image_end = pygame.transform.rotate(self.sprite_dir[2], 90)
        image_middle = pygame.transform.rotate(self.sprite_dir[0], 90)
        self.win.blit(image_end, (self.x, self.y) )
        # blit middle
        for i in range(self.length-2):
            self.win.blit(image_middle, (self.x, self.y + (i+1)*BOX_SIZE))
        # blit end
        self.win.blit(pygame.transform.flip(image_end, False, True), (self.x, self.y + (self.length-1)*BOX_SIZE))