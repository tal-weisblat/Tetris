

from gameSettings import * 
from classCube import Cube


# ------------------------------------- DRAW ----------------------------------------------
def drawCubeList(cubeList):
    for shape in cubeList:
        pygame.draw.rect(WIN, shape.color, shape.cube)        


# ------------------------------------- ADD -----------------------------------------------
def addCube(cubeList, new_shape):

    create_new_shape = False  

    # hit bottom
    max_y = max(cube.y for cube in new_shape.listOfCubes)
    if max_y  >= GRID_HEIGHT - CUBE_FACE:    
            
        # adjust cubes within new_shape
        delta = GRID_HEIGHT - (max_y + CUBE_FACE)    
        for cube in new_shape.listOfCubes: cube.y += delta
        
        # add cubes to cubeList 
        for cube in new_shape.listOfCubes:
            temp_cube = Cube(cube.x, cube.y, new_shape.color)
            cubeList.append(temp_cube) 
        
        create_new_shape = True
        COLLISION_SOUND.play()
        
    # hit cubes in cubeList 
    else: 
        for new_cube in new_shape.listOfCubes:  
            collision = False 
            for cube_list in cubeList: 

                # collision 
                if new_cube.colliderect(cube_list.cube):
                
                    # game-over (event) 
                    if cube_list.cube.y <= 0: 
                        pygame.event.post(pygame.event.Event(GAMEOVER))
                        
                    # adjust cubes in new_shape 
                    delta = cube_list.cube.y - (new_cube.y + CUBE_FACE)      
                    for new_cube in new_shape.listOfCubes: new_cube.y += delta
                    
                    # add new_cubes to cubeList 
                    for new_cube in new_shape.listOfCubes:        
                        temp_cube = Cube(new_cube.x, new_cube.y, new_shape.color)
                        cubeList.append(temp_cube)     

                    COLLISION_SOUND.play()
                    create_new_shape = True 
                    collision = True 
                    break 

            if collision: break

    return create_new_shape





# ------------------------------------- REMOVE-ROW -------------------------------------------
def removeRows(cubeList): 
    for y in np.arange(0, GRID_HEIGHT, CUBE_FACE):
        
        # check row 
        rowFilled = True
        for x in np.arange(0, GRID_WIDTH, CUBE_FACE):
            boxFilled = False
            for cube_shape in cubeList: 
                if cube_shape.cube.x == x and cube_shape.cube.y == y:
                    boxFilled = True 
                    break

            if boxFilled == False:
                rowFilled = False
                break 
        
        # remove-row
        if rowFilled: 
            for x in np.arange(0, GRID_WIDTH, CUBE_FACE):
                for cube_shape in cubeList: 
                    if (cube_shape.cube.y == y) and (cube_shape.cube.x in  np.arange(0, GRID_WIDTH, CUBE_FACE)): 
                        cubeList.remove(cube_shape)
                        LINEREMOVE_SOUND.play()

        # lower above rows
        if rowFilled: 
            for cube_in_list in cubeList:
                if cube_in_list.cube.y < y: 
                    cube_in_list.cube.y += CUBE_FACE



