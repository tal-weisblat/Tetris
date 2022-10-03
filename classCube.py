
from gameSettings import * 



class Cube():
    
    def __init__(self, x, y, color):
        self.cube = pygame.Rect(x, y, CUBE_FACE, CUBE_FACE)
        self.color = color 
        
    def draw(self):
        pygame.draw.rect(WIN, self.color, self.cube)



