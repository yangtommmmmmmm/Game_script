2-	import pygame
from ball1 import Ball
from paddle1 import Paddle






pygame.init()

#創建黑色視窗
window = pygame.display.set_mode((700,500))
pygame.display.set_caption("乒乓球")

#創建球物件
ball_object = Ball(350,250,10,(255,255,255))


#創建球拍物件
paddle_object1 = Paddle(10,200,15,100,(255,255,255))
paddle_object2 = Paddle(675,200,15,100,(255,255,255))
#初始化球拍左上角y座標
paddle_object1_y1 = 200
paddle_object2_y2 = 200

#創建文字物件
a = '0'
b = '0'
a = str(a)
b = str(b)
font = pygame.font.Font("微軟正黑體.ttf",50)

#定義比數運算處理
def update_text1(wx,parameter1):
    if wx == '1':
        ind1 = int(parameter1)
        ind1 += 1
        ind1 = str(ind1)
        return ind1
    return parameter1

def update_text2(wx,parameter2):
    if wx == '2':
        ind2 = int(parameter2)
        ind2 += 1
        ind2 = str(ind2)
        return ind2
    return parameter2


#讓視窗一直存在著
run = True
while run:

    #設定一秒只能run幾次此視窗
    clock = pygame.time.Clock() #Clock是time.py中的class
    clock.tick(60)

    #取得輸入資料
    #取得輸入資料-當按下x時，則關閉視窗
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #取得輸入資料-控制paddle運動。當w->左paddle往上，s->左paddle往下，UP->右paddle往上，DOWN->右paddle往下
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_object1_y1 -= 5
    if keys[pygame.K_s]:
        paddle_object1_y1 += 5
    if keys[pygame.K_UP]:
        paddle_object2_y2 -= 5
    if keys[pygame.K_DOWN]:
        paddle_object2_y2 += 5
    #取得輸入資料-輸入比數資料
    text1 = font.render(a, True, (255, 255, 255))
    text2 = font.render(b, True, (255, 255, 255))

    #更新遊戲
    paddle_object1.update(paddle_object1_y1)
    paddle_object2.update(paddle_object2_y2)
    wx = ball_object.update(700,500,paddle_object1_y1,paddle_object2_y2)
    a = update_text1(wx,a)
    b = update_text2(wx,b)


    #畫面顯示
    window.fill((0,0,0)) #讓視窗背景為黑色
    window.blit(text1,(100,20)) #顯示左邊比數
    window.blit(text2,(600,20)) #顯示右邊比數
    ball_object.draw(window) #顯示球
    paddle_object1.draw(window) #顯示左邊球拍
    paddle_object2.draw(window) #顯示右邊球拍
    pygame.display.update()



pygame.quit()
