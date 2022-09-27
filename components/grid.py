
import pygame 


# WINDOW 
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()

# COLORS
BLACK = (0,0,0)


COL_NUM = 8  
ROW_NUM = 12
box_face = WIN_WIDTH/COL_NUM


# CREATE 
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
 
 # DRAW 
def drawGrid(grid):    
    for box in grid:
        pygame.draw.rect(WIN,BLACK,box,1)
