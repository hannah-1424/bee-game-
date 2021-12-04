import pygame as PyG
import sys
from os import path
from settings import *
from sprites import *


class Game:
    def __init__(self):
        PyG.init()
        self.screen = PyG.display.set_mode((WIDTH, HEIGHT))
        PyG.display.set_caption(TITLE)
        self.clock = PyG.time.Clock()
        PyG.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.maze_data = []
        with open(path.join(game_folder, 'maze.txt'), 'rt') as f:
            for line in f:
                self.maze_data.append(line)

    def new(self):
        self.all_sprites = PyG.sprite.Group()
        self.walls = PyG.sprite.Group()
        self.Ai = PyG.sprite.Group()
        for row, tiles in enumerate(self.maze_data):
            for col, tile in enumerate(tiles):
                if tile == 'x':
                    Wall(self, col, row)
                if tile == 'A':
                    self.AiSprite = AiSprite(self, col, row)
                if tile == 'H':
                    self.Honey = Honey(self, col, row)
                if tile == 'Q':
                    self.QuestionA = QuestionA(self, col, row)
                if tile == 'S':
                    self.player = Player(self, col, row)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        PyG.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        PyG.display.flip()

    def events(self):
        for event in PyG.event.get():
            if event.type == PyG.QUIT:
                self.quit()
            if event.type == PyG.KEYDOWN:
                if event.key == PyG.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
