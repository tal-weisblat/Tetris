
import pygame 


# WINDOW 
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()

COL_NUM = 8
SHAPE_VEL = 4



# MOVE 
def moveObject(keys, key_pressed, object, objectList):
    
    # move downwards 
    for box in object:
        box.y += SHAPE_VEL


    # restrictions (left & rigth)
    shape_face = WIN_WIDTH/COL_NUM
    max_x = max(box.x for box in object)
    min_x = min(box.x for box in object)


    # restrictions (regarding objects in objectList)
    # right 
    object_temp = [] 
    no_collision_right = True 
    for box in object: 
        box_temp = pygame.Rect(box.x, box.y, shape_face, shape_face)
        box_temp.x += shape_face
        object_temp.append(box_temp)

    for box in objectList:
        for box_temp in object_temp: 
            if box.colliderect(box_temp):
                no_collision_right = False 
    # left 
    object_temp = [] 
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
