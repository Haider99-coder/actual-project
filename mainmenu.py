import pygame
import button
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  # 
pygame.display.set_caption('Cosmic command center')   # 

pause_game = False
menu_state = 'main'

font = pygame.font.SysFont('arialblack', 40)  # 
Text_colour = (255,255,255)

 # loads the buttons up
resume_image = pygame.image.load('Buttons/button_resume.png').convert_alpha()
options_image = pygame.image.load('Buttons/button_options.png').convert_alpha()
quit_image = pygame.image.load('Buttons/button_quit.png').convert_alpha()


# create an instance
resume_button = button.Button(304, 125, resume_image, 1)
options_button = button.Button(297, 250, options_image, 1)  #  304,125 represents the x and y co-ordinate
quit_button = button.Button(336, 375, quit_image, 1)



def draw_text(text , font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    
def loading_screen():
    screen.fill((0, 0, 128))  # Navy blue background
    draw_text('Loading...', font, Text_colour, 300, 250)
    pygame.display.update()
    time.sleep(3)
    
run = True
while run:
    
    screen.fill ((0, 0, 128)) # 
     # if the game pauses than it displays menu
    if pause_game == True:
        
     if menu_state == 'main':
         
       if resume_button.draw(screen):
           pause_game = False
       if options_button.draw(screen):
            menu_state = 'options'
       if quit_button.draw(screen):
           pause_game = False
           
     # can check if the menu options is open
    else:
         draw_text('press Enter to pause', font, Text_colour, 160, 250)
        #  pass  # so it will display the menu
     
   
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # means that a button is being pressed
            if event.key == pygame.K_RETURN:
                pause_game = True
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    
pygame.quit()
