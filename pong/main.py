import pygame as pg
import time

WIN_WIDTH = 1000
WIN_HEIGHT = 1000

window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

game = True


class Ball(pg.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.speed = 5
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = WIN_WIDTH//2
        self.rect.y = WIN_HEIGHT//2
        self.dirx = self.speed
        self.diry = self.speed

    def update(self):
        if pg.sprite.collide_rect(self, player1) or pg.sprite.collide_rect(self, player2):
            self.dirx *= -1
        if self.rect.y <= 0 or self.rect.y+10 >= WIN_HEIGHT:
            self.diry *= -1

        if self.rect.x <= 0:
            player2.score += 1
            self.rect.x = WIN_WIDTH//2
            self.rect.y = WIN_HEIGHT//2
            scored = font.render('PLAYER 2 SCORED!!!', True, (255, 255, 255))
            window.blit(scored, (WIN_WIDTH // 2 - 100, WIN_HEIGHT // 2))
            pg.display.update()
            start = time.time()
            while True:
                if time.time() - start >= 5:
                    break

        elif self.rect.x+10 >= WIN_HEIGHT:
            self.rect.x = WIN_WIDTH // 2
            self.rect.y = WIN_HEIGHT // 2
            player1.score += 1
            scored = font.render('PLAYER 1 SCORED!!!', True, (255, 255, 255))
            window.blit(scored, (WIN_WIDTH//2-100, WIN_HEIGHT//2))
            pg.display.update()
            start = time.time()
            while True:
                if time.time() - start >= 5:
                    break

        self.rect.y += self.diry
        self.rect.x += self.dirx

        window.blit(self.img, (self.rect.x, self.rect.y))


class Player(pg.sprite.Sprite):
    def __init__(self, img, num):
        super().__init__()
        self.score = 0
        self.img = img
        self.speed = 10
        self.rect = self.img.get_rect()
        if num:
            self.rect.x = WIN_WIDTH-10
            self.rect.y = WIN_HEIGHT//2
        else:
            self.rect.x = 0
            self.rect.y = WIN_HEIGHT//2

        self.num = num

    def update(self):
        keys = pg.key.get_pressed()
        if self.num:
            if keys[pg.K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pg.K_DOWN] and self.rect.y + 50 < WIN_HEIGHT:
                self.rect.y += self.speed
        else:
            if keys[pg.K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pg.K_s] and self.rect.y + 50 < WIN_HEIGHT:
                self.rect.y += self.speed

        window.blit(self.img, (self.rect.x, self.rect.y))


clock = pg.time.Clock()
FPS = 30

score1 = 0
score2 = 0

player1 = Player(pg.image.load('roketka.png'), 1)
player2 = Player(pg.image.load('roketka.png'), 0)
ball = Ball(pg.image.load('ball.png'))


pg.font.init()
font = pg.font.SysFont('Arial', 24)

while game:
    clock.tick(FPS)

    pg.draw.rect(window, (0, 0, 0), (0, 0, WIN_WIDTH, WIN_HEIGHT))

    first = font.render(str(player1.score), True, (255, 255, 255))
    second = font.render(str(player2.score), True, (255, 255, 255))

    pg.draw.rect(window, (255, 255, 255), ((WIN_WIDTH//2)-15, 100, 40, 30), 3)
    pg.draw.rect(window, (255, 255, 255), ((WIN_WIDTH//2)+3, 100, 3, 30))

    window.blit(first, (WIN_WIDTH//2-10, 100))
    window.blit(second, (WIN_WIDTH//2+10, 100))

    player1.update()
    player2.update()
    ball.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False

    pg.display.update()
