
import pygame 





WIN_WIDTH  = 100 * 4 
COL_NUM = 8  
box_face = WIN_WIDTH/COL_NUM




# CREATE OBJECT 
def L_create():
    L_object = []
    shape_1 = pygame.Rect(0,0, box_face, box_face)
    shape_2 = pygame.Rect(0,50, box_face, box_face)
    shape_3 = pygame.Rect(50,0, box_face, box_face)
    shape_4 = pygame.Rect(100,0, box_face, box_face)
    L_object.append(shape_1)
    L_object.append(shape_2)
    L_object.append(shape_3)
    L_object.append(shape_4)

    return L_object



# ROTATE 
def L_rotate(keys, space_pressed, complex_object):
    
    if keys[pygame.K_SPACE] and (space_pressed == False):    
        space_pressed = True 

        # SWITCH (to next phase)
        x1 = complex_object[0].x
        x2 = complex_object[1].x
        x3 = complex_object[2].x
        x4 = complex_object[3].x
        min_x = min(x1,x2,x3,x4)

        if x1-min_x == 0 and x2-min_x == 0 and x3-min_x == 50 and x4-min_x == 100:  
            x1, x2, x3, x4 = 0, 50, 50, 50 
            y1, y2, y3, y4 = 0, 0, 50, 100 
        elif x1-min_x == 0 and x2-min_x == 50 and x3-min_x == 50 and x4-min_x == 50:  
            x1, x2, x3, x4 = 100, 100, 50, 0
            y1, y2, y3, y4 = 0, 50, 50, 50 
        elif x1-min_x == 100 and x2-min_x == 100 and x3-min_x == 50 and x4-min_x == 0:  
            x1, x2, x3, x4 = 0, 0, 0, 50 
            y1, y2, y3, y4 = 0, 50, 100, 100   
        elif x1-min_x == 0 and x2-min_x == 0 and x3-min_x == 0 and x4-min_x == 50:  
            x1, x2, x3, x4 = 0, 0, 50, 100
            y1, y2, y3, y4 = 0, 50, 0, 0 
        
        # inner boxes 
        y = complex_object[0].y
        shape_1 = pygame.Rect(x1+min_x, y1+y, box_face, box_face)
        shape_2 = pygame.Rect(x2+min_x, y2+y, box_face, box_face)
        shape_3 = pygame.Rect(x3+min_x, y3+y, box_face, box_face)
        shape_4 = pygame.Rect(x4+min_x, y4+y, box_face, box_face)

        # complex object (the union of boxes)
        complex_object.clear()
        complex_object.append(shape_1)
        complex_object.append(shape_2)
        complex_object.append(shape_3)
        complex_object.append(shape_4)

    return space_pressed

