import pygame
from Levels import CorentLevel
from Objects.Character import MainCharacter

# param
LEVELS = [1, 2, 3, 5, 4, 6]
CORENT_LEVEL = 0

# GLOBAL
win = None
clock = None

# backgound size
GAME_SIZE = [None, None]

def set(name, size_x, size_y):
    global win, clock, GAME_SIZE
    GAME_SIZE = [size_x, size_y]
    # set pygame
    pygame.init()
    win = pygame.display.set_mode((size_x, size_y))
    pygame.display.set_caption(name)
    clock = pygame.time.Clock()

    return win, clock

def intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((100,150,100))
        font = pygame.font.Font('freesansbold.ttf', 115)
        text = font.render("Main Menu", True, (220,220,220))
        rect = text.get_rect()
        rect.center = (GAME_SIZE[0]//2, GAME_SIZE[1]//2-100)

        win.blit(text, rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        # rect
        in_play =False
        in_quit = False
        if 100 < mouse[0] < 100+200 and 300 < mouse[1] < 300+100:
            pygame.draw.rect(win, (0,150,0),(100, 300, 200,100))
            in_play = True
        else:
            pygame.draw.rect(win, (0, 200, 0), (100, 300, 200, 100))

        if 600 < mouse[0] < 600 + 200 and 300 < mouse[1] < 300 + 100:
            pygame.draw.rect(win, (150, 0, 0), (600, 300, 200, 100))
            in_quit = True
        else:
            pygame.draw.rect(win, (200, 0, 0), (600, 300, 200, 100))
        # text
        small_font = pygame.font.Font('freesansbold.ttf', 50)
        text = small_font.render("Play", True, (220, 220, 220))
        rect = text.get_rect()
        rect.center = (200,350)
        win.blit(text, rect)

        text = small_font.render("Quit", True, (220, 220, 220))
        rect = text.get_rect()
        rect.center = (700, 350)
        win.blit(text, rect)

        if click and in_play:
            intro = False
        if click and in_quit:
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(15)

def _if_do_run():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def _switch_record():
    # finish and save the record
    CorentLevel.corentPlayer.finish_recording()
    CorentLevel.corentRecord.insert(CorentLevel.index_character, CorentLevel.corentPlayer)
    CorentLevel.index_character += 1
    CorentLevel.corentRecord.reset()

    # create new record
    x = CorentLevel.corentPlayer.x_start
    y = CorentLevel.corentPlayer.y_start
    CorentLevel.corentPlayer = MainCharacter.creat(x, y, win)
    CorentLevel.corentPlayer.reset_record()

def _player_movement(keys):
    if keys[pygame.K_SPACE]:
        CorentLevel.corentPlayer.run_record("pick/drop")
    # move
    if keys[pygame.K_RIGHT]:
        CorentLevel.corentPlayer.run_record("right")
    if keys[pygame.K_LEFT]:
        CorentLevel.corentPlayer.run_record("left")

    if keys[pygame.K_UP]:
        CorentLevel.corentPlayer.run_record("jump")

def Launch():
    global win, clock
    levelIndex = CORENT_LEVEL

    CorentLevel.loadLevel(win, LEVELS[levelIndex])

    # tagel for R_key, T_key, Y_key
    pass_reset = False
    pass_true_reset = False
    pass_normal_reset = False

    # main loop
    run = True
    while run:
        clock.tick(100)
        run = _if_do_run()

        # draw beck ground
        pygame.draw.rect(win, (0, 0, 0), (0, 0, GAME_SIZE[0], GAME_SIZE[1]))
        # update the level
        CorentLevel.update()
        # see what keys was pressed
        keys = pygame.key.get_pressed()
        
        # if reset key was pressed
        if keys[pygame.K_r] and not pass_reset:
            _switch_record()
            CorentLevel.reset()
        pass_reset = keys[pygame.K_r]

        # true reset
        if keys[pygame.K_t] and not pass_true_reset:
            CorentLevel.cleanLevel()
            CorentLevel.loadLevel(win, LEVELS[levelIndex])
        pass_true_reset = keys[pygame.K_t]

        # normal reset
        if keys[pygame.K_y] and not pass_normal_reset:
            CorentLevel.corentRecord.reset()
            CorentLevel.corentPlayer.reset_record()
            CorentLevel.reset()
        pass_normal_reset = keys[pygame.K_y]

        #/
        # SET MOVEMENT
        # /#
        CorentLevel.corentPlayer.tick() # set record movement
        CorentLevel.corentRecord.rewind()    # move record
        # move the player
        _player_movement(keys)

        #/
        # UPDATE MOVEMENT
        # /#
        # update clones
        CorentLevel.corentRecord.update()
        # character update
        CorentLevel.corentPlayer.update()

        #/
        # blit objects
        # /#
        CorentLevel.blitLevel()
        pygame.display.update()

        if CorentLevel.next_level():
            CorentLevel.cleanLevel()
            levelIndex += 1
            CorentLevel.loadLevel(win, LEVELS[levelIndex])


    pygame.quit()
