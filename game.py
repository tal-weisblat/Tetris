


from gameSettings import *


from gameObjects.grid import createGrid, drawGrid    
from gameObjects.cubeList import addCube, drawCubeList, removeRows

from gameShapes.classCubeShape import CubeShape
from gameShapes.classLshape import Lshape
from gameShapes.classLineShape import LineShape
from gameShapes.classShortLineShape import ShortLineShape
from gameShapes.classFatCubeShape import FatCubeShape




def drawConsoleNextShape(next_shape):

    # duplicate 
    next_shape_temp = [] 
    for cube in next_shape.listOfCubes:
        cube_temp = pygame.Rect(cube.x, cube.y, CUBE_FACE, CUBE_FACE)    
        next_shape_temp.append(cube_temp)
    color = next_shape.color
    
    # set on screen 
    for cube_temp in next_shape_temp:
        cube_temp.x += drawNextShape_x
        cube_temp.y += drawNextShape_y

    # draw
    for cube_temp in next_shape_temp:
        pygame.draw.rect(WIN, color, cube_temp)


def drawGameOver(numRowsRemoved, entire_game_time):
    WIN.fill(CREEM)
    WIN.blit(tetris_txt, (tetris_txt_x,tetris_txt_y))
    WIN.blit(nextShape_txt, (nextShape_txt_x,nextShape_txt_y))
    WIN.blit(numOfLines_txt(numRowsRemoved), (numOfLines_txt_x, numOfLines_txt_y))
    WIN.blit(gameDuration_txt(entire_game_time), (gameDuration_txt_x, gameDuration_txt_y))
    gameOverBackround = pygame.Rect(0, 0, GRID_WIDTH, GRID_HEIGHT)
    pygame.draw.rect(WIN, PINK, gameOverBackround)
    WIN.blit(gameOver_txt, (gameOver_txt_x,gameOver_txt_y))
    pygame.display.update()

    


def draw(grid, new_shape, cubeList, next_shape, numRowsRemoved, game_time_duration):
    WIN.fill(CREEM)
    WIN.blit(tetris_txt, (tetris_txt_x,tetris_txt_y))
    WIN.blit(nextShape_txt, (nextShape_txt_x,nextShape_txt_y))
    WIN.blit(numOfLines_txt(numRowsRemoved), (numOfLines_txt_x, numOfLines_txt_y))
    WIN.blit(gameDuration_txt(game_time_duration), (gameDuration_txt_x, gameDuration_txt_y))
    drawConsoleNextShape(next_shape)
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
    
    next_shape = FatCubeShape(GREY)
    cubeList = []
    grid = createGrid()
    clock = pygame.time.Clock()
    time_start = time.time()            # 

    numRowsRemoved = 0 
    fix_time = True 
    key_pressed = False 
    create_new_shape = True 
    space_pressed = False 
    K_p_pressed = False 
    game_over = False 
    pause_game = False 
    run = True 

    while run: 

        clock.tick(60)
        game_time = int(time.time() - time_start)


        # events 
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False 
                break
            
            if event.type == GAMEOVER:
                GAMEOVER_SOUND.play()
                game_over = True 
                break

            if event.type == ROWREMOVED: 
                numRowsRemoved += 1 
                

        # game-over 
        if game_over:
            if fix_time: 
                entire_game_time = game_time
                fix_time = False
            drawGameOver(numRowsRemoved, entire_game_time)
            continue
         

        # new & next shapes  
        if create_new_shape == True:
            create_new_shape = False
            new_shape  = next_shape
            next_shape = random.choice([Lshape(BLACK),
                                        CubeShape(RED),
                                        LineShape(MAROON),
                                        ShortLineShape(GREEN), 
                                        FatCubeShape(GREY)])  
    


        drawConsoleNextShape(next_shape)

        keys = pygame.key.get_pressed()


        # pause-game 
        pause_game, K_p_pressed = p_button_pressed(keys, pause_game, K_p_pressed)
        if pause_game:      
            draw(grid, new_shape, cubeList, next_shape, numRowsRemoved, game_time)
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

        

        # draw 
        draw(grid, new_shape, cubeList, next_shape, numRowsRemoved, game_time)

game()



