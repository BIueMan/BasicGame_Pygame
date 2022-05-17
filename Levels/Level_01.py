from Objects.Character import MainCharacter
from Properties.Orea.Colide import Colide
from InGame.Static.Floor import *
from InGame.Static.Wall import *
from Properties.Orea.Exit import Exit
from Properties.Orea.Text import Text


FLOOR_COLOR = (0,255,0)
WALL_COLOR = (0,0,255)
CRATE_COLOR = (0,255,255)

def createFloor(win):
    FloorList = []
    FloorList.append(SpriteFloor(win, 0, 480, 45, "base_floor_01"))
    FloorList.append(SpriteHalfFloor(win, 200, 400, 6, "step_floor_01"))
    FloorList.append(SpriteFloor(win, -20, 150, 13, "base_floor_02"))
    FloorList.append(SpriteHalfFloor(win, 400, 350, 6, "floor_down_01"))
    FloorList.append(SpriteHalfFloor(win, 600, 300, 6, "floor_down_02"))
    FloorList.append(SpriteFloor(win, 800, 200, 6, "floor_down_03"))
    FloorList.append(SpriteHalfFloor(win, 350, 100, 5, "floor_up_02"))
    FloorList.append(SpriteHalfFloor(win, 600, 150, 5, "floor_up_03"))

    return FloorList

def createWall(win):
    WallList = []
    WallList.append(Wall(["End_wall_left", win, -10, 0, 10, 500]))
    WallList.append(Wall(["End_wall_right", win, 900, 0, 10, 500]))

    return WallList

def createCrate(win):
    return []

def createSpecial(win):
    return []

def creatOrea(win):
    Orea = []
    x, y = 10, 20
    Orea.append(Exit(win,x,y))
    return Orea

def creatPlayer(win):
    x = 30
    y = 200
    record = MainCharacter.creat(x, y, win)
    return record
