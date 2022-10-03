


from gameSettings import *
import random



from grid import createGrid, drawGrid    


from classCube import cube
from cubeList import addCube, drawCubeList, removeRow
from classCubeShape import CubeShape



def game():
    
    cube_shape = CubeShape(RED)    # 2 options so... 
    cubeList = []
    gridGui = createGrid()
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
            

        # new-cube  
        if create_new_shape == True:
            create_new_shape = False 
            cube_shape = CubeShape(random.choice([RED,BLACK]))
    

        # move cube 
        keys = pygame.key.get_pressed()
        key_pressed = cube_shape.moveCubeShape(keys, key_pressed, cubeList)   # move 
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False
        

        # BUG :  add cube 
        create_new_shape = addCube(cubeList, cube_shape)

        # remove row 
        removeRow(cubeList)


        # draw  
        WIN.fill(WHITE)
        drawGrid(gridGui)
        cube_shape.drawCubeShape()
        drawCubeList(cubeList)        
        pygame.display.update()


game()



