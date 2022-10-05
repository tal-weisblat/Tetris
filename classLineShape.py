


from gameSettings import * 


class LineShape():

    def __init__(self, color): 

        self.color = color
        self.listOfCubes = []
        cube_1 = pygame.Rect(CUBE_FACE,0, CUBE_FACE, CUBE_FACE)
        cube_2 = pygame.Rect(2*CUBE_FACE,0, CUBE_FACE, CUBE_FACE)
        cube_3 = pygame.Rect(3*CUBE_FACE,0, CUBE_FACE, CUBE_FACE)
        cube_4 = pygame.Rect(4*CUBE_FACE,0, CUBE_FACE, CUBE_FACE)
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
            y1 = self.listOfCubes[0].y
            if x1 == x2: 
                x2, y2 = x1 + 1*CUBE_FACE, y1
                x3, y3 = x1 + 2*CUBE_FACE, y1 
                x4, y4 = x1 + 3*CUBE_FACE, y1 
            else: 
                x2, y2 = x1, y1 + 1*CUBE_FACE
                x3, y3 = x1, y1 + 2*CUBE_FACE
                x4, y4 = x1, y1 + 3*CUBE_FACE
            
            # inner boxes 
            cube_1 = pygame.Rect(x1, y1, CUBE_FACE, CUBE_FACE)
            cube_2 = pygame.Rect(x2, y2, CUBE_FACE, CUBE_FACE)
            cube_3 = pygame.Rect(x3, y3, CUBE_FACE, CUBE_FACE)
            cube_4 = pygame.Rect(x4, y4, CUBE_FACE, CUBE_FACE)

            # add 
            self.listOfCubes.clear()
            self.listOfCubes.append(cube_1)
            self.listOfCubes.append(cube_2)
            self.listOfCubes.append(cube_3)
            self.listOfCubes.append(cube_4)

        return space_pressed
    