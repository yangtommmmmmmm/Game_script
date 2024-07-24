import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y,imgs,speedyy):
        super().__init__()
        self.origin_x = x
        self.origin_y = y
        self.imgs = imgs
        self.img_index = 0
        self.image = self.imgs[self.img_index]
        self.rect = self.image.get_rect() #圖片定位屬性
        self.rect.center = (x,y) #設定鳥中心點座標
        self.last_pic_time = pygame.time.get_ticks()
        self.img_frequency = 100
        self.sbp = speedyy

    def update(self,col):
        self.image = pygame.transform.rotate(self.image, +0.6)
        now = pygame.time.get_ticks()
        if now - self.last_pic_time > self.img_frequency:
            self.img_index += 1
            if self.img_index >= len(self.imgs):
                self.img_index = 0
            self.image = self.imgs[self.img_index]
            if col == True:
                self.image = pygame.transform.rotate(self.image,-180)
            self.last_pic_time = now
        #鳥引力
        self.sbp += 0.5
        if self.sbp > 9:
            self.sbp = 9
        self.rect.y += self.sbp

        if self.rect.y > 500:
            self.rect.y = 500



    def jump(self):
        self.sbp = -10


    def reset(self):
        self.img_index = 0
        self.image = self.imgs[self.img_index]
        self.rect.center = (self.origin_x, self.origin_y)  # 設定鳥中心點座標
        self.last_pic_time = pygame.time.get_ticks()
        self.img_frequency = 100
        self.sbp = 0
