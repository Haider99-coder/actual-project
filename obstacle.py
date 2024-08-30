import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self,color,size,x,y):
        super().__init__()
        self.image = pygame.Surface((6,6))
        self.image.fill('purple')
        self.rect = self.image.get_rect(topleft = (x,y))

barrier = [
'  xxxxxxx',
' xxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxx     xxx',
'xx       xx']

# any spaces WILL not be filled with a sprite
# the shape variable contains a list where each x block will be represented with a sprite'
# any space included within this list ont include a block'
