

import pygame 
import numpy as np
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



# COLORS 
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
MAROON = (128,0,0)
GREEN = (51,51,0)
GREY = (105,105,105)
CREEM = (254,251,234)

# GRID
COL_NUM = 8  
ROW_NUM = 12 
CUBE_FACE = GRID_WIDTH/COL_NUM

# VELOCITY 
SHAPE_VEL = 2.5
SHAPE_FAST_VEL = 5

# SOUNDS 
pygame.mixer.init()
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'tick.mp3'))
LINEREMOVE_SOUND = pygame.mixer.Sound(os.path.join('files/sounds','line_removal_2.wav'))

# EVENTS 
GAMEOVER   = pygame.USEREVENT + 1 
ROWREMOVED = pygame.USEREVENT + 2 


# FONTS 
TETRIS_FONT    = pygame.font.SysFont('comicsans', 60)   
NEXTSHAPE_FONT = pygame.font.SysFont('comicsans', 20)
LINESREMOVED   = pygame.font.SysFont('comicsans', 20)   


# TEXTS
tetris_txt     = TETRIS_FONT.render('Tetris',1, BLACK)  
nextShape_txt  = NEXTSHAPE_FONT.render('Next shape:',1, BLACK)  
def numOfLines_txt(numRowsRemoved):
  return LINESREMOVED.render('Number of rows:  ' + str (numRowsRemoved), 1, BLACK)  

# COORDINATES
GAP = 10 
MIDDLE = GRID_WIDTH + (WIN_WIDTH - GRID_WIDTH)/2  - tetris_txt.get_width()/2
LEFT   = GRID_WIDTH
(tetris_txt_x, tetris_txt_y)         = (MIDDLE      , 1*GAP)
(nextShape_txt_x, nextShape_txt_y)   = (LEFT + 2*GAP, 15*GAP) 
(drawNextShape_x, drawNextShape_y)   = (LEFT        , 23*GAP)
(numOfLines_txt_x, numOfLines_txt_y) = (LEFT + 2*GAP, 36*GAP) 