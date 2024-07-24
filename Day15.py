3-	import pygame
from bird import Bird
from pipe import Pipe
from restart import Restart
import random


pygame.init()

#創建黑色視窗
window = pygame.display.set_mode((780,600))
pygame.display.set_caption("冰淇淋耶誕跳跳樂")

#設定視窗左上角為裊裊icon
pygame.display.set_icon(pygame.image.load("img/rabbit0.png"))

#創建可調整FPS之物件
clock = pygame.time.Clock()


#創建背景圖片物件並將此物件填滿
bg_img = pygame.image.load("img/bg_snow_2.jpg")
bg_img = pygame.transform.scale(bg_img,(780,600))

#利用繼承Sprite類別來創建快速擺動鳥圖片物件
bird_imgs = []
bird_y_position = 100
for i in range(0, 2):
    r_img = pygame.image.load(f"img/rabbit{i}.png")
    r_img = pygame.transform.scale(r_img,(60,75))
    bird_imgs.append(r_img)
bird = Bird(50, bird_y_position, bird_imgs, 1)
bird_sprite = pygame.sprite.Group()
bird_sprite.add(bird)

#補充
#若要讓鳥圖片物件逆時鐘旋轉角度，可下以下code
#bird_img = pygame.transform.rotate(bird_img,60)-->代表鳥圖片物件逆時鐘旋轉60度
#若要讓鳥圖片物件翻轉，則可下以下code
#bird_img = pygame.transform.flip(bird_img,True,False)-->第二個參數代表鳥圖片物件是否可以水平翻轉，而第三個參數代表鳥圖片物件是否可以垂直翻轉

#利用繼承Sprite類別創建正面及顛倒管子圖片物件
pipe_img1 = pygame.image.load("img/pipe.png")
pipe_img2 = pygame.transform.flip(pipe_img1,False,True)
# 創建跟pipe有關之sprite群組
pipe_sprite = pygame.sprite.Group()


#最後一次創建管子的時間
last_pipe_time = pygame.time.get_ticks()
pipe_frequency = 1500
#初始化鳥和pipe碰撞時間
current_collision_time = 0
collision_det = False

#初始化比數
score = '0'
font = pygame.font.Font(None, 80)


#創建地面物件，初始化地面物件左邊x座標及地面物件x方向速度
ground_img = pygame.image.load("img/snowground.png")
ground_img = pygame.transform.scale(ground_img,(900,168))
ground_x_position = 0
ground_x_speed = 4

#創建ground循環往左運動function
def ground_update(x,sp):
    x_position = x
    x_position -= sp
    if x_position < -100: #當物件左上角x座標超出視窗100像素時，則就使物件左上角x座標重新定位於視窗x方向0像素
        x_position = 0
    return x_position

#產生管子的function
def generate_pipes(a,b):
    now = pygame.time.get_ticks()
    if now - a >= b:
        random_height = random.randint(-100,100)
        pipe1 = Pipe(pipe_img1, 780, 400+random_height, True, 4)
        pipe2 = Pipe(pipe_img2, 780, 150+random_height, False, 4)
        pipe_sprite.add(pipe1)
        pipe_sprite.add(pipe2)
        pipe_sprite.update()
        return now
    return a
#創建restart物件
restart_img = pygame.image.load("img/restart.png")
restart_sprite = pygame.sprite.Group()


#植入背景音樂
pygame.mixer.init()
pygame.mixer.music.load("img/xmas_song.mp3")
pygame.mixer.music.play(-1)



#讓視窗一直存在著
run = True
while run:
    #設定一秒只能run幾次視窗-設定FPS
    clock.tick(60)

    #輸入資料
    #輸入資料-碰撞資料輸入
    r = pygame.sprite.groupcollide(bird_sprite,pipe_sprite,False, False)
    bird_center = bird.rect.center

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#當按下x時，視窗會關閉
            run = False
        elif (r != {}) or (bird_center[1] < 0 ) or (bird_center[1] > 500):#碰撞停止情況判斷
            current_collision_time = pygame.time.get_ticks()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bird.jump()

    #判斷滑鼠是否有在運動中並取出滑鼠位置
    #if event.type == pygame.MOUSEMOTION:
    #    print(event.pos)
    #連續取出滑鼠按鍵狀態及滑鼠位置-->tuple type data
    #buttons = pygame.mouse.get_pressed()
    #positions = pygame.mouse.get_pos()

    #更新遊戲
    current_update_time = pygame.time.get_ticks()

    if (current_collision_time == 0) or (current_update_time < current_collision_time):
        ground_x_position = ground_update(ground_x_position, ground_x_speed)
        bird_sprite.update(collision_det)
        pipe_sprite.update()
        last_pipe_time = generate_pipes(last_pipe_time, pipe_frequency)
        #判斷鳥有無通過管子-->通過則比數加1，沒通過則比數不加1
        if len(pipe_sprite.sprites()) != 0:
            if not pipe_sprite.sprites()[0].bird_pass:
                if (pipe_sprite.sprites()[0].rect.right < bird.rect.left):
                    score = int(score)
                    score += 1
                    score = str(score)
                    pipe_sprite.sprites()[0].bird_pass = True
        text_surface = font.render(score, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (390, 50)

    elif (current_collision_time != 0):
        collision_det = True
        bird_sprite.update(collision_det)
        text_surface = font.render(score, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (390, 50)
        restart = Restart(restart_img, 240, 259)
        restart_sprite.add(restart)
        if len(restart_sprite.sprites()) > 20:
            restart_sprite.remove(restart_sprite.sprites()[0])
        pygame.mixer.music.stop()

        if keys[pygame.K_SPACE]:
            current_collision_time = 0
            score = '0'
            last_pipe_time = pygame.time.get_ticks()
            bird.reset()
            pipe_sprite.empty()
            restart_sprite.empty()
            ground_x_position = 0
            collision_det = False
            pygame.mixer.music.play(-1)



    #顯示遊戲
    window.fill((0,0,0))
    window.blit(bg_img,(0,0))
    bird_sprite.draw(window)
    pipe_sprite.draw(window)
    window.blit(text_surface,text_rect)
    window.blit(ground_img, (ground_x_position, 500))
    restart_sprite.draw(window)
    pygame.display.update()
pygame.quit()
