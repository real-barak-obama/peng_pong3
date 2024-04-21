from pygame import *
from random import choice


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.h = h
        self.rect.w = w

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def bounty_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-5-self.rect.height:
            self.rect.y += self.speed
    def bounty_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500-5-self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__(img,x,y,w,h,speed)
        self.speed_x = 0
        self.speed_y = 0

    def set_direction(self,speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x*self.speed
        self.rect.y += self.speed_y*self.speed

    def check_direction(self,pl1,pl2):
        global point_l, point_r
        if self.rect.y<=0:
            self.speed_y*=-1
        elif self.rect.y>=self.rect.y>=500-self.rect.height:
            self.speed_y*=-1
        elif self.rect.colliderect(pl1.rect):
            self.speed += 0.005
            self.speed_x*=-1
        elif self.rect.colliderect(pl2.rect):
            self.speed += 0.005
            self.speed_x*=-1
        elif self.rect.x<=0:
            point_r+=1
            self.rect.x = 700/2-self.rect.width/2
            self.rect.x = 500/2-self.rect.height/2
            self.set_direction(choice([-1,1]), choice([-1,1]))
            self.speed+=0.15
        elif self.rect.x>=700-self.rect.width:
            point_l+=1
            self.rect.x = 700/2-self.rect.width/2
            self.rect.x = 500/2-self.rect.height/2        
            self.set_direction(choice([-1,1]), choice([-1,1]))
            self.speed+=0.15


point_r = 0
point_l = 0

direction = [-1,1]



ball = Ball('kokos.png', 300,200,30,30,3)
ball.set_direction(choice(direction), choice(direction))
ball2 = Ball('kokos.png', 300,200,30,30,3)
ball2.set_direction(choice(direction), choice(direction))
ball3 = Ball('kokos.png', 300,200,30,30,3)
ball3.set_direction(choice(direction), choice(direction))
ball4 = Ball('kokos.png', 300,200,30,30,3)
ball4.set_direction(choice(direction), choice(direction))
ball5 = Ball('kokos.png', 300,200,30,30,3)
ball5.set_direction(choice(direction), choice(direction))
ball6 = Ball('kokos.png', 300,200,30,30,3)
ball6.set_direction(choice(direction), choice(direction))
ball7 = Ball('kokos.png', 300,200,30,30,3)
ball7.set_direction(choice(direction), choice(direction))





window = display.set_mode((700,500))
display.set_caption('Пэнг-Понг')

background = transform.scale(image.load('ostrov.jpg'), (700,500))

game = True
finish = True
clock = time.Clock()
FPS = 60
text=0



bounty_1 = Player('bounty_left.png', 40,150,40,130,7)
bounty_2 = Player('bounty_right.png', 620,150,40,130,7)

font.init()
font1 = font.SysFont('Arial',36)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    score_right = font1.render('Счёт:'+str(point_r),1, (0,0,175))
    score_left = font1.render('Счёт:'+str(point_l),1, (0,0,175))
    window.blit(background,(0,0))
    bounty_1.bounty_left()
    bounty_1.reset()
    bounty_2.bounty_right()
    bounty_2.reset()
    ball.update()
    ball.reset()
    ball.check_direction(bounty_1,bounty_2)

    if point_l + point_r >= 5:
        ball2.update()
        ball2.reset()
        ball2.check_direction(bounty_1,bounty_2)
    if point_l + point_r >= 10:
        ball3.update()
        ball3.reset()
        ball3.check_direction(bounty_1,bounty_2)
    if point_l + point_r >= 15:
        ball4.update()
        ball4.reset()
        ball4.check_direction(bounty_1,bounty_2)
    if point_l + point_r >= 20:
        ball5.update()
        ball5.reset()
        ball5.check_direction(bounty_1,bounty_2)
    if point_l + point_r >= 25:
        ball6.update()
        ball6.reset()
        ball6.check_direction(bounty_1,bounty_2)
    if point_l + point_r >= 30:
        ball7.update()
        ball7.reset()
        ball7.check_direction(bounty_1,bounty_2)
    window.blit(score_right,(10,30))
    window.blit(score_left,(550,30))
    display.update()
    clock.tick(FPS)
