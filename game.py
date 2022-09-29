


from gameSettings import *
import random



from grid import createGrid, drawGrid                     # grid 
from boxList import drawList, removeRow, addObject

# object (types)
from objectTypes import L_create, L_object, L_rotate
from objectTypes import cube_create

# common functions (of objects)
from objectsFunc import moveObject               
from objectsFunc import drawObject






def game():
    
    object = L_create()     # 2 options so far ... 
    #object = L_object()    # clases ... 

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


        # NEW-SHAPE (randomly)
        if create_new_shape == True:
            create_new_shape = False 
            object = random.choice([L_create(), cube_create()])

        # HANDLE-SHAPES   
        keys = pygame.key.get_pressed()
        key_pressed = moveObject(keys, key_pressed, object, objectList)   # move 
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False
        space_pressed = L_rotate(keys, space_pressed, object)             # rotate
        if keys[pygame.K_SPACE] == False : space_pressed = False 
        
        # ADD (object to list)
        create_new_shape = addObject(object, objectList)    
        
    
        # DRAW 
        WIN.fill(WHITE)
        drawGrid(gridGui)
        drawList(objectList)           # different colors ? 
        drawObject(object)             # different colors ? 
        pygame.display.update()


game()



