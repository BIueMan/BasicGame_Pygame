from Properties.Movable.character import CharacterHitBox
from enum import Enum, auto
import os
import pygame
from InGame.ImageExtractor import extractDirInFalder

# ROOT_PATH form main
from Path import ROOT_PATH

DEFAULT_PATH = ROOT_PATH + "\\Sprites\\Player"

class leg_state(Enum):
    IDLE = auto()
    WALK = auto()
    INAIR = auto()
class hand_state(Enum):
    IDLE = auto()
    WALK = auto()
    INAIR = auto()
    PICKUP = auto()
class blit_order(Enum):
    body_beck = 0
    gear = 1
    legs = 2
    hands = 3
    body_front = 4
    body_fact = 5
# gobal Sprite for player
# SPRITE_SCALE = [96, 96]
SPRITE_SCALE = [144, 144]
SPRITE_DIR = extractDirInFalder(DEFAULT_PATH, SPRITE_SCALE)
SPRITE_SHIFT = [-35, -5]
FRAME_DELAY = [1,7,5,7,1,1] # speed for every part of the character

FACE_TEXT_SIZE = 20
FACE_TEXT_COLOR = (0,200,150)
OFFSET = (37,42)


class Player(CharacterHitBox):
    def __init__(self, data, face_text ="X", size_text=FACE_TEXT_SIZE):
        CharacterHitBox.__init__(self, data)
        self.face_text = face_text
        self.size_text = size_text
        global SPRITE_DIR
        self.sprite_path = DEFAULT_PATH
        self.sprite_dir = SPRITE_DIR
        self.anime_speed = [0] * len(FRAME_DELAY)

        self.state = {'flip': False,
                      'leg': leg_state.IDLE,
                      'hand': hand_state.IDLE,
                      'inAir': True,
                      'walk': False,
                      'pick': False}
        self.past_state = self.state

        self.spriteCount = [0] * len(blit_order)

    def blit(self):
        CharacterHitBox.blit(self)

        """ body_beck """
        order_drawing = blit_order.body_beck.value
        self._draw_in_a_loop(self.sprite_dir['body']['beck'], order_drawing)
        """ gear """
        order_drawing = blit_order.gear.value
        self._draw_in_a_loop(self.sprite_dir['gear'], order_drawing)
        """ legs """
        order_drawing = blit_order.legs.value
        if self.state['leg'] is leg_state.INAIR:
            if self.past_state['leg'] is not leg_state.INAIR: self.spriteCount[order_drawing] = 0 # if state was change
            self._draw_to_end(self.sprite_dir['jump']['leg'], order_drawing)

        elif self.state['leg'] is leg_state.WALK:
            if self.past_state['leg'] is not leg_state.WALK: self.spriteCount[order_drawing] = 0 # if state was change
            self._draw_in_a_loop(self.sprite_dir['walk']['leg'], order_drawing)

        elif self.state['leg'] is leg_state.IDLE:
            if self.past_state['leg'] is not leg_state.IDLE: self.spriteCount[order_drawing] = 0 # if state was change
            self._draw_in_a_loop(self.sprite_dir['idle']['leg'], order_drawing)
        """ hands """
        order_drawing = blit_order.hands.value
        if self.state['hand'] is hand_state.PICKUP:
            if self.past_state['hand'] is not hand_state.PICKUP: self.spriteCount[order_drawing] = 0  # if state was change
            self._draw_to_end(self.sprite_dir['pick'], order_drawing, 5)

        elif self.state['hand'] is hand_state.INAIR:
            if self.past_state['hand'] is not hand_state.INAIR: self.spriteCount[order_drawing] = 0  # if state was change
            self._draw_to_end(self.sprite_dir['jump']['left_hand'], order_drawing)
            self._draw_to_end(self.sprite_dir['jump']['rigth_hand'], order_drawing, 0)

        elif self.state['hand'] is hand_state.WALK:
            if self.past_state['hand'] is not hand_state.WALK: self.spriteCount[order_drawing] = 0  # if state was change
            self._draw_in_a_loop(self.sprite_dir['walk']['left'], order_drawing)
            self._draw_in_a_loop(self.sprite_dir['walk']['right'], order_drawing, 0)

        elif self.state['hand'] is hand_state.IDLE:
            if self.past_state['hand'] is not hand_state.IDLE: self.spriteCount[order_drawing] = 0  # if state was change
            self._draw_in_a_loop(self.sprite_dir['idle']['hand'], order_drawing)
        """ front body """
        order_drawing = blit_order.body_front.value
        self._draw_in_a_loop(self.sprite_dir['body']['front'], order_drawing)
        """ face """
        order_drawing = blit_order.body_fact.value
        self._draw_in_a_loop(self.sprite_dir['body']['face'], order_drawing)
        """ face text """
        font = pygame.font.Font("freesansbold.ttf", self.size_text)
        text = font.render(self.face_text, True, FACE_TEXT_COLOR)
        rect = text.get_rect()
        rect.center = (self.x+OFFSET[0], self.y+OFFSET[1])
        self.win.blit(text, rect)


    def _draw_in_a_loop(self, sprite_vector, index, count_next_frame = 1):
        if len(sprite_vector) == 0:
            return
        if len(sprite_vector) <= self.spriteCount[index] or self.spriteCount[index] < 0:
            self.spriteCount[index] = 0

        image = pygame.transform.flip(sprite_vector[self.spriteCount[index]], self.state['flip'], False)
        self.win.blit(image, (self.x + SPRITE_SHIFT[0], self.y + SPRITE_SHIFT[1]))

        if self.anime_speed[index] == 0:
            self.spriteCount[index] += count_next_frame
            if self.spriteCount[index] >= len(sprite_vector):
                self.spriteCount[index] = 0

    def _draw_to_end(self, sprite_vector, index, count_next_frame = 1):
        if len(sprite_vector) == 0:
            return
        if len(sprite_vector) <= self.spriteCount[index] or self.spriteCount[index] < 0:
            self.spriteCount[index] = len(sprite_vector)-1

        image = pygame.transform.flip(sprite_vector[self.spriteCount[index]], self.state['flip'], False)
        self.win.blit(image, (self.x + SPRITE_SHIFT[0], self.y + SPRITE_SHIFT[1]))

        if self.anime_speed[index] == 0:
            self.spriteCount[index] += count_next_frame
            if self.spriteCount[index] >= len(sprite_vector):
                self.spriteCount[index] -= 1

    def update(self):
        CharacterHitBox.update(self)
        # check if we stand on object
        if self.onObject is not None: # if we stand on object
            self.state['inAir'] = False
        else:
            self.state['inAir'] = True

        # check if we pick object
        if self.pickedCrate is None:    # if we dont pick any object
            self.state['pick'] = False
            if not self.state['inAir']:
                self.state['hand'] = hand_state.WALK
            else:
                self.state['hand'] = hand_state.INAIR
        else:
            self.state['pick'] = True
            self.state['hand'] = hand_state.PICKUP

        # update leg and hands
        if self.x_past != self.x or self.y_past != self.y or self.state['inAir']: # then not idle
            if not self.state['inAir']:
                self.state['leg'] = leg_state.WALK
                if not self.state['pick']:
                    self.state['hand'] = hand_state.WALK
            else:
                self.state['leg'] = leg_state.INAIR
                if not self.state['pick']:
                    self.state['hand'] = hand_state.INAIR
        else:                                               # if idle
            self.state['leg'] = leg_state.IDLE
            if not self.state['pick']:
                self.state['hand'] = hand_state.IDLE

        self.past_state = self.state
        self.state['walk'] = False

        # anime frame
        for i in range(len(self.anime_speed)):
            self.anime_speed[i] += 1
            if self.anime_speed[i] >= FRAME_DELAY[i]:
                self.anime_speed[i] = 0


    def moveRight(self):
        CharacterHitBox.moveRight(self)
        self.state['walk'] = True
        self.state['flip'] = False

    def moveLeft(self):
        CharacterHitBox.moveLeft(self)
        self.state['walk'] = True
        self.state['flip'] = True
