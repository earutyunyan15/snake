from pygame import *
from random import randint

weidth, height = 700, 500
window = display.set_mode((weidth, height))
display.set_caption('Turtle')
font.init()
font1 = font.SysFont("Arial", 100)
font2 = font.SysFont("Arial", 36)
clock = time.Clock()
speed = 15
background = transform.scale(image.load('snake_back.jpg'), (weidth, height))
x = randint(0, weidth - 35)
y = randint(0, height - 35)
snake_list = [(x, y)]
snake_length = 1
apples = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Snake(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__(player_image, player_x, player_y, player_speed, size_x, size_y)
        self.dir_x = player_speed
        self.dir_y = 0

    def update(self):
        self.rect.x += self.dir_x
        self.rect.y += self.dir_y

class Food(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        super().__init__(player_image, player_x, player_y, 0, size_x, size_y)

    def relocate(self):
        self.rect.x = randint(0, weidth - 35)
        self.rect.y = randint(0, height - 35)

head = Snake('snake.png', x, y, speed, 35, 35)
apple = Food('apple_supernew.png', randint(0, weidth - 35), randint(0, height - 35), 50, 50)
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_LEFT and head.dir_x == 0:
                head.dir_x = -speed
                head.dir_y = 0
            elif e.key == K_RIGHT and head.dir_x == 0:
                head.dir_x = speed
                head.dir_y = 0
            elif e.key == K_UP and head.dir_y == 0:
                head.dir_x = 0
                head.dir_y = -speed
            elif e.key == K_DOWN and head.dir_y == 0:
                head.dir_x = 0
                head.dir_y = speed

    if not finish:
        window.blit(background, (0, 0))
        head.update()
        new_head_pos = (head.rect.x, head.rect.y)
        snake_list.append(new_head_pos)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for pos in snake_list:
            window.blit(transform.scale(image.load('snake.png'), (35, 35)), pos)
        if head.rect.x < 0 or head.rect.x > weidth - 35 or head.rect.y < 0 or head.rect.y > height - 35:
            loser = font1.render('Проигрыш!', True, (255, 0, 0))
            window.blit(loser, (weidth // 2 - loser.get_width() // 2, height // 2 - loser.get_height() // 2))
            finish = True
        apple.reset()
        if sprite.collide_rect(head, apple):
            apples += 1
            snake_length += 1
            apple.relocate()
        counter = font2.render(f'Счёт: {apples}', True, (255, 255, 255))
        window.blit(counter, (10, 10))

    display.update()
    clock.tick(speed)
