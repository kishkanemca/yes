import random

import pygame as pg

pg.init()
size = W,H = 700,700
FPS = 99
win = pg.display.set_mode(size)

class inginirium(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image('картинка')
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 360


    def update(self):
        self.rect = self.rect.move(random.randrange(5) -2, random.randrange(5) -2)


def load_image(name):
    img = pg.image.load(name)
    img = img.convert()
    color = img.get_at((0, 0))
    img.set_colorkey(color)
    return img

all_sprites = pg.sprite.Group()
for i in range(30):
    inginirium(all_sprites)
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    all_sprites.update()
    win.fill((0, 0, 0))
    all_sprites.draw(win)

    pg.display.update()