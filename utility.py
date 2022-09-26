
import pygame 
import os 




# WINDOW 
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()


# COLORS 
WHITE = (255,255,255)
BLACK = (0,0,0)

# SOUNDS 
pygame.mixer.init()
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'tick.mp3'))
LINEREMOVE_SOUND = pygame.mixer.Sound(os.path.join('files/sounds','line_removal_2.wav'))


ROW_NUM = 12
COL_NUM = 8 
SHAPE_VEL = 6


# ------------------------------------ GRID -----------------------------------------
def createGrid():   # create grid 
    gridGui = []
    box_face = WIN_WIDTH/COL_NUM
    for row in range(ROW_NUM):
        for col in range(COL_NUM):
            x = col*box_face
            y = row*box_face
            box = pygame.Rect(x,y, box_face, box_face)
            box.topleft = (x,y)
            gridGui.append(box)
    return gridGui 
 
def drawGrid(grid):    # draw grid 
    for box in grid:
        pygame.draw.rect(WIN,BLACK,box,1)



# ------------------------------------ SHAPE -----------------------------------------
# CREATE 
def createNewShape():
    box_face = WIN_WIDTH/COL_NUM
    x = 0
    y = 0
    shape = pygame.Rect(x,y, box_face, box_face)
    return shape 



def moveShape(shape, key_pressed, keys, shapeList):

    shape_face = WIN_WIDTH/COL_NUM
    
    # movement 
    shape.y += SHAPE_VEL

    # check collision-right 
    no_collision_right = True 
    shape_temp = pygame.Rect(shape.x, shape.y, shape_face, shape_face)
    shape_temp.x += shape_face 
    for shape_ in shapeList:
        if shape_.colliderect(shape_temp):
            no_collision_right = False 

    # check collision-left 
    no_collision_left = True 
    shape_temp = pygame.Rect(shape.x, shape.y, shape_face, shape_face)
    shape_temp.x -= shape_face 
    for shape_ in shapeList:
        if shape_.colliderect(shape_temp):
            no_collision_left = False 

    # taking right/left 
    if (keys[pygame.K_RIGHT]) and (key_pressed == False) and (shape.x + shape_face < WIN_WIDTH) and (no_collision_right):
        shape.x += shape_face
        key_pressed = True 
    if keys[pygame.K_LEFT] and (key_pressed == False) and (shape.x > 0) and (no_collision_left): 
        shape.x -= shape_face
        key_pressed = True

    return key_pressed 



def addToShapeList(shape, shapeList):
    
    create_new_shape = False  
    shape_face = WIN_WIDTH/COL_NUM
    
    # ADD TO shapeList
    if shape.y >= WIN_HEIGHT - shape_face:        # hit-bottom  
        COLLISION_SOUND.play()
        shape.y = WIN_HEIGHT - shape_face
        shapeList.append(shape)
        create_new_shape = True
    else:                                         # collision (with other shapes)
        for shape_ in shapeList:
            if shape_.colliderect(shape):
                COLLISION_SOUND.play()
                shape.y = shape_.y - shape_face
                shapeList.append(shape)
                create_new_shape = True 
                break 

    return create_new_shape


# DRAW 
def drawShape(shape):
    pygame.draw.rect(WIN, BLACK, shape)


# ------------------------------------ shapeList -----------------------------------------

# DRAW 
def drawShapeList(shapesList):
    for shape in shapesList:
        pygame.draw.rect(WIN,BLACK,shape)


# CHECK ROWS 
def removeRowFromShapeList(shapeList):
    
    # STAGE-1 ; check rows 
    rowFilled = True
    y = 550
    for x in [0,50,100,150,200,250,300,350]:
        boxFilled = False
        for shape in shapeList: 
            print (shape.y)
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


    
