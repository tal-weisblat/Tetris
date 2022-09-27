


import pygame 


from utility import createGrid
from utility import drawGrid

from utility import createNewShape
from utility import moveShape 
from utility import drawShape

from utility import addToShapeList
from utility import drawShapeList
from utility import removeRowFromShapeList



# WINDOW 
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()


# COLORS 
WHITE = (255,255,255)
BLACK = (0,0,0)




# COMPLEX SHAPE 
SHAPE_VEL = 1
COL_NUM = 8  
box_face = WIN_WIDTH/COL_NUM

complex_shape = []
complex_shape_phase = 1
shape_1 = pygame.Rect(0,0, box_face, box_face)
shape_2 = pygame.Rect(0,50, box_face, box_face)
shape_3 = pygame.Rect(50,0, box_face, box_face)
shape_4 = pygame.Rect(100,0, box_face, box_face)
complex_shape.append(shape_1)
complex_shape.append(shape_2)
complex_shape.append(shape_3)
complex_shape.append(shape_4)

# DRAW 
def drawComplexShape(complex_shape):
    for box in complex_shape:
        pygame.draw.rect(WIN, BLACK, box)

# MOVE 
def moveComplexShape(complex_shape):
    for box in complex_shape:
        box.y += SHAPE_VEL


# ROTATE 
def rotateShape(keys, complex_shape, space_pressed):
    
    if keys[pygame.K_SPACE] and (space_pressed == False):    
        space_pressed = True 

        # SWITCH (to next phase)
        x1 = complex_shape[0].x
        x2 = complex_shape[1].x
        x3 = complex_shape[2].x
        x4 = complex_shape[3].x
        if x1 == 0 and x2 == 0 and x3 == 50 and x4 == 100:  
            x1, x2, x3, x4 = 0, 50, 50, 50 
            y1, y2, y3, y4 = 0, 0, 50, 100 
        elif x1 == 0 and x2 == 50 and x3 == 50 and x4 == 50:  
            x1, x2, x3, x4 = 100, 100, 50, 0
            y1, y2, y3, y4 = 0, 50, 50, 50 
        elif x1 == 100 and x2 == 100 and x3 == 50 and x4 == 0:  
            x1, x2, x3, x4 = 0, 0, 0, 50 
            y1, y2, y3, y4 = 0, 50, 100, 100 
        elif x1 == 0 and x2 == 0 and x3 == 0 and x4 == 50:  
            x1, x2, x3, x4 = 0, 0, 50, 100
            y1, y2, y3, y4 = 0, 50, 0, 0 
        
        
        y = complex_shape[0].y
        shape_1 = pygame.Rect(x1, y1+y, box_face, box_face)
        shape_2 = pygame.Rect(x2, y2+y, box_face, box_face)
        shape_3 = pygame.Rect(x3, y3+y, box_face, box_face)
        shape_4 = pygame.Rect(x4, y4+y, box_face, box_face)

        complex_shape.clear()
        complex_shape.append(shape_1)
        complex_shape.append(shape_2)
        complex_shape.append(shape_3)
        complex_shape.append(shape_4)

    return space_pressed




def game():
    
    run = True 
    shapeList = []
    clock = pygame.time.Clock()
    gridGui = createGrid()
    shape = createNewShape() 
    key_pressed = False 
    create_new_shape = False 
    space_pressed = False 
    # complex_shape_phase = 1 

    while run: 

        clock.tick(60)


        # EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False 
                break
            

        # CHECK ROWS
        removeRowFromShapeList(shapeList) 


        # NEW-SHAPE 
        if create_new_shape == True:
            create_new_shape = False 
            shape = createNewShape()
            

        # HANDLE-SHAPES   
        keys = pygame.key.get_pressed()
        key_pressed = moveShape(shape, key_pressed, keys, shapeList)    
        create_new_shape = addToShapeList(shape, shapeList)    
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False


        # EXPERIMENT 
        moveComplexShape(complex_shape)

        keys = pygame.key.get_pressed()
        space_pressed = rotateShape(keys, complex_shape, space_pressed)
         
        if keys[pygame.K_SPACE] == False: space_pressed = False 
        


        # DRAW 
        WIN.fill(WHITE)
        drawGrid(gridGui)
        drawShapeList(shapeList)
        drawShapeList(shapeList)
        
        # EXPERIMENT
        drawComplexShape(complex_shape)
        
        
        #drawShape(shape)
        pygame.display.update()


game()



