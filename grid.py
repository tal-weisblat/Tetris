
from gameSettings import *


# ----------------------------------- CREATE -------------------------------------- 
def createGrid():  
    gridGui = []
    box_face = WIN_WIDTH/COL_NUM
    for row in range(ROW_NUM):
        for col in range(COL_NUM):
            x = col*box_face
            y = row*box_face
            box = pygame.Rect(x,y, box_face, box_face)
            box.topleft = (x,y)
            gridGui.append(box)
    return gridGui 
 
 # ------------------------------------ DRAW ---------------------------------------
def drawGrid(grid):    
    for box in grid:
        pygame.draw.rect(WIN,BLACK,box,1)
