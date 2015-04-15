from tile import *
from random import randint


class Map():
    def __init__(self):
        self.size = (80, 48)

        self.map = [[GrassTile() for x in range(self.size[1])] for x in range(self.size[0])]

        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if x == 0 or x == self.size[0]-1:
                    self.map[x][y] = WallTile()
                elif y == 0 or y == self.size[1]-1:
                    self.map[x][y] = WallTile()
                else:
                    self.map[x][y] = GrassTile()
        self.createRoom(0, 0, 10, 8)
        self.createRoom(9, 0, 15, 20)

    def update(self, player):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if player.x/self.map[x][y].getTileSize() == x and player.y/self.map[x][y].getTileSize() == y:
                    self.map[x][y].steppedOn()
                    if type(self.map[x][y]) is GrassTile:
                        if self.map[x][y].health <= 0:
                            self.map[x][y] = DirtTile()
                            self.map[x][y].health = 0
                else:
                    self.map[x][y].occupied = False
                    if type(self.map[x][y]) is DirtTile:
                        if self.map[x][y].health == 3:
                            self.map[x][y] = GrassTile()
                self.map[x][y].update()

    def render(self, window):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.map[x][y].render(window, (x*self.map[x][y].getTileSize(), y*self.map[x][y].getTileSize()))

    def createRoom(self, x, y, w, h):
        for _y in range(h):
            for _x in range(w):
                if _x == 0 or _x == w-1:
                    self.map[x + _x][y + _y] = WallTile()
                elif _y == 0 or _y == h-1:
                    if _y == h-1 and _x == int(w/2):
                        self.map[x + _x][y + _y] = FloorTile()
                    else:
                        self.map[x + _x][y + _y] = WallTile()
                else:
                    self.map[x + _x][y + _y] = FloorTile()