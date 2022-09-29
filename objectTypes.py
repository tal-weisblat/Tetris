





from gameSettings import * 


# -------------------------------------------- CREATE -------------------------------------------- 
def cube_create():
    cube_object = []
    x = 1*BOX_FACE            # make it random ? 
    y = 0
    box = pygame.Rect(x,y, BOX_FACE, BOX_FACE)
    cube_object.append(box)
    return cube_object 




# ---------------------------------------------- L-shape (create) -----------------------------------------------


class L_object():

    def __init__ (self, color):

        self.object = []
        shape_1 = pygame.Rect(0,0, BOX_FACE, BOX_FACE)
        shape_2 = pygame.Rect(0,50, BOX_FACE, BOX_FACE)
        shape_3 = pygame.Rect(50,0, BOX_FACE, BOX_FACE)
        shape_4 = pygame.Rect(100,0, BOX_FACE, BOX_FACE)
        self.object.append(shape_1)
        self.object.append(shape_2)
        self.object.append(shape_3)
        self.object.append(shape_4)

        self.color = color 

    


def L_create():
    L_object = []
    shape_1 = pygame.Rect(0,0, BOX_FACE, BOX_FACE)
    shape_2 = pygame.Rect(0,50, BOX_FACE, BOX_FACE)
    shape_3 = pygame.Rect(50,0, BOX_FACE, BOX_FACE)
    shape_4 = pygame.Rect(100,0, BOX_FACE, BOX_FACE)
    L_object.append(shape_1)
    L_object.append(shape_2)
    L_object.append(shape_3)
    L_object.append(shape_4)
    return L_object

# ---------------------------------------------- L-shape (rotate) -----------------------------------------------
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
        shape_1 = pygame.Rect(x1+min_x, y1+y, BOX_FACE, BOX_FACE)
        shape_2 = pygame.Rect(x2+min_x, y2+y, BOX_FACE, BOX_FACE)
        shape_3 = pygame.Rect(x3+min_x, y3+y, BOX_FACE, BOX_FACE)
        shape_4 = pygame.Rect(x4+min_x, y4+y, BOX_FACE, BOX_FACE)

        # complex object (the union of boxes)
        complex_object.clear()
        complex_object.append(shape_1)
        complex_object.append(shape_2)
        complex_object.append(shape_3)
        complex_object.append(shape_4)

    return space_pressed

