

from gameSettings import * 



# ------------------------------------- DRAW ----------------------------------------------
def drawList(boxList):
    for box in boxList:
        pygame.draw.rect(WIN,BLACK,box)


# ------------------------------------- REMOVE ----------------------------------------------
def removeRow(boxList):
    
    for y in np.arange(0, WIN_HEIGHT, CUBE_FACE):
        
        # CHECK ROW 
        rowFilled = True
        for x in np.arange(0, WIN_WIDTH, CUBE_FACE):
            boxFilled = False
            for box in boxList: 
                if box.x == x and box.y == y:
                    boxFilled = True 
                    break

            if boxFilled == False:
                rowFilled = False
                break 
        
        # REMOVE ROW 
        if rowFilled: 
            for x in np.arange(0, WIN_WIDTH, CUBE_FACE):
                for box in boxList: 
                    if (box.y == y) and (box.x in  np.arange(0, WIN_WIDTH, CUBE_FACE)): 
                        boxList.remove(box)
                        LINEREMOVE_SOUND.play()

        # LOWER (ABOVE) ROWS 
        if rowFilled: 
            for box in boxList:
                if box.y < y: 
                    box.y += CUBE_FACE





# ------------------------------------- ADD ---------------------------------------------- 
def addObject(object, boxList):
    
    max_y = max(box.y for box in object)
    create_new_shape = False  

    
    # ADD (hit-bottom)
    if max_y >= WIN_HEIGHT - CUBE_FACE:        
        
        delta = WIN_HEIGHT - (max_y + CUBE_FACE)     # adjust boxes in object 
        for box in object: box.y += delta
        for box in object: boxList.append(box)        # add boxes to boxList
        COLLISION_SOUND.play()
        create_new_shape = True
    
    # ADD (collided with boxes)
    else:                     
        
        for box in object:
            
            collision = False 
            for box_ in boxList: 

                if box.colliderect(box_):
                
                    delta = box_.y - (box.y + CUBE_FACE)      # adjusting boxes in object 
                    for box in object: box.y += delta
                    for box in object: boxList.append(box)     # adding boxes to boxList
                    COLLISION_SOUND.play()
                    create_new_shape = True 
                    collision = True 
                    break 

            if collision: break
                

    return create_new_shape
