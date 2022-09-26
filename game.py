


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





def game():
    
    run = True 
    shapeList = []
    clock = pygame.time.Clock()
    gridGui = createGrid()
    shape = createNewShape() 
    key_pressed = False 
    create_new_shape = False 

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


        # DRAW 
        WIN.fill(WHITE)
        drawGrid(gridGui)
        drawShapeList(shapeList)
        drawShapeList(shapeList)
        drawShape(shape)
        pygame.display.update()


game()



