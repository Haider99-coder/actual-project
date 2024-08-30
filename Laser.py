import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed = -7):
        super().__init__()
        self.image = pygame.Surface((4,20)) # draws surface
        self.image.fill('blue') # fill with white as the screen is black
        self.rect = self.image.get_rect(center = pos) # sets out position of the rectangle of laser
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
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
