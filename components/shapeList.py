


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


COL_NUM = 8 

# ------------------------------------- DRAW ----------------------------------------------
def drawList(shapesList):
    for shape in shapesList:
        pygame.draw.rect(WIN,BLACK,shape)


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
def addObject(object, shapeList):
    

    shape = object[0]   # only 1 cube within (need to generalize ....)

    create_new_shape = False  
    shape_face = WIN_WIDTH/COL_NUM
    
    # ADD TO shapeList
    if shape.y >= WIN_HEIGHT - shape_face:        # hit-bottom  
        COLLISION_SOUND.play()
        shape.y = WIN_HEIGHT - shape_face
        print (shape.y)
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
