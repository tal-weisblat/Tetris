


from game_settings import * 


# ------------------------------------ NEXT-SHAPE ----------------------------------------------
def draw_console_next_shape(next_shape):

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


# ------------------------------------ GAME-OVER ----------------------------------------------
def draw_game_over(numRowsRemoved, entire_game_time):
    WIN.fill(CREEM)
    WIN.blit(tetris_txt, (tetris_txt_x,tetris_txt_y))
    WIN.blit(nextShape_txt, (nextShape_txt_x,nextShape_txt_y))
    WIN.blit(numOfLines_txt(numRowsRemoved), (numOfLines_txt_x, numOfLines_txt_y))
    WIN.blit(gameDuration_txt(entire_game_time), (gameDuration_txt_x, gameDuration_txt_y))
    gameOverBackround = pygame.Rect(0, 0, GRID_WIDTH, GRID_HEIGHT)
    pygame.draw.rect(WIN, PINK, gameOverBackround)
    WIN.blit(gameOver_txt, (gameOver_txt_x,gameOver_txt_y))
    pygame.display.update()


# ------------------------------------ GAME ----------------------------------------------

from src.entities.grid import create_grid, draw_grid
from src.entities.cube_list import draw_cube_list
def draw_game(grid, new_shape, cubeList, next_shape, numRowsRemoved, game_time_duration):
    WIN.fill(CREEM)
    WIN.blit(tetris_txt, (tetris_txt_x,tetris_txt_y))
    WIN.blit(nextShape_txt, (nextShape_txt_x,nextShape_txt_y))
    WIN.blit(numOfLines_txt(numRowsRemoved), (numOfLines_txt_x, numOfLines_txt_y))
    WIN.blit(gameDuration_txt(game_time_duration), (gameDuration_txt_x, gameDuration_txt_y))
    draw_console_next_shape(next_shape)
    draw_grid(grid)
    new_shape.drawShape()
    draw_cube_list(cubeList)        
    pygame.display.update()
