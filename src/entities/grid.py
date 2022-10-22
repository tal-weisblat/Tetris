
from game_settings import *


'''
The grid at the backgournd. 
Involve two functions: Create & Draw. 
Its dimentions is detmined by gameSettings 
'''


# ----------------------------------- CREATE -------------------------------------- 
def create_grid():  
    gridGui = []
    box_face = GRID_WIDTH/COL_NUM
    for row in range(ROW_NUM):
        for col in range(COL_NUM):
            x = col*box_face
            y = row*box_face
            box = pygame.Rect(x,y, box_face, box_face)
            box.topleft = (x,y)
            gridGui.append(box)
    return gridGui 
 
 # ------------------------------------ DRAW ---------------------------------------
def draw_grid(grid):    
    for box in grid:
        pygame.draw.rect(WIN,BLACK,box,1)
