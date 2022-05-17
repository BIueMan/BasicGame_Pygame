from Objects.Character import MainCharacter
from Properties.Orea.Colide import Colide
from InGame.Static.Floor import *
from InGame.Static.Wall import *
from InGame.object.chraet import SpriteCrate
from InGame.object.button import SpriteButton
from InGame.object.door import SpriteDoor
from Properties.Orea.Exit import Exit
from Properties.Orea.Text import Text


FLOOR_COLOR = (0,255,0)
WALL_COLOR = (0,0,255)
CRATE_COLOR = (0,255,255)

def createFloor(win):
    FloorList = []
    FloorList.append(SpriteFloor(win, 0, 480, 45, "base_floor_01"))
    FloorList.append(SpriteFloor(win, 200, 400, 6, "step_floor_01"))
    FloorList.append(SpriteFloor(win, 0, 300, 10, "step_floor_02"))
    FloorList.append(SpriteHalfFloor(win, 300, 200, 5, "floor_01"))
    FloorList.append(SpriteHalfFloor(win, 550, 250, 5, "floor_02"))
    FloorList.append(SpriteHalfFloor(win, 800, 200, 6, "floor_03"))
    return FloorList

def createWall(win):
    WallList = []
    WallList.append(SpriteWall(win, 0, 0, 25, "base_wall_01"))
    WallList.append(SpriteWall(win, 300, 400, 5, "step_wall_01"))
    WallList.append(SpriteWall(win, 190, 300, 6, "step_wall_02"))

    WallList.append(Wall(["End_wall_left", win, -10, 0, 10, 500]))
    WallList.append(Wall(["End_wall_right", win, 900, 0, 10, 500]))

    return WallList

def createCrate(win):
    CrateList = []
    crate = SpriteCrate(win, 80, 200)
    CrateList.append(crate)
    return CrateList

def createSpecial(win):
    SolideList = []
    button_01 = SpriteButton(win, "button_01", 750, 460)
    door_01 = SpriteDoor(win, "door-01", 800, 50, button_01)
    SolideList.append(button_01)
    SolideList.append(door_01)
    return SolideList

def creatOrea(win):
    Orea = []
    x,y = 830, 50
    Orea.append(Exit(win,x,y))
    return Orea

def creatPlayer(win):
    x = 30
    y = 150
    record = MainCharacter.creat(x, y, win)
    return record