

from gameSettings import * 



# ------------------------------------- DRAW ----------------------------------------------
def drawList(boxList):
    for box in boxList:
        pygame.draw.rect(WIN,BLACK,box)


# ------------------------------------- REMOVE ----------------------------------------------
def removeRow(shapeList):
    
    # STAGE-1 ; check rows 
    rowFilled = True
    y = 550
    for x in [0,50,100,150,200,250,300,350]:
        boxFilled = False
        for shape in shapeList: 
            #print (shape.y)
            if shape.x == x and shape.y == y :
                boxFilled = True 
                break

        if boxFilled == False :
            rowFilled = False
            break 
        
    # STAGE-2 ; erase rows 
    if rowFilled: 
        y = 550
        for x in [0,50,100,150,200,250,300,350]:
            for shape in shapeList: 
                if (shape.y == y and 
                   (shape.x == 0 or shape.x == 50 or shape.x == 100 or shape.x == 150 or 
                    shape.x == 200 or shape.x == 250 or shape.x == 300 or 
                    shape.x == 350 )):
                    LINEREMOVE_SOUND.play()
                    shapeList.remove(shape)

    # STAGE-3 ; lower all rows above 
    if rowFilled: 
        for shape in shapeList: 
            shape.y += 50





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
