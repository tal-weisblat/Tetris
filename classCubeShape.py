
from gameSettings import * 



class CubeShape(): 

    def __init__(self, color): 
        
        self.color = color
        self.listOfCubes = []
        
        cube = pygame.Rect(1*CUBE_FACE, 0, CUBE_FACE, CUBE_FACE)
        self.listOfCubes.append(cube)
        

    def drawShape(self):
        for cube in self.listOfCubes:
            pygame.draw.rect(WIN, self.color, cube)
    
    def moveShape(self, keys, key_pressed, cubeList):
        
        BOX_FACE = WIN_WIDTH/COL_NUM

        # downwards
        self.listOfCubes[0].y += SHAPE_VEL
        
        # right-collision with cubeList
        right_collision = False  
        cube_temp = pygame.Rect(self.listOfCubes[0].x, self.listOfCubes[0].y, CUBE_FACE, CUBE_FACE)
        cube_temp.x += BOX_FACE
        for cube_shape in cubeList:
            if cube_shape.cube.colliderect(cube_temp):
                right_collision = True  

        # left collision with cubeList
        left_collision = False  
        cube_temp = pygame.Rect(self.listOfCubes[0].x, self.listOfCubes[0].y, CUBE_FACE, CUBE_FACE)
        cube_temp.x -= BOX_FACE
        for cube_shape in cubeList:
            if cube_shape.cube.colliderect(cube_temp):
                left_collision = True  

        # right & left 
        if ( (keys[pygame.K_RIGHT]) and  
             (key_pressed == False) and 
             (self.listOfCubes[0].x + BOX_FACE < WIN_WIDTH) and 
             (self.listOfCubes[0].x + BOX_FACE < WIN_WIDTH) and 
             (right_collision == False)): 

            key_pressed = True 
            self.listOfCubes[0].x += BOX_FACE
            
        if ( (keys[pygame.K_LEFT]) and 
             (key_pressed == False) and 
             (self.listOfCubes[0].x > 0) and 
             (self.listOfCubes[0].x > 0) and 
             (left_collision == False)): 
             
            key_pressed = True 
            self.listOfCubes[0].x -= BOX_FACE
            
        return key_pressed


    def rotate(self, keys, space_pressed):
        if ( keys[pygame.K_SPACE] and space_pressed == False):  
            space_pressed = True
            print ('space')
            