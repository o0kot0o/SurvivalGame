import pygame
from tile import *


class Map():
    def __init__(self):
        self.size = (40, 24)

        self.map = []

        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.map.append(GrassTile())

    def update(self):
        pass

    def render(self, window):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.map[x + y * self.size[1]].render(window, (x * 32, y * 32))