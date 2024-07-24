import pygame

class Restart(pygame.sprite.Sprite):
    def __init__(self,img,r_x,r_y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.x = r_x
        self.y = r_y
        self.rect.topleft = (self.x , self.y)
