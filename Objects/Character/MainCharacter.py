import pygame
from Properties.HIT_BOX import HitBox
from Properties.Movable.Movement import MovableHitBox
from Properties.Movable.character import CharacterHitBox
from Properties.Record import Record
from InGame.Character.Player import Player

def creat(x, y, win):
    # creat rect-player
    rect = MovableHitBox([HitBox(["crate_test", win, x, y, 70, 131, (255, 0, 0)]), 2, 6, 0.15])
    player = Player([rect])

    # creat rect-player
    record = Record(player, x, y)

    return record

