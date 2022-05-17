import pygame
from Levels import Level_01, Level_02, Level_03, Level_04, Level_05, END_GAME
from Properties.Record import *


LEVEL_LIST = [Level_01, Level_02, Level_03, Level_04, Level_05, END_GAME]
corentFloors = []
corentWalls = []
corentCrates = []
corentSpecial = []
corentOrea = []
# records
corentRecord = None
corentPlayer = None
index_character = 0
# next level triger
exitOrea = None

def loadLevel(win, num):
    global corentFloors, corentWalls, corentCrates, corentSpecial, corentPlayer, corentRecord, index_character, corentOrea, exitOrea, NEXT_LEVEL
    num -= 1
    corentFloors = LEVEL_LIST[num].createFloor(win)
    corentWalls = LEVEL_LIST[num].createWall(win)
    corentCrates = LEVEL_LIST[num].createCrate(win)
    corentSpecial = LEVEL_LIST[num].createSpecial(win)
    corentOrea = LEVEL_LIST[num].creatOrea(win)

    corentPlayer = LEVEL_LIST[num].creatPlayer(win)
    # ready record engein
    corentPlayer.reset_record()
    corentRecord = TapeRecorder()  # creat tape for the retocrds
    index_character = 0

    # next level triger
    for orea in corentOrea:
        if orea.name == "exit":
            exitOrea = orea

def cleanLevel():
    global corentFloors, corentWalls, corentCrates, corentSpecial, corentPlayer, corentRecord, index_character, corentOrea, exitOrea
    corentFloors = []
    corentWalls = []
    corentCrates = []
    corentSpecial = []
    corentOrea = []
    # records
    corentRecord = None
    corentPlayer = None
    index_character = 0
    # next level
    exitOrea = None

def next_level():
    if exitOrea is not None:
        return exitOrea.state
    else:
        return False

def blitLevel():
    for object in corentSpecial + corentFloors + corentWalls + corentCrates + [corentRecord, corentPlayer] + corentOrea:
        object.blit()



def update():
    for object in corentSpecial + corentCrates + corentOrea:
        object.update()


def reset():
    for object in corentCrates + corentSpecial:
        object.reset()