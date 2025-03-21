import pygame


class Laser(pygame.sprite.Sprite):
      def __init__(self,pos,speed = -7 ,screen_height= 800):
        super().__init__()
        self.image = pygame.Surface((7,20)) # draws surface
        self.image.fill('blue') # fill with white as the screen is black
        self.rect = self.image.get_rect(center = pos) # sets out position of the rectangle of laser
        self.speed = speed
        self.height_y_constraint = screen_height

      def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
           self.kill()

      def update(self):
        self.rect.y += self.speed
        self.destroy()



    

