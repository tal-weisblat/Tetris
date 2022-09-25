


import pygame 





# COLORS 
WHITE = (255,255,255)
BLACK = (0,0,0)

# WINDOW 
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()




# GRID 
ROW_NUM = 12
COL_NUM = 8 

def createGridBoard():
    
    gridBoard = [] 
    for row in range(ROW_NUM):
       gridBoard.append([0 for col in range(COL_NUM)])

    return gridBoard

def createGridGui():
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


# DRAW GRID 
def drawGrid(grid):
    for box in grid:
        pygame.draw.rect(WIN,BLACK,box,1)



# CREATE SHAPE
def createShape():
    box_face = WIN_WIDTH/COL_NUM
    x = 3 * box_face
    y = 0
    shape = pygame.Rect(x,y, box_face, box_face)
    return shape

# SHAPE MOVE 
SHAPE_VEL = 2
def shapeMove(shape, key_pressed, keys):

    shape_face = WIN_WIDTH/COL_NUM
    shape.y += SHAPE_VEL
    if (keys[pygame.K_RIGHT]) and (key_pressed == False):
        shape.x += shape_face
        key_pressed = True 
    if keys[pygame.K_LEFT] and (key_pressed == False):
        shape.x -= shape_face
        key_pressed = True

    #if shape.y >= WIN_HEIGHT - shape_face:

    
    return key_pressed 

    
# DRAW SHPAE 
def shapeDraw(shape):
    pygame.draw.rect(WIN, BLACK, shape)




def game():
    
    run = True 
    clock = pygame.time.Clock()
    gridGui = createGridGui()
    gridBoard = createGridBoard()
    shape = createShape()
    key_pressed = False 
    

    while run: 

        clock.tick(60)


        # EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False 
                break
            

        # SHAPE MOVE  
        keys = pygame.key.get_pressed()
        key_pressed = shapeMove(shape, key_pressed, keys)        
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False):  
            key_pressed = False


        # COLLISION 

        
        
        # DRAW 
        WIN.fill(WHITE)
        drawGrid(gridGui)
        shapeDraw(shape)
        pygame.display.update()


game()



