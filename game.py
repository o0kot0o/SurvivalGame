import pygame
from map import Map
from Entity import *


class Game():
    def __init__(self, title, window_size):
        self.title = title
        self.window_size = window_size

        pygame.init()
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()

        self.world = Map()
        self.player = Player(32, 32, (255, 85, 85), self.world)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.player.update()

    def render(self):
        self.window.fill((0, 0, 0))

        self.world.render(self.window)

        self.player.render(self.window)

        pygame.display.update()
        self.clock.tick(10)

    def gameloop(self):
        while True:
            self.update()
            self.render()