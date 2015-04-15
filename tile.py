import pygame
import time


class Tile(object):
    def __init__(self):
        self.solid = False
        self.color = (0, 0, 0)
        self.tick = 0
        self.lastStepOn = 0
        self.health = 3
        self.occupied = False

        self.start_time = time.clock()

        self.font = pygame.font.SysFont(None, 20)
        self.label = self.font.render(' ', True, (255, 255, 255))

    def setColor(self, color):
        self.color = color

    def setSolid(self, solid):
        self.solid = solid

    def isSolid(self):
        return self.solid

    def update(self):
        self.tick = time.clock() - self.start_time
        time_past = (self.tick - self.lastStepOn)
        if time_past > 10 and self.occupied == False:
            self.health += 1
            if self.health < 0:
                self.health = 0
            elif self.health > 3:
                self.health = 3

        self.label = self.font.render(str(self.health), True, (255, 255, 255))

    def steppedOn(self):
        if self.occupied:
            return
        self.tick = time.clock()
        time_past = (self.tick - self.lastStepOn)
        self.lastStepOn = time_past
        if time_past < 10:
            self.health -= 1
            if self.health < 0:
                self.health = 0
            elif self.health > 3:
                self.health = 3
        self.occupied = True
        self.start_time = time.clock()


    def render(self, window, position):
        pygame.draw.rect(window, self.color, (position[0], position[1], 32, 32))
        pygame.draw.rect(window, (0, 0, 0), (position[0], position[1], 32, 32), 1)

        # debug health on tiles
        lx = (position[0] + 32/2) - (self.label.get_width() / 2)
        ly = (position[1] + 32/2) - (self.label.get_height() / 2)
        # window.blit(self.label, (lx, ly))


class GrassTile(Tile):
    def __init__(self):
        super().__init__()
        self.color = (75, 255, 75)


class DirtTile(Tile):
    def __init__(self):
        super().__init__()
        self.color = (120,72,0)

class WallTile(Tile):
    def __init__(self):
        super().__init__()
        self.color = (25, 25, 25)
        self.setSolid(True)

class FloorTile(Tile):
    def __init__(self):
        super().__init__()
        self.color = (128, 128, 128)