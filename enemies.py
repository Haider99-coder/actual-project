import pygame
from pygame.sprite import Group

class Alien(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y,):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha() # file path for my sprites
        self.rect = self.image.get_rect(topleft = (x,y)) # will originally place it in the top left column
        
        if image_path == 'sprites/pixel_ship_red_small.png' : self.value = 100
        elif image_path ==  'sprites/pixel_ship_blue_small.png' : self.value = 200
        else: self.value = 300



      


    def update(self,direction): # function that i use for the movement
        self.rect.x += direction 

class Boss(pygame.sprite.Sprite):
    def __init__(self,side,screen_width):
        super().__init__()
        self.image = pygame.image.load ('sprites/blue_boss.png').convert_alpha()
            
        if side == 'right': # if boss spawns in right hand screen it moves to the left
            x = screen_width + 50
            self.speed = -3
        else:
            x = screen_width - 50
            self.speed = 3

        self.rect = self.image.get_rect(topleft =(x,300))


class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        self.image = pygame.image.load('sprites/blue_boss.png').convert_alpha()  
        if side == 'right':
            x = screen_width + 50
            self.speed = -5  # Adjust speed as needed
        else:
            x = -50
            self.speed = 5

        self.rect = self.image.get_rect(topleft=(x, 120))

    def update(self):
        self.rect.x += self.speed
        


    

   #14iter to write in word docu
   # def update(self,movement):
    #self.rect.x += movement
