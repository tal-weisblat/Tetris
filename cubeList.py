

from gameSettings import * 
from classCube import Cube


# ------------------------------------- DRAW ----------------------------------------------
def drawCubeList(cubeList):
    for shape in cubeList:
        pygame.draw.rect(WIN, shape.color, shape.cube)        


# ------------------------------------- ADD -----------------------------------------------
def addCube(cubeList, new_shape):
    
    create_new_shape = False  


    # max_y = .... 

    # hit bottom
    if new_shape.listOfCubes[0].y  >= WIN_HEIGHT - CUBE_FACE:    
        
        delta = WIN_HEIGHT - (new_shape.listOfCubes[0].y + CUBE_FACE)     # adjust cube 
        new_shape.listOfCubes[0].y += delta          # MODIFY : adjusting ALL cubes within new_shape 
        
        # ADD all cubes to cubeList 
        for cube in new_shape.listOfCubes:
            temp_cube = Cube(cube.x, cube.y, new_shape.color)
            cubeList.append(temp_cube) 
        
        create_new_shape = True
        COLLISION_SOUND.play()
        
    else: 
        for shape in cubeList:
            
            if shape.cube.colliderect(new_shape.listOfCubes[0]):
                
                new_shape.listOfCubes[0].y = shape.cube.y - CUBE_FACE  # MODIFY : adjusting ALL cubes within new_shape 
        
                # ADD all cubes to cubeList
                for cube in new_shape.listOfCubes:
                    temp_cube = Cube(cube.x, cube.y, new_shape.color)
                    cubeList.append(temp_cube)
                
                create_new_shape = True
                COLLISION_SOUND.play()
                break
    
    return create_new_shape





# ------------------------------------- REMOVE-ROW -------------------------------------------
def removeRows(cubeList): 
    for y in np.arange(0, WIN_HEIGHT, CUBE_FACE):
        
        # check row 
        rowFilled = True
        for x in np.arange(0, WIN_WIDTH, CUBE_FACE):
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
            for x in np.arange(0, WIN_WIDTH, CUBE_FACE):
                for cube_shape in cubeList: 
                    if (cube_shape.cube.y == y) and (cube_shape.cube.x in  np.arange(0, WIN_WIDTH, CUBE_FACE)): 
                        cubeList.remove(cube_shape)
                        LINEREMOVE_SOUND.play()

        # lower above rows
        if rowFilled: 
            for cube_in_list in cubeList:
                if cube_in_list.cube.y < y: 
                    cube_in_list.cube.y += CUBE_FACE



