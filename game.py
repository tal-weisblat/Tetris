


import pygame 


# grid 
from components.grid import createGrid, drawGrid
from components.shapeList import drawList, removeRow, addObject


# BUG: need to generalize to ALL objects 
# from utility import createNewShape     

# unique 
from objectTypes.L_object import L_create, L_rotate
from objectTypes.cube_object import cube_create

# common 
from objectCommonFunc.moveObject import moveObject
from objectCommonFunc.drawObject import draw



# WINDOWS
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()


# COLORS 
WHITE = (255,255,255)
BLACK = (0,0,0)

COL_NUM = 8  
box_face = WIN_WIDTH/COL_NUM






def game():
    
    # CHOOSE OBJECT (2 options so far)
    object = cube_create()    


    objectList = []
    gridGui = createGrid()
    clock = pygame.time.Clock()
    
    key_pressed = False 
    create_new_shape = False 
    space_pressed = False 
    run = True 

    while run: 

        clock.tick(60)

        # EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False 
                break
            

        # CHECK ROWS
        removeRow(objectList) 


        # NEW-SHAPE 
        if create_new_shape == True:
            create_new_shape = False 
            object = cube_create()             # develop to all types of objects (not only cubes ...)
            

        # HANDLE-SHAPES   
        keys = pygame.key.get_pressed()
        key_pressed = moveObject(keys, key_pressed, object, objectList)   # move 
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False
        space_pressed = L_rotate(keys, space_pressed, object)             # rotate
        if keys[pygame.K_SPACE] == False : space_pressed = False 
        
        
        # add object to list 
        create_new_shape = addObject(object, objectList)    
        
        

        # DRAW 
        WIN.fill(WHITE)
        drawGrid(gridGui)
        drawList(objectList)
        draw(object)
        pygame.display.update()


game()



