import pygame as PyG
from settings import *
import random 

class Player(PyG.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        PyG.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = PyG.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE          

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = PyG.key.get_pressed()
        if keys[PyG.K_LEFT]:  
            self.vx = -playerSpeed
        if keys[PyG.K_RIGHT]:
            self.vx = playerSpeed
        if keys[PyG.K_UP]:
            self.vy = -playerSpeed
        if keys[PyG.K_DOWN]:
            self.vy = playerSpeed
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = PyG.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = PyG.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')


class AiSprite (PyG.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.Ai
        PyG.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = PyG.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE 

    

class Honey(PyG.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        PyG.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = PyG.Surface((TILESIZE, TILESIZE))
        self.image.fill(LILAC)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE 

class QuestionA (PyG.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        PyG.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = PyG.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTBLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE 

class Wall(PyG.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        PyG.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = PyG.Surface((TILESIZE, TILESIZE))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
