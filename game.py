


import pygame 


from utility import createGridGui
from utility import drawGrid
from utility import createShape
from utility import handleShape 
from utility import drawShape


# COLORS 
WHITE = (255,255,255)
BLACK = (0,0,0)

# WINDOW 
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()




        




ROW_NUM = 12
COL_NUM = 8 





# shapeList
def drawShapeList(shapesList):
    for shape in shapesList:
        pygame.draw.rect(WIN,BLACK,shape)





def game():
    
    run = True 
    clock = pygame.time.Clock()
    gridGui = createGridGui()
    shape = createShape()
    shapeList = [] 
    key_pressed = False 
    create_new_shape = False 

    while run: 

        clock.tick(60)


        # EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False 
                break
            

        if create_new_shape == True:
            
            create_new_shape = False 
            box_face = WIN_WIDTH/COL_NUM
            x = 0
            y = 0
            shape = pygame.Rect(x,y, box_face, box_face)
            print (shape.y)
                    
            



        # HANDLE-SHAPES   
        keys = pygame.key.get_pressed()
        key_pressed, create_new_shape = handleShape(shape, key_pressed, create_new_shape, keys, shapeList)        
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False




        
        
        # DRAW 
        WIN.fill(WHITE)
        drawGrid(gridGui)
        drawShapeList(shapeList)
        drawShapeList(shapeList)
        drawShape(shape)
        pygame.display.update()


game()



