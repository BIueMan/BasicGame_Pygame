import os
import pygame

## convert dir with sprits to dictionarie
def extractDirInFalder(path, sprite_scale):
    dir = {}
    dir_name = path.split('\\')[-1]
    image_list = []

    # recorgen to work on all the dirs in the dir
    list = os.listdir(path)
    list.sort()
    for file in list:
        if '.' not in file:  # if files in dir are dirs
            dir[file] = extractDirInFalder(path + "\\" + file, sprite_scale)
        else:  # else, they are images
            image = pygame.image.load(path + '\\' + file)
            image_list.append(pygame.transform.scale(image, (sprite_scale[0], sprite_scale[1])))

    # save the sprite list in this dir
    if len(image_list) != 0:
        dir = image_list
    return dir