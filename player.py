import pygame

class player(pygame.sprite.Sprite):
    def __init__(self,pos,constraint,speed):
        super().__init__()
        self.image =  pygame.image.load('sprites/spaceship.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready1 = True
        # i will set this to standard assigning it to true
        self.time_laser = 0
        # measuring time when game started...
        self.laser_recharge = 600
        # allows the main player to shoot every 600 milliseconds 

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready1:
           self.shoot_laserweapon()
           self.ready1 = False 
           self.time_laser = pygame.time.get_ticks() #calculates the amount of miliseconds , measure time since game has been initialized

    def recharge(self): # when the laser can recharge
       if not self.ready1: # is a attribute that allows whether is ready to be fired again ; if false means is mean its already in cool time period
            current_time = pygame.time.get_ticks() # this get ticks is run contiously
            if current_time - self.time_laser >= self.laser_recharge: # would trigger and than shoot laser agan
                self.ready1 = True
                # method recharge allows laser to shot again ; if e.g 1600 - 1000 (1000 is the start time) = 600 ; self.laser_recharge would trigger...               

        


            # allows player to move right of the screen and also left of the screen by pressing left and right button

    def constraint(self):
     if self.rect.left <= 0:
        self.rect.left = 0
        #doesnt allow player to move off the screen doesnt go less than pos of 0
     if self.rect.right >= self.max_x_constraint:
        self.rect.right = self.max_x_constraint
        # doesnt allow player to move off screen when its further to the left
        #constraint method is a rule or condition that limits or restricts possible solutions to a problem
    def shoot_laserweapon(self):
       print('beware lasers incoming')

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
