from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('Turtle')
game = True
finish = False
font.init()
font1 = font.SysFont("Arial", 100)
weidth = 700
height = 500
x = randint(0, weidth - 35)
y = randint(0, height - 35)
snake_list = [(x,y)]
snake_segments = []
lenght = 1
x1 = 0
y1 = 0
apples = 0
font2 = font.SysFont('Arial', 36)
speed = 15
clock = time.Clock()
background = transform.scale(image.load('snake_back.jpg'),(weidth,height))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (35, 35))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Snake(GameSprite):
    def update(self):
        x1 = 0
        y1 = 0
        k_p = key.get_pressed()
        if k_p[K_LEFT] and self.rect.x > 0:
            x1 = -self.speed
            y1 = 0
        elif k_p[K_RIGHT] and self.rect.x < 665:
            x1 = self.speed
            y1 = 0
        elif k_p[K_UP] and self.rect.y > 0:
            y1 = -self.speed
            x1 = 0
        elif k_p[K_DOWN] and self.rect.y < 465:
            y1 = self.speed
            x1 = 0
        self.rect.x += x1
        self.rect.y += y1
    def grow_up(self):
        if lenght < 
class Food(GameSprite):
    def update(self):
        self.rect.x = randint(0, weidth - 35) 
        self.rect.y = randint(0, height - 35) 
player = Snake('snake.png', x, y, speed, 35, 35)
apple = Food('apple_new.jpg', randint(0, weidth - 35), randint(0, height - 35), 0, 20, 20)
while game:
    loser = font1.render('Проигрыш!', 1, (255, 0, 0))
    counter = font2.render('Счёт:' + str(apples), 1, (255, 255, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))   
        apple.reset()
        player.reset()
        player.update()
        player.grow_up()
        player1.reset()
        player1.update()
        window.blit(counter, (10, 10))
        if sprite.collide_rect(player, apple):
            apple.update()
            apples += 1
            snake_list.append((player.rect.x, player.rect.y))
        if player.rect.x == 660 or player.rect.y == 460 or player.rect.x == 0 or player.rect.y == 0:
            window.blit(loser, (175, 175))
            finish = True
    display.update()
    clock.tick(speed)
