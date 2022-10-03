

from gameSettings import * 
from classCube import cube


# ------------------------------------- DRAW ----------------------------------------------
def drawCubeList(cubeList):
    for cube_shape in cubeList:
        pygame.draw.rect(WIN, cube_shape.color, cube_shape.list[0])        


# ------------------------------------- ADD -----------------------------------------------
def addCube(cubeList, cube_shape):
    
    create_new_shape = False  

    # hit bottom
    if cube_shape.list[0].y  >= WIN_HEIGHT - CUBE_FACE:    
        
        delta = WIN_HEIGHT - (cube_shape.list[0].y + CUBE_FACE)     # adjust cube 
        cube_shape.list[0].y += delta
        
        print(cube_shape.list[0].x, cube_shape.list[0].y)


        cubeList.append(cube_shape)        
        create_new_shape = True
        COLLISION_SOUND.play()
        
    else: 
        for cube_in_list in cubeList:
            if cube_in_list.list[0].colliderect(cube_shape.list[0]):
                cube_shape.list[0].y = cube_in_list.list[0].y - CUBE_FACE 
                cubeList.append(cube_shape)
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
            for cube_shape in cubeList: 
                if cube_shape.list[0].x == x and cube_shape.list[0].y == y:
                    boxFilled = True 
                    break

            if boxFilled == False:
                rowFilled = False
                break 
        
        # remove-row
        if rowFilled: 
            for x in np.arange(0, WIN_WIDTH, CUBE_FACE):
                for cube_shape in cubeList: 
                    if (cube_shape.list[0].y == y) and (cube_shape.list[0].x in  np.arange(0, WIN_WIDTH, CUBE_FACE)): 
                        cubeList.remove(cube_shape)
                        LINEREMOVE_SOUND.play()

        # lower above rows
        if rowFilled: 
            for cube_in_list in cubeList:
                if cube_in_list.list[0].y < y: 
                    cube_in_list.list[0].y += CUBE_FACE



