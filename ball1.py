import pygame
import random




class Ball:
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        #設定球運動速度
        random_list = [3,4,5,6,7]
        self.speedx = random.choice(random_list)
        self.speedy = random.choice(random_list)

    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)

    def update(self,width,height,p_y1,p_y2):
        #調整每禎球圓心xy方向之運動位置
        self.x += self.speedx
        self.y += self.speedy

        #調整每禎球上下左右頂點方向之運動位置
        ball_top = self.y - self.radius
        ball_bottom = self.y + self.radius
        ball_left = self.x - self.radius
        ball_right = self.x + self.radius

        #調整左邊、右邊球拍邊界y座標範圍
        p_y11 = p_y1 + 100
        p_y22 =p_y2 + 100


        #重要球運動判斷
        #重要球運動判斷:當球碰到上下視窗邊界時，運動會反向
        if ball_top < 0 or ball_bottom >height:
            self.speedy *= -1
        #重要球運動判斷:當球碰到左邊球拍右邊邊界時，運動會反向
        if (ball_left == 25) and ((self.y <= p_y11) and (self.y >= p_y1)) :
            self.speedx *= -1
        # 重要球運動判斷:當球碰到右邊球拍左邊邊界時，運動會反向
        if (ball_right == 675) and ((self.y <= p_y22) and (self.y >= p_y2)):
            self.speedx *= -1
            self.speedy += random.randint(-5,5)
        # 要球運動判斷:當球左邊頂點座標小於x座標25時，其會歸回球體原來啟動位置，並判給另一方得分
        if (ball_left < 25):
            self.x = 350
            self.y = 250
            return '2'
        # 要球運動判斷:當球右邊頂點座標大於x座標675時，其會歸回球體原來啟動位置，並判給另一方得分
        if (ball_right > 675):
            self.x = 350
            self.y = 250
            return '1'
