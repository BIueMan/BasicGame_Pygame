from Properties.Static.Solide import Floor, Wall
from Properties.HIT_BOX import HitBox
from Properties.Movable.Crate import CrateHitBox
from Properties.Movable.Movement import MovableHitBox
from Objects.Character import MainCharacter
from Properties.Static.WithState.Button import Button
from Properties.Static.WithState.Door import Door
from Properties.Orea.Colide import Colide
from Properties.Orea.Text import Text


FLOOR_COLOR = (0,255,0)
WALL_COLOR = (0,0,255)
CRATE_COLOR = (0,255,255)

def createFloor(win):
    FloorList = []
    return FloorList

def createWall(win):
    WallList = []
    return WallList

def createCrate(win):
    return []

def createSpecial(win):
    return []

def creatOrea(win):
    Orea = []
    from Game import  GAME_SIZE
    Orea.append(Text(["End Of Game 01", win, GAME_SIZE[0] // 2, GAME_SIZE[1] // 2 -50, 0, 0], "Game Over", 110))
    Orea.append(Text(["End Of Game 02", win, GAME_SIZE[0] // 2, GAME_SIZE[1] // 2 +50, 0, 0], "yeaaa!", 110))
    return Orea

def creatPlayer(win):
    x = -12000
    y = 0
    record = MainCharacter.creat(x, y, win)
    return record
