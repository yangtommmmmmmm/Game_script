import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self,img,p_x,p_y,boo,speedxx):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.px = p_x
        self.py = p_y
        self.boo = boo
        self.sp = speedxx
        self.bird_pass = False

    def update(self):
        if self.rect.right < 0:
            self.kill()
        else:
            if(self.boo == True):
                self.px -= self.sp
                self.rect.topleft = (self.px,self.py)
            else:
                self.px -= self.sp
                self.rect.bottomleft = (self.px,self.py)
