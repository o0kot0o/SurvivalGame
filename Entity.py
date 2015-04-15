import pygame


class Entity(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 16

    def update(self):
        pass

    def render(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))
        pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, self.size, self.size), 1)


class Player(Entity):
    def __init__(self, x, y, color, world):
        super().__init__(x, y, color)
        self.world = world

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if not self.world.map[int(self.x / self.size)][int(self.y / self.size) - 1].isSolid():
                self.y -= self.size
        if key[pygame.K_s]:
            if not self.world.map[int(self.x / self.size)][int(self.y / self.size) + 1].isSolid():
                self.y += self.size
        if key[pygame.K_a]:
            if not self.world.map[int(self.x / self.size) - 1][int(self.y / self.size)].isSolid():
                self.x -= self.size
        if key[pygame.K_d]:
            if not self.world.map[int(self.x / self.size) + 1][int(self.y / self.size)].isSolid():
                self.x += self.size