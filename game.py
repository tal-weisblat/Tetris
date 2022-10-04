


from gameSettings import *
import random



from grid import createGrid, drawGrid    


#from classCube import cube
from cubeList import addCube, drawCubeList, removeRows
from classCubeShape import CubeShape
from classLshape import Lshape



def game():
    
    new_shape = CubeShape(RED) 
    cubeList = []
    grid = createGrid()
    clock = pygame.time.Clock()
    key_pressed = False 
    create_new_shape = False 
    space_pressed = False 
    run = True 

    while run: 

        clock.tick(60)

        # events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                break
            

        # new-shape  
        if create_new_shape == True:
            create_new_shape = False 
            new_shape =random.choice([Lshape(BLACK),CubeShape(RED)]) 
    

        # move-downwards 
        keys = pygame.key.get_pressed()
        key_pressed = new_shape.moveShape(keys, key_pressed, cubeList)   # move 
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False
        
        # rotate 
        space_pressed = new_shape.rotate(keys, space_pressed)
        if (keys[pygame.K_SPACE] == False): space_pressed = False


        # add cubes to cubeList
        create_new_shape = addCube(cubeList, new_shape)

        # remove row 
        removeRows(cubeList)


        # draw  
        WIN.fill(WHITE)
        drawGrid(grid)
        new_shape.drawShape()
        drawCubeList(cubeList)        
        pygame.display.update()


game()



