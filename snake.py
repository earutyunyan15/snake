from pygame import *
#создание окна
weidth = 700
height = 500
window = display.set_mode((700, 500))
display.set_caption('Snake')
#переменные
clock = time.Clock()
size = 20
FPS = 60
game = True
finish = False
x1 = 0 
y1 = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Snake(GameSprite):
    def update(self):
    # Тут логика движения змейки
        for e in event.get():
            if e.type == K_LEFT and self.recr.x > 0:
                x1 = -size
                y1 = 0
            if e.type == K_RIGHT and self.recr.x < 700:
                x1 = size
                y1 = 0
            if e.type == K_UP and self.rect.y < 500:
                y1 = -size
                x1 = 0
            if e.type == K_DOWN and self.rect.y > 0:
                y1 = size
                x1 = 0

background = transform.scale(image.load('snake_back.jpg'),(weidth,height))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))