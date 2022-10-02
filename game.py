


from gameSettings import *
import random



from grid import createGrid, drawGrid                     # grid 




from cubeClass import cube
from cubeList import addCube, drawCubeList, removeRow



def game():
    
    cube_new = cube(RED)    # 2 options so... 
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
            cube_new = cube(random.choice([RED,BLACK]))
    

        # move cube 
        keys = pygame.key.get_pressed()
        key_pressed = cube_new.moveCube(keys, key_pressed, cubeList)   # move 
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False
        

        # add cube 
        create_new_shape = addCube(cubeList, cube_new)

        # remove row 
        removeRow(cubeList)


        
        # draw  
        WIN.fill(WHITE)
        drawGrid(gridGui)
        cube_new.draw()
        drawCubeList(cubeList)        
        pygame.display.update()


game()



