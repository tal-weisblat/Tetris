


'''
This file contain all game-settings plus the libraries necessary 
for the game. Almost each file in the app import from gameSetting. 
'''


import pygame 
import numpy as np
import time 
import random
import os


# WINDOW
WIN_WIDTH  = 100 * 7  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()

# GRID 
GRID_WIDTH  = 100 * 4  
GRID_HEIGHT = 100 * 6 
COL_NUM = 8  
ROW_NUM = 12 
CUBE_FACE = GRID_WIDTH/COL_NUM





# EVENTS 
GAMEOVER   = pygame.USEREVENT + 1 
ROWREMOVED = pygame.USEREVENT + 2 




# VELOCITY 
SHAPE_VEL = 2.5
SHAPE_FAST_VEL = 5



# SOUNDS 
pygame.mixer.init()
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('soundFiles', 'tick.mp3'))
LINEREMOVE_SOUND = pygame.mixer.Sound(os.path.join('soundFiles','line_removal.wav'))
GAMEOVER_SOUND   = pygame.mixer.Sound(os.path.join('soundFiles', 'game_over.wav'))



# COLORS 
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
MAROON = (128,0,0)
GREEN = (51,51,0)
GREY = (105,105,105)
CREEM = (254,251,234)
PINK = (255,204,209)


# FONTS 
TETRIS_FONT    = pygame.font.SysFont('comicsans', 60)   
NEXTSHAPE_FONT = pygame.font.SysFont('comicsans', 20)
LINESREMOVED   = pygame.font.SysFont('comicsans', 20)   
GAMEDURATION   = pygame.font.SysFont('comicsans', 20)   

# TEXTS
tetris_txt     = TETRIS_FONT.render('Tetris',1, BLACK)  
nextShape_txt  = NEXTSHAPE_FONT.render('Next shape:',1, BLACK)  
def numOfLines_txt(numRowsRemoved):
  return LINESREMOVED.render('Number of rows:  ' + str (numRowsRemoved), 1, BLACK)  
def gameDuration_txt(game_time_duration):
  return GAMEDURATION.render('Time: ' + str(game_time_duration), 1, BLACK)
gameOver_txt = TETRIS_FONT.render('Game over',1, BLACK)  




# CONSOLE-COORDINATES
GAP = 10 
CONSLOE_MIDDLE = GRID_WIDTH + (WIN_WIDTH - GRID_WIDTH)/2  - tetris_txt.get_width()/2
CONSOLE_LEFT   = GRID_WIDTH
(tetris_txt_x, tetris_txt_y)             = (CONSLOE_MIDDLE,        1*GAP)     # title 
(nextShape_txt_x, nextShape_txt_y)       = (CONSOLE_LEFT + 2*GAP, 16*GAP)     # next-shape title 
(drawNextShape_x, drawNextShape_y)       = (CONSOLE_LEFT        , 24*GAP)     # draw next-shap
(gameDuration_txt_x, gameDuration_txt_y) = (CONSOLE_LEFT + 2*GAP, 38*GAP)     # time elapsed
(numOfLines_txt_x, numOfLines_txt_y)     = (CONSOLE_LEFT + 2*GAP, 41*GAP)     # number of lines removed 

# GAME-OVER COORDINATES 
GAME_OVER_SCREEN_MID_WIDTH  = GRID_WIDTH/2 - gameOver_txt.get_width()/2
(gameOver_txt_x, gameOver_txt_y) = (GAME_OVER_SCREEN_MID_WIDTH, 10*GAP) 