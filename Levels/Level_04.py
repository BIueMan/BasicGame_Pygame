from Objects.Character import MainCharacter
from Properties.Orea.Colide import Colide
from Properties.Orea.Text import Text
from InGame.Static.Floor import *
from InGame.Static.Wall import *
from InGame.object.chraet import SpriteCrate
from InGame.object.button import SpriteButton
from InGame.object.door import SpriteDoor
from Properties.Orea.Exit import Exit

FLOOR_COLOR = (0,255,0)
WALL_COLOR = (0,0,255)
CRATE_COLOR = (0,255,255)

def createFloor(win):
    FloorList = []
    FloorList.append(SpriteFloor(win, 0, 480, 45, "base_floor_01"))
    FloorList.append(SpriteFloor(win, 680, 280, 11, "base_floor_02"))
    FloorList.append(SpriteHalfFloor(win, 0, 180, 10, "step_floor_01"))
    FloorList.append(SpriteHalfFloor(win, 450, 180, 7, "step_floor_02"))

    return FloorList

def createWall(win):
    WallList = []
    WallList.append(Wall(["base_wall_01", win, -10, 0, 10, 500]))
    WallList.append(Wall(["base_wall_02", win, 900, 0, 10, 500]))

    WallList.append(SpriteWall(win, 680, 280, 11, "base_wall_01"))
    WallList.append(Wall(["step_wall_01", win, 900-210, 280, 10, 250]))
    return WallList

def createCrate(win):
    CrateList = []
    CrateList.append(SpriteCrate(win, 280, 400))
    CrateList.append(SpriteCrate(win, 380, 400))
    return CrateList

def createSpecial(win):
    SolideList = []
    return SolideList

def creatOrea(win):
    Orea = []
    x, y = 0, 30
    Orea.append(Exit(win,x,y))
    offset = 80
    Orea.append(Text(["backgound text", win, 150+offset, 20, 0, 0], "Press 'R' to start a new record"))
    Orea.append(Text(["backgound text 1", win, 123+offset, 40, 0, 0], "Press 'T' for a True reset"))
    Orea.append(Text(["backgound text 2", win, 160+offset, 60, 0, 0], "Press 'Y' to try this record again"))
    return Orea

def creatPlayer(win):
    x = 500
    y = 250
    record = MainCharacter.creat(x, y, win)
    return record
