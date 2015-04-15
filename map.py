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
                    self.map[x][y] = GrassTile()

        self.createRoom(0, 0, 10, 10)

    def update(self, player):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if player.x/self.map[x][y].getTileSize() == x and player.y/self.map[x][y].getTileSize() == y:
                    self.map[x][y].steppedOn()
                    if self.map[x][y].getTileType() is GrassTile:
                        if self.map[x][y].health <= 0:
                            self.map[x][y] = DirtTile()
                            self.map[x][y].health = 0
                else:
                    self.map[x][y].occupied = False
                    if self.map[x][y].getTileType() is DirtTile:
                        if self.map[x][y].health == 3:
                            self.map[x][y] = GrassTile()
                self.map[x][y].update()

    def render(self, window):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                tile = self.map[x][y]
                tile.render(window, (x*tile.getTileSize(), y*tile.getTileSize()))

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

    def createWall(self, x, y, x2, y2):
        for _y in range(y2):
            for _x in range(x2):
                self.map[x + _x][y + _y] = WallTile()