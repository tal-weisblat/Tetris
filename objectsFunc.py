


from gameSettings import * 



# ---------------------------------------- DRAW -------------------------------------------
def drawObject(object):
    for box in object:
        pygame.draw.rect(WIN, BLACK, box)


# ---------------------------------------- MOVE -------------------------------------------- 
def moveObject(keys, key_pressed, object, objectList):
    
    # move downwards 
    for box in object:
        box.y += SHAPE_VEL

    # restrictions (left & rigth)
    shape_face = WIN_WIDTH/COL_NUM
    max_x = max(box.x for box in object)
    min_x = min(box.x for box in object)

    # restrictions (regarding objects in objectList)
    object_temp = []                              # right 
    no_collision_right = True 
    for box in object: 
        box_temp = pygame.Rect(box.x, box.y, shape_face, shape_face)
        box_temp.x += shape_face
        object_temp.append(box_temp)

    for box in objectList:
        for box_temp in object_temp: 
            if box.colliderect(box_temp):
                no_collision_right = False 
    
    object_temp = []                               # left 
    no_collision_left = True 
    for box in object: 
        box_temp = pygame.Rect(box.x, box.y, shape_face, shape_face)
        box_temp.x -= shape_face
        object_temp.append(box_temp)

    for box in objectList:
        for box_temp in object_temp: 
            if box.colliderect(box_temp):
                no_collision_left = False
                
    # move left & right 
    if (keys[pygame.K_RIGHT]) and (key_pressed == False) and (max_x + shape_face < WIN_WIDTH) and (no_collision_right):
        key_pressed = True 
        for box in object: 
            box.x += 50
    if keys[pygame.K_LEFT] and (key_pressed == False) and (min_x > 0) and (no_collision_left): 
        key_pressed = True 
        for box in object: 
            box.x -= 50
        
    return key_pressed
