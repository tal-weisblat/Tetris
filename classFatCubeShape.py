
from gameSettings import * 



class FatCubeShape(): 

    def __init__(self, color): 
        
        self.color = color
        self.listOfCubes = []
        cube_1 = pygame.Rect(1*CUBE_FACE, 0, CUBE_FACE, CUBE_FACE)
        cube_2 = pygame.Rect(2*CUBE_FACE, 0, CUBE_FACE, CUBE_FACE)
        cube_3 = pygame.Rect(1*CUBE_FACE, CUBE_FACE, CUBE_FACE, CUBE_FACE)
        cube_4 = pygame.Rect(2*CUBE_FACE, CUBE_FACE, CUBE_FACE, CUBE_FACE)
        self.listOfCubes.append(cube_1)
        self.listOfCubes.append(cube_2)
        self.listOfCubes.append(cube_3)
        self.listOfCubes.append(cube_4)
        

    def __collision_with_cubeList__(self, cubeList, label):
            BOX_FACE = WIN_WIDTH/COL_NUM 
            temp_shape = []                              
            no_collision = True 
            for cube in self.listOfCubes: 
                temp_cube = pygame.Rect(cube.x, cube.y, BOX_FACE, BOX_FACE)
                if label == 'right': temp_cube.x += BOX_FACE
                if label == 'left' : temp_cube.x -= BOX_FACE
                temp_shape.append(temp_cube)
            for cube_list in cubeList:
                for temp_cube in temp_shape: 
                    if cube_list.cube.colliderect(temp_cube):
                        no_collision = False 
            return no_collision


    def drawShape(self):
        for cube in self.listOfCubes:
            pygame.draw.rect(WIN, self.color, cube)



    def moveShape(self, keys, key_pressed, cubeList):

        BOX_FACE = WIN_WIDTH/COL_NUM

        # downwards
        for cube in self.listOfCubes: cube.y += SHAPE_VEL
        
        x_max = max(box.x for box in self.listOfCubes)
        x_min = min(box.x for box in self.listOfCubes)
        no_collision_right = self.__collision_with_cubeList__(cubeList, 'right')
        no_collision_left  = self.__collision_with_cubeList__(cubeList, 'left')
        

        # down 
        if ( keys[pygame.K_DOWN] and key_pressed == False ):
            key_pressed = True 
            for box in self.listOfCubes: box.y += SHAPE_FAST_VEL 

        # right         
        if ( (keys[pygame.K_RIGHT]) and  
                (key_pressed == False) and 
                (x_max + BOX_FACE < WIN_WIDTH) and 
                (no_collision_right)): 
                
            key_pressed = True 
            for box in self.listOfCubes: box.x += BOX_FACE    
        
        # left 
        if ( (keys[pygame.K_LEFT]) and 
                (key_pressed == False) and 
                (x_min > 0) and 
                (no_collision_left)): 
                
            key_pressed = True 
            for box in self.listOfCubes: box.x -= BOX_FACE    
            
        return key_pressed


    def rotate(self, keys, space_pressed):
        pass