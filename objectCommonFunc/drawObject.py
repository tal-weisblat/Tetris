


import pygame 


# WINDOW 
WIN_WIDTH  = 100 * 4  
WIN_HEIGHT = 100 * 6 
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tetris')
pygame.init()

# COLORS 
BLACK = (0,0,0)



# DRAW 
def draw(object):
    for box in object:
        pygame.draw.rect(WIN, BLACK, box)
