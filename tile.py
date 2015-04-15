import pygame


class Tile(object):
    def __init__(self):
        self.solid = False
        self.color = (0, 0, 0)

    def setColor(self, color):
        self.color = color

    def setSolid(self, solid):
        self.solid = solid

    def isSolid(self):
        return self.solid

    def render(self, window, position):
        pygame.draw.rect(window, self.color, (position[0], position[1], 32, 32))
        pygame.draw.rect(window, (0, 0, 0), (position[0], position[1], 32, 32), 1)


class GrassTile(Tile):
    def __init__(self):
        super().__init__()
        self.color = (75, 255, 75)