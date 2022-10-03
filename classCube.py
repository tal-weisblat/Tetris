
from gameSettings import * 



class cube():
    
    def __init__(self, color):
        self.x = 1*CUBE_FACE            # make it random ? 
        self.y = 0
        self.cube = pygame.Rect(self.x, self.y, CUBE_FACE, CUBE_FACE)
        self.color = color 
        
    def draw(self):
        pygame.draw.rect(WIN, self.color, self.cube)

    def moveCube(self, keys, key_pressed, cubeList):
        
        BOX_FACE = WIN_WIDTH/COL_NUM

        # downwards
        self.cube.y += SHAPE_VEL
        
        # right collision with cubeList
        right_collision = False  
        cube_temp = pygame.Rect(self.cube.x, self.cube.y, CUBE_FACE, CUBE_FACE)
        cube_temp.x += BOX_FACE
        for cube in cubeList:
            if cube.cube.colliderect(cube_temp):
                right_collision = True  

        # left collision with cubeList
        left_collision = False  
        cube_temp = pygame.Rect(self.cube.x, self.cube.y, CUBE_FACE, CUBE_FACE)
        cube_temp.x -= BOX_FACE
        for cube in cubeList:
            if cube.cube.colliderect(cube_temp):
                left_collision = True  

        # right & left 
        if ( (keys[pygame.K_RIGHT]) and  
             (key_pressed == False) and 
             (self.x + BOX_FACE < WIN_WIDTH) and 
             (self.cube.x + BOX_FACE < WIN_WIDTH) and 
             (right_collision == False)): 

            key_pressed = True 
            self.cube.x += BOX_FACE
            
        if ( (keys[pygame.K_LEFT]) and 
             (key_pressed == False) and 
             (self.x > 0) and 
             (self.cube.x > 0) and 
             (left_collision == False)): 
             
            key_pressed = True 
            self.cube.x -= BOX_FACE
            
        return key_pressed



