

import pygame 
import numpy as np
import os


# WINDOWS
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()

# COLORS 
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)

# GRID
COL_NUM = 8  
ROW_NUM = 12 
CUBE_FACE = WIN_WIDTH/COL_NUM

# VELOCITY 
SHAPE_VEL = 6

# SOUNDS 
pygame.mixer.init()
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'tick.mp3'))
LINEREMOVE_SOUND = pygame.mixer.Sound(os.path.join('files/sounds','line_removal_2.wav'))
