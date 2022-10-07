


from gameSettings import *
import random



from grid import createGrid, drawGrid    
from cubeList import addCube, drawCubeList, removeRows
from classCubeShape import CubeShape
from classLshape import Lshape
from classLineShape import LineShape
from classShortLineShape import ShortLineShape
from classFatCubeShape import FatCubeShape


def draw(grid, new_shape, cubeList):
    WIN.fill(CREEM)
    WIN.blit ( tetris_txt, (tetris_txt_x,tetris_txt_y))
    drawGrid(grid)
    new_shape.drawShape()
    drawCubeList(cubeList)        
    pygame.display.update()


def p_button_pressed(keys, pause_game, K_p_pressed):

    if (keys[pygame.K_p] == True) and (K_p_pressed == False): 
        K_p_pressed = True 
        if pause_game == False : 
            pause_game = True 
        else: 
            pause_game = False  
    if (keys[pygame.K_p] == False): K_p_pressed = False

    return pause_game, K_p_pressed



def game():
    
    new_shape = FatCubeShape(GREY)
    cubeList = []
    grid = createGrid()
    clock = pygame.time.Clock()
    key_pressed = False 
    create_new_shape = False 
    space_pressed = False 
    K_p_pressed = False 
    game_over = False 
    pause_game = False 
    run = True 


    while run: 

        clock.tick(60)

        # events 
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False 
                break
            
            if event.type == GAMEOVER:
                game_over = True 
                break

            

        # new-shape  
        if create_new_shape == True:
            create_new_shape = False 
            new_shape =random.choice([Lshape(BLACK),
                                      CubeShape(RED),
                                      LineShape(MAROON),
                                      ShortLineShape(GREEN), 
                                      FatCubeShape(GREY)]) 
    

        keys = pygame.key.get_pressed()

        # pause-game 
        pause_game, K_p_pressed = p_button_pressed(keys, pause_game, K_p_pressed)
        if pause_game:         
            draw(grid, new_shape, cubeList)
            continue 

        # move-downwards 
        key_pressed = new_shape.moveShape(keys, key_pressed, cubeList)   # move 
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False
        
        # rotate 
        space_pressed = new_shape.rotate(keys, space_pressed)
        if (keys[pygame.K_SPACE] == False): space_pressed = False

        
        # add cubes to cubeList
        create_new_shape = addCube(cubeList, new_shape)

        # remove row 
        removeRows(cubeList)

        # game-over 
        if game_over: 
            print ('GAME OVER')

        # draw 
        draw(grid, new_shape, cubeList)

game()



