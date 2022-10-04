


from gameSettings import * 


class Lshape():

    def __init__(self, color): 
        
        self.color = color 
        self.listOfCubes = []

        cube_1 = pygame.Rect(0,0, CUBE_FACE, CUBE_FACE)
        cube_2 = pygame.Rect(0,50, CUBE_FACE, CUBE_FACE)
        cube_3 = pygame.Rect(50,0, CUBE_FACE, CUBE_FACE)
        cube_4 = pygame.Rect(100,0, CUBE_FACE, CUBE_FACE)
        self.listOfCubes.append(cube_1)
        self.listOfCubes.append(cube_2)
        self.listOfCubes.append(cube_3)
        self.listOfCubes.append(cube_4)


    def drawShape(self):
        for cube in self.listOfCubes:
            pygame.draw.rect(WIN, self.color, cube)


    
    def __collision_with_cubeList__(self, cubeList, label):
        
        BOX_FACE = WIN_WIDTH/COL_NUM
        
        # right 
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


    def moveShape(self, keys, key_pressed, cubeList):

        BOX_FACE = WIN_WIDTH/COL_NUM

        # downwards
        for cube in self.listOfCubes: cube.y += SHAPE_VEL
        
        x_max = max(box.x for box in self.listOfCubes)
        x_min = min(box.x for box in self.listOfCubes)
        no_collision_right = self.__collision_with_cubeList__(cubeList, 'right')
        no_collision_left  = self.__collision_with_cubeList__(cubeList, 'left')
        
        # right         
        if ( (keys[pygame.K_RIGHT])         and  
             (key_pressed == False)         and 
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
        
        if keys[pygame.K_SPACE] and (space_pressed == False):    
            space_pressed = True 

            # SWITCH (to next phase)
            x1 = self.listOfCubes[0].x
            x2 = self.listOfCubes[1].x
            x3 = self.listOfCubes[2].x
            x4 = self.listOfCubes[3].x
            min_x = min(x1,x2,x3,x4)

            if x1-min_x == 0 and x2-min_x == 0 and x3-min_x == 50 and x4-min_x == 100:  
                x1, x2, x3, x4 = 0, 50, 50, 50 
                y1, y2, y3, y4 = 0, 0, 50, 100 
            elif x1-min_x == 0 and x2-min_x == 50 and x3-min_x == 50 and x4-min_x == 50:  
                x1, x2, x3, x4 = 100, 100, 50, 0
                y1, y2, y3, y4 = 0, 50, 50, 50 
            elif x1-min_x == 100 and x2-min_x == 100 and x3-min_x == 50 and x4-min_x == 0:  
                x1, x2, x3, x4 = 0, 0, 0, 50 
                y1, y2, y3, y4 = 0, 50, 100, 100   
            elif x1-min_x == 0 and x2-min_x == 0 and x3-min_x == 0 and x4-min_x == 50:  
                x1, x2, x3, x4 = 0, 0, 50, 100
                y1, y2, y3, y4 = 0, 50, 0, 0 
            
            # inner boxes 
            y = self.listOfCubes[0].y
            cube_1 = pygame.Rect(x1+min_x, y1+y, CUBE_FACE, CUBE_FACE)
            cube_2 = pygame.Rect(x2+min_x, y2+y, CUBE_FACE, CUBE_FACE)
            cube_3 = pygame.Rect(x3+min_x, y3+y, CUBE_FACE, CUBE_FACE)
            cube_4 = pygame.Rect(x4+min_x, y4+y, CUBE_FACE, CUBE_FACE)

            # complex object (the union of boxes)
            self.listOfCubes.clear()
            self.listOfCubes.append(cube_1)
            self.listOfCubes.append(cube_2)
            self.listOfCubes.append(cube_3)
            self.listOfCubes.append(cube_4)

        return space_pressed
    
    