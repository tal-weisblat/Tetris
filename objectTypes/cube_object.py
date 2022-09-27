
# CUBE 
# from symmetry -> no rotation needed 


import pygame 


# WINDOW 
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()


COL_NUM = 8  
box_face = WIN_WIDTH/COL_NUM


# CREATE 
def cube_create():
    cube_object = []
    x = 1*box_face            # make it random ? 
    y = 0
    box = pygame.Rect(x,y, box_face, box_face)
    cube_object.append(box)
    return cube_object 


