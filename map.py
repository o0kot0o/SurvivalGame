from tile import *
from random import randint


class Map():
    def __init__(self):
        self.size = (40, 24)

        self.map = [[GrassTile() for x in range(self.size[1])] for x in range(self.size[0])]

        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if x == 0 or x == self.size[0]-1:
                    self.map[x][y] = WallTile()
                elif y == 0 or y == self.size[1]-1:
                    self.map[x][y] = WallTile()
                else:
                    if x % 10 == 0:
                        self.map[x][y] = DirtTile()
                    else:
                        self.map[x][y] = GrassTile()

    def update(self):
        pass

    def render(self, window):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.map[x][y].render(window, (x*32, y*32))