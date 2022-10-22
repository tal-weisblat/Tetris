

from game_settings import * 
from src.gui.draw_game import *

from src.entities.grid import create_grid    
from src.entities.cube_list import add_cube, remove_rows
from src.shapes.cube_shape import CubeShape
from src.shapes.L_shape import Lshape
from src.shapes.line_shape import LineShape
from src.shapes.short_line_shape import ShortLineShape
from src.shapes.fat_cube_shape import FatCubeShape
from src.buttons.buttons import * 
 


def game():
    
    next_shape = FatCubeShape(GREY)
    cubeList = []
    grid = create_grid()
    clock = pygame.time.Clock()
    time_start = time.time()             
    numRowsRemoved = 0 
    fix_time = True 
    key_pressed = False 
    create_new_shape = True 
    space_pressed = False 
    K_p_pressed = False 
    game_over = False 
    pause_game = False 
    run = True 

    while run: 

        clock.tick(60)
        game_time = int(time.time() - time_start)

        # events 
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False 
                break
            
            if event.type == GAMEOVER:
                GAMEOVER_SOUND.play()
                game_over = True 
                break

            if event.type == ROWREMOVED: 
                numRowsRemoved += 1 
                
        # game-over 
        if game_over:
            if fix_time: 
                entire_game_time = game_time
                fix_time = False
            draw_game_over(numRowsRemoved, entire_game_time)
            continue
         
        # new & next shapes  
        if create_new_shape == True:
            create_new_shape = False
            new_shape  = next_shape
            next_shape = random.choice([Lshape(BLACK),
                                        CubeShape(RED),
                                        LineShape(MAROON),
                                        ShortLineShape(GREEN), 
                                        FatCubeShape(GREY)])  
    
        draw_console_next_shape(next_shape)
        keys = pygame.key.get_pressed()

        # pause-game 
        pause_game, K_p_pressed = p_button_pressed(keys, pause_game, K_p_pressed)
        if pause_game:      
            draw_game(grid, new_shape, cubeList, next_shape, numRowsRemoved, game_time)
            continue 

        # move-downwards 
        key_pressed = new_shape.move_shape(keys, key_pressed, cubeList)   # move 
        if (keys[pygame.K_LEFT] == False) and (keys[pygame.K_RIGHT] == False): key_pressed = False
        
        # rotate 
        space_pressed = new_shape.rotate(keys, space_pressed)
        if (keys[pygame.K_SPACE] == False): space_pressed = False

        # add cubes to cubeList
        create_new_shape = add_cube(cubeList, new_shape)

        # remove row 
        remove_rows(cubeList)

        # draw 
        draw_game(grid, new_shape, cubeList, next_shape, numRowsRemoved, game_time)

game()



