
from game_settings import * 

def p_button_pressed(keys, pause_game, K_p_pressed):

    if (keys[pygame.K_p] == True) and (K_p_pressed == False): 
        K_p_pressed = True 
        if pause_game == False : 
            pause_game = True 
        else: 
            pause_game = False  
    if (keys[pygame.K_p] == False): K_p_pressed = False

    return pause_game, K_p_pressed
