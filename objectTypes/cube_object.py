

from gameSettings import * 


# -------------------------------------------- CREATE -------------------------------------------- 
def cube_create():
    cube_object = []
    x = 1*box_face            # make it random ? 
    y = 0
    box = pygame.Rect(x,y, box_face, box_face)
    cube_object.append(box)
    return cube_object 


