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
