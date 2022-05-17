from Objects.Character import MainCharacter
from Properties.Orea.Colide import Colide
from Properties.Orea.Exit import Exit
from Properties.Orea.Text import Text
from InGame.Static.Floor import *
from InGame.Static.Wall import *
from InGame.object.chraet import SpriteCrate
from InGame.object.button import SpriteButton
from InGame.object.door import SpriteDoor


FLOOR_COLOR = (0,255,0)
WALL_COLOR = (0,0,255)
CRATE_COLOR = (0,255,255)

def createFloor(win):
    FloorList = []
    FloorList.append(SpriteFloor(win, 0, 480, 45, "base_floor_01"))
    FloorList.append(SpriteFloor(win, 0, 250, 35, "base_floor_02"))
    FloorList.append(SpriteHalfFloor(win, 770, 300, 7, "step_floor_01"))
    FloorList.append(SpriteHalfFloor(win, 770, 400, 7, "step_floor_02"))
    return FloorList

def createWall(win):
    WallList = []
    WallList.append(Wall(["base_wall_01", win, -10, 0, 10, 500]))
    WallList.append(Wall(["base_wall_02", win, 900, 0, 10, 500]))

    return WallList

def createCrate(win):
    CrateList = []
    return CrateList

def createSpecial(win):
    SolideList = []
    # for second floor, so no body could jump up
    SolideList.append(Floor(["Stop_Down_floor_01", win, 0, 250, 700, 20]))

    # set of buttons and doors
    button_01 = SpriteButton(win, "button_01", 120, 460)
    door_01 = SpriteDoor(win, "door-01", 350, 250, button_01, speed=3)
    SolideList.append(button_01)
    SolideList.append(door_01)

    button_02 = SpriteButton(win, "button_02", 400, 460)
    door_02 = SpriteDoor(win, "door-02", 650, 250, button_02, speed=3)
    SolideList.append(button_02)
    SolideList.append(door_02)

    button_03 = SpriteButton(win, "button_02", 400, 230)
    door_03 = SpriteDoor(win, "door-02", 250, 100, button_03, speed=3)
    SolideList.append(button_03)
    SolideList.append(door_03)

    return SolideList

def creatOrea(win):
    Orea = []
    x, y = 0, 100
    Orea.append(Exit(win,x,y))
    Orea.append(Text(["backgound text", win, 150, 20, 0, 0], "Press 'R' to start a new record"))
    Orea.append(Text(["backgound text 1", win, 123, 40, 0, 0], "Press 'T' for a True reset"))
    Orea.append(Text(["backgound text 2", win, 160, 60, 0, 0], "Press 'Y' to try this record again"))
    return Orea

def creatPlayer(win):
    x = 30
    y = 350
    record = MainCharacter.creat(x, y, win)
    return record
