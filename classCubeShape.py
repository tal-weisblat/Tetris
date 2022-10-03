
from gameSettings import * 
from classCube import cube



class CubeShape(cube): 

    def __init__(self, color): 
        self.list = []
        cube = pygame.Rect(1*CUBE_FACE, 0, CUBE_FACE, CUBE_FACE)
        self.list.append(cube)
        self.color = color

    def drawCubeShape(self):
        for cube in self.list:
            pygame.draw.rect(WIN, self.color, cube)
    


    def moveCubeShape(self, keys, key_pressed, cubeList):
        
        BOX_FACE = WIN_WIDTH/COL_NUM

        # downwards
        self.list[0].y += SHAPE_VEL
        
        # right-collision with cubeList
        right_collision = False  
        cube_temp = pygame.Rect(self.list[0].x, self.list[0].y, CUBE_FACE, CUBE_FACE)
        cube_temp.x += BOX_FACE
        for cube_shape in cubeList:
            if cube_shape.list[0].colliderect(cube_temp):
                right_collision = True  

        # left collision with cubeList
        left_collision = False  
        cube_temp = pygame.Rect(self.list[0].x, self.list[0].y, CUBE_FACE, CUBE_FACE)
        cube_temp.x -= BOX_FACE
        for cube_shape in cubeList:
            if cube_shape.list[0].colliderect(cube_temp):
                left_collision = True  

        # right & left 
        if ( (keys[pygame.K_RIGHT]) and  
             (key_pressed == False) and 
             (self.list[0].x + BOX_FACE < WIN_WIDTH) and 
             (self.list[0].x + BOX_FACE < WIN_WIDTH) and 
             (right_collision == False)): 

            key_pressed = True 
            self.list[0].x += BOX_FACE
            
        if ( (keys[pygame.K_LEFT]) and 
             (key_pressed == False) and 
             (self.list[0].x > 0) and 
             (self.list[0].x > 0) and 
             (left_collision == False)): 
             
            key_pressed = True 
            self.list[0].x -= BOX_FACE
            
        return key_pressed

