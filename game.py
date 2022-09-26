


import pygame 


from utility import createGridGui
from utility import drawGrid
from utility import createNewShape
from utility import shapeMove 
from utility import drawShape
from utility import addToShapeList



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




# CHECK 1st ROW  
def CheckShapeListRows(shapeList):
    

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
        #print ('remove row')
        y = 550
        for x in [0,50,100,150,200,250,300,350]:
            for shape in shapeList: 
                if (shape.y == y and 
                   (shape.x == 0 or shape.x == 50 or shape.x == 100 or shape.x == 150 or 
                    shape.x == 200 or shape.x == 250 or shape.x == 300 or 
                    shape.x == 350 )):
                    shapeList.remove(shape)



    # STAGE-3 ; lower all rows above 
    if rowFilled: 
        for shape in shapeList: 
            shape.y += 50




    



def game():
    
    run = True 
    shapeList = []
    clock = pygame.time.Clock()
    gridGui = createGridGui()
    shape = createNewShape() 
    key_pressed = False 
    create_new_shape = False 

    while run: 

        clock.tick(60)


        # EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False 
                break
            

        # CHECK ROWS
        CheckShapeListRows(shapeList) 


        # NEW-SHAPE 
        if create_new_shape == True:
            create_new_shape = False 
            shape = createNewShape()
            

        # HANDLE-SHAPES   
        keys = pygame.key.get_pressed()
        key_pressed = shapeMove(shape, key_pressed, keys, shapeList)    
        create_new_shape = addToShapeList(shape, shapeList)    
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False


        # DRAW 
        WIN.fill(WHITE)
        drawGrid(gridGui)
        drawShapeList(shapeList)
        drawShapeList(shapeList)
        drawShape(shape)
        pygame.display.update()


game()



