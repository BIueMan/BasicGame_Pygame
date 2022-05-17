import pygame

Blit_HitBox = False
SHOW_NAME = False
DEFAULT_COLOR = (255,0,0)

class HitBox:
    def __init__(self, data=None):
        # copy constractor ( type(data) == class )
        if isinstance(data, HitBox):
            self.win = data.win
            self.x = data.x
            self.y = data.y
            self.width = data.width
            self.height = data.height
            self.color = data.color
            self.name = data.name

            # for collision
            self.x_past = data.x_past
            self.y_past = data.x_past

        # normal constractor, data will need to be in the shape of [name, win, x=0, y=0, width=1, height=1, color=(255, 0, 0)]
        # !!! past will not update in a normal constractor !!!
        else:
            self.name = data[0]
            self.win = data[1]
            self.x = data[2]
            self.y = data[3]
            self.width = data[4]
            self.height = data[5]
            # work with default color
            if len(data) >= 7:
                self.color = data[6]
            else:
                self.color = DEFAULT_COLOR

            # for collision
            self.x_past = self.x
            self.y_past = self.y


    def reset(self, x = None, y = None):
        if x is not None:
            self.x = x
            self.x_past = x
        if y is not None:
            self.y = y
            self.y_past = y

    def get(self):
        return (self.x, self.y, self.width, self.height)

    def update_location(self, new_x, new_y):
        self.x_past = self.x
        self.y_past = self.y

        self.x = new_x
        self.y = new_y

    def update_speed(self, x_speed, y_speed):
        self.x_past = self.x
        self.y_past = self.y

        self.x += x_speed
        self.y += y_speed

    def blit(self):
        if Blit_HitBox:
            pygame.draw.rect(self.win, self.color, self.get(), 1)
        if SHOW_NAME:
            font = pygame.font.Font("freesansbold.ttf", 10)
            text = font.render(self.name, True, self.color)
            rect = text.get_rect()
            rect.center = (self.x+30, self.y-5)

            self.win.blit(text, rect)

    def update(self):
        pass



# object a AND object b
def is_collide(a, b):
    if _dim_1_collide(a.x, a.width, b.x, b.width) or _dim_1_overshot(a.x, a.x_past, a.width, b.x, b.x_past, b.width):
        if _dim_1_collide(a.y, a.height, b.y, b.height) or _dim_1_overshot(a.y, a.y_past, a.height, b.y, b.y_past, b.height):
            return True

# normal collide (is 1 collide with 2)
def _dim_1_collide(x1, len_1, x2, len_2):
    return (x1 >= x2 and x1 <= (x2 + len_2)) or ((x1 + len_1) >= x2 and (x1 + len_1) <= (x2 + len_2)) or \
           (x2 >= x1 and x2 <= (x1 + len_1)) or ((x2 + len_2) >= x1 and (x2 + len_2) <= (x1 + len_1))

# if objects miss each other in frame (jump over)
def _dim_1_overshot(x1, x1_past, len_1, x2, x2_past, len_2):
    return (x1_past + len_1 <= x2 and x1 >= x2 + len_2) or (x1 + len_1 <= x2 and x1_past >= x2 + len_2) or \
           (x2_past + len_2 <= x1 and x2 >= x1 + len_1) or (x2 + len_2 <= x1 and x2_past >= x1 + len_1)



# will return where object a collide with object b
# was designed to be use if in the FRAM before hand. the second object did not collide
def where_collide(a,b):
    if not is_collide(b, a):
        return "none"
    elif is_collide(righter_pixels(b), lefter_pixels(a)):
        return "left"
    elif is_collide(lefter_pixels(b), righter_pixels(a)):
        return "right"
    elif is_collide(lower_pixels(b), uper_pixels(a)):
        return "up"
    elif is_collide(uper_pixels(b), lower_pixels(a)):
        return "down"
    else:
        return "none"  # default

REMAIN_PIXELS = 2 # minimom pixel the object need to be under the floor in order you count to be on the floor
# return only the lover/uper pixels of the object
def lower_pixels(object):
    temp = HitBox(["lower", object.win, object.x, object.y + object.height - REMAIN_PIXELS, object.width, REMAIN_PIXELS])
    # we creat new object, se we need to update his past manualy
    temp.x_past = object.x_past
    temp.y_past = object.y_past +object.height - REMAIN_PIXELS
    return temp

def uper_pixels(object):
    temp = HitBox(["uper", object.win, object.x, object.y, object.width, REMAIN_PIXELS])
    # we creat new object, se we need to update his past manualy
    temp.x_past = object.x_past
    temp.y_past = object.y_past
    return temp

def righter_pixels(object):
    temp = HitBox(["righter", object.win, object.x + object.width - REMAIN_PIXELS, object.y, REMAIN_PIXELS, object.height])
    # we creat new object, se we need to update his past manualy
    temp.x_past = object.x_past + object.width - REMAIN_PIXELS
    temp.y_past = object.y_past
    return temp

def lefter_pixels(object):
    temp = HitBox(["lefter", object.win, object.x, object.y, REMAIN_PIXELS, object.height])
    # we creat new object, se we need to update his past manualy
    temp.x_past = object.x_past
    temp.y_past = object.y_past
    return temp