

from gameSettings import * 


# ---------------------------------------- DRAW -------------------------------------------
def draw(object):
    for box in object:
        pygame.draw.rect(WIN, BLACK, box)
