import pygame

class Paddle:

    def __init__(self,left,top,width,height,color):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color

    def draw(self,window):
        pygame.draw.rect(window, self.color, (self.left,self.top,self.width,self.height))


    def update(self,update_top):
        self.top = update_top
        if self.top < 0:
            self.top = 0
        if self.top > 400:
            self.top = 400
