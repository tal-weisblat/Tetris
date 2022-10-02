

from gameSettings import * 
from cubeClass import cube


# ------------------------------------- DRAW ----------------------------------------------
def drawCubeList(cubeList):
    for cube in cubeList:
        pygame.draw.rect(WIN, cube.color, cube.cube)        

# ------------------------------------- ADD -----------------------------------------------
def addCube(cubeList, cube_new):
    
    create_new_shape = False  

    # hit bottom
    if cube_new.cube.y  >= WIN_HEIGHT - CUBE_FACE:    
        
        delta = WIN_HEIGHT - (cube_new.cube.y + CUBE_FACE)     # adjust cube 
        cube_new.cube.y += delta
        
        cubeList.append(cube_new)        
        create_new_shape = True
        COLLISION_SOUND.play()
    else: 
        for cube in cubeList:
            if cube.cube.colliderect(cube_new.cube):
                cube_new.cube.y = cube.cube.y - CUBE_FACE 
                cubeList.append(cube_new)
                create_new_shape = True
                COLLISION_SOUND.play()
                break
    
    return create_new_shape



# ------------------------------------- REMOVE-ROW -------------------------------------------
    
def removeRow(cubeList): 
    for y in np.arange(0, WIN_HEIGHT, CUBE_FACE):
        
        # check row 
        rowFilled = True
        for x in np.arange(0, WIN_WIDTH, CUBE_FACE):
            boxFilled = False
            for cube in cubeList: 
                if cube.cube.x == x and cube.cube.y == y:
                    boxFilled = True 
                    break

            if boxFilled == False:
                rowFilled = False
                break 
        
        # remove-row
        if rowFilled: 
            for x in np.arange(0, WIN_WIDTH, CUBE_FACE):
                for cube in cubeList: 
                    if (cube.cube.y == y) and (cube.cube.x in  np.arange(0, WIN_WIDTH, CUBE_FACE)): 
                        cubeList.remove(cube)
                        LINEREMOVE_SOUND.play()

        # lower above rows
        if rowFilled: 
            for cube in cubeList:
                if cube.cube.y < y: 
                    cube.cube.y += CUBE_FACE



