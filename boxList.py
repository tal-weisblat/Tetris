

from gameSettings import * 



# ------------------------------------- DRAW ----------------------------------------------
def drawList(boxList):
    for box in boxList:
        pygame.draw.rect(WIN,BLACK,box)


# ------------------------------------- REMOVE ----------------------------------------------
def removeRow(boxList):
    
    for y in np.arange(0, WIN_HEIGHT, BOX_FACE):
        
        # CHECK ROW 
        rowFilled = True
        for x in np.arange(0, WIN_WIDTH, BOX_FACE):
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
            for x in np.arange(0, WIN_WIDTH, BOX_FACE):
                for box in boxList: 
                    if (box.y == y) and (box.x in  np.arange(0, WIN_WIDTH, BOX_FACE)): 
                        boxList.remove(box)
                        LINEREMOVE_SOUND.play()

        # LOWER (ABOVE) ROWS 
        if rowFilled: 
            for box in boxList:
                if box.y < y: 
                    box.y += BOX_FACE





# ------------------------------------- ADD ---------------------------------------------- 
def addObject(object, boxList):
    

    max_y = max(box.y for box in object)


    create_new_shape = False  
    shape_face = WIN_WIDTH/COL_NUM
    
    # ADD (hit-bottom)
    if max_y >= WIN_HEIGHT - shape_face:        
        
        delta = WIN_HEIGHT - (max_y + shape_face)     # adjust boxes in object 
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
                
                    delta = box_.y - (box.y + shape_face)      # adjusting boxes in object 
                    for box in object: box.y += delta
                    for box in object: boxList.append(box)     # adding boxes to boxList
                    COLLISION_SOUND.play()
                    create_new_shape = True 
                    collision = True 
                    break 

            if collision: break
                

    return create_new_shape
